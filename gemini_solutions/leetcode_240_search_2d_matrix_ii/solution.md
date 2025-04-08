# search_2d_matrix.md) ✅
- 搜索二维矩阵 II / Search 2D Matrix II [LeetCode 240]

## Problem Description

```markdown
## 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

*   Integers in each row are sorted in ascending from left to right.
*   Integers in each column are sorted in ascending from top to bottom.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

**Input:** `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 5`
**Output:** `true`

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

**Input:** `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 20`
**Output:** `false`

**Constraints:**

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= n, m <= 300`
*   `-10^9 <= matrix[i][j] <= 10^9`
*   All the integers in each row are **sorted** in ascending order.
*   All the integers in each column are **sorted** in ascending order.
*   `-10^9 <= target <= 10^9`
```

## Solution

Okay, let's break down the "Search a 2D Matrix II" problem.

**1. Explanation of the Problem**

We are given a 2D integer matrix (`m` rows, `n` columns). This matrix has special properties:
*   Each row is sorted in ascending order from left to right.
*   Each column is sorted in ascending order from top to bottom.

Our goal is to determine if a given integer `target` exists within this matrix. We need an *efficient* algorithm, implying something better than checking every single element (which would be O(m*n)).

**2. Step-by-Step Approach**

The key insight comes from leveraging *both* sorting properties simultaneously. Consider the element at the top-right corner of the matrix, `matrix[0][n-1]`. Let this element be `current`.

*   **Case 1: `target == current`**
    *   We found the target! Return `true`.

*   **Case 2: `target < current`**
    *   Since `target` is smaller than `current`, and all elements in the current column (`n-1`) below `current` are *greater* than `current` (due to column sorting), the `target` cannot possibly be in the current column (`n-1`).
    *   Therefore, we can eliminate the entire last column and continue our search in the submatrix to the left. We move our focus one column to the left (decrement the column index).

*   **Case 3: `target > current`**
    *   Since `target` is greater than `current`, and all elements in the current row (`0`) to the left of `current` are *smaller* than `current` (due to row sorting), the `target` cannot possibly be in the current row (`0`).
    *   Therefore, we can eliminate the entire first row and continue our search in the submatrix below. We move our focus one row down (increment the row index).

We can repeat this process, starting from the top-right corner (`row = 0`, `col = n - 1`), and iteratively eliminating either a row or a column based on the comparison between the `target` and the `current` element at `matrix[row][col]`.

The search continues as long as our row and column indices are within the bounds of the matrix. If the indices go out of bounds (e.g., `col < 0` or `row >= m`) before finding the target, it means the target is not present in the matrix.

**Algorithm Summary:**

1.  Check for edge cases: If the matrix is empty or `None`, return `false`.
2.  Get the dimensions: `m` (number of rows) and `n` (number of columns).
3.  Initialize pointers: `row = 0`, `col = n - 1`.
4.  Start a loop that continues as long as `row < m` and `col >= 0`.
5.  Inside the loop, get the element `current = matrix[row][col]`.
6.  Compare `target` with `current`:
    *   If `target == current`, return `true`.
    *   If `target < current`, move left: `col--`.
    *   If `target > current`, move down: `row++`.
7.  If the loop finishes without returning `true`, it means the target was not found. Return `false`.

*Alternative Starting Point:* We could also start from the bottom-left corner (`row = m - 1`, `col = 0`) and apply similar logic:
*   If `target < current`, move up (`row--`).
*   If `target > current`, move right (`col++`).
Both approaches yield the same time and space complexity. We'll implement the top-right approach.

**3. Python Solution**

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a value target in an m x n integer matrix matrix.
        Integers in each row are sorted left-to-right.
        Integers in each column are sorted top-to-bottom.

        Args:
            matrix: The m x n integer matrix.
            target: The integer value to search for.

        Returns:
            True if the target is found in the matrix, False otherwise.
        """
        # Handle edge cases: empty matrix or matrix with empty rows
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)       # Number of rows
        n = len(matrix[0])    # Number of columns

        # Start search from the top-right corner
        row = 0
        col = n - 1

        # Loop while the pointers are within the matrix bounds
        while row < m and col >= 0:
            current_element = matrix[row][col]

            if target == current_element:
                return True  # Target found
            elif target < current_element:
                # Target is smaller, must be to the left (if it exists)
                # Eliminate the current column
                col -= 1
            else: # target > current_element
                # Target is larger, must be below (if it exists)
                # Eliminate the current row
                row += 1

        # If the loop finishes, the target was not found
        return False

# --- Test Cases ---

solver = Solution()

# Example 1
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target1 = 5
print(f"Matrix 1:\n{matrix1}")
print(f"Target 1: {target1}, Found: {solver.searchMatrix(matrix1, target1)}") # Expected: True

# Example 2
target2 = 20
print(f"Target 2: {target2}, Found: {solver.searchMatrix(matrix1, target2)}") # Expected: False

# Edge Case: Empty matrix
matrix_empty = []
target_empty = 5
print(f"\nMatrix Empty: {matrix_empty}")
print(f"Target Empty: {target_empty}, Found: {solver.searchMatrix(matrix_empty, target_empty)}") # Expected: False

# Edge Case: Matrix with empty row (handled by initial check)
matrix_empty_row = [[]]
target_empty_row = 1
# This case is typically disallowed by constraints but good to consider
# The code handles it via `if not matrix or not matrix[0]:`
# print(f"\nMatrix Empty Row: {matrix_empty_row}")
# print(f"Target Empty Row: {target_empty_row}, Found: {solver.searchMatrix(matrix_empty_row, target_empty_row)}") # Expected: False (due to check)

# Edge Case: Single element matrix
matrix_single = [[5]]
target_single_found = 5
target_single_not_found = 3
print(f"\nMatrix Single: {matrix_single}")
print(f"Target Single Found: {target_single_found}, Found: {solver.searchMatrix(matrix_single, target_single_found)}") # Expected: True
print(f"Target Single Not Found: {target_single_not_found}, Found: {solver.searchMatrix(matrix_single, target_single_not_found)}") # Expected: False

# Edge Case: Single row matrix
matrix_row = [[1, 3, 5, 7, 9]]
target_row_found = 7
target_row_not_found = 4
print(f"\nMatrix Row: {matrix_row}")
print(f"Target Row Found: {target_row_found}, Found: {solver.searchMatrix(matrix_row, target_row_found)}") # Expected: True
print(f"Target Row Not Found: {target_row_not_found}, Found: {solver.searchMatrix(matrix_row, target_row_not_found)}") # Expected: False

# Edge Case: Single column matrix
matrix_col = [[2], [4], [6], [8]]
target_col_found = 6
target_col_not_found = 5
print(f"\nMatrix Col: {matrix_col}")
print(f"Target Col Found: {target_col_found}, Found: {solver.searchMatrix(matrix_col, target_col_found)}") # Expected: True
print(f"Target Col Not Found: {target_col_not_found}, Found: {solver.searchMatrix(matrix_col, target_col_not_found)}") # Expected: False

# Target smaller than smallest element
target_small = 0
print(f"\nTarget Small: {target_small}, Found: {solver.searchMatrix(matrix1, target_small)}") # Expected: False

# Target larger than largest element
target_large = 35
print(f"Target Large: {target_large}, Found: {solver.searchMatrix(matrix1, target_large)}") # Expected: False

# Target at top-right
target_top_right = 15
print(f"Target Top-Right: {target_top_right}, Found: {solver.searchMatrix(matrix1, target_top_right)}") # Expected: True

# Target at bottom-left
target_bottom_left = 18
print(f"Target Bottom-Left: {target_bottom_left}, Found: {solver.searchMatrix(matrix1, target_bottom_left)}") # Expected: True
```

