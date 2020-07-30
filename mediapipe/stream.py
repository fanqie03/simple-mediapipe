from enum import Enum
import queue


class NodeReadiness(Enum):
    kNotReady = 0
    kReadyForProcess = 1
    kReadyForClose = 2


class InputStream:
    def __init__(self, notify_callback):
        self._queue = queue.Queue()
        self.notify = notify_callback

    def add_packet(self, packet):
        self._queue.put(packet)
        self.notify()

class OutputStream:
    def __init__(self):
        self._propogate_queue = queue
        self.mirrors = []

    def add_mirrors(self, mirrors):
        if not isinstance(mirrors, (list, tuple)):
            mirrors = [mirrors]
        self.mirrors.extend(mirrors)



    def propogate_to_mirrors(self):
        for
        for mirror in self.mirrors:
            mirror.add_packet()