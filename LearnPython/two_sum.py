"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

www.leetcode.com

"""

class TwoSum:
    def sums(self, arr, target):
        map = {}

        """ 2 passes
        # create a hash table to store the element and it's index
        # for lookup
        for idx, val in enumerate(arr):
            #print(idx , " -> ", val)
            map[val] = idx
        #print(map)

        # check if complement of an element and target exists in the map
        for idx, val in enumerate(arr):
            if target - val in map:
                return [idx, map[target - val]]
        """

        # 1 pass
        for idx, val in enumerate(arr):
            map[val] = idx

            if target - val in map:
                return [idx, map[target - val]]


if __name__ == "__main__":
    ts = TwoSum()
    arr = [2, 7, 11, 15]
    target = 25
    print(ts.sums(arr, target))