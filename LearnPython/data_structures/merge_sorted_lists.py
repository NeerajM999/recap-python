"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""

class Solution:
    def merge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        j = 0

        while (i < len(nums1)) and (j < len(nums2)):
            print("nums1 = ", nums1[i])
            print("nums2 = ", nums2[j])

            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                print("inserted, j=", j)
                j += 1

            else:
                print("not inserted, i=",i)
                i += 1

        return nums1

if __name__ == "__main__":

    nums1 = [1,2,3,4,5,7]
    nums2 = [2,5,6]

    s = Solution()
    nums1 = s.merge(nums1, nums2)

    print(nums1)
