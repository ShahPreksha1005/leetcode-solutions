class Solution:
    def myPow(self, x: float, n: int) -> float:
        # If n is negative, change x to its reciprocal and make n positive
        if n < 0:
            n = -n
            x = 1 / x
        
        pow_result = 1
        
        # Iterate until n becomes 0
        while n != 0:
            # If the least significant bit of n is set
            if n & 1:
                pow_result *= x  # Multiply pow_result by x
            
            x *= x  # Square x for the next iteration
            n >>= 1  # Right shift n by 1 bit
        
        return pow_result  # Return the final result
