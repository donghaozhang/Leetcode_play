# backpack_iii.md)
- 不同路径 / Unique Paths [LeetCode 62]

## Problem Description

```markdown
## 62. Unique Paths

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

**Input:** m = 3, n = 7
**Output:** 28

**Example 2:**

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

**Constraints:**

*   `1 <= m, n <= 100`
```

## Solution

Okay, let's break down the "Unique Paths" problem (LeetCode 62).

**1. Explanation of the Problem**

Imagine a grid with `m` rows and `n` columns. A robot starts at the very top-left cell `(0, 0)` and wants to reach the bottom-right cell `(m-1, n-1)`. The robot has a restriction: it can *only* move one step down or one step right at any time. We need to find the total number of distinct sequences of moves (paths) the robot can take to get from the start to the finish.

**2. Step-by-Step Approach**

This problem has optimal substructure and overlapping subproblems, making it a classic candidate for Dynamic Programming (DP).

*   **Define Subproblem:** Let `dp[i][j]` represent the number of unique paths to reach the cell at row `i` and column `j`.
*   **Base Cases:**
    *   To reach any cell in the first row (`i=0`), the robot must have only moved right. There's only one way to do this for each cell. So, `dp[0][j] = 1` for all `0 <= j < n`.
    *   Similarly, to reach any cell in the first column (`j=0`), the robot must have only moved down. There's only one way. So, `dp[i][0] = 1` for all `0 <= i < m`.
    *   Specifically, `dp[0][0] = 1` (the starting point).
*   **Recurrence Relation:** Consider any cell `(i, j)` where `i > 0` and `j > 0`. How could the robot have arrived at this cell?
    *   It could have come from the cell directly above, `(i-1, j)`, by moving down.
    *   It could have come from the cell directly to the left, `(i, j-1)`, by moving right.
    *   Since these are the only two possible previous moves, the total number of unique paths to reach `(i, j)` is the sum of the paths to reach `(i-1, j)` and the paths to reach `(i, j-1)`.
    *   Therefore, the recurrence relation is: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
*   **Goal:** We want to find the number of paths to the bottom-right corner, which is `dp[m-1][n-1]`.
*   **Implementation (DP Table):** We can build an `m x n` table (or grid) and fill it using the base cases and the recurrence relation. We start by filling the first row and first column with 1s. Then, we iterate through the rest of the grid (e.g., row by row, column by column) and calculate `dp[i][j]` using the values already computed.

