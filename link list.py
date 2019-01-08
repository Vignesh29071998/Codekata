class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=node(data)
    def display(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
l=linkedlist()
l.head=node(10)
for i in range(20,100,10):
    l.insert(i)
l.display()
        


        
