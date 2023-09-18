from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found


if __name__ == "__main__":
    myList = UnorderedList()
    myList.add(31)
    myList.add(77)
    myList.add(17)
    myList.add(93)
    myList.add(26)
    myList.add(54)
    print(myList.size())
    print(myList.search(17))
