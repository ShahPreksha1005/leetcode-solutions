# Wiggle Sort II

## Problem Statement

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]....`

You may assume the input array always has a valid answer.

### Example 1:

**Input:** `nums = [1,5,1,1,6,4]`  
**Output:** `[1,6,1,5,1,4]`  
**Explanation:** `[1,4,1,5,1,6]` is also accepted.

### Example 2:

**Input:** `nums = [1,3,2,2,3,1]`  
**Output:** `[2,3,1,3,1,2]`  

## Constraints:

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- It is guaranteed that there will be an answer for the given input `nums`.

## Follow Up:

Can you do it in `O(n)` time and/or in-place with `O(1)` extra space?

## Solution

```python
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Reorders the array such that nums[0] < nums[1] > nums[2] < nums[3]....
        
        Parameters:
        nums (List[int]): The input list of integers to be reordered.
        
        Returns:
        None: The function modifies the list in place.
        """
        n = len(nums)
        # Sort the numbers in reverse order
        nums.sort(reverse=True)
        
        # Partition the array into two halves
        # First half will be the larger half in reverse order
        # Second half will be the smaller half in reverse order
        mid = (n + 1) // 2
        # Split and reorder the elements into the required wiggle pattern
        nums[::2], nums[1::2] = nums[mid:], nums[:mid]

        # The above line can be broken down into:
        # nums[::2] (even index positions) should be filled with the smaller half
        # nums[1::2] (odd index positions) should be filled with the larger half
