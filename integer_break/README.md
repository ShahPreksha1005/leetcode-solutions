# Integer Break

## Problem Statement

Given an integer `n`, break it into the sum of `k` positive integers, where `k >= 2`, and maximize the product of those integers.

Return the maximum product you can get.

### Example 1:

**Input:** `n = 2`  
**Output:** `1`  
**Explanation:** `2 = 1 + 1`, `1 × 1 = 1`.

### Example 2:

**Input:** `n = 10`  
**Output:** `36`  
**Explanation:** `10 = 3 + 3 + 4`, `3 × 3 × 4 = 36`.

## Constraints:

- `2 <= n <= 58`

## Solution

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Given an integer n, break it into the sum of k positive integers, where k >= 2, 
        and maximize the product of those integers. Return the maximum product you can get.
        
        Parameters:
        n (int): The input integer to be broken.
        
        Returns:
        int: The maximum product of the broken integers.
        """
        # Base case: if n is 2 or 3, the best we can do is n-1
        if n <= 3:
            return n - 1
        
        # Determine how many times 3 fits into n
        n3 = n // 3
        # Determine the remainder when n is divided by 3
        r3 = n % 3
        
        # If there is no remainder, the maximum product is 3 raised to the power of n3
        if r3 == 0:
            return 3 ** n3
        # If the remainder is 1, we should take one less 3 and use 4 instead (3+1)
        if r3 == 1:
            return 3 ** (n3 - 1) * 4
        # If the remainder is 2, multiply the remaining 2 with 3 raised to the power of n3
        return 3 ** n3 * 2
