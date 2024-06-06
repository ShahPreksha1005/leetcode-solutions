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
