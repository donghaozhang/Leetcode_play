# # LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。

## 二分查找 (Binary Search)
- 搜索二维矩阵 / Search 2D Matrix [LeetCode 74]

## Problem Description

```markdown
## 74. Search a 2D Matrix

You are given an `m x n` integer matrix `matrix` with the following two properties:

*   Each row is sorted in non-decreasing order.
*   The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

You must write a solution in `O(log(m * n))` time complexity.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Constraints:**

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= m, n <= 100`
*   `-10^4 <= matrix[i][j], target <= 10^4`
```

## Solution

Okay, let's break down the LeetCode problem #74: Search a 2D Matrix.

## 1. Problem Explanation

We are given a 2D integer matrix (`m` rows, `n` columns). This matrix has two special properties:
1.  **Sorted Rows:** Each row is sorted in non-decreasing (ascending) order from left to right.
2.  **Increasing Rows:** The first number in any row is strictly greater than the last number in the previous row.

Our goal is to determine if a given `target` integer exists within this matrix. The solution must be efficient, specifically with a time complexity of `O(log(m * n))`.

The combination of these two properties implies that if you were to "flatten" the matrix into a single list by concatenating the rows in order, the resulting list would be sorted. For example:
`[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]`
can be thought of as the sorted list:
`[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]`

## 2. Step-by-Step Approach

The `O(log(m * n))` time complexity requirement strongly suggests using **Binary Search**. Since the matrix can be conceptually treated as a single sorted list of `m * n` elements, we can perform a binary search directly on this conceptual list.

Here's the plan:

1.  **Initialization:**
    *   Get the dimensions of the matrix: `m` (number of rows) and `n` (number of columns).
    *   Handle edge cases: If the matrix is empty or has no columns, the target cannot be found, so return `False`.
    *   Define the search space for the binary search. We can think of the matrix elements indexed from `0` to `m * n - 1`. So, initialize `low = 0` and `high = m * n - 1`.

2.  **Binary Search Loop:**
    *   Continue the loop as long as `low <= high`.
    *   Calculate the middle index `mid_idx = low + (high - low) // 2`. This `mid_idx` represents the index in the conceptual flattened sorted list.
    *   **Map 1D index to 2D coordinates:** Convert `mid_idx` back into matrix row and column indices:
        *   `row = mid_idx // n` (Integer division gives the row index)
        *   `col = mid_idx % n` (Modulo operation gives the column index)
    *   Get the value at these coordinates: `mid_val = matrix[row][col]`.
    *   **Compare and Adjust Search Space:**
        *   If `mid_val == target`: We found the target, return `True`.
        *   If `mid_val < target`: The target must be in the right half of the current search space (larger values). Update `low = mid_idx + 1`.
        *   If `mid_val > target`: The target must be in the left half of the current search space (smaller values). Update `high = mid_idx - 1`.

3.  **Target Not Found:** If the loop finishes without finding the target (i.e., `low > high`), it means the target is not in the matrix. Return `False`.

## 3. Python Solution

