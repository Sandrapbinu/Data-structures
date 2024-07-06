from collections import deque

class Stack:
    def __init__(self):
        self.st=deque()
    def push(self,data):
        self.st.append(data)
    def pop(self):
        return self.st.pop()
    def peek(self):
        return self.st[-1]
    def is_empty(self):
        return len(self.st)==0
    def size(self):
        return len(self.st)

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.pop())
print(s.peek())
print(s.is_empty())
print(s.size())