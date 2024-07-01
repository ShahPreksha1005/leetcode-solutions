# LeetCode Problem: Valid Parentheses

## Problem Statement
Given a string `s` containing just the characters `('(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
- **Input:** `s = "()"`
- **Output:** `true`

### Example 2:
- **Input:** `s = "()[]{}"`
- **Output:** `true`

### Example 3:
- **Input:** `s = "(]"`
- **Output:** `false`

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `()[]{}'`.

## Solution

### Approach
To determine if the given string of parentheses is valid:
1. **Use a Stack**: Use a stack to keep track of the opening brackets encountered.
2. **Match Brackets**: When a closing bracket is encountered, check if it matches the top of the stack.
3. **Final Check**: At the end, if the stack is empty, all brackets were matched correctly.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

### Edge Cases
- If the string is empty, it is considered valid.
- If the string starts with a closing bracket, it is invalid.
- If there are unmatched brackets, the string is invalid.

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the string. We iterate through each character once.
- **Space Complexity**: O(n) in the worst case, where all characters are opening brackets.

## Usage

You can use the `Solution` class to check if a string of parentheses is valid. Here is how you can do it in Python:

```python
s = "([{}])"
sol = Solution()
print(sol.isValid(s))  # Output: true
