class Node:
    # Class Node that represents a nodes of a singlelinkedlists.
    def __init__(self, value):
        self.info = value  # Actual data that is stored in current node
        self.link = None  # Pointer / reference to the next node


class SingleLinkedList:

    def __init__(self):
        self.start = None
        self.length = 0

    # Running time O(n)
    def display_list(self):
        if self.start is None:
            return 'List is empty'
        else:
            print("List is :  ")
            p = self.start
            while p is not None:
                print(p.info, ' ', end='')
                p = p.link
            print()

    # running time: O(1)
    def __len__(self):
        return self.length

    # running time: O(1)
    def appendLeft(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
        self.length += 1

    # searches the position of the element in list. Running time O(n)
    def search(self, x):
        # Zero based positioning of nodes.
        position = 0
        p = self.start
        while p is not None:
            if p.info == x:
                return "{}, is at position {}".format(x, position)
                break
            position += 1
            p = p.link
        else:
            return "{}, not in the list".format(x)

    # adds a node to the back. O(n)
    def append(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp
        self.length += 1

    def createList(self, *elements):
        for elem in elements:
            self.append(elem)


l = SingleLinkedList()
# print(l.start)
# print(l.display_list())
# l.appendLeft(5)
# l.appendLeft(5)
# l.appendLeft(5)
# l.append(25)
l.createList()
l.display_list()
print(len(l))
print(l.search(25))