```python
import math # Not strictly needed, but good practice

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Searches for a target value in an m x n matrix with sorted rows
        and the first element of each row greater than the last of the previous row.

        Args:
            matrix: The m x n integer matrix.
            target: The integer value to search for.

        Returns:
            True if the target is found, False otherwise.
        """
        # Handle edge cases: empty matrix or matrix with empty rows
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # Initialize binary search boundaries for the conceptual 1D array
        low = 0
        high = m * n - 1 # Index of the last element

        while low <= high:
            # Calculate the middle index in the conceptual 1D array
            # Using low + (high - low) // 2 prevents potential integer overflow
            mid_idx = low + (high - low) // 2

            # Convert the 1D index back to 2D matrix coordinates
            row = mid_idx // n
            col = mid_idx % n

            # Get the value at the middle position
            mid_val = matrix[row][col]

            # Perform comparison
            if mid_val == target:
                return True  # Target found
            elif mid_val < target:
                # Target is in the upper half (larger values)
                low = mid_idx + 1
            else: # mid_val > target
                # Target is in the lower half (smaller values)
                high = mid_idx - 1

        # Target not found after the loop finishes
        return False

# --- Test Cases ---
solver = Solution()

# Example 1
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(f"Matrix: {matrix1}, Target: {target1}, Found: {solver.searchMatrix(matrix1, target1)}") # Expected: True

# Example 2
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(f"Matrix: {matrix2}, Target: {target2}, Found: {solver.searchMatrix(matrix2, target2)}") # Expected: False

# Custom Test Cases
# Target at the beginning
target3 = 1
print(f"Matrix: {matrix1}, Target: {target3}, Found: {solver.searchMatrix(matrix1, target3)}") # Expected: True

# Target at the end
target4 = 60
print(f"Matrix: {matrix1}, Target: {target4}, Found: {solver.searchMatrix(matrix1, target4)}") # Expected: True

# Target in the middle
target5 = 11
print(f"Matrix: {matrix1}, Target: {target5}, Found: {solver.searchMatrix(matrix1, target5)}") # Expected: True

# Target smaller than min
target6 = 0
print(f"Matrix: {matrix1}, Target: {target6}, Found: {solver.searchMatrix(matrix1, target6)}") # Expected: False

# Target larger than max
target7 = 70
print(f"Matrix: {matrix1}, Target: {target7}, Found: {solver.searchMatrix(matrix1, target7)}") # Expected: False

# Target between rows but not present
target8 = 8
print(f"Matrix: {matrix1}, Target: {target8}, Found: {solver.searchMatrix(matrix1, target8)}") # Expected: False

# Single row matrix
matrix9 = [[1, 2, 3, 4]]
target9 = 3
print(f"Matrix: {matrix9}, Target: {target9}, Found: {solver.searchMatrix(matrix9, target9)}") # Expected: True

# Single column matrix
matrix10 = [[1], [10], [23]]
target10 = 10
print(f"Matrix: {matrix10}, Target: {target10}, Found: {solver.searchMatrix(matrix10, target10)}") # Expected: True

# Single element matrix (found)
matrix11 = [[5]]
target11 = 5
print(f"Matrix: {matrix11}, Target: {target11}, Found: {solver.searchMatrix(matrix11, target11)}") # Expected: True

# Single element matrix (not found)
matrix12 = [[5]]
target12 = 6
print(f"Matrix: {matrix12}, Target: {target12}, Found: {solver.searchMatrix(matrix12, target12)}") # Expected: False

# Empty matrix
matrix13 = []
target13 = 1
print(f"Matrix: {matrix13}, Target: {target13}, Found: {solver.searchMatrix(matrix13, target13)}") # Expected: False

# Matrix with empty row (handled by initial check)
matrix14 = [[]]
target14 = 1
# Note: This case technically violates constraints (1 <= n), but the code handles it.
# If the constraints were strictly followed, this test wouldn't be needed.
# Let's assume valid inputs per constraints, but the check is robust.
# If matrix = [[]] was possible, the check `if not matrix or not matrix[0]:` would catch it.
# For a valid matrix like [[1],[2]], target = 0:
matrix15 = [[1],[2]]
target15 = 0
print(f"Matrix: {matrix15}, Target: {target15}, Found: {solver.searchMatrix(matrix15, target15)}") # Expected: False

```

**Complexity Analysis:**

*   **Time Complexity:** `O(log(m * n))`
    *   The binary search performs `log(N)` iterations, where `N` is the total number of elements in the matrix (`N = m * n`).
    *   Each iteration involves constant time operations (index calculation, comparison).
*   **Space Complexity:** `O(1)`
    *   We only use a few extra variables (`m`, `n`, `low`, `high`, `mid_idx`, `row`, `col`, `mid_val`) to store indices and values. The space used does not depend on the size of the input matrix.

## 4. Test Cases Summary

Here's a summary of the test cases used above to verify the solution:

1.  **Example 1:** `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3` -> `True`
2.  **Example 2:** `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13` -> `False`
3.  **Target at Start:** `target = 1` -> `True`
4.  **Target at End:** `target = 60` -> `True`
5.  **Target in Middle:** `target = 11` -> `True`
6.  **Target Too Small:** `target = 0` -> `False`
7.  **Target Too Large:** `target = 70` -> `False`
8.  **Target Between Rows:** `target = 8` -> `False`
9.  **Single Row:** `matrix = [[1, 2, 3, 4]], target = 3` -> `True`
10. **Single Column:** `matrix = [[1], [10], [23]], target = 10` -> `True`
11. **Single Element (Found):** `matrix = [[5]], target = 5` -> `True`
12. **Single Element (Not Found):** `matrix = [[5]], target = 6` -> `False`
13. **Empty Matrix:** `matrix = [], target = 1` -> `False`
14. **Valid Matrix, Target Too Small:** `matrix = [[1],[2]], target = 0` -> `False`

These test cases cover various scenarios, including edge cases and typical inputs, ensuring the solution's correctness and robustness.