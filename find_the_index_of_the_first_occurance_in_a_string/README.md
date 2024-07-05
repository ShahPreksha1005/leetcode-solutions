
# Find the Index of the First Occurrence in a String

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

## Examples

### Example 1

- **Input:** `haystack = "sadbutsad"`, `needle = "sad"`
- **Output:** `0`
- **Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

### Example 2

- **Input:** `haystack = "leetcode"`, `needle = "leeto"`
- **Output:** `-1`
- **Explanation:** "leeto" did not occur in "leetcode", so we return -1.

## Constraints

- `1 <= haystack.length, needle.length <= 104`
- `haystack` and `needle` consist of only lowercase English characters.

## Approach

To solve this problem efficiently, we can use a sliding window approach to check each substring of `haystack` that is of the same length as `needle` to see if it matches `needle`.

## Solution

### Detailed Code with Comments

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Args:
        haystack (str): The string to be searched.
        needle (str): The substring to search for.

        Returns:
        int: The index of the first occurrence of needle, or -1 if not found.
        """
        # Lengths of the haystack and the needle
        h_len = len(haystack)
        n_len = len(needle)
        
        # If needle is empty, return 0 (common convention)
        if n_len == 0:
            return 0
        
        # If haystack is shorter than needle, needle cannot be part of haystack
        if h_len < n_len:
            return -1
        
        # Iterate through the haystack using a sliding window of size equal to needle length
        for i in range(h_len - n_len + 1):
            # Check if the substring of haystack starting at i matches needle
            if haystack[i:i + n_len] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1
```

## Explanation

1. **Initialization:**
   - Calculate the lengths of `haystack` and `needle`.
   - Check for the special case when `needle` is empty; by convention, we return 0.
   - If `haystack` is shorter than `needle`, return -1 as `needle` cannot be a substring of `haystack`.

2. **Sliding Window:**
   - Use a for-loop to iterate through `haystack`, where each iteration considers a substring of length equal to `needle`.
   - Compare the current substring with `needle`.
   - If a match is found, return the current index.

3. **Return -1:**
   - If the loop completes without finding a match, return -1.
