import threading
from logzero import logger


class List:
    def __init__(self, max_size=100):
        self.cond = threading.Condition()
        self.max_size = 100 if max_size <= 0 else max_size
        self.arr = []

    def __len__(self):
        with self.cond:
            return len(self.arr)

    def get_first(self, blocking=None):
        with self.cond:
            item = None
            if blocking and len(self) == 0:
                self.cond.wait(blocking)
            if len(self) != 0:
                item = self.arr[0]
            return item

    def pop_first(self, blocking=None):
        with self.cond:
            item = None
            if blocking and len(self) == 0:
                self.cond.wait(blocking)
            if len(self) != 0:
                item = self.arr.pop(0)
            return item

    def push_last(self, item):
        with self.cond:
            ret = None
            if len(self) + 1 >= self.max_size:
                ret = self.arr.pop()
                logger.warn('current list size out of max size, remove %s', ret)
            self.arr.append(item)
            if len(self) == 1:
                self.cond.notify()
            return ret

    def clear(self):
        with self.cond:
            self.arr.clear()


