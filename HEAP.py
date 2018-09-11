import math


class maxHeap:

    def __init__(self):
        self.H = []
        self.size = -1

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def siftUp(self, i):
        while i > 0:
            if self.H[i] > self.H[self.parent(i)]:
                self.H[self.parent(i)], self.H[i] = self.H[i], self.H[self.parent(i)]
                i = self.parent(i)
            else:
                break

    def siftDown(self, i):
        maxIndex = i
        l = self.leftChild(i)
        if l <= self.size and self.H[l] > self.H[maxIndex]:
            maxIndex = l
        r = self.rightChild(i)
        if r <= self.size and self.H[r] > self.H[maxIndex]:
            maxIndex = r
        if i != maxIndex:
            self.H[i], self.H[maxIndex] = self.H[maxIndex], self.H[i]
            self.siftDown(maxIndex)

    def getMax(self):
        return self.H[0]

    def insert(self, p):
        self.H.append(p)
        self.size += 1
        self.siftUp(self.size)

    def extractMax(self):
        result = self.H[0]
        self.H[0] = self.H[self.size]
        self.H.pop()
        self.size -= 1
        self.siftDown(0)
        return result

    def remove(self, i):
        self.H[i] = math.inf
        self.siftUp(i)
        self.extractMax()

    def changePriority(self, i, p):
        oldp = self.H[i]
        self.H[i] = p
        if p > oldp:
            self.siftUp(i)
        else:
            self.siftDown(i)

    def buildHeap(self, A):
        self.size = len(A) - 1
        self.H = A
        for i in range(len(A) // 2 - 1, -1, -1):
            self.siftDown(i)
        return self.H

    def heapSort(self, A):
        self.buildHeap(A)
        for i in range(len(A) - 1):
            self.H[0], self.H[self.size] = self.H[self.size], self.H[0]
            self.size -= 1
            self.siftDown(0)
        return self.H
