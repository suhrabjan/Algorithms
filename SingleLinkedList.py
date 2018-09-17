class Node:
    # Class Node that represents a nodes of a singlelinkedlists.
    def __init__(self, value):
        self.info = value  # Actual data that is stored in current node
        self.link = None  # Pointer / reference to the next node


class SingleLinkedList:

    def __init__(self):
        self.start = None

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp


# l = SingleLinkedList()
# print(l.start)
