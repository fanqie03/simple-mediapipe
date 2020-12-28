from queue import LifoQueue,Queue
from collections import deque
from simple_mediapipe.packet import Packet

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