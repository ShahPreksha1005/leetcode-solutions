# Minimum Window Substring

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

### Example 1:

**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`  
**Output:** `"BANC"`  
**Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

### Example 2:

**Input:** `s = "a"`, `t = "a"`  
**Output:** `"a"`  
**Explanation:** The entire string s is the minimum window.

### Example 3:

**Input:** `s = "a"`, `t = "aa"`  
**Output:** `""`  
**Explanation:** Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

## Constraints:

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Solution

```python
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Returns the minimum window substring of s such that every character in t
        (including duplicates) is included in the window. If there is no such
        substring, returns the empty string "".
        
        Parameters:
        s (str): The source string.
        t (str): The target string.
        
        Returns:
        str: The minimum window substring of s.
        """
        if not s or not t:
            return ""

        # Dictionary to keep count of all unique characters in t
        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        # Number of unique characters in t that must be present in the desired window
        required = len(dictT)
        
        # Pointers for the sliding window
        l, r = 0, 0
        
        # Formed is used to keep track of how many unique characters in t
        # are currently in the window with their desired frequency
        formed = 0

        # Dictionary to keep count of all unique characters in the current window
        windowCounts = defaultdict(int)
        
        # The result tuple: (window length, left, right)
        ans = float('inf'), None, None

        # Start sliding the window
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            windowCounts[character] += 1

            # If the frequency of the current character added equals to the
            # desired count in t, increment the formed count
            if character in dictT and windowCounts[character] == dictT[character]:
                formed += 1

            # Try to contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]

                # Update the result if this window is smaller than the previous best
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer
                # is no longer a part of the window
                windowCounts[character] -= 1
                if character in dictT and windowCounts[character] < dictT[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window
                l += 1

            # Keep expanding the window once we are done contracting
            r += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
