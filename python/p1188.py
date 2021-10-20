from threading import Lock, Semaphore
from collections import deque


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = deque()
        self.lock = Lock()
        self.enq = Semaphore(capacity)
        self.deq = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.enq.acquire()
        self.lock.acquire()
        self.q.append(element)
        self.lock.release()
        self.deq.release()

    def dequeue(self) -> int:
        self.deq.acquire()
        self.lock.acquire()
        ret = self.q.popleft()
        self.lock.release()
        self.enq.release()
        return ret

    def size(self) -> int:
        return len(self.q)
