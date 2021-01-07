"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def addAtBeginning(self, aNode):
        if self.head:
            print("adding node: ", aNode.val)
            aNode.next = self.head
            self.head = aNode
        else:
            print("adding first node: ", aNode.val)
            self.head = aNode

    def display(self):
        print("displaying list")
        node = self.head
        while node is not None:
            print(node.val, "->")
            node = node.next

    def sum(self, bList):
        sumLL = SLinkedList()
        a = self.head
        b = bList.head
        carry = 0

        while a != None or b != None:
            x = a.val if a != None else 0
            y = b.val if b != None else 0

            s = carry + x + y
            carry = s/10
            sumLL.head = Node(s%10)
            sumLL = sumLL.head.next

            if a != None:
                a = a.next
            if b != None:
                b = b.next
        if carry > 0:
            sumLL.head = Node(carry)

        return sumLL

if __name__ == "__main__":
    aLL = SLinkedList()
    aLL.addAtBeginning(Node(3))
    aLL.addAtBeginning(Node(4))
    aLL.addAtBeginning(Node(2))
    aLL.display()


    bLL = SLinkedList()
    bLL.addAtBeginning(Node(4))
    bLL.addAtBeginning(Node(6))
    bLL.addAtBeginning(Node(5))
    bLL.display()

    sumLL = aLL.sum(bLL)
    sumLL.display()


