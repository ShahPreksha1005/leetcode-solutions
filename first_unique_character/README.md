# First Unique Character in a String

## Problem Statement

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

### Example 1:

Input: s = "leetcode"
Output: 0

### Example 2:

Input: s = "loveleetcode"
Output: 2

### Example 3:

Input: s = "aabb"
Output: -1

## Solution

```python
class Solution:
    def firstUniqChar(self, s):
        # Dictionary to store character counts
        char_count = {}

        # Count occurrences of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Iterate over the string to find the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no non-repeating character is found, return -1
        return -1
```

## How to Use

1. Create an instance of the `Solution` class.
2. Call the `firstUniqChar` method with the input string as the argument.

```python
solution = Solution()
print(solution.firstUniqChar("leetcode"))      # Output: 0
print(solution.firstUniqChar("loveleetcode"))  # Output: 2
print(solution.firstUniqChar("aabb"))          # Output: -1
```

This README provides a problem statement, examples, solution approach, and usage instructions for the First Unique Character in a String problem.
