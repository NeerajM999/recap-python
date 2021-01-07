class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Circular_DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def _add_to_empty(self, value):
        if self.head is not None:
            return self.head

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        new_node.next = self.head
        new_node.prev = self.head


    def append(self, value):
        if self.head is None:
            self._add_to_empty(value)
            return

        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        new_node.next = self.head


    def prepend(self, value):
        if self.head is None:
            self._add_to_empty(value)
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = self.tail

    def remove_from_end(self):
        if self.head is None:
            return

        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        del node

    def remove_from_start(self):
        if self.head is None:
            return
        if self.head == self.tail:
            # its last node
            print("last node")
            self.head = None
            self.tail = None
        else:
            print("not last node")
            self.head = self.head.next
            self.head.prev = self.tail

    def remove_from_pos(self, pos=0):
        if self.head is not None:
            if pos == 0:
                self.remove_from_start()
                return

            if pos == self.length():
                self.remove_from_end()
                return

            else:
                i = 1
                node = self.head
                while i < pos:
                    node = node.next
                    i += 1

                node.prev.next = node.next
                node.next.prev = node.prev
                del node

    def length(self):
        if self.head is None:
            return 0

        node = self.head
        i = 1
        while node != self.tail:
            i += 1
            node = node.next

        return i

    def search(self, value):
        if self.head is None:
            return False

        node = self.head
        if node.data == value:
            return True
        elif node.prev.data == value:
            return True
        else:
            while node != self.tail:
                if node.data == value:
                    return True
                node = node.next

            return False


    def print_list(self, direction="forward"):
        if self.head is not None:
            if direction == "forward":
                node = self.head

                while node != self.tail:
                    print(node.data, end="->")
                    node = node.next
                print(node.data)

            elif direction == "reverse":
                node = self.tail

                while node != self.head:
                    print(node.data, end="->")
                    node = node.prev
                print(node.data)


if __name__ == "__main__":
    cd = Circular_DLL()
    cd.append(10)
    cd.append(20)
    cd.append(30)
    cd.append(40)

    cd.print_list()
    cd.print_list("reverse")

    cd.prepend(-10)
    cd.prepend(-20)

    cd.print_list()
    #cd.print_list("reverse")

    print("Length = ", cd.length())

    cd.remove_from_pos(3)
    cd.print_list()

    print(cd.search(30))
    print(cd.search(22))

    """
    
    cd.remove_from_end()
    cd.remove_from_end()
    print("2 removed from end")
    cd.print_list()
    
    
    cd.remove_from_start()
    cd.print_list()
    cd.remove_from_start()
    cd.print_list()
    cd.remove_from_start()
    cd.print_list()
    cd.remove_from_start()
    cd.print_list()
    """


