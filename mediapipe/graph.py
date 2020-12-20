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
from .collection import Collection
import sys


class StreamType:
    INPUT_STREAM=0
    OUTPUT_STREAM=1
    INPUT_SIDE_PACKET=2
    OUTPUT_SIDE_PACKET=3
    GRAPH_INPUT_STREAM = 4
    GRAPH_OUTPUT_STREAM = 5


class SubGraph:
    def __init__(self, graph_pb, graph_df):
        # self.name = name
        self.graph_pb = graph_pb
        # self.id = id
        self.graph_input_streams = Collection()
        self.graph_output_streams = Collection()

        self._stream_df_columns = ['type', 'tag', 'index', 'name', 'tag_index_name', 'item', 'node_id', 'graph_id']
        self._node_df_columns   = ['type', 'item', 'node_id', 'graph_id']
        self._graph_df_columns  = ['type', 'item', 'graph_id', 'config']

        self._stream_df = pd.DataFrame(columns=self._stream_df_columns)
        self._node_df = pd.DataFrame(columns=self._node_df_columns)
        self._graph_df = graph_df

    def parse_config(self):
        # graph input stream
        streams = []
        for input_stream_pb in self.graph_pb.input_stream:
            tag, index, name = parse_tag_index_name(input_stream_pb)
            stream = Stream(input_stream_pb)
            self.graph_input_streams.add(input_stream_pb, stream)
            streams.append([StreamType.GRAPH_INPUT_STREAM, tag, index, name, input_stream_pb, stream, -1, 0])

        # graph output stream
        for output_stream_pb in self.graph_pb.output_stream:
            tag, index, name = parse_tag_index_name(output_stream_pb)
            stream = Stream(output_stream_pb)
            self.graph_output_streams.add(output_stream_pb, stream)
            streams.append([StreamType.GRAPH_OUTPUT_STREAM, tag, index, name, output_stream_pb, stream, -1, 0])

        # node input stream
        for node_id, node_pb in enumerate(self.graph_pb.node):
            for input_stream_pb in node_pb.input_stream:
                tag, index, name = parse_tag_index_name(input_stream_pb)
                stream = Stream(input_stream_pb)
                streams.append([StreamType.INPUT_STREAM, tag, index, name, input_stream_pb, stream, node_id, 0])

        # node output stream
        for node_id, node_pb in enumerate(self.graph_pb.node):
            for output_stream_pb in node_pb.output_stream:
                tag, index, name = parse_tag_index_name(output_stream_pb)
                stream = Stream(output_stream_pb)
                streams.append([StreamType.OUTPUT_STREAM, tag, index, name, output_stream_pb, stream, node_id, 0])

        df = pd.DataFrame(columns=self._stream_df_columns, data=streams)
        self._stream_df = pd.concat([self._stream_df, df], axis=0)

        # graph input stream connect input stream
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.GRAPH_INPUT_STREAM].iterrows():
            stream_name = row['name']
            stream = row['item']
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'] == StreamType.INPUT_STREAM) &
                (self._stream_df['name'] == stream_name)
            ].iterrows():
                stream.add_downstream(down_row['item'])

        # output stream connect input stream and graph output stream
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.OUTPUT_STREAM]:
            stream_name = row['name']
            stream = row['item']
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'].isin([StreamType.INPUT_STREAM, StreamType.GRAPH_OUTPUT_STREAM])) &
                (self._stream_df['name'] == stream_name)
            ].iterrows():
                stream.add_downstream(down_row['item'])

        # init node
        nodes = []
        for node_id, node_pb in enumerate(self.graph_pb.node):
            # check node exists
            node_type = node_pb.calculator
            node = None
            if CALCULATOR.get(node_type) is None and node_type not in self._graph_df.type:
                logger.error('Calculator {} not exists. Please registry it or add sub graph dependence.'
                             .format(node_type))
                sys.exit(1)
            elif CALCULATOR.get(node_type) is not None:
                node = CalculatorNode(node_pb)
            elif node_type in self._graph_df.type:
                # recursive
                sub_graph_pb = self._graph_df[self._graph_df['type'] == node_type]['config'][0]
                node = SubGraph(sub_graph_pb, self._graph_df)
                node.parse_config()
            nodes.append([node_pb.calculator, node, node_id, 0])
        df = pd.DataFrame(columns=self._node_df_columns, data=nodes)
        self._node_df = pd.concat([self._node_df, df], axis=0)

        # node or sub graph input stream connect input stream and output stream
        for index, row in self._node_df.iterrows():
            item = row['item']
            item_name = row['type']
            input_streams = self._stream_df[
                (self._stream_df['name'] == item_name) &
                (self._stream_df['type'] == StreamType.INPUT_STREAM)
            ]
            output_streams = self._stream_df[
                (self._stream_df['name'] == item_name) &
                (self._stream_df['type'] == StreamType.OUTPUT_STREAM)
            ]
            if isinstance(item, CalculatorNode):
                for stream_index, stream_row in input_streams.iterrows():
                    stream_tag_index_name = stream_row['tag_index_name']
                    stream = stream_row['item']
                    stream.add_downstream(item.input_stream_listener)
                    item.input_streams.add(stream_tag_index_name, stream)
                for stream_index, stream_row in output_streams.iterrows():
                    stream_tag_index_name = stream_row['tag_index_name']
                    stream = stream_row['item']
                    # stream.add_downstream(item.input_stream_listener)
                    item.output_streams.add(stream_tag_index_name, stream)
            elif isinstance(item, SubGraph):
                # sub graph GraphInputStream
                for stream_index, stream in enumerate(item.graph_input_streams):
                    # tag, index = stream.tag, stream.index
                    # parent graph InputStream
                    # generally only one result (one InputStream connect one SubGraph GraphInputStream)
                    for parent_index, parent_row in input_streams[
                        (input_streams['tag'] == stream.tag) &
                        (input_streams['index'] == stream.index)
                    ]:
                        parent_row['item'].add_downstream(stream)
                # sub graph GraphOutputStream
                for stream_index, stream in enumerate(item.graph_output_streams):
                    # tag, index = stream.tag, stream.index
                    # parent graph OutputStream
                    # generally only one result (one SubGraph GraphInputStream connect one parent OutputStream)
                    for parent_index, parent_row in output_streams[
                        (input_streams['tag'] == stream.tag) &
                        (input_streams['index'] == stream.index)
                    ]:
                        parent_row['item'].add_downstream(stream)


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
        self.input_streams = Collection()
        self.output_streams = Collection()

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
        self._graph_df = pd.DataFrame(columns=self._graph_df_columns, data=graphs)

        main_graph = SubGraph(configs[0], self._graph_df)
        main_graph.parse_config()
        self.input_streams = main_graph.graph_input_streams
        self.output_streams = main_graph.graph_output_streams

    def add_packet(self, tag=None, index=0, packet=None):
        stream = self.input_streams.get(tag, index)
        stream.add_packet(packet)
        stream.propagate_downstream()

    def get_packet(self, tag=None, index=0):
        stream = self.output_streams.get(tag, index)
        return stream.pop_left()

    def initialize_executors(self): ...

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self):
        for stream_index, stream_row in self._stream_df.iterrows():
            # 拼接stream
            name = stream_row['name']
            graph_id = stream_row['graph_id']
            node_id = stream_row['node_id']
            stream = stream_row['item']
            stream_class = stream_row['type']
            tag_index_name = stream_row['tag_index_name']
            if stream_class == StreamType.INPUT_STREAM:
                # 下游是同一个图的node，需要node的notyfy callback
                # 或者是另一个图的GraphInputStream
                next_nodes = self._node_df[
                    (self._node_df['node_id'] == node_id) &
                    (self._node_df['graph_id'] == graph_id)
                ]
                if len(next_nodes) == 0:
                    logger.warning('InputStream:"{}" did not find any connected node.'.format(tag_index_name))
                for next_node_index, next_node in next_nodes.iterrows():
                    node = next_node['item']
                    if isinstance(node, CalculatorNode):
                        node.input_streams.add(tag_index_name, stream)
                        stream.add_downstream(node)
                    else:
                        # sub graph
                        # 找到该子图的GraphInputStream
                        sub_graph_name = node.name
                        sub_graph_id =...
                        next_streams = self._stream_df[
                            (self._stream_df['type'] == sub_graph_name) &
                            (self._stream_df[''])
                        ]
            elif stream_class == StreamType.OUTPUT_STREAM:
                # 下游是同一个图的Input Stream、GraphOutputStream
                # 或者是另一个图的GraphInputStream
                next_streams = self._stream_df[
                    ((self._stream_df['name'] == name) &
                     (self._stream_df['graph_id'] == graph_id) &
                     (self._stream_df['type'].isin([InputStream, GraphOutputStream])) |
                    ((self._stream_df['type'] == GraphInputStream) &
                     (self._stream_df['graph_id'])))
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
