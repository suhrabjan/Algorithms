class Node:
    # Class Node that represents a nodes of a singlelinkedlists.
    def __init__(self, value):
        self.info = value  # Actual data that is stored in current node
        self.link = None  # Pointer / reference to the next node


class SingleLinkedList:

    def __init__(self):
        self.start = None
        self.length = 0

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

    def __len__(self):
        return self.length

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
        self.length += 1


l = SingleLinkedList()
# print(l.start)
# print(l.display_list())
l.insert_in_beginning(5)
l.insert_in_beginning(5)
l.insert_in_beginning(5)
l.display_list()
print(len(l))
