
# Length of Last Word

## Problem Description

Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

## Examples

### Example 1

- **Input:** `s = "Hello World"`
- **Output:** `5`
- **Explanation:** The last word is "World" with length 5.

### Example 2

- **Input:** `s = "   fly me   to   the moon  "`
- **Output:** `4`
- **Explanation:** The last word is "moon" with length 4.

### Example 3

- **Input:** `s = "luffy is still joyboy"`
- **Output:** `6`
- **Explanation:** The last word is "joyboy" with length 6.

## Constraints

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces ' '.
- There will be at least one word in `s`.

## Approach

The goal is to find the length of the last word in the string `s`. We can achieve this by iterating backwards through the string, counting characters until we encounter a space after some characters.

## Solution

### Detailed Code with Comments

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the string s.

        Args:
        s (str): A string consisting of words and spaces.

        Returns:
        int: The length of the last word.
        """
        length = 0
        # Start from the end of the string and move backwards
        for i in range(len(s) - 1, -1, -1):
            # If we encounter a space after counting some characters, break
            if s[i] == ' ' and length > 0:
                break
            # If the character is not a space, increment the length counter
            elif s[i] != ' ':
                length += 1
        
        return length
```

## Explanation

1. **Initialization:**
   - Initialize `length` to keep track of the length of the last word.

2. **Iterate Backwards:**
   - Iterate from the end of the string towards the beginning.
   - If a space is encountered after counting some characters (indicating the end of the last word), break out of the loop.
   - If the character is not a space, increment the `length` counter.

3. **Return Length:**
   - Return the length of the last word.
