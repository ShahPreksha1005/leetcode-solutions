# Spiral Matrix

## Problem Statement

Given an m x n matrix, return all elements of the matrix in spiral order.

### Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

### Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## Constraints:

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

## Solution

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        spiral = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            # Traverse from top to bottom
            for row in range(top + 1, bottom + 1):
                spiral.append(matrix[row][right])
            # Traverse from right to left (if applicable)
            if top < bottom and left < right:
                for col in range(right - 1, left, -1):
                    spiral.append(matrix[bottom][col])
                for row in range(bottom, top, -1):
                    spiral.append(matrix[row][left])
            # Update boundaries
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return spiral
