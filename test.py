class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        # if not empty
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

ll = LinkedList()
ll.print_list()
ll.append("A")
ll.print_list()
ll.append("B")
ll.print_list()
ll.append("C")
ll.print_list()
