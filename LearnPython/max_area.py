"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 [1,8,6,2,5,4,8,3,7]



"""

class Solution:
    def max_area(self, lst):
        if len(lst) <=2:
            print("container can't exist")
            return 0

        res = {}
        maxarea = 0
        for i in range(0,len(lst)):
            for j in range(i+1, len(lst)):
                area = min(lst[i], lst[j]) * (j-i)
                if maxarea < area:
                    maxarea = area

        return maxarea


if __name__ == "__main__":
    s = Solution()
    lst =  [1,8,6,2,5,4,8,3,7]
    print(s.max_area(lst))

    print(s.max_area([1,2]))
