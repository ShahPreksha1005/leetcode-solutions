from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the subarray with the largest sum and return its sum.
        
        Parameters:
        nums (List[int]): Input array of integers.
        
        Returns:
        int: Sum of the subarray with the largest sum.
        """
        # Initialize variables to store the maximum sum and current sum
        maxSum = float('-inf')
        currentSum = 0
        
        # Iterate through the array
        for num in nums:
            # Add the current number to the current sum
            currentSum += num
            
            # Update the maximum sum if the current sum is greater
            if currentSum > maxSum:
                maxSum = currentSum
            
            # If the current sum becomes negative, reset it to 0
            if currentSum < 0:
                currentSum = 0
        
        # Return the maximum sum found
        return maxSum
