class LongestSubString:
    def lengthOfLongestSubstring(self, string):
        max_length = 0
        substr = ""
        strSize = len(string)
        for idx, char in enumerate(string):
            print("searching for: ", char, "at idx: ", idx)
            i = string.find(char, idx+1, strSize)
            sub = string[idx:i] if i > 0 else string[idx:]
            sz = len(sub)
            print('sub=',sub, "sz=",sz)
            if sz > max_length:
                max_length = sz
                substr = sub
                if sz == strSize - idx:
                    print("reached end")
                    break
        print(max_length, substr)



if __name__ == "__main__":
    ls = LongestSubString()
    ls.lengthOfLongestSubstring('abcabcdef')