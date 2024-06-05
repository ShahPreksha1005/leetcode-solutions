### Minimum Deletions to Make Character Frequencies Unique

**Problem Statement:**
Given a string `s`, determine the minimum number of characters needed to delete to make the character frequencies unique.

**Approach:**
We count the frequencies of characters in the string and keep track of the characters whose frequencies are not unique. The number of deletions needed is equal to the count of non-unique frequencies.

**Implementation:**
- Count the frequencies of characters in the string.
- Keep track of characters whose frequencies are not unique.
- Return the count of non-unique frequencies as the result.

**Example Usage:**
```python
s = "aaabbbcc"
print(minDeletionsToMakeUnique(s))  # Output: 2
```
