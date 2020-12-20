import threading
from logzero import logger


class List:
    # TODO block
    def __init__(self, max_size=100):
        self.arr_lock = threading.Lock()
        self.max_size = max_size
        self.arr = []

    def __len__(self):
        return len(self.arr)

    def get_first(self):
        with self.arr_lock:
            item = None
            if len(self) != 0:
                item = self.arr[0]
        return item

    def pop_first(self):
        with self.arr_lock:
            item = None
            if len(self) != 0:
                item = self.arr.pop(0)
        return item

    def push_last(self, item):
        ret = None
        with self.arr_lock:
            if len(self) + 1 >= self.max_size:
                ret = self.arr.pop()
                logger.warn('current list size out of max size, remove {}'.format(ret))
            self.arr.append(item)
        return ret

    def clear(self):
        with self.arr_lock:
            self.arr.clear()
