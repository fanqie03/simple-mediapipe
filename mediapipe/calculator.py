from enum import Enum
from mediapipe.registration import CALCULATOR, build_calculator
from logzero import logger


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


class CalculatorNode:

    def __init__(self, config):
        calculator_module = CALCULATOR.get(config.calculator)
        self.calculator_base = calculator_module()

        self.input_streams = []
        self.output_streams = []
        self._default_context = CalculatorContext()
        self._default_context_mutex = None
        self._graph = None
        # TODO init calculator contract and check calculator base.

    def set_graph(self, graph):
        self._graph = graph

    def input_stream_listener(self):
        self._graph.add_task(self.run)

    def prepare_pakcage(self):
        """input stream callback function
        TODO first do it
        1. check input stream timestamp is ready
        2. get correct packet from input_stream to default_context
        3. if default_context is ready, add self.run to schedule queue"""
        pass

    def run(self):
        # TODO add lock in this function
        if not self.prepare_pakcage():  # default_context没有准备好
            return
        self.calculator_base(self._default_context)
        for stream in self.output_streams:
            stream.propogate_mirrors()
        # TODO if calculator base is complete, clear default context



    def __str__(self):
        return 'node has {}'.format(self.calculator_base)
    
    def is_source(self):
        ...

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
    def __init__(self):
        self.input_stream_shards=[]
        self.output_stream_shards=[]

    def inputs(self):
        return self.input_stream_shards

    def outputs(self):
        return self.output_stream_shards


class CalculatorContract:
    """
    // CalculatorContract contains the expectations and properties of a Node
    // object, such as the expected packet types of input and output streams and
    // input and output side packets.
    """