*   **Space Optimization:** Notice that to calculate the values for the current row `i`, we only need the values from the previous row `i-1` and the value immediately to the left in the current row `i`. We don't need rows `i-2`, `i-3`, etc. This suggests we can optimize the space.
    *   We can use only two rows: `prev_row` and `curr_row`.
    *   Even better, we can use just *one* row (let's call it `dp_row` of size `n`). When calculating the value for `dp_row[j]` (representing `dp[i][j]`), the value `dp_row[j]` currently holds the value from the previous row (`dp[i-1][j]`), and `dp_row[j-1]` holds the *already updated* value for the current row (`dp[i][j-1]`).
    *   So, the update becomes `dp_row[j] = dp_row[j] + dp_row[j-1]`. We iterate this process `m` times (or `m-1` times after initialization).

*   **Alternative Approach (Combinatorics):**
    *   To reach `(m-1, n-1)` from `(0, 0)`, the robot must make exactly `m-1` down moves and `n-1` right moves.
    *   The total number of moves is `(m-1) + (n-1) = m + n - 2`.
    *   Any path is a sequence of these `m + n - 2` moves. The problem is equivalent to finding how many ways we can arrange `m-1` 'D's (Down) and `n-1` 'R's (Right) in a sequence of length `m + n - 2`.
    *   This is a combination problem: Choose `m-1` positions for the 'D' moves out of `m + n - 2` total positions (the rest will be 'R's).
    *   The number of paths is given by the binomial coefficient: `C(m + n - 2, m - 1)` or equivalently `C(m + n - 2, n - 1)`.
    *   `C(N, k) = N! / (k! * (N - k)!)`. This can be calculated efficiently without computing large factorials directly, or by using library functions like `math.comb` in Python.

**3. Python Solution**

We'll provide the space-optimized DP solution first, as it's a common interview expectation, followed by the combinatorial solution.

```python
import math
import time

# Solution 1: Dynamic Programming (Space Optimized)
def uniquePaths_dp(m: int, n: int) -> int:
    """
    Calculates the number of unique paths using space-optimized DP.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths.
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # Use the smaller dimension for the dp array for better space optimization
    if m < n:
        m, n = n, m # Ensure n is the smaller dimension

    # dp_row represents the number of paths to reach cells in the current row
    # Initialize with 1s (representing the first row of the conceptual grid)
    dp_row = [1] * n

    # Iterate through the rows (starting from the second row, index 1)
    for i in range(1, m):
        # Iterate through the columns (starting from the second column, index 1)
        for j in range(1, n):
            # dp_row[j] currently holds the value from the previous row (paths from above)
            # dp_row[j-1] holds the updated value for the current row (paths from left)
            dp_row[j] = dp_row[j] + dp_row[j-1]

    # The last element contains the number of paths to the bottom-right cell
    return dp_row[n - 1]

# Solution 2: Combinatorial Approach
def uniquePaths_combinatorial(m: int, n: int) -> int:
    """
    Calculates the number of unique paths using combinatorics.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths.
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # Total number of moves needed
    total_moves = m + n - 2
    # Number of 'down' moves needed (or 'right' moves, choose the smaller for efficiency)
    k = min(m - 1, n - 1)

    # Calculate combinations: C(total_moves, k)
    # math.comb(n, k) calculates n! / (k! * (n-k)!)
    return math.comb(total_moves, k)

# --- Testing ---
def run_tests(solution_func):
    test_cases = [
        ((3, 7), 28),
        ((3, 2), 3),
        ((7, 3), 28),
        ((2, 3), 3),
        ((1, 1), 1),
        ((1, 10), 1),
        ((10, 1), 1),
        ((2, 2), 2),
        ((19, 13), 86493225), # Larger test case
        ((51, 9), 169884720), # Another larger test case
    ]

    print(f"--- Testing {solution_func.__name__} ---")
    all_passed = True
    for i, (inputs, expected) in enumerate(test_cases):
        m, n = inputs
        start_time = time.time()
        result = solution_func(m, n)
        end_time = time.time()
        duration = (end_time - start_time) * 1000 # milliseconds

        if result == expected:
            print(f"Test Case {i+1}: PASSED ({duration:.4f} ms)")
        else:
            print(f"Test Case {i+1}: FAILED")
            print(f"  Input: m={m}, n={n}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            all_passed = False
            print("-" * 20)

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
    print("-" * 30)


# Run tests for both solutions
run_tests(uniquePaths_dp)
run_tests(uniquePaths_combinatorial)

# Example Usage
print("\nExample Usage:")
m1, n1 = 3, 7
print(f"Input: m={m1}, n={n1}")
print(f"DP Solution: {uniquePaths_dp(m1, n1)}")
print(f"Combinatorial Solution: {uniquePaths_combinatorial(m1, n1)}")

m2, n2 = 3, 2
print(f"\nInput: m={m2}, n={n2}")
print(f"DP Solution: {uniquePaths_dp(m2, n2)}")
print(f"Combinatorial Solution: {uniquePaths_combinatorial(m2, n2)}")
```

**Complexity Analysis:**

1.  **DP (Space Optimized):**
    *   **Time Complexity:** O(m * n). We have nested loops iterating through the conceptual grid dimensions.
    *   **Space Complexity:** O(min(m, n)). We use a 1D array whose size is the smaller of the two dimensions (`n` after potential swap).

2.  **Combinatorial:**
    *   **Time Complexity:** O(min(m, n)). The `math.comb(N, k)` function in Python is efficient. Calculating combinations iteratively takes time proportional to `k`, which is `min(m-1, n-1)`.
    *   **Space Complexity:** O(1). We only use a few variables to store intermediate values.

**Which solution to use?**

*   The **Combinatorial approach** is generally faster and more concise for this specific problem.
*   The **DP approach** (especially the space-optimized version) is valuable because it demonstrates a fundamental problem-solving technique applicable to many other grid-based or sequence problems where simple combinatorics might not apply (e.g., if there were obstacles in the grid).

**4. Test Cases**

The provided Python code includes a `run_tests` function with the following test cases:

*   `((3, 7), 28)`: Example 1
*   `((3, 2), 3)`: Example 2
*   `((7, 3), 28)`: Swapped dimensions of Example 1
*   `((2, 3), 3)`: Swapped dimensions of Example 2
*   `((1, 1), 1)`: Smallest grid
*   `((1, 10), 1)`: Single row
*   `((10, 1), 1)`: Single column
*   `((2, 2), 2)`: Small square grid
*   `((19, 13), 86493225)`: Larger grid
*   `((51, 9), 169884720)`: Larger grid with disparate dimensions