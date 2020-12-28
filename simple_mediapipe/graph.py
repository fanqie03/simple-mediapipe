from .counter import BasicCounterFactory
from .scheduler import Scheduler
from .calculator import CalculatorNode
# TODO remove pandas
import pandas as pd
from .stream import *
from .registration import CALCULATOR
from .collection import Collection
import sys


class SubGraph:
    def __init__(self, main_graph, graph_pb, graph_df):
        # self.name = name
        self.main_graph = main_graph
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
            stream = Stream(StreamType.GRAPH_INPUT_STREAM, input_stream_pb, max_size=self.graph_pb.max_queue_size)
            self.graph_input_streams.add(input_stream_pb, stream)
            streams.append([StreamType.GRAPH_INPUT_STREAM, tag, index, name, input_stream_pb, stream, -1, 0])

        # graph output stream
        for output_stream_pb in self.graph_pb.output_stream:
            tag, index, name = parse_tag_index_name(output_stream_pb)
            stream = Stream(StreamType.GRAPH_OUTPUT_STREAM, output_stream_pb, max_size=self.graph_pb.max_queue_size)
            self.graph_output_streams.add(output_stream_pb, stream)
            streams.append([StreamType.GRAPH_OUTPUT_STREAM, tag, index, name, output_stream_pb, stream, -1, 0])

        # node input stream
        for node_id, node_pb in enumerate(self.graph_pb.node):
            for input_stream_pb in node_pb.input_stream:
                tag, index, name = parse_tag_index_name(input_stream_pb)
                stream = Stream(StreamType.INPUT_STREAM, input_stream_pb, max_size=self.graph_pb.max_queue_size)
                streams.append([StreamType.INPUT_STREAM, tag, index, name, input_stream_pb, stream, node_id, 0])

        # node output stream
        for node_id, node_pb in enumerate(self.graph_pb.node):
            for output_stream_pb in node_pb.output_stream:
                tag, index, name = parse_tag_index_name(output_stream_pb)
                stream = Stream(StreamType.OUTPUT_STREAM, output_stream_pb, max_size=self.graph_pb.max_queue_size)
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
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.OUTPUT_STREAM].iterrows():
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
                logger.error('Calculator %s not exists. Please registry it or add sub graph dependence.', node_type)
                sys.exit(1)
            elif CALCULATOR.get(node_type) is not None:
                node = CalculatorNode(self.main_graph, node_pb)
                node.init_context()
            elif node_type in self._graph_df.type:
                # recursive
                sub_graph_pb = self._graph_df[self._graph_df['type'] == node_type]['config'][0]
                node = SubGraph(self.main_graph, sub_graph_pb, self._graph_df)
                node.parse_config()
            nodes.append([node_pb.calculator, node, node_id, 0])
        df = pd.DataFrame(columns=self._node_df_columns, data=nodes)
        self._node_df = pd.concat([self._node_df, df], axis=0)

        # node or sub graph input stream connect input stream and output stream
        for index, row in self._node_df.iterrows():
            item = row['item']
            item_name = row['type']
            node_id = row['node_id']
            input_streams = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
                (self._stream_df['type'] == StreamType.INPUT_STREAM)
            ]
            output_streams = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
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

        for node_row in nodes:
            item = node_row[1]
            if isinstance(item, CalculatorNode):
                item.init_context()
                item.calculator_base.get_contract(item._default_context)


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
        # validate_graph(input_config)
        self._validated_graph = input_config

        # TODO 待完善，会出现GraphInputStream连着GraphInputStream，GraphOutputStram连着GraphOutputGream
        self.parse_config([input_config] + deps_config)
        logger.info(self._stream_df)
        logger.info(self._node_df)
        logger.info(self._graph_df)

        self.initialize_executors(input_config.num_threads)
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

        sub_graph = SubGraph(self, configs[0], self._graph_df)
        # main_graph = SubGraph(1,2)
        sub_graph.parse_config()
        self.input_streams = sub_graph.graph_input_streams
        self.output_streams = sub_graph.graph_output_streams

    def add_packet(self, tag=None, index=0, packet=None):
        stream = self.input_streams.get(tag, index)
        stream.add_packet(packet)
        stream.propagate_downstream()

    def get_packet(self, tag=None, index=0, blocking=None):
        stream = self.output_streams.get(tag, index)
        return stream.get(blocking)

    def pop_packet(self, tag=None, index=0, blocking=None):
        stream = self.output_streams.get(tag, index)
        return stream.popleft(blocking)

    def initialize_executors(self, num_threads):
        self._scheduler.init_executor(num_threads)

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self):...

    def initialize_calculator_nodes(self):...

    def initialize_profiler(self): ...

    def start_run(self, extra_side_packet, stream_headers, blocking=True):
        # prepare run(extra_side_packet, stream_headers)
        self._scheduler.start(blocking=blocking)
        return True

    def __str__(self):
        return 'graph'

