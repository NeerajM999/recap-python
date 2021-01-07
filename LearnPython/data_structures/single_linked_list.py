class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def addAtBeginning(self, item):
        print("adding item in beginning: ", item)
        node = Node(item)

        node.next = self.head
        self.head = node

    def addAtEnd(self, item):
        print("adding item in end: ",item)
        node = Node(item)

        if self.head is None:
            self.head = node
            return

        temp_node = self.head

        while temp_node.next:
            temp_node = temp_node.next

        temp_node.next = node

    def addAtLocation(self, item, loc):
        print("adding item {} at location {}".format(item, loc))

        if loc < 1:
            print("Invalid location")
            return

        if self.head is None:
            print("Linked List is smaller than size: ", loc)
            return

        new_node = Node(item)
        temp_node = self.head
        while loc > 1:
            temp_node = temp_node.next
            loc -= 1
        # point new node to node which was at this position earlier
        new_node.next = temp_node.next
        # point previous node to new node
        temp_node.next = new_node

    def addAfterNode(self, afternode, item):
        if not self.head:
            print("Linked list is empty")
            return

        temp_node = self.head
        found = False
        while temp_node.next:
            if temp_node.value == afternode:
                new_node = Node(item)
                new_node.next = temp_node.next
                temp_node.next = new_node
                found = True

            temp_node = temp_node.next

        if not found:
            print(afternode, " not found. ")

    def removeFirstNode(self):
        if not self.head:
            print("Linked list is empty")
            return

        self.head = self.head.next


    def removeLastNode(self):
        if not self.head:
            print("Linked list is empty")
            return

        tmp_node = self.head

        while tmp_node.next.next:
            # print(tmp_node.value)
            tmp_node = tmp_node.next

        tmp_node.next = None

    def removeNode(self, item):
        if not self.head:
            print("Linked list is empty")
            return

        temp_node = self.head

        if temp_node.value == item:
            print("Removing first node")
            self.head = temp_node.next
            temp_node = None
            return

        while temp_node:
            if temp_node.value == item:
                print("found item")
                break
            prev = temp_node
            temp_node = temp_node.next

        if temp_node is None:
            print("Item not found")
            return

        prev.next = temp_node.next



    def print_list(self):
        temp_node = self.head

        while temp_node:
            print(temp_node.value, end="->")
            temp_node = temp_node.next



if __name__ == "__main__":
    s = SingleLinkedList()
    s.addAtBeginning(1)
    s.addAtBeginning(2)
    s.addAtBeginning(3)
    s.addAtBeginning(4)

    # s.print_list()

    s.addAtEnd(5)
    # s.print_list()

    s.addAtEnd(6)
    s.addAtEnd(7)
    # s.print_list()

    s.addAtLocation(22,3)
    s.print_list()
    print("")
    s.addAfterNode(5, 55)
    s.print_list()

    print("")
    s.addAfterNode(35, 335)
    s.print_list()
    print("")
    s.removeFirstNode()
    s.print_list()

    print("")
    s.removeLastNode()
    s.print_list()

    print("")
    s.removeNode(6)
    s.print_list()