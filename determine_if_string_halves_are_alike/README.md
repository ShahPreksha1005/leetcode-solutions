### Determine if String Halves Are Alike

**Problem Statement:**
Given a string `s` of even length, determine if the first and second halves of the string have the same number of vowels.

**Approach:**
We count the number of vowels in each half of the string and compare the counts to determine if they are equal.

**Implementation:**
- Iterate through the string and count the number of vowels in each half.
- Compare the counts of vowels in both halves to determine if they are equal.

**Example Usage:**
```python
s = "book"
print(halvesAreAlike(s))  # Output: true
```
