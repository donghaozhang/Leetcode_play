# search_2d_matrix.md) ✅
- 搜索二维矩阵 II / Search 2D Matrix II [LeetCode 240]

## Problem Description

**Problem Description:**

Write an efficient algorithm that searches for a target value in an `m x n` integer matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg)

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`

## Solution

### Problem Explanation:
We are given a 2D matrix where each row is sorted in ascending order from left to right, and each column is sorted in ascending order from top to bottom. Our task is to determine whether a given target value exists in this matrix. The challenge is to do this efficiently given the matrix's properties.

### Approach:
The key observation here is that the matrix is sorted in a way that allows us to eliminate entire rows or columns in each step. Here's a step-by-step approach:

1. **Start from the Top-Right Corner**: Begin at the top-right corner of the matrix (i.e., first row, last column). This position allows us to leverage the sorted properties of both rows and columns.
2. **Compare with Target**:
   - If the current element is equal to the target, return `True`.
   - If the current element is greater than the target, move left in the current row (i.e., decrement the column index) because all elements below in this column will be larger.
   - If the current element is less than the target, move down to the next row (i.e., increment the row index) because all elements to the left in this row will be smaller.
3. **Terminate if Indices Go Out of Bounds**: If the row or column index goes out of the matrix bounds, the target is not present, and we return `False`.

This approach efficiently narrows down the search space by either moving left or down, ensuring we do not revisit any elements, leading to an optimal solution.

### Solution Code:
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down
    
    return False

# Test cases
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target1 = 5
print(searchMatrix(matrix1, target1))  # Expected output: True

target2 = 20
print(searchMatrix(matrix1, target2))  # Expected output: False

matrix2 = [[-5]]
target3 = -5
print(searchMatrix(matrix2, target3))  # Expected output: True

matrix3 = [[1, 1]]
target4 = 2
print(searchMatrix(matrix3, target4))  # Expected output: False
```

### Time and Space Complexity Analysis:
- **Time Complexity**: O(m + n), where m is the number of rows and n is the number of columns. In the worst case, we might traverse from the top-right to the bottom-left corner, visiting each row and column once.
- **Space Complexity**: O(1), as we are using a constant amount of additional space regardless of the input size.

### Test Cases:
1. **Example 1**: The target `5` is present in the matrix, so the output is `True`.
2. **Example 2**: The target `20` is not present in the matrix, so the output is `False`.
3. **Single Element Matrix**: The target `-5` is the only element in the matrix, so the output is `True`.
4. **Small Matrix**: The target `2` is not present in the small matrix `[[1, 1]]`, so the output is `False`.

These test cases cover various scenarios, including edge cases, to ensure the solution's correctness and robustness.