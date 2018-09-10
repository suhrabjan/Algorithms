# Algorithms

## Table of Contents

No | Algorithm Name | Python3 Implementation
:---: | :-----------------------------: | :-----------:
1 | Heaps (min-heap, max-heap) | [HEAP.py](Algorithms/HEAP.py)


## Instructions

##### 1. Heaps (min-heap, max-heap). Works on zero based arrays and lists. All heap operations are O(nlogn) time except for getMax and getMin, which are O(1) time if heap structure is provided in the beginning.

    * Download or copy HEAP.py
    * To implement min-heap or max-heap instantiate minHeap or maxHeap object:
    ```
    h_min = minHeap()
    h_max = maxHeap()
    ```
    * Basic Operations
    ```
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

    h_min.buildHeap(A)  <!-- where A is array (list), buildHeap builds heap structure in place, space complexity O(1) -->
    h_max.buildHeap(A)  <!-- where A is array (list), buildHeap builds heap structure in place, space complexity O(1) -->

    h_min.heapSort(A)  <!-- where A is array (list), heapSort sorts heap structure in place, space complexity O(1) -->
    h_max.heapSort(A)  <!-- where A is array (list), heapSort sorts heap structure in place, space complexity O(1) -->
    ```
