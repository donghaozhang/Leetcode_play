def uniquePaths(m: int, n: int) -> int:
    # Create a DP table initialized to 1 since dp[0][j] and dp[i][0] are all 1
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Test cases
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(1, 1))  # Output: 1
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 3))  # Output: 6
