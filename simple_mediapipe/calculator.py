from .registration import CALCULATOR
from logzero import logger
import copy
from threading import Lock
from .collection import Collection


class CalculatorNode:

    _static_id = 0

    def __init__(self, graph, config):
        calculator_module = CALCULATOR.get(config.calculator)
        self.calculator_base = calculator_module()
        self._options = config.options

        # TODO 1. only one 2. total 3. point which stream
        self._default_run_condition = 'one or more'
        self.timestamp = -1
        self.input_streams = Collection()
        self.output_streams = Collection()
        self._default_context = None
        self._default_context_mutex = Lock()
        self._graph = graph
        # self._scheduler = self._graph._scheduler
        self.exception_count = 0
        self.max_exception_count = 100
        self.id = CalculatorNode._static_id
        CalculatorNode._static_id += 1
        self.is_opened = False
        # TODO init calculator contract and check calculator base.

    def open_node(self):
        self.calculator_base.open(self._default_context)
        self.is_opened = True
        self.run()

    def close_node(self):
        self.calculator_base.close(self._default_context)
        self.is_opened = False

    def init_context(self):
        # when stream init, call this function
        self._default_context = CalculatorContext(self)

    def set_graph(self, graph):
        self._graph = graph

    def input_stream_listener(self):
        self._graph.add_task(self)

    def prepare_packet(self):
        """input stream callback function
        TODO first do it
        1. check input stream timestamp is ready
        2. get correct packet from input_stream to default_context
        3. if default_context is ready, add self.run to schedule queue"""
        flag = False
        packet_timestamp = -1
        if self._default_run_condition == 'one or more':
            for index, stream in enumerate(self.input_streams):
                # deprecated some expire package
                while len(stream) and stream.get().timestamp < self.timestamp:
                    expire_package = stream.popleft()
                    logger.warn('[%s] deprecated some expire package [%s]', self, expire_package)
                if len(stream) and stream.get().timestamp >= self.timestamp:
                    packet = stream.popleft()
                    stream_mirror = self._default_context.inputs()[index]
                    stream_mirror.add_packet(packet)
                    flag = True
                    packet_timestamp = packet.timestamp
        # TODO prepare update accept timestamp
        if flag:
            self.timestamp = packet_timestamp
            logger.debug('%s update timestamp:%s', self, self.timestamp)
        return flag

    def run(self):
        with self._default_context_mutex:
            try:
                logger.debug('%s execute!', self)
                if not self.is_source() and not self.prepare_packet():  # default_context没有准备好
                    logger.debug('%s did not prepare', self)
                    return
                self.calculator_base.process(self._default_context)
                for stream in self._default_context.outputs():
                    stream.propagate_downstream()
                # if calculator base is complete, clear default context
                self._default_context.clear()
            except Exception as e:
                self.exception_count += 1
                logger.exception(e)
                logger.info('%s exception count is %s, max exception count is %s'
                            ,self, self.exception_count, self.max_exception_count)
                if self.exception_count >= self.max_exception_count:
                    logger.error("Excetion count >= Max exception count")
                    self._graph._scheduler.set_queues_running(False)
                    # TODO exit?
            finally:
                if self.is_source() and self.exception_count < self.max_exception_count:
                    self._graph.add_task(self)

    def __str__(self):
        return '{}_{}, inputs: {}, outputs: {}'.format(self.calculator_base, self.id, self.input_streams, self.output_streams)

    def __repr__(self):
        return str(self)
    
    def is_source(self):
        return len(self.input_streams) == 0 and len(self.output_streams) != 0

    def __lt__(self, other):
        # not opened node 优先级最高
        # 次之 source node
        # 接着是id值大的优先级高
        self_source = self.is_source()
        other_source = self.is_source()
        if not self.is_opened or not other.is_opened:
            if not self.is_opened: return True
            if not other.is_opened: return False
            return self.id > other.id
        if self_source:
            if not other_source: return True
            return self.id > other.id
        else:
            if other_source: return False
            return self.id < other.id


class CalculatorContext:
    """
    // A CalculatorContext provides information about the graph it is running
    // inside of through a number of accessor functions: Inputs(), Outputs(),
    // InputSidePackets(), Options(), etc.
    """
    def __init__(self, node: CalculatorNode):
        # mirror of calculator inputs
        self.input_stream_shards = copy.deepcopy(node.input_streams)
        # mirror of calculator outputs
        self.output_stream_shards = copy.deepcopy(node.output_streams)
        self._options = node._options

    def options(self):
        return self._options

    def clear(self):
        for stream in self.input_stream_shards:
            stream.clear()

    def inputs(self) -> Collection:
        return self.input_stream_shards

    def outputs(self) -> Collection:
        return self.output_stream_shards


class CalculatorBase:
    def __init__(self):
        self._options = None

    @staticmethod
    def get_contract(cc: CalculatorContext):
        """检查graph的配置是否符合要求"""
        return True

    def open(self, cc: CalculatorContext):
        """初始化改Calculator"""

    def process(self, cc: CalculatorContext):
        """处理"""

    def close(self, cc: CalculatorContext):
        """释放资源"""

    def __str__(self):
        return self.__class__.__name__

