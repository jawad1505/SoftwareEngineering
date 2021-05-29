class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left  = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    
    def preorder_print(self, start, traversal):
        """
        1. Check if current node is None/empty.
        2. Display the data part of root/current.
        3. Traverse the left subtree by recursively calling pre order method.
        4. Traverse the right subtree by recursively calling the pre order method.
        """
        pass

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left  = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left  = Node(6)
tree.root.right.right = Node(7)
