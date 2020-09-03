from .counter import BasicCounterFactory
from .graph_profiler import *
from .scheduler import Scheduler
from logzero import logger
from .graph_validation import validate_graph
from .calculator import CalculatorNode
from .collection import parse_tag_index_name
import pandas as pd



class StreamType:
    INPUT_STREAM=0
    OUTPUT_STREAM=1
    INPUT_SIDE_PACKET=2
    OUTPUT_SIDE_PACKET=3

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

        self._stream_df_columns = ['type', 'tag', 'index', 'name', 'tag_index_name', 'item', 'node_id', 'graph_id']

        self._node_df_columns = ['type', 'item', 'node_id', 'graph_id']

        self._graph_df_columns = ['type', 'item', 'graph_id', 'config']

        self._stream_df = pd.DataFrame(columns=self._stream_df_columns)
        self._node_df = pd.DataFrame(columns=self._node_df_columns)
        self._graph_df = pd.DataFrame(columns=self._graph_df_columns)

    def initialize(self, input_config, deps_config=[], side_packets={}):
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

        self.parse_config([input_config] + deps_config)
        logger.info(self._stream_df)
        logger.info(self._node_df)
        logger.info(self._graph_df)

        self.initialize_executors()
        self.initialize_packet_generator_graph(side_packets)
        self.initialize_streams()
        self.initialize_calculator_nodes()

        self.initialize_profiler()
        self._initialized = True
        logger.info('initialize graph success ^_^ ')


    def parse_config(self, configs):
        for graph_id, graph_pb in enumerate(configs):
            # graph input stream
            for input_stream_pb in graph_pb.input_stream:
                tag, index, name = parse_tag_index_name(input_stream_pb)
                df = pd.DataFrame(columns=self._stream_df_columns,
                                  data=[[StreamType.INPUT_STREAM, tag, index, name, input_stream_pb, None, -1, graph_id]])
                self._stream_df = pd.concat([self._stream_df, df], axis=0)
            # graph output stream
            for output_stream_pb in graph_pb.output_stream:
                tag, index, name = parse_tag_index_name(output_stream_pb)
                df = pd.DataFrame(columns=self._stream_df_columns,
                                  data=[[StreamType.INPUT_STREAM, tag, index, name, output_stream_pb, None, -1, graph_id]])
                self._stream_df = pd.concat([self._stream_df, df], axis=0)

            # node input stream
            for node_id, node_pb in enumerate(graph_pb.node):
                for input_stream_pb in node_pb.input_stream:
                    tag, index, name = parse_tag_index_name(input_stream_pb)
                    # logger.info('{},{},{},{}'.format(input_stream_pb, tag, index, name) )
                    df = pd.DataFrame(columns=self._stream_df_columns,
                                      data=[
                                          [StreamType.INPUT_STREAM, tag, index, name, input_stream_pb, None, node_id, graph_id]])
                    self._stream_df = pd.concat([self._stream_df, df], axis=0)
            # node output stream
            for node_id, node_pb in enumerate(graph_pb.node):
                for output_stream_pb in node_pb.output_stream:
                    tag, index, name = parse_tag_index_name(output_stream_pb)
                    # logger.info('{},{},{},{}'.format(output_stream_pb, tag, index, name))
                    df = pd.DataFrame(columns=self._stream_df_columns,
                                      data=[[StreamType.OUTPUT_STREAM, tag, index, name, output_stream_pb, None,
                                             node_id, graph_id]])
                    self._stream_df = pd.concat([self._stream_df, df], axis=0)

            # graph
            self._graph_df = pd.DataFrame(columns=self._graph_df_columns,
                                         data=[[graph_pb.type, None, graph_id, graph_pb]])
            # node
            for node_id, node_pb in enumerate(graph_pb.node):
                df = pd.DataFrame(columns=self._node_df_columns,
                                  data=[[node_pb.calculator, None, node_id, graph_id]])
                self._node_df = pd.concat([self._node_df, df], axis=0)

    def initialize_executors(self): ...

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self): ...

    def initialize_calculator_nodes(self):
        for i, node_config in enumerate(self._validated_graph.node):
            node = CalculatorNode(node_config)
            self._nodes.append(node)
        logger.info(self._nodes)

    def initialize_profiler(self): ...

    def start_run(self, extra_side_packet, stream_headers, blocking=True):
        # prepare run(extra_side_packet, stream_headers)
        self._scheduler.start(blocking=blocking)
        return True
