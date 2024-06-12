# LeetCode Problem: Longest Palindromic Substring

## Problem Statement
Given a string `s`, return the longest palindromic substring in `s`.

### Example 1:
- **Input:** `s = "babad"`
- **Output:** `"bab"`
- **Explanation:** `"aba"` is also a valid answer.

### Example 2:
- **Input:** `s = "cbbd"`
- **Output:** `"bb"`

### Constraints:
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Solution

### Approach
The problem can be solved using the concept of expanding around the center. Here are the steps taken:

1. **Define a function to expand around the center**: This function will take two indices as input and expand around the center to find the longest palindrome substring centered at those indices.

2. **Initialize variables to store the start and end indices of the longest palindrome**: These variables will be updated as we iterate through each character in the string.

3. **Iterate through each character in the string**: For each character, we expand around the center to find both odd-length and even-length palindromes. We update the start and end indices if a longer palindrome is found.

4. **Return the longest palindrome substring**: After iterating through all characters, we return the substring of the longest palindrome found.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(n^2), where n is the length of the input string. Each character is expanded around its center, resulting in a quadratic time complexity.
- **Space Complexity**: O(1), as only a constant amount of extra space is used.

## Usage

You can use the `Solution` class to find the longest palindromic substring. Here is how you can do it in Python:

```python
s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))  # Output: "bab"
