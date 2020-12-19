from queue import LifoQueue,Queue
from collections import deque


class Packet:
    def __init__(self, data=None, timestamp=0):
        self.data = data
        self.timestamp = timestamp

    def __str__(self):
        return 'Timestamp: {}, Data: {}'.format(self.timestamp, self.data)

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


if __name__ == '__main__':

    lst = [Packet(timestamp=1), Packet(timestamp=0), Packet(timestamp=-1), Packet(timestamp=0)]
    print(lst)
    # lst.sort()
    # print(lst)
    import queue

    q = queue.PriorityQueue()
    for i in lst:
        q.put(i)
    while not q.empty():
        print(q.get())
        q.get()
    dq = queue.Queue()

    q = deque()
    q.extend([1,2,3])
    print(q)
    print(len(q))
    print(q[0])
    print(q.popleft())
    # print()