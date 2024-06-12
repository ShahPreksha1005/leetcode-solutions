# LeetCode Problem: Zigzag Conversion

## Problem Statement
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P A H N
A P L S I I G
Y I R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

### Example 1:
- **Input:** `s = "PAYPALISHIRING"`, `numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`

### Example 2:
- **Input:** `s = "PAYPALISHIRING"`, `numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`
- **Explanation:**

P I N
A L S I G
Y A H R
P I


### Example 3:
- **Input:** `s = "A"`, `numRows = 1`
- **Output:** `"A"`

### Constraints:
- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), ',' and '.'
- `1 <= numRows <= 1000`

## Solution

### Approach
The problem can be solved by simulating the zigzag pattern and storing characters in each row. Here are the steps taken:

1. **Edge Case Handling**: If numRows is 1, return the original string.

2. **Initialize Data Structures**: Initialize a list of strings to store characters in each row.

3. **Iterate Through the String**: Iterate through each character in the string and append it to the appropriate row.

4. **Update Row and Direction**: Update the current row and the direction of movement based on reaching the top or bottom row.

5. **Concatenate Rows**: Concatenate all rows to form the zigzag pattern.

### Code Explanation
The provided Python code implements the approach described above. Detailed comments are provided within the code to explain each step.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input string. Each character is processed once.
- **Space Complexity**: O(n), where n is the length of the input string. Space is used to store characters in each row.

## Usage

You can use the `Solution` class to convert a string into the zigzag pattern. Here is how you can do it in Python:

```python
s = "PAYPALISHIRING"
numRows = 3

sol = Solution()
print(sol.convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"
