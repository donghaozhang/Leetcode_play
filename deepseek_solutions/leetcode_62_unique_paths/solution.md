# backpack_iii.md)
- 不同路径 / Unique Paths [LeetCode 62]

## Problem Description

# 62. Unique Paths

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

## Example 1:
![robot_maze](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

**Input:** m = 3, n = 7  
**Output:** 28  

## Example 2:

**Input:** m = 3, n = 2  
**Output:** 3  
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

## Constraints:
- `1 <= m, n <= 100`

## Solution

### Problem Explanation:
The problem requires us to find the number of unique paths a robot can take from the top-left corner (0,0) to the bottom-right corner (m-1, n-1) of an m x n grid. The robot can only move either right or down at any point in time. 

This is a classic combinatorial problem where the solution can be derived using dynamic programming or combinatorics. The key observation is that to reach the bottom-right corner, the robot must make exactly (m-1) down moves and (n-1) right moves, in any order. The total number of unique paths is the number of ways to arrange these moves.

### Approach:
1. **Dynamic Programming (DP) Approach**:
   - We can use a DP table where `dp[i][j]` represents the number of unique paths to reach cell (i, j).
   - The robot can reach cell (i, j) either from the cell above (i-1, j) or from the cell to the left (i, j-1). Therefore, `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
   - The base case is `dp[0][j] = 1` for all j (only one way to move right) and `dp[i][0] = 1` for all i (only one way to move down).

2. **Combinatorics Approach**:
   - The total number of moves required is (m-1 + n-1) = (m+n-2) moves.
   - Out of these, we need to choose (m-1) down moves (or equivalently (n-1) right moves).
   - The number of unique paths is given by the binomial coefficient C(m+n-2, m-1) or C(m+n-2, n-1).

The DP approach is more intuitive and easier to implement, especially for those unfamiliar with combinatorics. The combinatorics approach is more efficient in terms of time and space but requires understanding of binomial coefficients.

### Solution Code (Dynamic Programming Approach):
```python
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
```

### Time and Space Complexity Analysis:
- **Time Complexity**: O(m * n) because we fill up a DP table of size m x n.
- **Space Complexity**: O(m * n) for the DP table. This can be optimized to O(n) by using a single array since we only need the previous row to compute the current row.

### Optimized Space Complexity Solution (O(n) space):
```python
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[-1]

# Test cases
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(1, 1))  # Output: 1
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 3))  # Output: 6
```

### Combinatorics Approach:
```python
import math

def uniquePaths(m: int, n: int) -> int:
    return math.comb(m + n - 2, m - 1)

# Test cases
print(uniquePaths(3, 7))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
print(uniquePaths(1, 1))  # Output: 1
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 3))  # Output: 6
```

### Time and Space Complexity for Combinatorics Approach:
- **Time Complexity**: O(min(m, n)) because calculating the binomial coefficient C(m+n-2, m-1) can be done in linear time relative to the smaller of m-1 or n-1.
- **Space Complexity**: O(1) as we only use a constant amount of space.

### Test Cases:
1. **Example 1**:
   - Input: m = 3, n = 7
   - Output: 28
2. **Example 2**:
   - Input: m = 3, n = 2
   - Output: 3
3. **Edge Case 1**:
   - Input: m = 1, n = 1
   - Output: 1 (only one cell, no moves needed)
4. **Edge Case 2**:
   - Input: m = 7, n = 3
   - Output: 28 (same as Example 1, just swapped m and n)
5. **Edge Case 3**:
   - Input: m = 3, n = 3
   - Output: 6 (paths: RRDD, RDRD, RDDR, DRRD, DRDR, DDRR)

These test cases cover various scenarios including the given examples, a single cell grid, and swapped dimensions to ensure the solution works correctly.