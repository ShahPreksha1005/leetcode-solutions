## Longest Repeating Character Replacement

### Problem Description:
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Examples:
#### Example 1:
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```
#### Example 2:
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

### Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.

### Detailed Explanation:
1. **Character Count Array Initialization**:
   - `int[] charCount = new int[26];`: This array will store the count of each character in the current window.

2. **Variables Initialization**:
   - `int result = 0;`: This will store the length of the longest valid window.
   - `int maxCount = 0;`: This will store the maximum frequency of any single character in the current window.

3. **Sliding Window Approach**:
   - Use two pointers, `left` and `right`, to represent the window.
   - Iterate with the `right` pointer over the string.

4. **Update Character Count**:
   - `charCount[s.charAt(right) - 'A']++;`: Increment the count of the current character.

5. **Update Maximum Frequency**:
   - `maxCount = Math.max(maxCount, charCount[s.charAt(right) - 'A']);`: Update the maximum frequency of any character in the current window.

6. **Check Validity of Window**:
   - `if (right - left + 1 - maxCount > k)`: If the current window is invalid (i.e., the number of changes needed is more than `k`), shrink the window from the left.
   - `charCount[s.charAt(left) - 'A']--;`: Decrement the count of the character at the left pointer.
   - `left++;`: Move the left pointer to the right.

7. **Update Result**:
   - `result = Math.max(result, right - left + 1);`: Update the result with the maximum window size seen so far.

### Usage:
- The `characterReplacement` method can be used to find the length of the longest substring containing the same letter you can get after performing at most `k` replacements in the given string `s`. This solution is efficient and operates in O(n) time complexity, suitable for large inputs as specified in the problem constraints.