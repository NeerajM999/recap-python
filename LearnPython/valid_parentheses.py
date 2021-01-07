class ValidParentheses:
    def isValid(self, s):

        stack = []

        mapping = {
                ")": "(",
                "}": "{",
                "]": "["
                }

        for char in s:
            # if character is a closing bracket
            if char in mapping:
                print("popping: ", char)
                # if closing bracket comes before opening bracket, then it will assign # and fail the flow
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                # we have opening bracket, push it to stack
                print("appending: ", char)
                stack.append(char)

        # in end, if we have empty stack then it's a valid expression
        return not stack

if __name__ == "__main__":
    input = "{(a())}[]()"
    v = ValidParentheses()

    print("It's a valid expression") if v.isValid(input) else print("It's invalid expression")
