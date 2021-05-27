""" First in First Out"""
class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.items)

