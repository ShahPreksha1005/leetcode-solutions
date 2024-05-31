# Power(x, n)

## Problem Statement

Implement `pow(x, n)`, which calculates x raised to the power n (i.e., x^n).

### Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

### Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

### Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

## Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= x^n <= 104

## Solution

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If n is negative, change x to its reciprocal and make n positive
        if n < 0:
            n = -n
            x = 1 / x
        
        pow_result = 1
        
        # Iterate until n becomes 0
        while n != 0:
            # If the least significant bit of n is set
            if n & 1:
                pow_result *= x  # Multiply pow_result by x
            
            x *= x  # Square x for the next iteration
            n >>= 1  # Right shift n by 1 bit
        
        return pow_result  # Return the final result
        