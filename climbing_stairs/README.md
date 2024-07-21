
# Climbing Stairs

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Examples

### Example 1

- **Input:** `n = 2`
- **Output:** `2`
- **Explanation:** There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps

### Example 2

- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step

## Constraints

- `1 <= n <= 45`

## Solution

To solve the problem of finding the number of distinct ways to climb `n` steps, we can use a dynamic programming approach. We define a `dp` array where `dp[i]` represents the number of ways to reach step `i`.

### Code Explanation

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize dp array to store number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There's only one way to reach step 1
        dp[2] = 2  # There are two ways to reach step 2 (1+1 or 2)
        
        # Fill dp array for steps from 3 to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
```

In this solution:
- We handle the base case where `n = 1` separately because there's only one way to reach the top (by taking one step).
- We initialize a `dp` array where `dp[i]` stores the number of ways to reach step `i`.
- We compute `dp[i]` using the relation `dp[i] = dp[i - 1] + dp[i - 2]`, which means you can reach step `i` by either coming from step `i-1` with a single step or from step `i-2` with a double step.

This approach ensures that we calculate the number of ways efficiently in O(n) time complexity and O(n) space complexity.

---