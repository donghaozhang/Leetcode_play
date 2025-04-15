# 搜索大有序数组 / Search in a Big Sorted Array

## 题目描述 / Problem Description

### 中文 / Chinese
给定一个未知大小的有序数组，实现一个解决方案来查找第一个等于目标值的位置。数组的大小未知，但你可以通过 ArrayReader 接口访问数组：
- ArrayReader.get(k) 返回数组中位置 k 处的值
- 如果你访问了数组越界的位置，ArrayReader.get 会返回 2^31 - 1

### English
Given a sorted array of unknown size, implement a solution to find the first position of a target value. The size of the array is unknown, but you can access the array via an ArrayReader interface:
- ArrayReader.get(k) returns the value at position k in the array.
- If you access an out-of-bounds position, ArrayReader.get will return 2^31 - 1.

## 示例 / Example

### 中文 / Chinese
输入: [1, 3, 6, 9, 21, 21, 21, 29, 31], target = 21
输出: 4 (第一个21的位置)

### English
Input: [1, 3, 6, 9, 21, 21, 21, 29, 31], target = 21
Output: 4 (the position of the first 21)

## 解题思路 / Solution Approach

### 中文 / Chinese
使用两步法解决：
1. **确定搜索范围**
   - 使用倍增法找到右边界
   - 从1开始，每次将范围扩大一倍
   - 直到找到一个比目标值大的位置

2. **二分查找**
   - 在确定的范围内使用二分查找
   - 使用第一个位置的二分查找模板
   - 找到目标值的第一个位置

### English
Use a two-step method:
1. **Determine the Search Range**
   - Use an exponential backoff (doubling) method to find the right boundary.
   - Start with index 1 and double the index in each step.
   - Stop when you find a position whose value is greater than or equal to the target value, or when you hit the out-of-bounds value.

2. **Binary Search**
   - Perform a binary search within the determined range.
   - Use the binary search template for finding the first position of an element.
   - Find the first position of the target value.

### 复杂度分析 / Complexity Analysis

#### 中文 / Chinese
- 时间复杂度：O(log T)，其中 T 是目标值的位置
- 空间复杂度：O(1)

#### English
- Time Complexity: O(log T), where T is the index of the target value. The first step takes O(log T) and the second step (binary search) also takes O(log T).
- Space Complexity: O(1)

## 代码实现要点 / Key Implementation Points

### 中文 / Chinese
1. 正确实现倍增法找右边界
2. 处理数组访问越界情况
3. 使用正确的二分查找模板
4. 注意边界条件的处理

### English
1. Correctly implement the exponential backoff method to find the right boundary.
2. Handle the out-of-bounds access condition (checking for 2^31 - 1).
3. Use the correct binary search template for finding the first occurrence.
4. Pay attention to boundary conditions.

## 相关题目 / Related Problems

### 中文 / Chinese
1. 经典二分查找
2. 目标值的第一个位置
3. 搜索插入位置

### English
1. Classical Binary Search
2. Find First Position of Target
3. Search Insert Position 