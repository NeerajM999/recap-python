""""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""
def common_prefix(arr):
    prefix = ""
    i = 0

    while i < len(arr):
        first = arr[i] if prefix == "" else prefix
        second = arr[i+1] if (i + 1) < len(arr) else ""

        if first == "" or second == "":
            break

        print("first {}, second {}".format(first, second))

        if len(first) > len(second):
            # swap
            print("swapped")
            first, second = second, first

        j = len(first) # first will always have smaller string
        print("j = ", j)
        while j > 0:
            # traverse through first to find a matching substring
            if first[0:j] in second:
                prefix = first[0:j]
                print("found: ", prefix)
                break
            j -= 1
        if prefix == "":
            return "No common prefix"  # if there's no match between any elements, exit

        i += 1

    return "Common Prefix Found = " + prefix





def to_dict(arr):
    """
    find shortest element in the array
    :param arr:
    :return:
    """
    return {arr[i]: len(arr[i]) for i in range(0, len(arr))}


a = ["flower","flow","flight"]
b = ["dog","racecar","car"]
print(common_prefix(a))

print(common_prefix(b))



#d = to_dict(a)
#dm = min(d, key=d.get)
#print(dm)

