class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("{} has been added to the stack".format(item))

    def pop(self):
        popped_item = self.items.pop()
        print("{} has been poped from the stack".format(popped_item))
        return popped_item

    def peek(self):
        return "{} is the top element on the stack".format(self.items[len(self.items) - 1])

    def is_empty(self):
        print("Stack emptiness:", self.items == [])
        return self.items == []

    def size(self):
        print("Stack size:", end=" ")
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(3)

    stack.push(2)
    print(stack.peek())
    stack.push(1)
    print(stack.size())
    stack.pop()
    print(stack.size())
    print(stack.is_empty())
