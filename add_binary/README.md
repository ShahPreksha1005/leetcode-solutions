
# Add Binary

## Problem Description

Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

### Example 1

- **Input:** `a = "11"`, `b = "1"`
- **Output:** `"100"`

### Example 2

- **Input:** `a = "1010"`, `b = "1011"`
- **Output:** `"10101"`

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution

To solve the problem of adding two binary strings, we can simulate the addition process manually, handling the carry as we traverse each digit from right to left.

### Code Explanation

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return the sum as a binary string.
        
        Args:
        a (str): The first binary string.
        b (str): The second binary string.
        
        Returns:
        str: The sum of the two binary strings as a binary string.
        """
        # Initialize the result and carry
        result = []
        carry = 0
        
        # Pointers for a and b starting from the end
        i, j = len(a) - 1, len(b) - 1
        
        # Loop through both strings from end to start
        while i >= 0 or j >= 0 or carry:
            # Get the current bits
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum and the carry
            total = bit_a + bit_b + carry
            carry = total // 2  # Determine the new carry
            result.append(str(total % 2))  # Append the result bit
            
            # Move to the next digits
            i -= 1
            j -= 1
        
        # Reverse the result list and convert it to a string
        return ''.join(result[::-1])
```

## Explanation

1. **Initialization**:
   - `result` is an empty list that will store the resulting binary string.
   - `carry` is initialized to 0.

2. **Pointers**:
   - `i` and `j` are pointers that start from the end of the strings `a` and `b` respectively.

3. **Loop Through Strings**:
   - The loop runs while there are still digits to process in either string or there is a carry left to add.
   - `bit_a` and `bit_b` are the current bits from `a` and `b` respectively, defaulting to 0 if the pointer is out of bounds.

4. **Sum and Carry**:
   - The `total` is calculated by adding `bit_a`, `bit_b`, and `carry`.
   - The new `carry` is determined by `total // 2`.
   - The current bit (either 0 or 1) is appended to the `result` list by `total % 2`.

5. **Move Pointers**:
   - `i` and `j` are decremented to move to the next digits in `a` and `b`.

6. **Return Result**:
   - The `result` list is reversed (since we appended bits from the least significant to the most significant) and converted to a string.

This approach ensures an efficient solution with optimal space and time complexity.
