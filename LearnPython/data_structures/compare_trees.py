"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Tree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.val) + "->")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)

        return traversal

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True


        pt = self.preorder_traversal(p.root, "")
        qt = self.preorder_traversal(q.root, "")

        if pt == qt:
            return True
        else:
            return False


    def isSameTree2(self, p, q):
        if p is None and q is None:
            return True

        if p is not None and q is not None and p.val == q.val:
            # compare rest of nodes
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)

        else:
            return False


    def isSymmetricTree(self, p):
        return p is None or self.isMirror(p, p)

    def isMirror(self, a, b):
        if (a is None) or (b is None):
            return (a == b)

        return (a.val == b.val) and self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)


if __name__ == "__main__":

    atree = Tree(1)
    atree.root.left = TreeNode(2)
    atree.root.right = TreeNode(2)
    atree.root.left.left = TreeNode(3)
    atree.root.left.right = TreeNode(4)
    atree.root.right.left = TreeNode(4)
    atree.root.right.right = TreeNode(3)

    print(atree.preorder_traversal(atree.root, ""))


    btree = Tree(1)
    btree.root.left = TreeNode(2)
    btree.root.right = TreeNode(3)
    btree.root.left.left = TreeNode(4)
    btree.root.left.right = TreeNode(6)
    print(btree.preorder_traversal(btree.root, ""))

    print("1st approach")
    print(atree.isSameTree(atree, btree))

    print("2nd approach")
    print(atree.isSameTree2(atree.root, btree.root))


    print("is Symmetric")
    print(atree.isSymmetricTree(atree.root))
    
    

