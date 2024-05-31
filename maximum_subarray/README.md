# Maximum Subarray

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

### Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

### Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

### Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

## Constraints:

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Solution

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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
