from .scheduler import Scheduler
from .calculator import CalculatorNode
# TODO remove pandas
import pandas as pd
from .stream import *
from .registration import CALCULATOR
from .collection import Collection
import sys
from .tool import parse_side_packets, parse_tag_index_name


class SubGraph:
    def __init__(self, main_graph, graph_pb, graph_df):
        # self.name = name
        self.main_graph = main_graph
        self.graph_pb = graph_pb
        # self.id = id
        self.graph_input_streams = Collection()
        self.graph_output_streams = Collection()
        self.node_input_side_packets = Collection()
        self.node_output_side_packets = Collection()
        self.graph_input_side_packets = Collection()
        self.graph_output_side_packets = Collection()

        self._stream_df_columns = ['type', 'tag', 'index', 'name', 'tag_index_name', 'item', 'node_id', 'graph_id']
        self._node_df_columns   = ['type', 'item', 'node_id', 'graph_id']
        self._graph_df_columns  = ['type', 'item', 'graph_id', 'config']

        self._stream_df = pd.DataFrame(columns=self._stream_df_columns)
        self._node_df = pd.DataFrame(columns=self._node_df_columns)
        self._graph_df = graph_df

    def parse_config(self):
        # graph input stream
        streams = []
        return_streams = []
        for input_stream_pb in self.graph_pb.input_stream:
            tag, index, name = parse_tag_index_name(input_stream_pb)
            stream = Stream(StreamType.GRAPH_INPUT_STREAM, input_stream_pb, max_size=self.graph_pb.max_queue_size)
            self.graph_input_streams.add(input_stream_pb, stream)
            streams.append([StreamType.GRAPH_INPUT_STREAM, tag, index, name, input_stream_pb, stream, -1, 0])
            return_streams.append(stream)

        # graph output stream
        for output_stream_pb in self.graph_pb.output_stream:
            tag, index, name = parse_tag_index_name(output_stream_pb)
            stream = Stream(StreamType.GRAPH_OUTPUT_STREAM, output_stream_pb, max_size=self.graph_pb.max_queue_size)
            self.graph_output_streams.add(output_stream_pb, stream)
            streams.append([StreamType.GRAPH_OUTPUT_STREAM, tag, index, name, output_stream_pb, stream, -1, 0])
            return_streams.append(stream)

        # graph input side packet
        for input_side_packet_pb in self.graph_pb.input_side_packet:
            tag, index, name = parse_tag_index_name(input_side_packet_pb)
            packet = Packet(packet_type=StreamType.GRAPH_INPUT_SIDE_PACKET, tag_index_name=input_side_packet_pb)
            streams.append([StreamType.GRAPH_INPUT_SIDE_PACKET, tag, index, name, input_side_packet_pb, packet, -1, 0])
            return_streams.append(packet)
            self.graph_input_side_packets.add(input_side_packet_pb, packet)

        # graph output side packet
        for output_side_packet_pb in self.graph_pb.output_side_packet:
            tag, index, name = parse_tag_index_name(output_side_packet_pb)
            packet = Packet(packet_type=StreamType.GRAPH_OUTPUT_SIDE_PACKET, tag_index_name=output_side_packet_pb)
            streams.append([StreamType.GRAPH_OUTPUT_SIDE_PACKET, tag, index, name, output_side_packet_pb, packet, -1, 0])
            return_streams.append(packet)
            self.graph_output_side_packets.add(output_side_packet_pb, packet)

        # node input and output
        for node_id, node_pb in enumerate(self.graph_pb.node):
            # node input stream
            for input_stream_pb in node_pb.input_stream:
                tag, index, name = parse_tag_index_name(input_stream_pb)
                stream = Stream(StreamType.INPUT_STREAM, input_stream_pb, max_size=self.graph_pb.max_queue_size)
                streams.append([StreamType.INPUT_STREAM, tag, index, name, input_stream_pb, stream, node_id, 0])
                return_streams.append(stream)
            # node output stream
            for output_stream_pb in node_pb.output_stream:
                tag, index, name = parse_tag_index_name(output_stream_pb)
                stream = Stream(StreamType.OUTPUT_STREAM, output_stream_pb, max_size=self.graph_pb.max_queue_size)
                streams.append([StreamType.OUTPUT_STREAM, tag, index, name, output_stream_pb, stream, node_id, 0])
                return_streams.append(stream)
            # node input side packet
            for input_side_packet_pb in node_pb.input_side_packet:
                tag, index, name = parse_tag_index_name(input_side_packet_pb)
                packet = Packet(packet_type=StreamType.INPUT_SIDE_PACKET, tag_index_name=input_side_packet_pb)
                streams.append([StreamType.INPUT_SIDE_PACKET, tag, index, name, input_side_packet_pb, packet, node_id, 0])
                return_streams.append(packet)
                self.node_input_side_packets.add(input_side_packet_pb, packet)
            # node output side packet
            for output_side_packet_pb in node_pb.output_side_packet:
                tag, index, name = parse_tag_index_name(output_side_packet_pb)
                packet = Packet(packet_type=StreamType.OUTPUT_SIDE_PACKET, tag_index_name=output_side_packet_pb)
                streams.append([StreamType.OUTPUT_SIDE_PACKET, tag, index, name, output_side_packet_pb, packet, node_id, 0])
                return_streams.append(packet)
                self.node_output_side_packets.add(output_side_packet_pb, packet)

        df = pd.DataFrame(columns=self._stream_df_columns, data=streams)
        self._stream_df = pd.concat([self._stream_df, df], axis=0)

        # graph input stream connect input stream
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.GRAPH_INPUT_STREAM].iterrows():
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'] == StreamType.INPUT_STREAM) &
                (self._stream_df['name'] == row['name'])
            ].iterrows():
                row['item'].add_downstream(down_row['item'])

        # output stream connect input stream and graph output stream
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.OUTPUT_STREAM].iterrows():
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'].isin([StreamType.INPUT_STREAM, StreamType.GRAPH_OUTPUT_STREAM])) &
                (self._stream_df['name'] == row['name'])
            ].iterrows():
                row['item'].add_downstream(down_row['item'])

        # graph input side packet connect node input side packet
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.GRAPH_INPUT_SIDE_PACKET].iterrows():
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'].isin([StreamType.INPUT_SIDE_PACKET])) &
                (self._stream_df['name'] == row['name'])
            ].iterrows():
                row['item'].add_mirror(down_row['item'])
        # node output side packet connect graph output side packet
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.OUTPUT_SIDE_PACKET].iterrows():
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'].isin([StreamType.GRAPH_OUTPUT_SIDE_PACKET])) &
                (self._stream_df['name'] == row['name'])
            ].iterrows():
                row['item'].add_mirror(down_row['item'])
        # node output side packet connect node input side packet
        for index, row in self._stream_df[self._stream_df['type'] == StreamType.OUTPUT_SIDE_PACKET].iterrows():
            for down_index, down_row in self._stream_df[
                (self._stream_df['type'].isin([StreamType.INPUT_SIDE_PACKET])) &
                (self._stream_df['name'] == row['name'])
            ].iterrows():
                row['item'].add_mirror(down_row['item'])

        # init node
        return_nodes = []
        nodes = []
        for node_id, node_pb in enumerate(self.graph_pb.node):
            # check node exists
            node_type = node_pb.calculator
            node = None
            if CALCULATOR.get(node_type) is None and node_type not in self._graph_df.type.tolist():
                logger.error('Calculator %s not exists. Please registry it or add sub graph dependence.', node_type)
                sys.exit(1)
            elif CALCULATOR.get(node_type) is not None:
                node = CalculatorNode(self.main_graph, node_pb)
                node.init_context()
                return_nodes.append(node)
                logger.debug('init calculator %s complete', node)
            elif node_type in self._graph_df.type.tolist():
                # recursive
                sub_graph_pb = self._graph_df[self._graph_df['type'] == node_type]['config'].iloc[0]
                node = SubGraph(self.main_graph, sub_graph_pb, self._graph_df)
                sub_nodes, sub_streams = node.parse_config()
                return_nodes.extend(sub_nodes)
                logger.debug('init sub graph  %s complete', node_type)
            nodes.append([node_pb.calculator, node, node_id, 0])
        df = pd.DataFrame(columns=self._node_df_columns, data=nodes)
        self._node_df = pd.concat([self._node_df, df], axis=0)

        # node or sub graph input stream connect input stream and output stream
        # TODO node add side packet
        # node connect node input side packet
        # node connect node output side packet
        for index, row in self._node_df.iterrows():
            item, item_name, node_id = row['item'], row['type'], row['node_id']
            input_streams = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
                (self._stream_df['type'] == StreamType.INPUT_STREAM)
            ]
            output_streams = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
                (self._stream_df['type'] == StreamType.OUTPUT_STREAM)
            ]
            input_side_packets = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
                (self._stream_df['type'] == StreamType.INPUT_SIDE_PACKET)
            ]
            output_side_packets = self._stream_df[
                (self._stream_df['node_id'] == node_id) &
                (self._stream_df['type'] == StreamType.OUTPUT_SIDE_PACKET)
            ]
            if isinstance(item, CalculatorNode):
                for stream_index, stream_row in input_streams.iterrows():
                    stream_tag_index_name, stream = stream_row['tag_index_name'], stream_row['item']
                    stream.add_downstream(item.input_stream_listener)
                    item.input_streams.add(stream_tag_index_name, stream)
                for stream_index, stream_row in output_streams.iterrows():
                    stream_tag_index_name, stream = stream_row['tag_index_name'], stream_row['item']
                    # stream.add_downstream(item.input_stream_listener)
                    item.output_streams.add(stream_tag_index_name, stream)
                for packet_index, packet_row in input_side_packets.iterrows():
                    packet_tag_index_name, packet = packet_row['tag_index_name'], packet_row['item']
                    item.input_side_packets.add(packet_tag_index_name, packet)
                for packet_index, packet_row in output_side_packets.iterrows():
                    packet_tag_index_name, packet = packet_row['tag_index_name'], packet_row['item']
                    item.output_side_packets.add(packet_tag_index_name, packet)

            elif isinstance(item, SubGraph):
                # parent node input stream connect sub graph GraphInputStream
                for stream_index, stream in enumerate(item.graph_input_streams):
                    # tag, index = stream.tag, stream.index
                    # parent graph InputStream
                    # generally only one result (one InputStream connect one SubGraph GraphInputStream)
                    for parent_index, parent_row in input_streams[
                        (input_streams['tag'] == stream.tag) &
                        (input_streams['index'] == stream.index)
                    ].iterrows():
                        parent_row['item'].add_downstream(stream)
                # sub graph GraphOutputStream connect parent node output stream
                for stream_index, stream in enumerate(item.graph_output_streams):
                    # tag, index = stream.tag, stream.index
                    # parent graph OutputStream
                    # generally only one result (one SubGraph GraphInputStream connect one parent OutputStream)
                    for parent_index, parent_row in output_streams[
                        (output_streams['tag'] == stream.tag) &
                        (output_streams['index'] == stream.index)
                    ].iterrows():
                        stream.add_downstream(parent_row['item'])
                # parent node input side packet connect sub graph input side packet
                for packet_index, packet in enumerate(item.graph_input_side_packets):
                    for parent_index, parent_row in input_side_packets[
                        (input_side_packets['tag'] == packet.tag) & (input_side_packets['index'] == packet.index)
                    ].iterrows():
                        parent_row['item'].add_mirror(packet)
                # sub graph output side packet connect parent node output side packet
                for packet_index, packet in enumerate(item.graph_output_side_packets):
                    for parent_index, parent_row in output_side_packets[
                        (output_side_packets['tag'] == packet.tag) & (output_side_packets['index'] == packet.index)
                    ].iterrows():
                        packet.add_mirror(parent_row['item'])

        for node_row in nodes:
            item = node_row[1]
            if isinstance(item, CalculatorNode):
                item.init_context()
                item.calculator_base.get_contract(item._default_context)
        return return_nodes, return_streams


