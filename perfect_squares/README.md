# Perfect Squares

## Problem Statement

Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

### Example 1:

**Input:** `n = 12`  
**Output:** `3`  
**Explanation:** `12 = 4 + 4 + 4`

### Example 2:

**Input:** `n = 13`  
**Output:** `2`  
**Explanation:** `13 = 4 + 9`

## Constraints:

- `1 <= n <= 10^4`

## Solution

```python
import math
from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        """
        Returns the least number of perfect square numbers that sum to n.
        
        Parameters:
        n (int): The target number.
        
        Returns:
        int: The least number of perfect square numbers that sum to n.
        """
        # Initialize dp array with size n+1 and fill it with maximum possible value n
        dp = [n] * (n + 1)
        dp[0] = 0  # Base case: 0 requires 0 perfect squares
    
        # Iterate from 1 to n
        for i in range(1, n + 1):
            # Iterate over all perfect squares less than or equal to i
            for j in range(1, int(math.sqrt(i)) + 1):
                # Update dp[i] if taking this perfect square reduces the number of squares required
                dp[i] = min(dp[i], dp[i - j*j] + 1)
    
        return dp[n]
