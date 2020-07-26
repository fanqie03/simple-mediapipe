from enum import Enum
from mediapipe.registration import CALCULATOR, build_calculator


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
        self.calculator = calculator_module()

    def __str__(self):
        return 'node has {}'.format(self.calculator)

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


class CalculatorRunner:
    """The class for running the Calculator with given inputs and examining outputs."""


class CalculatorContext:
    """
    // A CalculatorContext provides information about the graph it is running
    // inside of through a number of accessor functions: Inputs(), Outputs(),
    // InputSidePackets(), Options(), etc.
    """


class ClaculatorState:
    """
    // Holds data that the Calculator needs access to.  This data is not
    // stored in Calculator directly since Calculator will be destroyed after
    // every CalculatorGraph::Run() .  It is not stored in CalculatorNode
    // because Calculator should not depend on CalculatorNode.  All
    // information conveyed in this class is flowing from the CalculatorNode
    // to the Calculator.
    """


class CalculatorContract:
    """
    // CalculatorContract contains the expectations and properties of a Node
    // object, such as the expected packet types of input and output streams and
    // input and output side packets.
    """
