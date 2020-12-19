from enum import Enum
import queue
from collections import deque
from .list import List


class NodeReadiness(Enum):
    kNotReady = 0
    kReadyForProcess = 1
    kReadyForClose = 2


class InputStream:
    """
    只有此stream才有唤醒node，进行任务调度的能力
    """
    def __init__(self, notify_callback, max_size=100):
        # TODO set max len
        self.max_size = max_size
        self._queue = List(self.max_size)
        self.notify = notify_callback

    def add_packet(self, packet):
        self._queue.push_last(packet)
        self.notify()

    def get(self):
        """get and return item"""
        return self._queue.get_first()

    def __len__(self):
        return len(self._queue)

    def popleft(self):
        """get and pop left item in queue"""
        return self._queue.pop_first()

    def clear(self):
        self._queue.clear()

    def __deepcopy__(self, memodict={}):
        copyobj = type(self)(self.notify, self.max_size)
        return copyobj


class OutputStream(InputStream):
    def __init__(self, max_size=100):
        super(OutputStream, self).__init__(None, max_size)
        self.mirrors = []

    def add_package(self, package):
        self._queue.push_last(package)

    def propagate_mirrors(self):
        if len(self.mirrors):
            packet = self._queue.pop_first()
            for mirror in self.mirrors:
                mirror.add_packet(packet)

    def add_mirrors(self, mirrors):
        if not isinstance(mirrors, (list, tuple)):
            mirrors = [mirrors]
        for mirror in mirrors:
            if mirror not in (InputStream.__class__, GraphOutputStream.__class__, GraphInputStream.__class__):
                raise TypeError("mirror type should be InputStream or GraphOutputStream or GraphInputStream")
        self.mirrors.extend(mirrors)

    def __deepcopy__(self, memodict={}):
        copyobj = type(self)(self.max_size)
        return copyobj


class GraphOutputStream(OutputStream):
    """
    上游是图内的OutputStream
    下游是无，或者是图外的InputStream，或者是另一个图的GraphInputStream
    当来一个package时，此stream为一个中转站，来一个出去一个，除非没有下游
    """
    def add_package(self, package):
        self._queue.push_last(package)
        self.propagate_mirrors()


class GraphInputStream(GraphOutputStream):
    """
    上游是无，或者是图外的OutputStream，或者是另一个图的GraphOutputStream
    下游是图内的InputStream
    当来一个package时，此stream为一个中转站，来一个出去一个，除非没有下游
    """
