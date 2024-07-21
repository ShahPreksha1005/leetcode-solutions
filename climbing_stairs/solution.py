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
