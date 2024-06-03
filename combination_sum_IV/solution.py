from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a list `dp` where dp[i] represents the number of ways to get the sum `i`.
        # We use target+1 because we want to include the target index.
        dp = [0] * (target + 1)
        
        # Base case: There is one way to get a sum of 0, which is to use no elements.
        dp[0] = 1

        # Iterate over each value from 1 to target (inclusive) to fill the dp array.
        for i in range(1, target + 1):
            # For each value `i`, iterate over each number in `nums`.
            for num in nums:
                # If `i - num` is non-negative, it means we can form the sum `i` by adding `num`
                # to the combinations that form the sum `i - num`.
                if i - num >= 0:
                    # Update dp[i] by adding the number of ways to form the sum `i - num`.
                    dp[i] += dp[i - num]

        # The answer will be in dp[target], which represents the number of ways to form the sum `target`.
        return dp[target]

# Example usage:
# Uncomment the lines below to test the function with example inputs.
# solution = Solution()
# print(solution.combinationSum4([1, 2, 3], 4))  # Output: 7
# print(solution.combinationSum4([9], 3))       # Output: 0
