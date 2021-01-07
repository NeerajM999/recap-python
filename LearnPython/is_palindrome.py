# check if number is a palindrome

class Solution:
    def is_palindrome(self, num):
        x = str(num)

        if x[0] == '-':
            return False

        if x[:] == x[::-1]:
            return True

        else:
            return False


    def is_palindrome2(self, num):

        if (num < 0 ) or (num % 10 == 0 and num != 0):
            return False

        rev = 0
        while num > rev:
            rev = rev * 10 + num % 10
            num = num/10

        print(num)
        print(rev)
        return num == rev or num == rev / 10

if __name__ == "__main__":
    s = Solution()
    print(s.is_palindrome(121))
    print(s.is_palindrome(-121))
    print(s.is_palindrome(342))
    print(s.is_palindrome(10))

    print(s.is_palindrome2(121))
