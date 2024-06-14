class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Store the original value of x to compare later
        original = x
        reversed_num = 0
        
        # Reverse the integer
        while x != 0:
            # Get the last digit
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Compare the reversed integer with the original value
        return reversed_num == original
