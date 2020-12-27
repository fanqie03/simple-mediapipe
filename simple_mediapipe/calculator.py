from enum import Enum
from .registration import CALCULATOR, build_calculator
from logzero import logger
import copy
from typing import List
from threading import Lock
from .collection import Collection


class CalculatorBase:
    @staticmethod
    def get_contract(cc):
        """检查graph的配置是否符合要求"""
        return True

    def open(self, cc):
        """初始化改Calculator"""

    def process(self, cc):
        """处理"""

    def close(self, cc):
        """释放资源"""

    def __str__(self):
        return self.__class__.__name__


class CalculatorNode:

    def __init__(self, graph, config):
        calculator_module = CALCULATOR.get(config.calculator)
        self.calculator_base = calculator_module()

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
        # TODO init calculator contract and check calculator base.

    def init_context(self):
        # when stream init, call this function
        self._default_context = CalculatorContext(self)

    def set_graph(self, graph):
        self._graph = graph

    def input_stream_listener(self):
        self._graph.add_task(self.run)

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
                    logger.warn('[{}] deprecated some expire package [{}]'
                                .format(self, expire_package))
                if len(stream) and stream.get().timestamp >= self.timestamp:
                    packet = stream.popleft()
                    stream_mirror = self._default_context.inputs()[index]
                    stream_mirror.add_packet(packet)
                    flag = True
                    packet_timestamp = packet.timestamp
        # TODO prepare update accept timestamp
        if flag:
            self.timestamp = packet_timestamp
        return flag

    def run(self):
        with self._default_context_mutex:
            try:
                logger.debug('{} execute!'.format(self))
                if not self.is_source() and not self.prepare_packet():  # default_context没有准备好
                    logger.debug('{} did not prepare'.format(self))
                    return
                self.calculator_base.process(self._default_context)
                for stream in self._default_context.outputs():
                    stream.propagate_downstream()
                # if calculator base is complete, clear default context
                self._default_context.clear()
            except Exception as e:
                self.exception_count += 1
                logger.exception(e)
                logger.info('{} exception count is {}, max exception count is {}'
                            .format(self, self.exception_count, self.max_exception_count))
                if self.exception_count >= self.max_exception_count:
                    logger.error("Excetion count >= Max exception count")
                    self._graph._scheduler.set_queues_running(False)
                    # TODO exit?
            finally:
                if self.is_source() and self.exception_count < self.max_exception_count:
                    self._graph.add_task(self.run)

    def __str__(self):
        return 'Node {}'.format(self.calculator_base)
    
    def is_source(self):
        return len(self.input_streams) == 0 and len(self.output_streams) != 0

    class NodeStatus(Enum):
        """
        // The status of the current Calculator that this CalculatorNode
        // is wrapping.  kStateActive is currently used only for source nodes.
        """
        kStateUninitialized = 0
        kStatePrepared = 1
        kStateOpened = 2
        kStateActive = 3
        kStateClosed = 4

    class SchedulingState(Enum):
        """
        // SchedulingState incidates the current state of the node scheduling process.
        // There are four possible transitions:
        // (a) From kIdle to kScheduling.
        // Any thread that makes this transition becomes the scheduling thread and
        // will be responsible for preparing and scheduling all possible invocations.
        // (b) From kScheduling to kSchedulingPending.
        // Any thread, except the scheduling thread, can make this transition.
        // kSchedulingPending indicates that some recent changes require the
        // scheduling thread to recheck the node readiness after current scheduling
        // iteration.
        // (c) From kSchedulingPending to kScheduling.
        // Made by the scheduling thread to indicate that it has already caught up
        // with all the recent changes that can affect node readiness.
        // (d) From kScheduling to kIdle. Made by the scheduling thread when there is
        // no more scheduling work to be done.
        """
        kIdle = 0
        kScheduling = 1
        kSchedulingPending = 2


class CalculatorContext:
    """
    // A CalculatorContext provides information about the graph it is running
    // inside of through a number of accessor functions: Inputs(), Outputs(),
    // InputSidePackets(), Options(), etc.
    """
    def __init__(self, node:CalculatorNode):
        # mirror of calculator inputs
        self.input_stream_shards = copy.deepcopy(node.input_streams)
        # mirror of calculator outputs
        self.output_stream_shards = copy.deepcopy(node.output_streams)

    def clear(self):
        for stream in self.input_stream_shards:
            stream.clear()

    def inputs(self) -> Collection:
        return self.input_stream_shards

    def outputs(self) -> Collection:
        return self.output_stream_shards


class CalculatorContract:
    """
    // CalculatorContract contains the expectations and properties of a Node
    // object, such as the expected packet types of input and output streams and
    // input and output side packets.
    """
