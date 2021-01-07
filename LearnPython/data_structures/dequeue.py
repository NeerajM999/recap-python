# double ended queue

class Dqueue(object):
    def __init__(self):
        self.dqueue = []

    def addLeft(self, item):
        self.dqueue.insert(0, item)

    def addRight(self, item):
        self.dqueue.insert(len(self.dqueue), item)

    def get_queue(self):
        return self.dqueue


if __name__ == "__main__":
    dq = Dqueue()
    dq.addLeft(1)
    dq.addLeft(2)
    dq.addLeft(3)

    print(dq.get_queue())

    dq.addRight(0)
    dq.addRight(-1)
    dq.addRight(-2)

    print(dq.get_queue())