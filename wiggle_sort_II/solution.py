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