**Complexity Analysis:**

*   **Time Complexity:** O(m + n)
    *   In each step of the `while` loop, we either decrement the column index (`col`) or increment the row index (`row`).
    *   The `row` index starts at 0 and can go up to `m`.
    *   The `col` index starts at `n-1` and can go down to -1.
    *   The maximum number of steps the algorithm can take is the sum of the maximum possible movements in rows and columns, which is `m + n`. Therefore, the time complexity is linear with respect to the sum of the dimensions.
*   **Space Complexity:** O(1)
    *   We only use a few extra variables (`m`, `n`, `row`, `col`, `current_element`) regardless of the input matrix size. Thus, the space complexity is constant.

This O(m + n) approach is significantly more efficient than the naive O(m * n) search and typically better than the O(m log n) or O(n log m) approaches involving binary search on each row/column, especially for matrices that are closer to square.

**4. Test Cases (Included in the Python code above)**

*   **Example 1:** `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 5` -> `True`
*   **Example 2:** `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 20` -> `False`
*   **Empty Matrix:** `matrix = []`, `target = 5` -> `False`
*   **Single Element Matrix (Found):** `matrix = [[5]]`, `target = 5` -> `True`
*   **Single Element Matrix (Not Found):** `matrix = [[5]]`, `target = 3` -> `False`
*   **Single Row Matrix (Found):** `matrix = [[1, 3, 5, 7, 9]]`, `target = 7` -> `True`
*   **Single Row Matrix (Not Found):** `matrix = [[1, 3, 5, 7, 9]]`, `target = 4` -> `False`
*   **Single Column Matrix (Found):** `matrix = [[2], [4], [6], [8]]`, `target = 6` -> `True`
*   **Single Column Matrix (Not Found):** `matrix = [[2], [4], [6], [8]]`, `target = 5` -> `False`
*   **Target Smaller than Min:** `matrix = [[1,...]]`, `target = 0` -> `False`
*   **Target Larger than Max:** `matrix = [[..., 30]]`, `target = 35` -> `False`
*   **Target at Top-Right Corner:** `matrix = [[..., 15], ...]`, `target = 15` -> `True`
*   **Target at Bottom-Left Corner:** `matrix = [[...], [18, ...]]`, `target = 18` -> `True`