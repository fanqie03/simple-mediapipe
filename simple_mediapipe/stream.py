from .list import List
from types import MethodType, FunctionType
from logzero import logger
import sys
from .tool import parse_tag_index_name
from .packet import Packet


class StreamType:
    INPUT_STREAM = "INPUT_STREAM"
    OUTPUT_STREAM = "OUTPUT_STREAM"
    INPUT_SIDE_PACKET = "INPUT_SIDE_PACKET"
    OUTPUT_SIDE_PACKET = "OUTPUT_SIDE_PACKET"
    GRAPH_INPUT_STREAM = "GRAPH_INPUT_STREAM"
    GRAPH_OUTPUT_STREAM = "GRAPH_OUTPUT_STREAM"


class Stream:
    def __init__(self, stream_type, tag_index_name, downstream=None, max_size=100):
        self.max_size = max_size
        self._queue = List(self.max_size)
        # single callback or list of Stream
        self.downstream = downstream
        self.tag_index_name = tag_index_name
        self.stream_type = stream_type
        self.tag, self.index, self.name = parse_tag_index_name(self.tag_index_name)

    def __str__(self):
        return '{}:"{}", current queue size is {}'.format(self.stream_type, self.tag_index_name, len(self))

    def add_packet(self, packet: Packet):
        self._queue.push_last(packet)

    def add_downstream(self, downstream):
        logger.info('stream <%s> add downstream <%s>', self, downstream)
        if isinstance(downstream, (MethodType, FunctionType)) and self.downstream is None:
            self.downstream = downstream
        elif not isinstance(downstream, (list, tuple)):
            downstream = [downstream]
            if not isinstance(downstream[0], Stream):
                logger.error('downstream should be Stream or Method')
                sys.exit(1)
            if self.downstream is None:
                self.downstream = []
            self.downstream.extend(downstream)
        else:
            logger.error('unknown situation')

    def propagate_downstream(self):
        if self.downstream is None:
            logger.debug('Stream %s, downstream is None', self)
            return
        elif isinstance(self.downstream, (MethodType, FunctionType)):
            self.downstream()
        elif len(self.downstream):
            packet = self._queue.pop_first()
            for downstream in self.downstream:
                downstream.add_packet(packet)
                # recursive
                downstream.propagate_downstream()

    def get(self, blocking=None) -> Packet:
        """get and return item"""
        return self._queue.get_first(blocking)

    def __len__(self):
        return len(self._queue)

    def popleft(self, blocking=None) -> Packet:
        """get and pop left item in queue"""
        return self._queue.pop_first(blocking)

    def clear(self):
        self._queue.clear()

    def __deepcopy__(self, memodict={}):
        copyobj = type(self)(self.stream_type, self.tag_index_name, self.downstream, self.max_size)
        return copyobj
