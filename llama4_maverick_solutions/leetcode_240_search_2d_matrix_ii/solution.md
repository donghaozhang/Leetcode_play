# search_2d_matrix.md) ✅
- 搜索二维矩阵 II / Search 2D Matrix II [LeetCode 240]

## Problem Description

## Search a 2D Matrix II

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. The matrix has the following properties:

*   Integers in each row are sorted in ascending from left to right.
*   Integers in each column are sorted in ascending from top to bottom.

### Example 1:

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

### Example 2:

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

### Constraints:

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= n, m <= 300`
*   `-10^9 <= matrix[i][j] <= 10^9`
*   All the integers in each row are sorted in ascending order.
*   All the integers in each column are sorted in ascending order.
*   `-10^9 <= target <= 10^9`

## Solution

**Problem Explanation**
=======================

The problem requires writing an efficient algorithm to search for a target value in a 2D matrix where integers in each row are sorted in ascending order from left to right, and integers in each column are sorted in ascending order from top to bottom.

**Step-by-Step Approach**
------------------------

1.  Start by understanding the properties of the given matrix:
    *   The matrix is sorted row-wise and column-wise.
    *   The integers in each row are sorted in ascending order from left to right.
    *   The integers in each column are sorted in ascending order from top to bottom.
2.  To efficiently search for the target, we can utilize the sorted properties of the matrix.
3.  We can begin the search from a specific corner of the matrix (either top-right or bottom-left) to take advantage of the sorted order.
4.  By comparing the target with the current element at the chosen corner, we can decide whether to move left, right, up, or down in the matrix.
5.  Continue this comparison and movement process until we find the target or reach the boundaries of the matrix.

**Python Solution**
------------------

```python
def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix sorted row-wise and column-wise.

    Args:
    matrix (list[list[int]]): A 2D list of integers sorted row-wise and column-wise.
    target (int): The target value to be searched.

    Returns:
    bool: True if the target is found, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# Test cases
if __name__ == "__main__":
    # Example 1
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: True

    # Example 2
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    print(searchMatrix(matrix, target))  # Expected output: False

    # Edge case: Empty matrix
    matrix = []
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: False

    # Edge case: Matrix with a single element
    matrix = [[5]]
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: True
```

**Time and Space Complexity Analysis**
--------------------------------------

*   **Time complexity:** O(m + n), where m is the number of rows and n is the number of columns in the matrix. This is because in the worst-case scenario, we might need to traverse m rows and n columns.
*   **Space complexity:** O(1), as we are using a constant amount of space to store the row and column indices, and not using any additional data structures that scale with the input size.

The provided Python solution is efficient, readable, and well-documented, making it suitable for solving the given problem. The test cases cover various scenarios, including the examples provided in the problem statement and edge cases like an empty matrix and a matrix with a single element.