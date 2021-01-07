class Node(object):
    def __init__(self, v):
        self.value = v
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

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

    def remove_dups(self, nums):
        """
        remove duplicates in-place inside a sorted array/list
        :param nums:
        :return: length of final array
        """

        ## delete from end of the list

        if not nums:
            return 0

        tail = len(nums) - 1 # last element
        i = tail - 1  # 2nd last element

        while tail >= 0 and i >= 0:
            if nums[tail] == nums[i]:
                del(nums[tail])

            tail = i
            i -= 1

        return len(nums)


    def remove_dups_sorted_linked_list(self, head):
        """
        Given a sorted linked list, delete all duplicates such that each element appear only once.
        :param head: Input: 1->1->2->3->3
        :return: Output: 1->2->3
        """

        if not head:
            return 0

        current = head
        nxt = current.next

        while current and nxt:
            if current.value == nxt.value:
                current.next = nxt.next
                nxt.next = None # dropped
                nxt = current.next

            else:
                current = nxt
                nxt = current.next



nums = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
l = s.remove_dups(nums)

print("length = ", l)
print(nums)


n = Solution()
n.add(20)
n.add(20)
n.add(15)
n.add(10)
n.add(10)
n.add(4)


n.display()
n.remove_dups_sorted_linked_list(n.head)
print("sorted: ")
n.display()

