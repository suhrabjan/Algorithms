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
            print ('List is empty')
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
            self.length += 1
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp
        self.length += 1

    # appends every input and creates list. O(n**2) running time
    def createList(self, *elements):
        for elem in elements:
            self.append(elem)

    # inserts a node at a give position. Inserting O(1) but finding position O(n)
    def insert(self, data, position):
        if position == 0:
            return self.appendLeft(data)
        try:
            temp = Node(data)
            i = 0
            p = self.start
            while i < (position - 1):
                p = p.link
                i += 1
            temp.link = p.link
            p.link = temp
            self.length += 1
        except AttributeError:
            print("Given position not in list and not available for inserting.")

    # removes the last element and returns it. O(n)
    def pop(self):
        if self.start is None:
            print('List is Empty')
        elif self.start.link is None:
            x = self.start.info
            self.start = None
            self.length -= 1
            return x
        p = self.start
        while p.link.link is not None:
            p = p.link
        x = p.link.info
        p.link = None
        self.length -= 1
        return x

    # removes the first element and returns it. O(1)
    def popLeft(self):
        if self.start is None:
            print('List is Empty')
        else:
            x = self.start.info
            self.start = self.start.link
            self.length -= 1
            return x

    def remove(self, position):
        if self.start is None:
            print('List is Empty')
        elif self.length <= position:
            print('Given position not in list and not available for deleting.')
        elif position == 0:
            self.start = self.start.link
            self.length -= 1
        else:
            i = 0
            p = self.start
            while i < position - 1:
                p = p.link
                i += 1
            p.link = p.link.link
            self.length -= 1
