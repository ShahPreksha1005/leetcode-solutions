# LeetCode Problem: Reverse Integer

## Problem Statement
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

### Example 1:
- **Input:** `x = 123`
- **Output:** `321`

### Example 2:
- **Input:** `x = -123`
- **Output:** `-321`

### Example 3:
- **Input:** `x = 120`
- **Output:** `21`

### Constraints:
- `-2^31 <= x <= 2^31 - 1`

## Solution

### Approach
The problem can be solved by reversing the digits of the given integer `x`. Here are the steps taken:

1. **Define the range of 32-bit signed integer**: Define constants `INT_MIN` and `INT_MAX` to represent the range of 32-bit signed integers.

2. **Initialize variables**: Initialize variables to store the result and the sign of `x`. Convert `x` to positive to handle negative numbers.

3. **Reverse the digits**: Use a while loop to iterate through each digit of `x`, extract the digits one by one, and build the reversed number.

4. **Handle overflow**: Check if adding the next digit will cause overflow. If so, return 0.

5. **Apply sign and check for range**: Apply the sign to the result and check if the result is within the 32-bit signed integer range. If not, return 0.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(log(x)), where x is the given integer. The number of digits in `x` determines the number of iterations needed.
- **Space Complexity**: O(1), as only a constant amount of extra space is used.

## Usage

You can use the `Solution` class to reverse an integer. Here is how you can do it in Python:

```python
x = 123
sol = Solution()
print(sol.reverse(x))  # Output: 321
