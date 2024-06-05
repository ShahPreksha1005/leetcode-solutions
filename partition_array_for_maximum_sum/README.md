# Partition Array for Maximum Sum

## Problem Statement

Given an integer array `arr`, partition the array into contiguous subarrays of length at most `k`. After partitioning, each subarray has its values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

## Examples

### Example 1
Input: `arr = [1, 15, 7, 9, 2, 5, 10]`, `k = 3`  
Output: `84`  
Explanation: The array becomes `[15, 15, 15, 9, 10, 10, 10]`.

### Example 2
Input: `arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]`, `k = 4`  
Output: `83`

### Example 3
Input: `arr = [1]`, `k = 1`  
Output: `1`

## Constraints
- `1 <= arr.length <= 500`
- `0 <= arr[i] <= 10^9`
- `1 <= k <= arr.length`

## Solution

We solve this problem using dynamic programming. The core idea is to maintain a DP array `dp` where `dp[i]` represents the maximum sum we can achieve for the subarray `arr[0]` to `arr[i]`.

### Approach
1. **Dynamic Programming Array (`dp`)**: Initialize a DP array `dp` with zeros, where `dp[i]` holds the maximum sum of the subarray from the start to the `i`th element.
2. **Partitioning Logic**: For each element `i`, consider all possible partitions ending at `i` with lengths from `1` to `k`. Track the maximum value within each partition and update `dp[i]` accordingly.
3. **Look-back and Update**: Use a nested loop to look back up to `k` elements. For each partition length, compute the possible maximum sum by adding the best partition sum up to the start of the current partition and the current partition's maximum value multiplied by its length.

### Code

```python
def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        max_partition_value = 0
        for j in range(1, k+1):
            if i - j + 1 >= 0:
                max_partition_value = max(max_partition_value, arr[i - j + 1])
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + max_partition_value * j)
                else:
                    dp[i] = max(dp[i], max_partition_value * j)
    return dp[-1]
