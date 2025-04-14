# 搜索二维矩阵  
# Search a 2D Matrix

## 题目描述  
## Description

给定一个 m x n 的有序矩阵，该矩阵具有以下特性：  
Given an m x n matrix with the following properties:

1. 每行中的整数从左到右按升序排列  
   1. Integers in each row are sorted in ascending order from left to right  
2. 每行的第一个整数大于前一行的最后一个整数  
   2. The first integer of each row is greater than the last integer of the previous row

编写一个高效的算法来判断矩阵中是否存在一个目标值。  
Write an efficient algorithm to determine if a target value exists in the matrix.

## 示例  
## Example

输入:  
Input:
```
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
```
输出: true  
Output: true

## 解题思路  
## Solution Approach

### 二分查找法  
### Binary Search Method

由于矩阵的特殊性质，我们可以将其视为一个有序数组来进行二分查找：  
Because of the special properties of the matrix, we can treat it as a sorted array and perform binary search:

1. **转换思路**  
   1. **Transformation Idea**
   - m × n 的矩阵可以看作长度为 m*n 的有序数组  
     - The m x n matrix can be viewed as a sorted array of length m*n
   - 对于位置 mid，可以通过以下方式转换为矩阵坐标：  
     - For position mid, convert to matrix coordinates as follows:
     - 行号 = mid // n（n为列数）  
       - Row = mid // n (n is the number of columns)
     - 列号 = mid % n  
       - Col = mid % n

2. **算法步骤**  
   2. **Algorithm Steps**
   - 初始化左右指针：left = 0, right = m*n - 1  
     - Initialize left and right pointers: left = 0, right = m*n - 1
   - 当 left <= right 时进行二分查找：  
     - While left <= right, perform binary search:
     - 计算中间位置 mid = (left + right) // 2  
       - Calculate mid = (left + right) // 2
     - 将 mid 转换为矩阵中的行列坐标  
       - Convert mid to matrix row and column
     - 比较矩阵中该位置的值与目标值  
       - Compare the value at that position with the target
     - 根据比较结果调整左右指针  
       - Adjust left and right pointers based on the comparison

### 复杂度分析  
### Complexity Analysis

- 时间复杂度：O(log(m*n))  
  - Time Complexity: O(log(m*n))
- 空间复杂度：O(1)  
  - Space Complexity: O(1)

## 代码实现要点  
## Key Implementation Points

1. 注意处理空矩阵的边界情况  
   1. Handle edge cases for empty matrices
2. 正确计算行列索引  
   2. Correctly calculate row and column indices
3. 使用整数除法和取模运算进行坐标转换  
   3. Use integer division and modulo for coordinate conversion

## 算法说唱  
## Algorithm Rap

```
二维矩阵有序排，特性助我寻目标
二分查找是法宝，一维转换是关键

左右指针框边界，中值计算比大小
行用mid除列数，列用mid求余数

相等返真不相等，指针调整再循环
空矩阵要判断，log(mn)效率高

分而治之有妙招，复杂问题简单解
```

```
2D matrix sorted in line, properties help me find the sign
Binary search is the key, flatten to 1D, that's the plea

Left and right pointers set the bound, mid value checks what is found
Row is mid divided by columns, col is mid modulo columns

If equal return true, else adjust and loop anew
Check for empty matrix too, log(mn) efficiency through

Divide and conquer, clever way, complex problems solved today