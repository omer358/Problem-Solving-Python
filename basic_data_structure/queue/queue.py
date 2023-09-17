class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        print("queue emptiness: ", self.items == [])
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        print(item, " has been added to the queue")

    def dequeue(self):
        print(self.items[-1], " has been popped from the queue")
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    q.dequeue()
