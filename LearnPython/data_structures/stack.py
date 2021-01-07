class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def get_stack(self):
        return self.stack


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)

    print(s.get_stack())

    s.pop()

    print(s.get_stack())

    s.push(2)

    print(s.get_stack())