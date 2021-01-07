class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def _add_to_empty(self, item):
        if self.tail is not None:
            return self.tail

        print("adding first element")
        new_node = Node(item)
        self.head = new_node
        self.tail = self.head
        self.tail.next = self.tail


    def prepend(self, data):
        if self.head is None:
            # empty list
            self._add_to_empty(data)
            return

        # non-empty list
        print("adding next element")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head


    def append(self, item):
        if self.head is None:
            # add in empty list
            self._add_to_empty(item)
            return

        print("adding next element")
        # add to end of non-empty list
        new_node = Node(item)
        self.tail.next = new_node  # point last element to new node
        self.tail = new_node  # tail is pointing to new node
        self.tail.next = self.head # tail.next points circular to head

    def remove(self):
        """
        removes an element from end
        :return:
        """
        if self.head is not None:
            node = self.head

            while node.next != self.tail:
                node = node.next

            self.tail = node
            node.next = self.head

    def search(self, value):
        """
        searches if node with value exists
        :param value:
        :return: true/false
        """

        if self.head is not None:
            node = self.head

            if node.data == value:
                return True

            node = node.next
            while node != self.head:
                if node.data == value:
                    return True
                node = node.next

        return False



    def print_list(self):
        if self.head is not None:
            print("list is not empty")
            node = self.head

            while node != self.tail:
                print(node.data, end="->")
                node = node.next
            print(node.data)

    def length(self):
        if self.head is not None:
            node = self.head
            l = 1
            while node != self.tail:
                l += 1
                node = node.next
            return l

        else:
            return 0


if __name__ == "__main__":
    cl = CircularLinkedList()
    cl.append(10)
    cl.append(20)
    cl.append(30)

    cl.prepend(1)
    cl.prepend(2)

    cl.print_list()

    print("Circular Linked list size: ", cl.length())

    cl.remove()
    cl.remove()

    cl.print_list()
    print("Circular Linked list size: ", cl.length())

    print(cl.search(10))
    print(cl.search(-10))
    print(cl.search(1))
    print(cl.search(2))

