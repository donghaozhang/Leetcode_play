# 经典二分查找
# Classical Binary Search

## 题目描述
在一个有序数组中找到目标值的任意位置，如果目标值不存在则返回 -1。

## Description
Find any position of the target value in a sorted array, return -1 if the target does not exist.

## 示例
输入: nums = [1, 2, 3, 3, 4, 5], target = 3
输出: 2 或 3 (返回任意一个目标值的位置)

## Example
Input: nums = [1, 2, 3, 3, 4, 5], target = 3
Output: 2 or 3 (Return any position of the target value)

## 解题思路
使用标准的二分查找算法：
1. 初始化左右指针
2. 当左指针小于等于右指针时循环
3. 计算中间位置
4. 比较中间值与目标值
5. 根据比较结果调整左右指针

## Solution
Use the standard binary search algorithm:
1. Initialize left and right pointers
2. Loop while the left pointer is less than or equal to the right pointer
3. Calculate the middle position
4. Compare the middle value with the target value
5. Adjust the left and right pointers according to the comparison result

### 复杂度分析
- 时间复杂度：O(log n)
- 空间复杂度：O(1)

### Complexity Analysis
- Time Complexity: O(log n)
- Space Complexity: O(1)

## 代码实现要点
1. 正确处理边界条件
2. 避免整数溢出
3. 正确的循环终止条件
4. 返回任意一个目标值的位置即可

## Code Implementation Key Points
1. Correctly handle boundary conditions
2. Avoid integer overflow
3. Correct loop termination condition
4. Return any position of the target value
