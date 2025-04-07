def uniquePaths(m: int, n: int) -> int:
    """
    Compute the number of unique paths a robot can take to reach the bottom-right corner of a m x n grid.

    Args:
    m (int): The number of rows in the grid.
    n (int): The number of columns in the grid.

    Returns:
    int: The number of unique paths.
    """
    # Initialize the dp table with zeros
    dp = [[0] * n for _ in range(m)]

    # Initialize the base cases
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill in the dp table using the transition
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # The solution is stored in the bottom-right cell of the dp table
    return dp[m-1][n-1]

# Test cases
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 3))  # Output: 6
