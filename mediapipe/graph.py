from .counter import BasicCounterFactory
from .graph_profiler import *
from .scheduler import Scheduler
from logzero import logger
from .graph_validation import validate_graph
from .calculator import CalculatorNode



class CalculatorGraph:
    def __init__(self):
        self._counter_factory = BasicCounterFactory()
        # TODO
        self._scheduler = Scheduler(self)
        # TODO
        self._profiler = None
        self._initialized = False
        self._validated_graph = None
        self._nodes = []

    def initialize(self, input_config, side_packets={}):
        """

        :param config: type of CalculatorGraphConfig
        :return:
        """
        if self._initialized:
            logger.warming("CalculatorGraph can be initialized only once.")
            return

        # TODO check input_config is valid
        validate_graph(input_config)
        self._validated_graph = input_config

        self.initialize_executors()
        self.initialize_packet_generator_graph(side_packets)
        self.initialize_streams()
        self.initialize_calculator_nodes()

        self.initialize_profiler()
        self._initialized = True
        logger.info('initialize graph success ^_^ ')

    def initialize_executors(self): ...

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self): ...

    def initialize_calculator_nodes(self):
        for i, node_config in enumerate(self._validated_graph.node):
            node = CalculatorNode(node_config)
            self._nodes.append(node)
        logger.info(self._nodes)

    def initialize_profiler(self): ...

    def start_run(self, extra_side_packet, stream_headers):
        # prepare run(extra_side_packet, stream_headers)
        self._scheduler.start()
        return True
