from enum import Enum
import queue
from collections import deque

class NodeReadiness(Enum):
    kNotReady = 0
    kReadyForProcess = 1
    kReadyForClose = 2


class InputStream:
    def __init__(self, notify_callback):
        # TODO set max len
        self._queue = deque()
        self.notify = notify_callback

    def add_packet(self, packet):
        self._queue.append(packet)
        self.notify()

    def get(self):
        """get and return item"""
        return self._queue[0]

    def __len__(self):
        return len(self._queue)

    def popleft(self):
        """get and pop left item in queue"""
        return self._queue.popleft()

class OutputStream:
    def __init__(self):
        self.mirrors = []
        # TODO set max len
        self._queue = deque()
    def __len__(self):
        return len(self._queue)
    def add_package(self, package):
        self._queue.append(package)

    def propogate_mirrors(self):
        packet = self._queue.popleft()
        for mirror in self.mirrors:
            mirror.add_packet(packet)

    def add_mirrors(self, mirrors):
        if not isinstance(mirrors, (list, tuple)):
            mirrors = [mirrors]
        if not isinstance(mirrors[0], InputStream):
            raise TypeError("mirror type should be InputStream")
        self.mirrors.extend(mirrors)
