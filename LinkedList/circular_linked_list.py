class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


class CircularLinkedList:
    def __init__(self):
        self.head = None 

  
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def is_circular_linked_list(self, input_list):
        if input_list.head:
            cur = input_list.head
            while cur.next:
                cur = cur.next
                if cur.next == input_list.head:
                    return True
            return False
        else:
            return False

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))