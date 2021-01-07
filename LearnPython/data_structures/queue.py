class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.insert(0, item)

    def addUniqueItem(self, item):
        if not item in self.queue:
            self.add(item)

    def remove(self):
        return self.queue.pop()

    def get_queue(self):
        return self.queue

    def __sizeof__(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)

    print(q.get_queue())

    q.remove()

    print(q.get_queue())

    dq = Queue()
    dq.addUniqueItem(11)
    dq.addUniqueItem(22)
    dq.addUniqueItem(33)

    print(dq.get_queue())

    dq.addUniqueItem(33)

    print(dq.get_queue())

    print("size of queue: ", dq.__sizeof__())