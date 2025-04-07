# backpack_iii.md
- 不同路径 / Unique Paths [LeetCode 62]

## Problem Description

## Unique Paths
A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

### Example 1:
```
Input: m = 3, n = 7
Output: 28
```

### Example 2:
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

### Example 3:
```
Input: m = 7, n = 3
Output: 28
```

### Example 4:
```
Input: m = 3, n = 3
Output: 6
```

### Constraints:
* `1 <= m, n <= 100`
* It's guaranteed that the answer will be less than or equal to `2 * 10^9`.

## Solution

**Problem Explanation**
The problem is to find the number of unique paths a robot can take to reach the bottom-right corner of a `m x n` grid, starting from the top-left corner. The robot can only move either down or right at any point in time.

**Step-by-Step Approach**
1. **Understand the problem constraints**: The grid size is `m x n`, where `1 <= m, n <= 100`. The robot starts at the top-left corner and can only move down or right.
2. **Identify the problem type**: This is a classic dynamic programming problem, as the number of unique paths to a cell depends on the number of unique paths to its neighboring cells.
3. **Define the state**: Let `dp[i][j]` be the number of unique paths to reach the cell at position `(i, j)`.
4. **Derive the transition**: To reach a cell `(i, j)`, the robot can come from either the top cell `(i-1, j)` or the left cell `(i, j-1)`. Therefore, `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
5. **Initialize the base cases**: The first row and the first column are special cases, as there is only one way to reach each cell in these rows (by always moving right or always moving down, respectively). Therefore, `dp[0][j] = 1` for all `j`, and `dp[i][0] = 1` for all `i`.
6. **Compute the solution**: Fill in the `dp` table using the transition derived above.

**Python Solution**
```python
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
```

**Time and Space Complexity Analysis**

* Time complexity: O(m*n), as we need to fill in the `dp` table of size `m x n`.
* Space complexity: O(m*n), as we need to store the `dp` table of size `m x n`.

**Optimized Space Complexity Solution**
We can optimize the space complexity to O(n) by observing that we only need to keep track of the previous row to compute the current row.
```python
def uniquePaths(m: int, n: int) -> int:
    prev_row = [1] * n
    for _ in range(1, m):
        curr_row = [1] * n
        for j in range(1, n):
            curr_row[j] = prev_row[j] + curr_row[j-1]
        prev_row = curr_row
    return prev_row[-1]

# Test cases
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 3))  # Output: 6
```
* Time complexity: O(m*n)
* Space complexity: O(n)