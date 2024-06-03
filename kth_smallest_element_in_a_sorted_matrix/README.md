### README

## Kth Smallest Element in a Sorted Matrix

### Problem Description

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n²).

### Example 1

- **Input:** `matrix = [[1,5,9],[10,11,13],[12,13,15]]`, `k = 8`
- **Output:** `13`
- **Explanation:**
  The elements in the matrix are [1, 5, 9, 10, 11, 12, 13, 13, 15], and the 8th smallest number is 13.

### Example 2

- **Input:** `matrix = [[-5]]`, `k = 1`
- **Output:** `-5`

### Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the rows and columns of the matrix are guaranteed to be sorted in non-decreasing order.
- `1 <= k <= n²`

### Follow-up

- **Constant Memory Complexity:** Can you solve the problem with a constant memory (i.e., O(1) memory complexity)?
- **O(n) Time Complexity:** Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

### Solution Explanation

This solution uses a min-heap to efficiently find the kth smallest element in a sorted matrix.

#### Detailed Explanation

1. **Imports and Class Definition:**
    - Import the `heappush` and `heappop` functions from the `heapq` module.
    - Import the `List` type from the `typing` module for type hinting.
    - Define a class named `Solution`.

2. **Method Definition:**
    - Define a method `kthSmallest` that takes a 2D list `matrix` and an integer `k`, and returns an integer.

3. **Matrix Dimensions:**
    - Get the dimensions of the matrix `m` (number of rows) and `n` (number of columns).

4. **Initialize Min-Heap:**
    - Create an empty min-heap `minHeap`.

5. **Push First Elements of Each Row:**
    - Push the first element of each row (up to `k` rows) onto the heap. This step ensures that we start with the smallest elements from each row.

6. **Initialize Answer:**
    - Initialize the answer `ans` with a dummy value `-1`.

7. **Extract Smallest Element k Times:**
    - Extract the smallest element from the heap `k` times. Each time we extract an element, we push the next element in the same row (if it exists) onto the heap. This step ensures that we always have the smallest elements in the heap.

8. **Return Answer:**
    - After extracting the smallest element `k` times, return the answer.

9. **Example Usage:**
    - The commented-out lines at the end of the script demonstrate how to create an instance of `Solution` and call the `kthSmallest` method with example inputs. These lines can be uncommented to run the examples.