#Author = Vignesh Goutham

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue("vg")
    q.enqueue(999)
    print(q.dequeue())