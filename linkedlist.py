class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    def inse_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node
    def inse_at_end(self,data):
        if self.head is None:
            node=Node(data,self.head)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_value(self,index,data):
        if index<0 or index>self.get_len():
            raise Exception("Invalide input")
        if index==0:
            self.inse_at_beg(data)
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def del_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception("Invalid input")
        if index==0:
            self.head=self.head.next
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def print(self):
        if self.head is None:
            print("empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
if __name__=="__main__":
    ll=Linkedlist()
    ll.inse_at_beg(21)
    ll.inse_at_beg(23)
    ll.inse_at_end(45)
    ll.inse_at_end(48)
    ll.insert_value(2,56)
    ll.print()
    print("len:",ll.get_len())
    ll.del_at(4)
    ll.print()
    print("len:",ll.get_len())