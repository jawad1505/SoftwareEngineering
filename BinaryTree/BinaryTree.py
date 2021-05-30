class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left  = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        else:
            print("Traversal Type " + str(traversal_type) + "is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """
           Root -> Left -> Right
        1. Check if current node is None/empty.
        2. Display the data part of root/current.
        3. Traverse the left subtree by recursively calling pre order method.
        4. Traverse the right subtree by recursively calling the pre-order method.
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        """
            Left -> Root -> Right
        1. Check if current node in None/empty.
        2. Traverse the left subtree by recursively calling the in-order method.
        3. Display the data part of the root (current node).
        4. Traverse the rigth subtree by recursively calling the in-order method.
        """
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal +=(str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """
            Left -> Right -> Root
        1. Check if the current node is None/empty.
        2. Traverse the left subtree by recursively calling the post-order method.
        3. Traverse the right subtree bt recursively calling the post-order method.
        4. Display the data part of the root (or current node).
        """
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# tree = BinaryTree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left  = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left  = Node(6)
# tree.root.right.right = Node(7)

# Tree 2:
#            A             
#         /     \
#        B       H
#       / \       \
#      F   Z       K
#         / \       \
#        D   I       G
# tree = BinaryTree("A")

# tree.root.left = Node("B")
# tree.root.left.left  = Node("F")
# tree.root.left.right = Node("Z")
# tree.root.left.right.left  = Node("D")
# tree.root.left.right.right = Node("I")

# tree.root.right = Node("H")
# tree.root.right.right = Node("K")
# tree.root.right.right.right = Node("G")



# Tree 3:
#            A             
#         /     \
#        B       H
#       / \       \
#      F   Z       K
#         / \     / \
#        D   I   G   M
tree = BinaryTree("A")

tree.root.left = Node("B")
tree.root.left.left  = Node("F")
tree.root.left.right = Node("Z")
tree.root.left.right.left  = Node("D")
tree.root.left.right.right = Node("I")

tree.root.right = Node("H")
tree.root.right.right = Node("K")
tree.root.right.right.right = Node("M")
tree.root.right.right.left = Node("G")

print("Pre order= ",tree.print_tree("preorder"),"")
# print("Post order= ",tree.print_tree("postorder"),"")
# print("In order= ",tree.print_tree("inorder"),"")