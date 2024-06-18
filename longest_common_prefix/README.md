# LeetCode Problem: Longest Common Prefix

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

### Example 1:
- **Input:** `strs = ["flower","flow","flight"]`
- **Output:** `"fl"`

### Example 2:
- **Input:** `strs = ["dog","racecar","car"]`
- **Output:** `""`
- **Explanation:** There is no common prefix among the input strings.

### Constraints:
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## Solution

### Approach
To find the longest common prefix, we can use the following approach:
1. **Find the Shortest String**: Identify the shortest string in the list, as the common prefix can't be longer than this string.
2. **Compare Characters**: Iterate through each character of the shortest string and compare it with the same position in all other strings.
3. **Stop at Mismatch**: If a mismatch is found, return the substring up to that point. If no mismatch is found, the shortest string itself is the common prefix.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

### Edge Cases
- If the input list is empty, return an empty string.
- If there is no common prefix, return an empty string.

## Complexity Analysis
- **Time Complexity**: O(S), where S is the sum of all characters in all strings. In the worst case, all characters are checked.
- **Space Complexity**: O(1), as no extra space proportional to input size is used.

## Usage

You can use the `Solution` class to find the longest common prefix among an array of strings. Here is how you can do it in Python:

```python
strs = ["flower", "flow", "flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))  # Output: "fl"
