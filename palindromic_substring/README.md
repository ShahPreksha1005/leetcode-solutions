## Palindromic Substring

### Problem Description:

Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

### Example:

**Input:**
```
s = "abc"
```

**Output:**
```
3
```

**Explanation:**
Three palindromic strings: "a", "b", "c".

**Input:**
```
s = "aaa"
```

**Output:**
```
6
```

**Explanation:**
Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

### Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.

### Approach:

We can solve this problem by iterating over all possible substrings and checking if each substring is a palindrome. To do this, we define a helper function to check if a given substring is a palindrome. Then, we iterate over all possible substrings and count the number of palindromic substrings.

### Code Implementation:

Refer to the provided code.

---