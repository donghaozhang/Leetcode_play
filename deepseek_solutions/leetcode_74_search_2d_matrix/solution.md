# # LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。

## 二分查找 (Binary Search)
- 搜索二维矩阵 / Search 2D Matrix [LeetCode 74]

## Problem Description

**Problem Title:** Search a 2D Matrix  

**Description:**  
Write an efficient algorithm that searches for a value `target` in an `m x n` matrix. This matrix has the following properties:  

- Integers in each row are sorted from left to right.  
- The first integer of each row is greater than the last integer of the previous row.  

**Examples:**  

**Example 1:**  
![Example 1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)  
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3  
Output: true  
```  

**Example 2:**  
![Example 2](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)  
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13  
Output: false  
```  

**Constraints:**  
- `m == matrix.length`  
- `n == matrix[i].length`  
- `1 <= m, n <= 100`  
- `-10^4 <= matrix[i][j], target <= 10^4`

## Solution

### Explanation of the Problem

We are given a 2D matrix where:
1. Each row is sorted in ascending order from left to right.
2. The first element of each row is greater than the last element of the previous row.

Our task is to determine if a given `target` value exists in this matrix efficiently.

### Approach
1. **Flatten the 2D Matrix into a 1D Array Conceptually**: Due to the matrix's properties, we can treat it as a single sorted list. The first element of the matrix is the smallest, and the last element is the largest.
2. **Binary Search**: Use binary search on this conceptual 1D array. The key is to map the 1D index to 2D matrix indices:
   - For a matrix with `m` rows and `n` columns, the total number of elements is `m * n`.
   - The middle element in the 1D array can be found at `matrix[mid // n][mid % n]`, where `n` is the number of columns.

### Solution Code
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(searchMatrix(matrix1, target1))  # Output: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(searchMatrix(matrix2, target2))  # Output: False

matrix3 = []
target3 = 0
print(searchMatrix(matrix3, target3))  # Output: False

matrix4 = [[1]]
target4 = 1
print(searchMatrix(matrix4, target4))  # Output: True

matrix5 = [[1, 1]]
target5 = 2
print(searchMatrix(matrix5, target5))  # Output: False
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(log(m * n)), where `m` is the number of rows and `n` is the number of columns. This is because binary search runs in logarithmic time relative to the number of elements in the matrix.
- **Space Complexity**: O(1), as we are using a constant amount of extra space.

### Test Cases
1. **Example 1**: The target `3` is present in the matrix, so the output is `True`.
2. **Example 2**: The target `13` is not present, so the output is `False`.
3. **Empty Matrix**: The matrix is empty, so the output is `False`.
4. **Single Element Matrix**: The matrix contains only one element which matches the target, so the output is `True`.
5. **No Match**: The target `2` is not in the matrix, so the output is `False`.

This solution efficiently checks for the presence of the target in the matrix using binary search, leveraging the matrix's sorted properties.