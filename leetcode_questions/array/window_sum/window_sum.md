# Window Sum

## Problem Description
Given an integer array nums and a window size k, calculate the sum of all consecutive subarrays of length k in the array.

## Example
Input: 
- nums = [1, 2, 7, 8, 5]
- k = 3
Output: [10, 17, 20]
Explanation:
- First window [1, 2, 7] = 10
- Second window [2, 7, 8] = 17
- Third window [7, 8, 5] = 20

## Solution Approach

### Sliding Window Method
Using the sliding window technique to efficiently calculate the sum of consecutive subarrays:

1. **Initialization**
   - Calculate the sum of the first window
   - Add the result to the result array

2. **Sliding Process**
   - Move one position to the right each time
   - Subtract the leftmost number from the window
   - Add the new number entering the window
   - Add the new sum to the result

### Optimization
Instead of recalculating the sum of all numbers in the window each time:
- Maintain the sum of the current window
- Only update the changing parts (subtract the exiting number, add the entering number)

### Complexity Analysis
- Time Complexity: O(n)
  - Initialize the first window: O(k)
  - Sliding window process: O(n-k)
  - Overall: O(n)
- Space Complexity: O(n-k+1), for storing the result array

## Key Implementation Points
1. Handle edge cases
   - Empty array
   - k <= 0
   - k > array length
2. Correctly calculate the sum of the first window
3. Properly maintain the sum of the sliding window
4. Pay attention to array index ranges

---

# 滑动窗口求和

## 题目描述
给定一个整数数组 nums 和一个窗口大小 k，计算数组中所有长度为 k 的连续子数组的和。

## 示例
输入: 
- nums = [1, 2, 7, 8, 5]
- k = 3
输出: [10, 17, 20]
解释:
- 第一个窗口 [1, 2, 7] = 10
- 第二个窗口 [2, 7, 8] = 17
- 第三个窗口 [7, 8, 5] = 20

## 解题思路

### 滑动窗口法
使用滑动窗口技巧可以高效地计算连续子数组的和：

1. **初始化**
   - 计算第一个窗口的和
   - 将结果添加到结果数组中

2. **滑动过程**
   - 每次向右移动一位
   - 减去窗口最左边的数
   - 加上新进入窗口的数
   - 将新的和添加到结果中

### 优化
不需要每次都重新计算窗口内所有数的和，而是：
- 维护当前窗口的和
- 每次只更新变化的部分（减去移出的数，加上移入的数）

### 复杂度分析
- 时间复杂度：O(n)
  - 初始化第一个窗口：O(k)
  - 滑动窗口过程：O(n-k)
  - 总体：O(n)
- 空间复杂度：O(n-k+1)，用于存储结果数组

## 代码实现要点
1. 处理边界情况
   - 空数组
   - k <= 0
   - k > 数组长度
2. 正确计算第一个窗口的和
3. 正确维护滑动窗口的和
4. 注意数组索引的范围 