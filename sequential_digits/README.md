# Sequential Digits

## Problem Statement

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Given a range `[low, high]`, return a sorted list of all the integers in the range that have sequential digits.

## Examples

### Example 1
Input: `low = 100`, `high = 300`  
Output: `[123, 234]`

### Example 2
Input: `low = 1000`, `high = 13000`  
Output: `[1234, 2345, 3456, 4567, 5678, 6789, 12345]`

## Constraints

- `10 <= low <= high <= 10^9`

## Solution

We solve this problem by generating all possible sequential digit numbers and filtering them to find those within the given range `[low, high]`.

### Approach
1. **Generate Sequential Digits**: Generate all possible sequential digit numbers by iterating through starting digits from 1 to 9.
2. **Filter by Range**: Only include numbers within the specified range `[low, high]`.
3. **Sort the Result**: Return the sorted list of filtered sequential digit numbers.

### Code

```python
def sequentialDigits(low, high):
    # List to store all possible sequential digit numbers
    sequential_numbers = []

    # Start digits can be from 1 to 9
    for start in range(1, 10):
        num = start
        next_digit = start
        
        # Generate sequential numbers starting with 'start' digit
        while num <= high and next_digit < 10:
            if num >= low:
                sequential_numbers.append(num)
            next_digit += 1
            num = num * 10 + next_digit

    # Return sorted list of sequential digit numbers within the range
    return sorted(sequential_numbers)

# Example usage
print(sequentialDigits(100, 300))  # Output: [123, 234]
print(sequentialDigits(1000, 13000))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]
