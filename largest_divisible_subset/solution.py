from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] will store the size of the largest divisible subset ending with nums[i]
        max_size, max_index = 1, 0

        # Fill the dp array
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        # Reconstruct the largest divisible subset
        result = []
        current_num = nums[max_index]
        current_size = max_size
        for i in range(max_index, -1, -1):
            if current_num % nums[i] == 0 and dp[i] == current_size:
                result.append(nums[i])
                current_num = nums[i]
                current_size -= 1

        return result[::-1]  # reverse the result to get the correct order

# Example usage:
# solution = Solution()
# print(solution.largestDivisibleSubset([1,2,4,8]))  # Output: [1, 2, 4, 8]
