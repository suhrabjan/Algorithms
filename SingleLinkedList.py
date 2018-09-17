class Node:
    # Class Node that represents a nodes of a singlelinkedlists.
    def __init__(self, value):
        self.info = value # Actual data that is stored in current node
        self.link = None # Pointer / reference to the next node
