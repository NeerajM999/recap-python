class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Linked list is empty")
            return

        tmp_node = self.head
        while tmp_node:
            if tmp_node.next:
                print(tmp_node.value, end="->")
            else:
                print(tmp_node.value, end="")
            tmp_node = tmp_node.next

    def add(self, item):
        new_node = Node(item)

        new_node.next = self.head
        self.head = new_node

    def length(self):
        if not self.head:
            print("list is empty")
            return 0

        node = self.head
        i = 0

        while node:
            i += 1
            node = node.next

        return i


    # sort a linked list using bubble sort
    def bubble_sort(self):
        if self.head:
            first = self.head
            second = first.next

            def swap(first, second):
                #print("swapping: {}, {}".format(first.value, second.value))
                first.value, second.value = second.value, first.value

            swapped = True

            n = self.length()

            while swapped:
               swapped = False
               for i in range(1, n):
                   if int(first.value) > int(second.value):
                       swap(first, second)
                       swapped = True

                   if second.next is None:
                       # revind
                       first = self.head
                       second = first.next
                   else:
                       first = second
                       second = second.next
                   #print("swapped = ", swapped)


    # sort linked list using selection sort

    def selection_sort(self):
        n = self.length()
        if n <=0:
            return

        minimum = self.head
        b = minimum.next
        for i in range(n):
            #print("minimum = ", minimum.value)
            for j in range(i+1, n):
                if b.value < minimum.value:
                    # swap
                    print("swapping: {} with {}".format(minimum.value, b.value))
                    minimum.value, b.value = b.value, minimum.value
                # otherwise continue with next node
                print("minimum = {}, b = {}".format(minimum.value, b.value))
                b = b.next
            # in the end, reset b to start over
            minimum = minimum.next
            if minimum:
                b = minimum.next


    # sort linked list using insertion sort
    def insertion_sort(self):
        if self.head:
            pntr = self.head
            node = pntr.next

            while pntr:
                if node.value > pntr.value:
                    #insert this node before pntr
                    pass








if __name__ == "__main__":
    l = LinkedList()

    l.add(10)
    l.add(20)
    l.add(30)
    l.add(60)
    l.add(45)
    l.add(95)
    l.add(-3)
    print("\nlist length: ", l.length())
    print("Input Linked List: ", end="")
    l.display()

    print("\n")
    #l.bubble_sort()
    #print("Bubble sorted list: ", end="")
    #l.display()
    #print("\n")
    l.selection_sort()
    print("Selection sorted list: ", end="")
    l.display()


