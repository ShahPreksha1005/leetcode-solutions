# LeetCode Problem: Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1:
- **Input:** `s = "abcabcbb"`
- **Output:** `3`
- **Explanation:** The answer is "abc", with the length of 3.

### Example 2:
- **Input:** `s = "bbbbb"`
- **Output:** `1`
- **Explanation:** The answer is "b", with the length of 1.

### Example 3:
- **Input:** `s = "pwwkew"`
- **Output:** `3`
- **Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Solution

### Approach
The solution uses the sliding window technique combined with a hash map (or dictionary) to efficiently find the length of the longest substring without repeating characters. Here are the steps taken:

1. **Initialize Data Structures**: Use a hash map to store the last occurrence index of each character. Also, initialize variables to track the start of the current window and the maximum length of substrings found.

2. **Iterate Through the String**: Loop through each character in the string while maintaining the current window of characters that do not repeat.

3. **Update Window**: If a repeating character is found within the current window, move the start of the window to the next character after the last occurrence of the repeating character.

4. **Update Maximum Length**: Calculate the length of the current window and update the maximum length found.

### Code Explanation (Python)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last positions of each character
        char_index = {}
        # Initialize the start of the current window and max length
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            # If the character is already in the dictionary and is in the current window
            if char in char_index and char_index[char] >= start:
                # Move the start to the next position of the last occurrence
                start = char_index[char] + 1
            # Update the last position of the character
            char_index[char] = i
            # Calculate the length of the current window
            max_length = max(max_length, i - start + 1)

        return max_length
