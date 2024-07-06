from collections import deque
class Queue:
    def __init__(self):
        self.buf=deque()
    def enqueue(self,data):
        self.buf.appendleft(data)
    def dequeue(self):
        return self.buf.pop()
    def is_empty(self):
        return len(self.buf)==0
    def size(self):
        return len(self.buf)
pq=Queue()
pq.enqueue({
    'company':'wal mart',
    'timestamp':'15 apr, 11:01 AM',
    'price':'131.10'

})
pq.enqueue({
    'company':'wal mart',
    'timestamp':'15 apr, 11:02 AM',
    'price':'141.10'

})
pq.enqueue({
    'company':'wal mart',
    'timestamp':'15 apr, 11:03 AM',
    'price':'151.10'

})
print(pq.buf)
print(pq.dequeue())
print(pq.buf)