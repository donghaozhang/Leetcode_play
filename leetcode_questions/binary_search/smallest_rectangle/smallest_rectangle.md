# Smallest Rectangle Enclosing Black Pixels
# 包围黑色像素的最小矩形

## Description
Given a 2D matrix containing `'0'` and `'1'`, where `'0'` represents white pixels and `'1'` represents black pixels, and a coordinate (x, y) of one of the black pixels.

Find the area of the smallest (axis-aligned) rectangle that encloses all black pixels. It is guaranteed that at least one black pixel is present in the matrix.

## 题目描述
给定一个二维矩阵，包含 `'0'` 和 `'1'`，其中 `'0'` 表示白色像素，`'1'` 表示黑色像素。你还会得到一个黑色像素点的坐标 (x, y)。

要求找到包含所有黑色像素的最小矩形的面积。已知所有黑色像素都是相连的。

## Example
Input:
```
[
  "0010",
  "0110",
  "0100"
]
```
and x = 0, y = 2 (one of the location of pixel with value '1')

Output: 6

Explanation: The upper-left corner of the minimum rectangle is (0, 1) and the lower-right corner is (2, 2), so the area is 6.

## 示例
输入:
```
[
  "0010",
  "0110",
  "0100"
]
```
和 x = 0, y = 2（即值为 "1" 的位置之一）

输出: 6

解释: 最小矩形的左上角在 (0,1)，右下角在 (2,2)，面积为 6。

## Solution

### Binary Search
Since all black pixels are connected, and a black pixel's location is given, we can use binary search to find the four boundaries of the rectangle:

1. **Search Principle**
   - For each column, if it contains a black pixel, then this column must be within the minimum rectangle
   - For each row, if it contains a black pixel, then this row must be within the minimum rectangle

2. **Search Process**
   - Left Boundary: Find the first column containing a black pixel from left to right
   - Right Boundary: Find the first column containing a black pixel from right to left
   - Upper Boundary: Find the first row containing a black pixel from top to bottom
   - Lower Boundary: Find the first row containing a black pixel from bottom to top

3. **Optimization**
   - When searching for row boundaries, only check the known column range
   - When searching for column boundaries, only check the known row range

## 解题思路

### 二分查找法
由于已知所有黑色像素是连通的，且给定了一个黑色像素的位置，我们可以使用二分查找来找到矩形的四个边界：

1. **查找原理**
   - 对于每一列，如果包含黑色像素，那么这一列一定在最小矩形内
   - 对于每一行，如果包含黑色像素，那么这一行一定在最小矩形内

2. **查找过程**
   - 左边界：从左向右找第一个包含黑色像素的列
   - 右边界：从右向左找第一个包含黑色像素的列
   - 上边界：从上向下找第一个包含黑色像素的行
   - 下边界：从下向上找第一个包含黑色像素的行

3. **优化**
   - 在查找行边界时，只需要检查已知的列范围
   - 在查找列边界时，只需要检查已知的行范围

### Complexity Analysis
- Time Complexity: O(mlogn + nlogm), where m and n are the number of rows and columns of the matrix respectively
- Space Complexity: O(1)

### 复杂度分析
- 时间复杂度：O(mlogn + nlogm)，其中 m 和 n 分别是矩阵的行数和列数
- 空间复杂度：O(1)

## Code Implementation Key Points
1. Handle boundary conditions (empty matrix)
2. Correctly implement the boundary conditions of binary search
3. Note that when searching for row boundaries, you only need to check the known column range, and vice versa
4. The final rectangle area needs to include the boundaries

## 代码实现要点
1. 处理边界情况（空矩阵）
2. 正确实现二分查找的边界条件
3. 注意在查找行边界时只需要检查已知的列范围，反之亦然
4. 计算最终矩形面积时需要包含边界
