# Algorithms

## Table of Contents

No | Algorithm Name | Python3 Implementation
:---: | :-----------------------------: | :-----------:
1 | Heaps (min-heap, max-heap) | [HEAP.py](/HEAP.py)
2 | Single Linked List | [SingleLinkedList.py](/SingleLinkedList.py)

## Instructions

##### 1. Heaps (min-heap, max-heap). Works on zero based arrays and lists. All heap basic operations are O(nlogn) running time except for getMax and getMin, which are O(1) time if heap structure is provided in advance.

* Download or copy HEAP.py
* To implement min-heap or max-heap instantiate minHeap or maxHeap object:
    ```
    h_min = minHeap()
    h_max = maxHeap()
    ```
* Basic Operations
    ```
    h_min.parent(i) or h_max.parent(i)  <!-- returns parent's index of the child at i'th index, runnint time O(1) -->
    h_min.leftChild(i) or h_max.leftChild(i)  <!-- returns index of the left child of a parent at index i, runnint time O(1) -->
    h_min.rightChild(i) or h_max.rightChild(i)  <!-- returns index of the right child of a parent at index i, runnint time O(1) -->
    
    h_min.insert(element)  <!-- Inserts an element in a correct location -->
    h_max.insert(element)  <!-- Inserts an element in a correct location -->

    h_min.getMin()  <!-- Returns min element -->
    h_max.getMax()  <!-- Returns max element -->

    h_min.extractMin()  <!-- Removes Min element from heap and returns this element  -->
    h_max.extractMax()  <!-- Removes Max element from heap and returns this element -->

    h_min.remove(i)  <!-- Removes element at index i  -->
    h_max.remove(i)  <!-- Removes element at index i -->

    h_min.changePriority(i, element)  <!-- raplaces the element at index i with provided element -->
    h_max.changePriority(i, element)  <!-- raplaces the element at index i with provided element -->
    ```
* Building and Sorting HEAP
    ```
    h_min.buildHeap(A)  <!-- where A is an array (list), buildHeap builds heap structure in place, space complexity O(1), time complexity O(nlogn) -->
    h_max.buildHeap(A)  <!-- where A is an array (list), buildHeap builds heap structure in place, space complexity O(1), time complexity O(nlogn) -->

    h_min.heapSort(A)  <!-- where A is an array (list), heapSort sorts heap structure in place, space complexity O(1), time complexity O(nlogn) -->
    h_max.heapSort(A)  <!-- where A is an array (list), heapSort sorts heap structure in place, space complexity O(1), time complexity O(nlogn) -->
    ```
    
    
##### 2. Single Linked List.
