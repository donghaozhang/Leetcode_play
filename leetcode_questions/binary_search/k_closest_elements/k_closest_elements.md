# 找到K个最接近的元素

## 题目描述
给定一个排序数组，两个整数 k 和 target，找到数组中最接近目标值 target 的 k 个数。结果需要按照升序排列。如果有两个数与 target 的差值相等，优先选择较小的那个数。

## 示例
输入: [1, 2, 3, 4, 5], k = 4, target = 3
输出: [1, 2, 3, 4]

## 解题思路

### 方法一：二分查找
1. **确定起始位置**
   - 使用二分查找找到最优的起始位置
   - 比较 [mid, mid+k] 区间两端到 target 的距离
   - 根据比较结果调整搜索范围

2. **返回结果**
   - 从找到的起始位置返回连续的k个数

### 方法二：双指针
1. **初始化指针**
   - 左指针指向开头，右指针指向结尾
   - 需要删除 len(arr) - k 个数

2. **收缩区间**
   - 比较两端到 target 的距离
   - 删除距离较远的数
   - 直到剩下k个数

### 复杂度分析
- 二分查找方法：
  - 时间复杂度：O(log(n-k))
  - 空间复杂度：O(1)
- 双指针方法：
  - 时间复杂度：O(n-k)
  - 空间复杂度：O(1)

## 代码实现要点
1. 正确处理边界条件
2. 处理相等距离的情况
3. 注意返回值需要排序
4. 优化代码可读性：
   - 使用有意义的变量名
   - 添加清晰的注释
   - 分离逻辑步骤
   - 提供多种实现方法

## 相关题目
1. 找到最接近的值
2. 二分查找
3. 双指针技巧 

---

# Find K Closest Elements (English Version)

## Problem Description
Given a sorted array, two integers k and target, find the k closest elements to the target in the array. The result should be sorted in ascending order. If two numbers have the same absolute difference from the target, the smaller number should be preferred.

## Example
Input: [1, 2, 3, 4, 5], k = 4, target = 3
Output: [1, 2, 3, 4]

## Solution Approach

### Method 1: Binary Search
1. **Determine the Start Position**
   - Use binary search to find the optimal starting position
   - Compare the distances from both ends of the [mid, mid+k] range to the target
   - Adjust the search range based on the comparison result

2. **Return the Result**
   - Return k consecutive numbers starting from the found position

### Method 2: Two Pointers
1. **Initialize Pointers**
   - Left pointer points to the beginning, right pointer points to the end
   - Need to remove len(arr) - k numbers

2. **Shrink the Range**
   - Compare the distances from both ends to the target
   - Remove the number with the larger distance
   - Continue until k numbers remain

### Complexity Analysis
- Binary Search Method:
  - Time Complexity: O(log(n-k))
  - Space Complexity: O(1)
- Two Pointers Method:
  - Time Complexity: O(n-k)
  - Space Complexity: O(1)

## Key Implementation Points
1. Handle boundary conditions correctly
2. Process cases with equal distances
3. Ensure the return value is sorted
4. Optimize code readability:
   - Use meaningful variable names
   - Add clear comments
   - Separate logical steps
   - Provide multiple implementation methods

## Related Problems
1. Find the closest value
2. Binary search
3. Two-pointer technique 