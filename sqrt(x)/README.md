
# Sqrt(x)

## Problem Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.

## Examples

### Example 1

- **Input:** `x = 4`
- **Output:** `2`
- **Explanation:** The square root of 4 is 2, so we return 2.

### Example 2

- **Input:** `x = 8`
- **Output:** `2`
- **Explanation:** The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

## Constraints

- `0 <= x <= 2^31 - 1`

## Solution

To solve the problem efficiently, we can use the binary search algorithm. Binary search is effective because the square root of a number lies between 0 and the number itself. By narrowing the search range based on the mid-point comparisons, we can find the square root in logarithmic time.

### Code Explanation

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Calculate the square root of x rounded down to the nearest integer.
        
        Args:
        x (int): The non-negative integer to find the square root of.
        
        Returns:
        int: The square root of x rounded down to the nearest integer.
        """
        if x < 2:
            return x
        
        # Initialize the binary search bounds
        left, right = 1, x // 2
        
        while left <= right:
            # Calculate the mid-point
            mid = (left + right) // 2
            # Calculate the square of the mid-point
            square = mid * mid
            
            if square == x:
                return mid  # If mid*mid is exactly x, mid is the square root
            elif square < x:
                left = mid + 1  # If mid*mid is less than x, move to the right half
            else:
                right = mid - 1  # If mid*mid is greater than x, move to the left half
        
        return right  # Right is the integer part of the square root of x
```

## Explanation

1. **Edge Case Handling**:
   - If `x` is less than 2, return `x` because the square root of 0 is 0 and the square root of 1 is 1.

2. **Binary Search Initialization**:
   - `left` is set to 1.
   - `right` is set to `x // 2` because the square root of a number `x` is always less than or equal to `x // 2` for `x >= 4`.

3. **Binary Search Loop**:
   - The loop continues while `left` is less than or equal to `right`.
   - Calculate the `mid` point.
   - Compute `square` as `mid * mid`.
   - If `square` equals `x`, return `mid` because it's the exact square root.
   - If `square` is less than `x`, adjust the `left` bound to `mid + 1`.
   - If `square` is greater than `x`, adjust the `right` bound to `mid - 1`.

4. **Return Result**:
   - When the loop ends, `right` will be the integer part of the square root of `x`.

This approach ensures an efficient solution with optimal space and time complexity.
