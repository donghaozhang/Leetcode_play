# # LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。

## 二分查找 (Binary Search)
- 搜索二维矩阵 / Search 2D Matrix [LeetCode 74]

## Problem Description

## Search a 2D Matrix
<p>Write an efficient algorithm that searches for a value <code>target</code> in an <code>m x n</code> integer matrix. The matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted from left to right.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-10<sup>4</sup> &lt;= matrix[i][j], target &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

## Problem Explanation

The problem requires writing an efficient algorithm to search for a target value in a given `m x n` integer matrix. The matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

This means the matrix is sorted in a way that if we were to flatten it into a single array, the array would be sorted in ascending order.

## Step-by-Step Approach

1. **Understand the Matrix Structure**: Recognize that the given matrix is essentially a sorted array when flattened. This is because the elements are sorted within each row and the rows are sorted among themselves.

2. **Apply Binary Search**: Since the matrix is essentially a sorted array, we can apply binary search to find the target. The challenge is to map the binary search indices to the 2D matrix indices.

3. **Map Binary Search Indices to 2D Matrix Indices**: To do this, we need to calculate the row and column indices from a given "flat" index. For a matrix of size `m x n`, the element at flat index `i` can be found at row `i // n` and column `i % n`, where `//` denotes integer division and `%` denotes the modulus operation.

4. **Perform Binary Search**:
   - Initialize two pointers, `low` and `high`, to the start and end of the "flat" array representation of the matrix.
   - Loop until `low` is greater than `high`.
   - In each iteration, calculate the `mid` index and compare the element at this index (mapped to the 2D matrix) with the target.
   - If the element matches the target, return `True`.
   - If the element is less than the target, move the `low` pointer to `mid + 1`.
   - If the element is greater than the target, move the `high` pointer to `mid - 1`.
   - If the loop ends without finding the target, return `False`.

## Python Solution

```python
def searchMatrix(matrix, target):
    """
    Searches for a target value in a given m x n integer matrix.

    Args:
    matrix (list[list[int]]): A 2D list of integers sorted as described.
    target (int): The target value to search for.

    Returns:
    bool: True if the target is found, False otherwise.
    """
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

# Test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(searchMatrix(matrix1, target1))  # Expected output: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(searchMatrix(matrix2, target2))  # Expected output: False
```

## Time and Space Complexity Analysis

- **Time Complexity**: The algorithm performs a binary search on a "flat" array of size `m * n`, where `m` is the number of rows and `n` is the number of columns in the matrix. Therefore, the time complexity is `O(log(m*n))`.
- **Space Complexity**: The algorithm uses a constant amount of space to store the indices and the target value. Hence, the space complexity is `O(1)`.

## Test Cases

The provided Python solution includes test cases to verify its correctness. These test cases cover scenarios where the target is present in the matrix and where it is not. Additional test cases can be added to further validate the solution under different conditions, such as an empty matrix, a matrix with a single element, or edge cases involving the minimum and maximum possible values for the target and matrix elements.