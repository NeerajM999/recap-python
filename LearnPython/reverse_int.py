# this function reverses an integer
# 123 -> 321, -123 -> -321, 120 -> 12

class Solution:
    def reverse_int(self, num):
        n = str(num)
        ret = ""
        if n[0] == '-':
            ret = int("-" + n[1::][::-1])
        else:
            ret = int(n[::-1])

        if (ret >= -2**31) and (ret <= (2**31) -1 ):
            pass
        else:
            ret = 0

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.reverse_int(-1234))
    print(s.reverse_int(4321345))
    print(s.reverse_int(343456432426463))

