#### Python Solution

from heapq import heappush, heappop
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # Get the dimensions of the matrix
        minHeap = []  # Initialize a min-heap to keep track of the smallest elements

        # Push the first element of each row (up to k rows) onto the heap
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1  # Initialize the answer with a dummy value

        # Extract the smallest element from the heap k times
        for i in range(k):
            ans, r, c = heappop(minHeap)  # Pop the smallest element from the heap
            if c + 1 < n:  # If there are more elements in the row
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))  # Push the next element in the row onto the heap

        return ans  # Return the kth smallest element

# Example usage:
# Uncomment the lines below to test the function with example inputs.
# solution = Solution()
# print(solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Output: 13
# print(solution.kthSmallest([[-5]], 1))  # Output: -5