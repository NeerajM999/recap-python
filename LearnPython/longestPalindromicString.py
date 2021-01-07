class PalindromicString:

    def __init__(self):
        self.maxlen = 0
        self.start = 0

    def longestSubstring(self, input):
        maxLen = 0
        iSize = len(input)
        palinStr = ""

        print("Input string = ",input)
        for idx, char in enumerate(input):
            i = input.find(char, idx+1, iSize)
            # print("i = ", i)
            # if char is found, then there's possibility that we could get a palindromic string
            if i > 0:
                # extract the substring
                sub = input[idx:i+1]
                print("sub = ", sub)

                # compare sub with its rev sub
                if sub == sub[::-1]:
                    # we found a palindrome
                    if len(sub) > maxLen:
                        maxLen = len(sub)
                        palinStr = sub

        if palinStr == "":
            print("No palindrome string found")
        else:
            print("Found longest palindrome substring: ", palinStr, "with len=", maxLen)


    def longestPalindrome(self, input):

        if input == "" or len(input) < 1:
            raise ValueError

        for i in range(len(input)):
            self.expandFromCenter(input, i, i)
            self.expandFromCenter(input, i, i+1)

        return input[self.start: self.start + self.maxlen]

    def expandFromCenter(self, input, l, r):
        while l > -1 and r < len(input) and input[l] == input[r]:
            l -= 1
            r += 1

        if self.maxlen < r-l-1:
            self.maxlen = r-l-1
            self.start = l + 1




if __name__ == "__main__":
    input = "amanaplanacanalpanam"
    #input = "bad"
    lp = PalindromicString()
    #lp.longestSubstring(input)
    a = lp.longestPalindrome(input)
    print("Palindrome = ", a, " size = ", len(a))