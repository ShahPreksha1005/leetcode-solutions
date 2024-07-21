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
