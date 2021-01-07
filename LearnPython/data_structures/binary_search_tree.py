class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None # parent node of this node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            # empty tree
            self.root = Node(value)

        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if current_node.data > value:
            if current_node.left is None:
                current_node.left = Node(value)
                current_node.left.parent = current_node
            else:
                self._insert(current_node.left, value)
        elif current_node.data < value:
            if current_node.right is None:
                current_node.right = Node(value)
                current_node.right.parent = current_node
            else:
                self._insert(current_node.right, value)
        else:
            print("Duplicate node")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            # in order traversal - gives sorted tree output
            self._print_tree(current_node.left)
            print(current_node.data, end="-")
            self._print_tree(current_node.right)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, -1)

    def _height(self, current_node, curr_height):
        if current_node is None:
            return curr_height
        else:
            left_height = self._height(current_node.left, curr_height+1)
            right_height = self._height(current_node.right, curr_height+1)
            return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            counter = 1
            return self._search(self.root, value, counter)

        else:
            return False

    def _search(self, current_node, value, counter):
        if current_node is None:
            return False

        if value == current_node.data:
            return "Found {} in {} iterations".format(value, counter)
        elif value < current_node.data:
            return self._search(current_node.left, value, counter+1)
        else:
            return self._search(current_node.right, value, counter+1)

    def find(self, value):
        if self.root is not None:
            return self._find(self.root, value)

        else:
            return False

    def _find(self, current_node, value):
        if current_node is None:
            return False

        if current_node.data == value:
            return current_node
        elif current_node.data > value:
            return self._find(current_node.left, value)
        elif current_node.data < value:
            return self._find(current_node.right, value)

    def _find_parents(self, node, v, parents):
        if node is None:
            return None
        elif v == node.data:
            parents.append(node.data)
            return parents
        elif v < node.data:
            parents.append(node.data)
            return self._find_parents(node.left, v, parents)
        elif v > node.data:
            parents.append(node.data)
            return self._find_parents(node.right,v, parents)

    def lca(self, v1, v2):
        """
        return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.
        :param v1:
        :param v2:
        :return:
        """
        node = self.root
        if node is None:
            return None
        if v1.data == v2.data:
            return None

        if v1.data == self.root.data or v2.data == self.root.data:
            return False

        v1_parents = []
        v2_parents = []
        v1_parents = self._find_parents(node, v1, v1_parents)
        v2_parents = self._find_parents(node, v2, v2_parents)

        print(v1_parents)
        print(v2_parents)
        #return v1_parents.intersect(v2_parents)

        if v1_parents is not None and v2_parents is not None:
            common = [ i for i in v1_parents if i in v2_parents ]
            return common[-1] # take the last matching items to get lowest common ancestor

        return None

    def remove(self, value):
        return self._delete_node(self.find(value))

    def _delete_node(self, node):

        # returns left node of the node to be deleted
        def min_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # returs no. of children for given node
        def childrens(n):
            num = 0
            if n.left is not None:
                num += 1
            if n.right is not None:
                num += 1

            return num

        node_parent = node.parent

        node_children = childrens(node)

        if node_children == 0:
            print("\n{} has {} children".format(node.data, node_children))
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None

        if node_children == 1:
            print("\n{} has {} children".format(node.data, node_children))
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            # change reference from parent to new child node
            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            child.parent = node_parent

        if node_children == 2:
            print("\n{} has {} children".format(node.data, node_children))
            # get next node in the tree
            successor = min_node(node.right)
            node.data = successor.data

            self._delete_node(successor)


    def get_count_of_leafs(self):
        return self._get_leafs(self.root)

    def _get_leafs(self, current_node):
        if current_node is None:
            return 0

        if current_node.left is None and current_node.right is None:
            return 1
        else:
            return self._get_leafs(current_node.left) + self._get_leafs(current_node.right)


    def print_leafs(self):
        return self._print_leafs(self.root)

    def _print_leafs(self, current_node):
        if current_node is None:
            return ""
        if current_node.left is None and current_node.right is None:
            print(str(current_node.data) + " ")

        self._print_leafs(current_node.left)
        self._print_leafs(current_node.right)

import sys
def tree_validator(node, min= -sys.maxsize, max=sys.maxsize):
    """
    tests if given tree is a binary search tree or not
    :return: true/false
    """
    if node is None:
        return True

    if (node.data > min and
        node.data < max and
        tree_validator(node.left, min, node.data) and
        tree_validator(node.right, node.data, max)):
        return True

    else:
        return False


def create_tree(tree, nums=20):
    from random import randint
    for _ in range(nums):
        data = randint(0, 200)
        tree.insert(data)

if __name__ == "__main__":
    bst = BinarySearchTree()
    #create_tree(bst, 5)

    bst.insert(50)
    bst.insert(17)
    bst.insert(72)
    bst.insert(12)
    bst.insert(23)
    bst.insert(54)
    bst.insert(76)
    bst.insert(9)
    bst.insert(14)
    bst.insert(19)
    bst.insert(67)


    bst.print_tree()
    print("\nHeight of the tree: ", bst.get_height())

    print(bst.search(66))
    print(bst.search(34))
    print(bst.search(100))
    print(bst.search(200))

    print(bst.lca(30, 88))

    print("Leaf nodes Count = ", bst.get_count_of_leafs())
    print("Leaf nodes are = ", )
    bst.print_leafs()

    bst.remove(23)
    bst.print_tree()

    bst.remove(50)
    bst.print_tree()

    bst.remove(72)
    bst.print_tree()

    print("\n A Tree Validation ")
    root = Node(50)
    root.left = Node(20)
    root.right = Node(60)
    root.right.left = Node(55)
    root.right.right = Node(66)

    print(tree_validator(root))