class CalculatorGraph:
    def __init__(self):
        self._scheduler = Scheduler(self)
        # TODO
        self._profiler = None
        self._initialized = False
        self._nodes = None
        self._streams = None
        self.input_streams = Collection()
        self.output_streams = Collection()
        self.input_side_packets = Collection()
        self.output_side_packets = Collection()

        self._graph_df_columns = ['type', 'item', 'graph_id', 'config']
        self._graph_df = pd.DataFrame(columns=self._graph_df_columns)

    def add_task(self, task_node):
        self._scheduler.add_task(task_node)

    def initialize(self, input_config, deps_config=[], side_packets={}):
        """

        :param config: type of CalculatorGraphConfig
        :return:
        """
        if self._initialized:
            logger.warming("CalculatorGraph can be initialized only once.")
            return

        # TODO 待完善，会出现GraphInputStream连着GraphInputStream，GraphOutputStram连着GraphOutputGream
        self.parse_config([input_config] + deps_config)
        logger.debug(self._graph_df)

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
        self._nodes, self._streams = sub_graph.parse_config()
        self.input_streams = sub_graph.graph_input_streams
        self.output_streams = sub_graph.graph_output_streams
        self.input_side_packets = sub_graph.node_input_side_packets
        self.output_side_packets = sub_graph.node_output_side_packets

    def add_packet_to_input_stream(self, tag=None, index=0, packet=None):
        stream = self.input_streams.get(tag, index)
        stream.add_packet(packet)
        stream.propagate_downstream()

    def get_packet_from_output_stream(self, tag=None, index=0, blocking=None):
        return self.output_streams.get(tag, index).get(blocking)

    def get_output_side_packet(self, tag=None, index=0):
        return self.output_side_packets.get(tag, index).get()

    def pop_packet(self, tag=None, index=0, blocking=None):
        stream = self.output_streams.get(tag, index)
        return stream.popleft(blocking)

    def initialize_executors(self, num_threads):
        self._scheduler.init_executor(num_threads)

    def initialize_packet_generator_graph(self, side_packets): ...

    def initialize_streams(self):...

    def initialize_calculator_nodes(self):
        # 检查source node
        for node in self._nodes:
            if node.is_source():
                self.add_task(node)

    def initialize_profiler(self): ...

    def prepare_run(self, extra_side_packet, stream_headers):
        kv = parse_side_packets(extra_side_packet)
        for side_packet_name, side_packet_value in kv.items():
            for packet in self.input_side_packets:
                if packet.name == side_packet_name:
                    packet.set(side_packet_value)

    def start_run(self, extra_side_packet, stream_headers, blocking=True):
        self.prepare_run(extra_side_packet, stream_headers)
        self._scheduler.start(blocking=blocking)
        return True

    def __str__(self):
        return 'graph'

