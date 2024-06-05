# Minimum Number of Steps to Make Two Strings Anagram

## Problem Statement

You are given two strings of the same length `s` and `t`. In one step, you can choose any character of `t` and replace it with another character.

Return the minimum number of steps to make `t` an anagram of `s`.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

## Examples

### Example 1
Input: `s = "bab"`, `t = "aba"`  
Output: `1`  
Explanation: Replace the first 'a' in `t` with 'b', resulting in `t = "bba"`, which is an anagram of `s`.

### Example 2
Input: `s = "leetcode"`, `t = "practice"`  
Output: `5`  
Explanation: Replace 'p', 'r', 'a', 'i', and 'c' in `t` with the proper characters to make `t` an anagram of `s`.

### Example 3
Input: `s = "anagram"`, `t = "mangaar"`  
Output: `0`  
Explanation: "anagram" and "mangaar" are already anagrams.

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `s.length == t.length`
- `s` and `t` consist of lowercase English letters only.

## Solution

To solve this problem, we count the frequency of each character in both strings `s` and `t`, calculate the differences, and sum these differences to find the minimum number of steps required.

### Approach

1. **Count Frequencies**: Count the frequency of each character in both strings `s` and `t`.
2. **Calculate Differences**: For each character, calculate how many times more it appears in `t` than in `s`.
3. **Sum of Differences**: The total number of steps required will be the sum of all these differences.

### Code

```python
from collections import Counter

def minSteps(s, t):
    # Count the frequency of each character in both strings
    s_count = Counter(s)
    t_count = Counter(t)
    
    # Initialize the number of steps needed to 0
    steps = 0
    
    # Iterate over the character counts in s
    for char in s_count:
        # If the character is more frequent in s than in t,
        # calculate the difference and add it to steps
        if s_count[char] > t_count[char]:
            steps += s_count[char] - t_count[char]
    
    return steps

# Example usage
print(minSteps("bab", "aba"))         # Output: 1
print(minSteps("leetcode", "practice")) # Output: 5
print(minSteps("anagram", "mangaar"))   # Output: 0
