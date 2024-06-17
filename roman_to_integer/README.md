# LeetCode Problem: Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Given a Roman numeral, convert it to an integer.

### Example 1:
- **Input:** `s = "III"`
- **Output:** `3`
- **Explanation:** `III = 3`.

### Example 2:
- **Input:** `s = "LVIII"`
- **Output:** `58`
- **Explanation:** `L = 50`, `V = 5`, `III = 3`.

### Example 3:
- **Input:** `s = "MCMXCIV"`
- **Output:** `1994`
- **Explanation:** `M = 1000`, `CM = 900`, `XC = 90`, and `IV = 4`.

### Constraints:
- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is guaranteed that `s` is a valid Roman numeral in the range `[1, 3999]`.

## Solution

### Approach
To convert a Roman numeral to an integer, follow these steps:
1. **Dictionary for Mapping**: Create a dictionary to map Roman numerals to their integer values.
2. **Iterate and Calculate**: Iterate through the string in reverse order. If the current numeral is less than the previous one, subtract it from the total; otherwise, add it to the total.
3. **Update Previous Value**: Update the previous value to the current numeral's value for the next iteration.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the string `s`. We iterate through the string once.
- **Space Complexity**: O(1), as the space used by the dictionary and variables does not depend on the input size.

## Usage

You can use the `Solution` class to convert a Roman numeral to an integer. Here is how you can do it in Python:

```python
s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))  # Output: 1994
