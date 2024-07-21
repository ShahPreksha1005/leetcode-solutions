class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Calculate the square root of x rounded down to the nearest integer.
        
        Args:
        x (int): The non-negative integer to find the square root of.
        
        Returns:
        int: The square root of x rounded down to the nearest integer.
        """
        if x < 2:
            return x
        
        # Initialize the binary search bounds
        left, right = 1, x // 2
        
        while left <= right:
            # Calculate the mid-point
            mid = (left + right) // 2
            # Calculate the square of the mid-point
            square = mid * mid
            
            if square == x:
                return mid  # If mid*mid is exactly x, mid is the square root
            elif square < x:
                left = mid + 1  # If mid*mid is less than x, move to the right half
            else:
                right = mid - 1  # If mid*mid is greater than x, move to the left half
        
        return right  # Right is the integer part of the square root of x
