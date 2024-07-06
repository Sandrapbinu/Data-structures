from collections import deque

class Stack:
    def __init__(self):
        self.st=deque()
    def push(self,data):
        self.st.append(data)
    def pop(self):
        return self.st.pop()
    def is_empty(self):
        return len(self.st)==0
    def size(self):
        return len(self.st)
    def peek(self):
        return self.st[-1]
def rev(s):
    sta=Stack()
    for ch in s:
        sta.push(ch)
    re=''
    while sta.size()!=0:
        re+=sta.pop()
    print(re)
if __name__=="__main__":
    rev("We will conquere COVI-19")