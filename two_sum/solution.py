class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers `nums` and an integer `target`, return indices of the 
        two numbers such that they add up to `target`.

        You may assume that each input would have exactly one solution, and you may not 
        use the same element twice.

        Parameters:
        nums (List[int]): List of integers.
        target (int): Target sum for which we need to find two numbers in `nums`.

        Returns:
        List[int]: Indices of the two numbers such that they add up to `target`.
        
        Example:
        --------
        >>> solution = Solution()
        >>> solution.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        
        Constraints:
        ------------
        - 2 <= nums.length <= 10^4
        - -10^9 <= nums[i] <= 10^9
        - -10^9 <= target <= 10^9
        - Only one valid answer exists.
        """
        # Dictionary to store the value and its index
        num_dict = {}

        # Enumerate over the list to get both index and value
        for i, num in enumerate(nums):
            # Calculate the complement that when added to the current number equals the target
            complement = target - num
            
            # If the complement is found in the dictionary, return the indices
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

        # If no solution is found (though the problem guarantees one solution), return an empty list
        return []

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
