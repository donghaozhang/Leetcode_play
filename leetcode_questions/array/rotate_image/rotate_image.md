# Rotate Image

## Problem Description
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

## Examples

### Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

Visual representation:
```
Input:         Output:
1 2 3          7 4 1
4 5 6    →     8 5 2
7 8 9          9 6 3
```

### Example 2:
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

Visual representation:
```
Input:            Output:
 5  1  9 11       15 13  2  5
 2  4  8 10   →   14  3  4  1
13  3  6  7       12  6  8  9
15 14 12 16       16  7 10 11
```

## Constraints
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## Solution Approach
To rotate the matrix in-place by 90 degrees clockwise, we can break down the operation into two simpler steps:

1. **Transpose the matrix** (swap elements across the main diagonal)
2. **Reverse each row** of the transposed matrix

### Detailed Steps:

#### Step 1: Transpose the Matrix
In this step, we swap elements across the main diagonal. For example, the element at position (i, j) is swapped with the element at position (j, i).

We only need to process half of the matrix (elements above or below the main diagonal) to avoid double-swapping.

```
Original Matrix:    After Transpose:
1 2 3               1 4 7
4 5 6       →       2 5 8
7 8 9               3 6 9
```

#### Step 2: Reverse Each Row
After transposing, we reverse the elements in each row.

```
After Transpose:    After Reversing Rows:
1 4 7               7 4 1
2 5 8       →       8 5 2
3 6 9               9 6 3
```

And now we have completed the 90-degree clockwise rotation.

### Time and Space Complexity:
- **Time Complexity**: O(n²) - We need to visit each element in the matrix.
- **Space Complexity**: O(1) - We perform the rotation in-place without using additional space (except for a few variables).

## Code Implementation
```python
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_num = len(matrix)
    col_num = len(matrix[0])
    
    # Step 1: Transpose the matrix
    for row_i in range(row_num):
        for col_i in range(row_i+1, col_num):
            matrix[row_i][col_i], matrix[col_i][row_i] = matrix[col_i][row_i], matrix[row_i][col_i]
    
    # Step 2: Reverse each row
    for row_i in range(row_num):
        matrix[row_i][0:row_num] = matrix[row_i][::-1]
```

## Alternative Approaches

### Four Groups Rotation
Another approach is to directly rotate four elements at a time, working from the outermost layer inward:

1. For an n×n matrix, we have n/2 layers (for odd n, the center element doesn't rotate)
2. For each layer, we rotate the four corners, then the next elements along each edge, and so on

```python
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[layer][i]
            
            # Move left to top
            matrix[layer][i] = matrix[n-1-i][layer]
            
            # Move bottom to left
            matrix[n-1-i][layer] = matrix[n-1-layer][n-1-i]
            
            # Move right to bottom
            matrix[n-1-layer][n-1-i] = matrix[i][n-1-layer]
            
            # Move top to right
            matrix[i][n-1-layer] = top
```

## Related Problems
- [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) - Return all elements of a matrix in spiral order
- [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) - Return the transpose of a matrix 