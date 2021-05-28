from typing import Counter


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        new_node  = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            self.head.prev = new_node
            new_node.next  = self.head
            self.head      = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def add_node_before(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                
                # Make space
                prev.next = new_node
                cur.prev = new_node
                
                # Fit in
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next

    def add_node_after(self, key, data):
        new_node = Node(data)
        cur = self.head
        prev = None

        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                prev = cur.next
                
                # make room
                cur.next  = new_node
                prev.prev = new_node
                
                # fit in
                new_node.next = prev
                new_node.prev = cur
                return
            cur = cur.next

    def delete_node_key(self, key):
        
        cur = self.head
        while cur:
            print("insi: ",key)
            # head
            if cur.data == key and cur == self.head:
                # Case 1: delete only Node
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # Case 2: delete head
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # Case 3: other than head where cur.next is not None #
                if cur.next:
                    print("here")
                    # get next and prev
                    nxt  = cur.next
                    prev = cur.prev
                    
                    # make room
                    prev.next = nxt
                    nxt.prev  = prev

                    # Delete
                    cur.next = None
                    cur.prev = None

                    cur = None
                    return
                else:
                # Case 4: Delete node not head, where cur.next is None = > Tail
                    prev = cur.prev
                    prev.next = None
                    cur.prev  = None
                    cur       = None
                    return
            cur = cur.next
              
    def reverse(self):
        tmp =  None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        cur = self.head
        duplicates = dict()
        while cur:
            if cur.data not in duplicates:
                duplicates[cur.data] = 1
                cur = cur.next
                
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt
                
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    def pair_with_sums(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if (p.data + q.data) == sum_val:
                    pairs.append(f'({p.data},{q.data})')
                q = q.next
            p = p.next
        return pairs




doubly = DoublyLinkedList()
doubly.append(1)
doubly.append(2)
doubly.append(3)
doubly.append(3)
doubly.append(4)
doubly.prepend(5)
# doubly.add_node_before("G","H")
# doubly.add_node_after("G","Z")
doubly.print_list()

# print("Reverse: ")
# doubly.reverse()

# print(doubly.pair_with_sums(6))
# print("remove duplicates: ")
doubly.remove_duplicates()

# print("Delete Case: ","")
# doubly.delete_node("D")
# doubly.delete_node("H")
# doubly.delete_node("C")
# doubly.delete_node("Z")
doubly.print_list()
