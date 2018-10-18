
# Example, calculate External Path Length of the following string. normally each letter represents 2 bits, and total length of the string is 100 chars, in which case there are 200 bits will be used to store the file. If we want to compress it to make it shorter we can use Huffman Code algorithm.
string = {'a': 40, 'b': 30, 'c': 20, 'd': 5, 'e': 3, 'f': 2}  # total chars are 100 characters. 2 bits per each normally.

# Now lets compress it with huffman algorithm.

import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.value)


def huffman(string, n):
    heap = []
    # O(nlogn)
    for key in string:
        x = Node(string[key])
        heapq.heappush(heap, (x.value, x))
    # O(nlogn)
    for i in range(n - 1):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z = Node(x[0] + y[0])
        z.left = x[1]
        z.right = y[1]
        heapq.heappush(heap, (z.value, z))
    # Now we need the traverse the tree, and get the dot product of the all the leafs x leafHeights, I will add it later.
    return heap[0][1], heap[0][1].left


print(huffman(string, len(string)))
