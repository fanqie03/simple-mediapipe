import time
from typing import Union, Dict
from logzero import logger
from .tool import parse_tag_index_name


class Packet:

    _static_id = 0

    def __init__(
            self,
            data: Union[None, Dict] = None,
            timestamp: Union[None, float] = None,
            tag_index_name: Union[None, str] = None,
            packet_type: Union[None, "StreamType"] = None,
         ):
        # timestamp default unit is milli seconds
        self.data = data
        self.timestamp = timestamp or time.time()
        self.mirrors = []
        self.tag_index_name = tag_index_name
        self.packet_type = packet_type
        if tag_index_name is not None:
            # side packet have tag_index_name
            logger.info('create %s %s', packet_type, tag_index_name)
            self._id = Packet._static_id
            Packet._static_id += 1
            self.tag, self.index, self.name = parse_tag_index_name(tag_index_name)
        else:
            self._id = None

    def get(self):
        return self.data

    def set(self, data):
        logger.debug('%s set %s', self, data)
        self.data = data
        for mirror in self.mirrors:
            logger.debug('%s propagate to mirror %s', self, mirror)
            mirror.set(data)

    def add_mirror(self, mirror):
        logger.info('%s add mirror packet %s', self, mirror)
        self.mirrors.append(mirror)

    def __str__(self):
        return 'Packet:{}_{}, Timestamp: {}, Data: {}'.format(self.tag_index_name, self._id,
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.timestamp)), self.data)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __ge__(self, other):
        return self.timestamp >= other.timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __ne__(self, other):
        return self.timestamp != other.timestamp
