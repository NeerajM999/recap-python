"""
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

"""

class Solution:
    def __init__(self):
        self.ref = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (3, "III"),
            (2, "II"),
            (1, "I")
        ]

        self.map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "III": 3,
            "II": 2,
            "I": 1
        }

    def toRoman(self, x):
        roman = ""

        while x > 0:
            for i, r in self.ref:
                #print(i, r)
                while x >= i:
                    #print("check {}, {}".format(i,r))
                    roman += r
                    x -= i

        return roman

    def getValue(self, x):
        try:
            return self.map[x]
        except KeyError as k:
            print("Invalid key: ", k)
            exit

    def toInt(self, s):
        num = 0
        i = 0
        while i < len(s):
            current = self.getValue(s[i])

            if (i+1) < len(s):
                next = self.getValue(s[i+1])

                if current >= next:
                    num = num + current
                    i = i+1
                else:
                    num = num + next - current
                    i = i + 2

            else:
                num = num + current
                i = i + 1

        return num

if __name__ == "__main__":
    s = Solution()
    #print(s.toRoman(12))

    print(s.toInt("MCDIVIT"))