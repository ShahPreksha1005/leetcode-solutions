def maxSumAfterPartitioning(arr, k):
    # Length of the array
    n = len(arr)
    
    # DP array initialized to zero
    dp = [0] * n
    
    # Iterate over each position in the array
    for i in range(n):
        # Initialize variables to store the maximum value in the current partition
        max_partition_value = 0
        
        # Look back up to k elements to form the partition
        for j in range(1, k+1):
            # Ensure we do not go out of bounds
            if i - j + 1 >= 0:
                # Update the maximum value in the current partition
                max_partition_value = max(max_partition_value, arr[i - j + 1])
                # Update the DP array considering the maximum value of the current partition
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + max_partition_value * j)
                else:
                    dp[i] = max(dp[i], max_partition_value * j)
    
    # The last element of dp array contains the answer
    return dp[-1]

# Example usage
print(maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))  # Output: 84
print(maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))  # Output: 83
print(maxSumAfterPartitioning([1], 1))  # Output: 1
