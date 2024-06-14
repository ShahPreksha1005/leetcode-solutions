class Solution:
    def reverse(self, x: int) -> int:
        # Define the range of 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize variables to store the result and sign of x
        result, sign = 0, 1 if x >= 0 else -1
        # Convert x to positive to handle negative numbers
        x = abs(x)
        
        # Reverse the digits of x
        while x != 0:
            digit = x % 10
            # Check if adding the next digit will cause overflow
            if result > (INT_MAX - digit) // 10:
                return 0
            # Update the result by adding the next digit
            result = result * 10 + digit
            x //= 10
        
        # Apply the sign to the result
        result *= sign
        
        # Check if the result is within the 32-bit signed integer range
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result
