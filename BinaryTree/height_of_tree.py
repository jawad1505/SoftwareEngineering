class Stack(object):
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == 0

    def get_stack(self):
        return self.items
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        print("stack = ",self.get_stack())

        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Queue(object):
    def __init__(self) -> None:
        self.items = []
    
    def enqueue (self, item):
        self.items.insert(0, item)

    def dequeue (self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left  = None

class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
  
    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        # print("items = ",queue.size())

        while len(queue) > 0:
            # print(queue.peek(), len(queue))
            
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
            
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        
        return traversal

    def height(self, node):
        if node is None:
            return -1

        left_height  = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


    def size_(self, node):
        pass
 
# Calculate height of binary tree:
#       1
#      / \
#     2  3
#    / \
#   4  5
#  / \
# 6   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.left.left = Node(6)
tree.root.left.left.right = Node(7)
tree.root.left.right = Node(5)

print(tree.height(tree.root))