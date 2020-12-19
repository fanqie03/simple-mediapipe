from .counter import BasicCounterFactory
from .graph_profiler import *
from .scheduler import Scheduler
from logzero import logger
from .graph_validation import validate_graph
from .calculator import CalculatorNode
from .collection import parse_tag_index_name
import pandas as pd
from .stream import *
from .registration import CALCULATOR
import sys


class StreamType:
    INPUT_STREAM=InputStream
    OUTPUT_STREAM=OutputStream
    INPUT_SIDE_PACKET=2
    OUTPUT_SIDE_PACKET=3
    GRAPH_INPUT_STREAM = GraphInputStream
    GRAPH_OUTPUT_STREAM = GraphOutputStream


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

    def add_task(self, task_fn):
        self._scheduler.add_task(task_fn)

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

        # TODO 待完善，会出现GraphInputStream连着GraphInputStream，GraphOutputStram连着GraphOutputGream
        self.parse_config([input_config] + deps_config)
        logger.info(self._stream_df)
        logger.info(self._node_df)
        logger.info(self._graph_df)

        self.initialize_executors()
        # TODO side package
        # self.initialize_packet_generator_graph(side_packets)
        self.initialize_streams()
        self.initialize_calculator_nodes()

        self.initialize_profiler()
        self._initialized = True
        logger.info('initialize graph success ^_^ ')

    def parse_config(self, configs):
        # read each graph config, first read graph
        graphs = []
        for graph_id, graph_pb in enumerate(configs):
            # graph
            graphs.append([graph_pb.type, None, graph_id, graph_pb])
        self._graph_df = pd.DataFrame(columns=self._graph_df_columns, data=[graphs])

        # read each graph config
        for graph_id, graph_pb in enumerate(configs):
            # node
            nodes = []
            for node_id, node_pb in enumerate(graph_pb.node):
                # check node exists
                node_type = node_pb.calculator
                node = None
                if CALCULATOR.get(node_type) is None and node_type not in self._graph_df.type:
                    logger.error('Calculator {} not exists. Please registry it or add sub graph dependence.'
                                 .format(node_type))
                    sys.exit(1)
                elif CALCULATOR.get(node_type) is not None:
                    node = CalculatorNode(node_pb)
                    self._nodes.append(node)
                nodes.append([node_pb.calculator, node, node_id, graph_id])
            df = pd.DataFrame(columns=self._node_df_columns, data=nodes)
            self._node_df = pd.concat([self._node_df, df], axis=0)

            # graph input stream
            streams = []
            for input_stream_pb in graph_pb.input_stream:
                tag, index, name = parse_tag_index_name(input_stream_pb)
                stream = GraphInputStream()
                streams.append([GraphInputStream, tag, index, name, input_stream_pb, stream, -1, graph_id])

            # graph output stream
            for output_stream_pb in graph_pb.output_stream:
                tag, index, name = parse_tag_index_name(output_stream_pb)
                stream = GraphOutputStream()
                streams.append([GraphOutputStream, tag, index, name, output_stream_pb, stream, -1, graph_id])

            # node input stream
            for node_id, node_pb in enumerate(graph_pb.node):
                for input_stream_pb in node_pb.input_stream:
                    tag, index, name = parse_tag_index_name(input_stream_pb)
                    node_type = node_pb.calculator
                    # real node
                    if CALCULATOR.get(node_type) is not None:
                        _, node, _, _ = list(filter(lambda node: node[2] == node_id and node[3] == graph_id, nodes))[0]
                        stream = InputStream(node.input_stream_listener)
                        streams.append([InputStream, tag, index, name, input_stream_pb, stream, node_id, graph_id])
                    # sub graph
                    elif node_type in self._graph_df.type:
                        stream = GraphInputStream()
                        streams.append([GraphInputStream, tag, index, name, input_stream_pb, stream, node_id, graph_id])
                    else:
                        logger.error('Calculator {} not exists. Please registry it or add sub graph dependence.'
                                     .format(node_type))
                        sys.exit(1)

            # node output stream
            for node_id, node_pb in enumerate(graph_pb.node):
                for output_stream_pb in node_pb.output_stream:
                    tag, index, name = parse_tag_index_name(output_stream_pb)
                    node_type = node_pb.calculator
                    # real node
                    if CALCULATOR.get(node_type) is not None:
                        stream = OutputStream()
                        streams.append([InputStream, tag, index, name, output_stream_pb, stream, node_id, graph_id])
                    # sub graph
                    elif node_type in self._graph_df.type:
                        stream = GraphOutputStream()
                        streams.append([GraphInputStream, tag, index, name, output_stream_pb, stream, node_id, graph_id])
                    else:
                        logger.error('Calculator {} not exists. Please registry it or add sub graph dependence.'
                                     .format(node_type))
                        sys.exit(1)

            df = pd.DataFrame(columns=self._stream_df_columns,data=streams)
            self._stream_df = pd.concat([self._stream_df, df], axis=0)



    def initialize_executors(self): ...

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self):
        for stream_index, stream_row in self._stream_df.iterrows():
            # 拼接stream
            name = stream_row['name']
            graph_id = stream_row['graph_id']
            stream = stream_row['item']
            stream_class = stream_row['type']
            tag_index_name = stream_row['tag_index_name']
            if stream_class == InputStream:
                # 下游是node，需要node的notyfy callback
                pass
            elif stream_class == OutputStream:
                # 下游是同一个图的Input Stream、GraphInputStream、GraphOutputStream
                next_streams = self._stream_df[
                    (self._stream_df['name'] == name) &
                    (self._stream_df['graph_id'] == graph_id) &
                    (self._stream_df['type'].isin([InputStream, GraphInputStream, GraphOutputStream]))
                ]
                if len(next_streams) == 0:
                    logger.warning('{}:"{}" did not find down stream'.format(stream_class, tag_index_name))
                for next_stream_index, next_stream_row in next_streams.iterrows():
                    stream.add_mirrors(next_stream_row['item'])
            elif stream_class == GraphInputStream:
                # 下游是同一个图的InputStream，
                # 或者是子图的GraphInputStream
                next_streams = self._stream_df[
                    (self._stream_df['name'] == name) &
                    (self._stream_df['graph_id'] == graph_id) &
                    (self._stream_df['type'].isin([InputStream, GraphInputStream]))
                ]
                if len(next_streams) == 0:
                    logger.warning('{}:"{}" did not find down stream'.format(stream_class, tag_index_name))
                for next_stream_index, next_stream_row in next_streams.iterrows():
                    stream.add_mirrors(next_stream_row['item'])
            elif stream_class == GraphOutputStream:
                # 下游是OutputStream，或者是GraphOutputStream，或者没有
                # 同一个图的同一个name
                next_streams = self._stream_df[
                    (self._stream_df['name'] == name) &
                    (self._stream_df['graph_id'] == graph_id) &
                    (self._stream_df['type'].isin([[OutputStream, GraphOutputStream]]))
                ]
                for next_stream_index, next_stream_row in next_streams.iterrows():
                    stream.add_mirrors(next_stream_row['item'])
            else:
                logger.error("Don't know the stream category {}".format(stream_class))

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

    def __str__(self):
        return 'graph'


class SubGraph:
    # offer graph config
    def __init__(self, config):
        pass
