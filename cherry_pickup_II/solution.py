def cherryPickup(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Initialize the DP table
    dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]
    
    # Base case: fill the last row with grid values
    for col1 in range(cols):
        for col2 in range(cols):
            if col1 == col2:
                dp[rows-1][col1][col2] = grid[rows-1][col1]
            else:
                dp[rows-1][col1][col2] = grid[rows-1][col1] + grid[rows-1][col2]
    
    # Fill the DP table from bottom to top
    for row in range(rows-2, -1, -1):
        for col1 in range(cols):
            for col2 in range(cols):
                max_cherries = 0
                for new_col1 in [col1-1, col1, col1+1]:
                    for new_col2 in [col2-1, col2, col2+1]:
                        if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                            max_cherries = max(max_cherries, dp[row+1][new_col1][new_col2])
                if col1 == col2:
                    dp[row][col1][col2] = grid[row][col1] + max_cherries
                else:
                    dp[row][col1][col2] = grid[row][col1] + grid[row][col2] + max_cherries
    
    return dp[0][0][cols-1]

# Example usage
grid1 = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(cherryPickup(grid1))  # Output: 24

grid2 = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
print(cherryPickup(grid2))  # Output: 28
