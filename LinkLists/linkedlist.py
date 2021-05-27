from typing import Counter


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None  

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        """At end of LL"""
        new_node = Node(data)

        if self.head is None:       # if empty
            self.head = new_node 
            return                  # break if first entry
        
        last_node = self.head       # This implies we’re at the start of the linked list
        
        while last_node.nextNode:
            last_node = last_node.nextNode
        last_node.nextNode = new_node

    def print_list(self):
        cur_node = self.head    
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.nextNode

    def get_size(self):
        cur_node = self.head    
        counter = 0 
        while cur_node:
            counter +=1
            cur_node = cur_node.nextNode
        return counter

    def prepend(self, data):
        new_node = Node(data)
        new_node.nextNode = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node.nextNode = prev_node.nextNode
        prev_node.nextNode = new_node
    
    def insert_pos(self, pos, data): # 3, E
        current = self.head
        counter = 0
        Temp = Node(data)

        Prev = None

        if pos <0 or pos > self.get_size():
            print("invalid index")
            
        elif pos == 0:
           Temp.nextNode = self.head
           self.head     = Temp

        else:
            while counter < pos:
                Prev    = current
                current = current.nextNode
                counter +=1
            
            Temp.nextNode = Prev.nextNode
            Prev.nextNode = Temp
            # current = Temp

    def del_node_pos(self, pos):
        if self.head:
            current = self.head
            if pos == 0:
                self.head = current.nextNode
                current = None
                return
            
            prev = None
            counter = 0
            while current and counter != pos:
                prev = current
                current = current.nextNode
                print("cur: ",current.data)
                counter +=1
            
            if current is None:
                print("not found")
                return
            prev.nextNode = current.nextNode
            current = None

    def del_node(self, key):
        cur_node = self.head

        # Delete Head
        if cur_node and cur_node.data == key:
            self.head = cur_node.nextNode
            cur_node - None
            return
        

        prev = None
        while cur_node and cur_node.data !=key:
            prev = cur_node
            cur_node = cur_node.nextNode
        
        if cur_node is None:
            return
        
        prev.nextNode = cur_node.nextNode
        cur_node = None

    def swap_nodes_keys(self, key_1, key_2):
        
        if key_1 == key_2:
            return

        current = self.head 
        previous = None
        
        # Check if key_1 is not tail, and not the key_2
        # move to next until current.data == key
        while current and current.data != key_1:
            previous = current
            current  = current.nextNode
        
        # Check if key_2 is not tail, and not the key_2
        previous_2 = None
        current_2  = self.head
        while current_2 and current_2.data != key_2:
            previous_2 = current_2
            current_2  = current_2.nextNode

        # if not found
        if not current or not current_2:
            return

        # if found swap 
        if previous:
            print("prev_1: ",previous.data)
            previous.nextNode = current_2
        else:
            self.head = current_2
        
        if previous_2:
            print("prev_2: ",previous_2.data)
            previous_2.nextNode = current
        else:
            self.head = current
        
        print("cur_1: ",current.data)
        print("cur_2: ",current_2.data)
        current.nextNode, current_2.nextNode = current_2.nextNode, current.nextNode

    def rotate(self, k):
        if self.head and self.head.nextNode:
            p = self.head 
            q = self.head 
            prev = None
            count = 0
            
            while p and count < k:
                prev = p
                p = p.nextNode 
                q = q.nextNode 
                count += 1
            p = prev
            while q:
                prev = q 
                q = q.nextNode 
            q = prev 
            # print("q= ",q.data)
            
            q.nextNode = self.head 
            self.head = p.nextNode 
            p.nextNode = None

        
    def reverse_iterative(self):
         
        # Set up current,previous, and next nodes
        prev = None
        cur  = self.head
        nxt  = None

        # until we have gone through to the end of the list 
        while cur:

            # Make sure to copy the current nodes next node to a variable next_node
            # Before overwriting as the previous node for reversal
            nxt = cur.nextNode

            # Reverse the pointer ot the next_node
            cur.nextNode = prev

            # Go one forward in the list
            prev = cur
            cur  = nxt

        self.head = prev


    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            
            nxt = cur.nextNode
            cur.nextNode = prev
            prev = cur
            cur  = nxt
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None) 

    def merged_sorted(self, llist):
        q = llist.head
        p = self.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:

            if p.data <= q.data:
                print("L2 is larger")
                s = p
                p = s.nextNode
            else:
                print("L1 is larger")
                s = q 
                q = s.nextNode
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.nextNode = p
                s = p
                p = s.nextNode
            else:
                s.nextNode = q
                s = q
                q = s.nextNode
        
        if not p:
            s.nextNode = q
        
        if not q:
            s.nextNode = p

        self.head = new_head
        return self.head


    def remove_duplicates(self):
        cur = self.head
        prev = None
        duplicates = dict()

        while cur:
            if cur.data in duplicates:
                # Remove Node
                prev.nextNode = cur.nextNode
                cur = None
            else:
                # new element
                duplicates[cur.data] = 1
                prev = cur
            cur = prev.nextNode

    def nth_to_last(self, nth):
        total_len = self.get_size()
        cur = self.head

        while cur:

            if total_len == nth:
                # element
                print("element: ",cur.data)
                return cur.data
            
            total_len -=1
            cur  = cur.nextNode
        
        # not found
        if cur is None:
            return

    def print_nth_from_last(self, n):
        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.nextNode

            # print("q: ",q.data)    
      
            while p and q.nextNode:
                print("p: ", p.data)
                print("q: ", q.data)
                p = p.nextNode
                q = q.nextNode
                print("after: ", q.data)    
            return p.data
        else:
            return None           

    def count_occurances_iterative(self, data):
        count = 0
        cur = self.head

        while cur:
            if cur.data == data:
                count +=1
            cur = cur.nextNode
        return count
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0 
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)


llist_1 = LinkedList()
llist_1.append(1)
llist_1.append(2)
llist_1.append(3)
llist_1.append(4)
llist_1.append(5)
llist_1.rotate(4)
# print("count =",llist_1.count_occurances_iterative(5))
# llist_2 = LinkedList()
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
# llist_1.merged_sorted(llist_2)

# llist.insert_after_node()
llist_1.print_list()

# llist_1.print_nth_from_last(4)

# print("Swapping")
# llist_2.print_list()
# llist.swap_nodes_keys("D","F")
# llist.append("C")
# llist.prepend("D")
# llist.append("E")
# llist.append("F")
# # llist.get_size()
# llist.del_node("B")
# llist.insert_pos(4,"G")
# llist.del_node_pos(7)
# llist.reverse_iterative()
# llist.reverse_recursive()

# # llist.insert_after_node(llist.head.nextNode, "C")
# llist.print_list()


# class LinkedListNode(object):
    
#     def __init__(self,value):        
#         self.value = value
#         self.nextnode = None

# a = LinkedListNode(1)
# b = LinkedListNode(2)
# c = LinkedListNode(3)
# a.nextnode = b
# b.nextnode = c
