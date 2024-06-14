# LeetCode Problem: Palindrome Number

## Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

### Example 1:
- **Input:** `x = 121`
- **Output:** `true`
- **Explanation:** `121` reads as `121` from left to right and from right to left.

### Example 2:
- **Input:** `x = -121`
- **Output:** `false`
- **Explanation:** From left to right, it reads `-121`. From right to left, it becomes `121-`. Therefore it is not a palindrome.

### Example 3:
- **Input:** `x = 10`
- **Output:** `false`
- **Explanation:** Reads `01` from right to left. Therefore it is not a palindrome.

### Constraints:
- `-2^31 <= x <= 2^31 - 1`

### Follow Up:
Could you solve it without converting the integer to a string?

## Solution

### Approach
To solve this problem without converting the integer to a string, we can reverse the integer and compare it to the original value. If the reversed integer matches the original integer, then the number is a palindrome. Here are the steps taken:

1. **Handle Negative Numbers**: Negative numbers are not palindromes by definition since the negative sign only appears on one side.

2. **Store Original Value**: Store the original value of `x` to compare it later with the reversed number.

3. **Reverse the Integer**: Use a loop to reverse the digits of `x`. Extract the last digit of `x` and build the reversed number.

4. **Compare with Original Value**: Compare the reversed number with the original value. If they are equal, `x` is a palindrome.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(log(x)), where `x` is the given integer. The number of digits in `x` determines the number of iterations needed.
- **Space Complexity**: O(1), as only a constant amount of extra space is used.

## Usage

You can use the `Solution` class to check if an integer is a palindrome. Here is how you can do it in Python:

```python
x = 121
sol = Solution()
print(sol.isPalindrome(x))  # Output: true
