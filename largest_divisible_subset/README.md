# Largest Divisible Subset

## Problem Statement

Given a set of distinct positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

- `answer[i] % answer[j] == 0`, or
- `answer[j] % answer[i] == 0`

If there are multiple solutions, return any of them.

## Examples

### Example 1:
**Input:** `nums = [1, 2, 3]`

**Output:** `[1, 2]`

**Explanation:** `[1, 3]` is also accepted.

### Example 2:
**Input:** `nums = [1, 2, 4, 8]`

**Output:** `[1, 2, 4, 8]`

## Constraints:

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 10^9`
- All the integers in `nums` are unique.

## Solution

The solution uses dynamic programming to find the largest subset. We first sort the array. Then, we use a `dp` array where `dp[i]` represents the size of the largest subset ending with `nums[i]`. For each element, we check all previous elements to see if they divide the current element. We also maintain the maximum size of any subset found and the index of the last element in that subset.

### Python Code

```python
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
