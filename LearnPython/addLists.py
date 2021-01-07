class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        node = self
        while node is not None:
            print(node.val, end="->")
            node = node.next
        print()

"""
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

"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            a = (l1.val if l1 else 0)
            b = (l2.val if l2 else 0)

            carry, out = divmod(a + b + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

if __name__ == "__main__":
    l1 = ListNode(9)
    l1.next = ListNode(6)
    l1.next.next = ListNode(6)
    l1.display()

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.display()



    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print()
    while result:
        print(result.val, end="->")
        result = result.next
