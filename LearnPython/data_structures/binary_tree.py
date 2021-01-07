class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root_val):
        self.root = Node(root_val)

    def preorder_traversal(self, start, traversal):
        """ Root -> left -> right """

        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)

        return traversal

    def inorder_traversal(self, start, traversal):
        """ left -> root -> right """
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)

        return traversal

    def postorder_traversal(self, start, traversal):
        """ left -> right -> root """
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")

        return traversal


if __name__ == "__main__":
    """
         1
       /  \
      2    3
    /  \  / \
    4  5  6  7
    """
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("preorder-traversal: ", tree.preorder_traversal(tree.root, ""))

    print("inorder-traversal: ", tree.inorder_traversal(tree.root, ""))

    print("postorder-traversal: ", tree.postorder_traversal(tree.root, ""))