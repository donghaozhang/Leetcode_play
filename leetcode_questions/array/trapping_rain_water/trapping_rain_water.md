# Trapping Rain Water

## Problem Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples

**Example 1:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

## Approach

### English

This problem can be solved by understanding that the amount of water trapped at any position depends on the minimum of the maximum heights to its left and right, minus the height at that position.

The algorithm follows these steps:
1. Create two arrays: `left` and `right` of the same length as the input array.
   - `left[i]` will store the maximum height seen from the beginning up to the position i (including the height at position i)
   - `right[i]` will store the maximum height seen from the end up to the position i (including the height at position i)
2. Fill the `left` array by iterating from left to right.
3. Fill the `right` array by iterating from right to left.
4. Iterate through the array and compute the amount of water trapped at each position.
   - The water trapped at position i = min(left[i], right[i]) - height[i]
5. Sum up the water trapped at each position to get the total amount of water.

The intuition is that for each position, the water level is determined by the minimum of the maximum heights to its left and right. If the current height is less than this water level, then water will be trapped at this position.

### Chinese

这个问题可以通过理解任何位置处的积水量取决于其左右最大高度的最小值减去该位置的高度来解决。

算法步骤如下：
1. 创建两个与输入数组长度相同的数组：`left` 和 `right`。
   - `left[i]` 存储从开始到位置 i（包括位置 i 的高度）看到的最大高度
   - `right[i]` 存储从结束到位置 i（包括位置 i 的高度）看到的最大高度
2. 通过从左向右迭代填充 `left` 数组。
3. 通过从右向左迭代填充 `right` 数组。
4. 遍历数组并计算每个位置的积水量。
   - 位置 i 处的积水量 = min(left[i], right[i]) - height[i]
5. 把每个位置的积水量相加，得到总的积水量。

直观理解是，对于每个位置，水位由其左右最大高度的最小值决定。如果当前高度小于这个水位，那么这个位置就会积水。

## Complexity Analysis

### English

- **Time Complexity**: O(n), where n is the length of the array. We make three passes through the array: one to fill `left`, one to fill `right`, and one to compute the total water.
- **Space Complexity**: O(n), for storing the `left` and `right` arrays.

There is an optimization that can reduce the space complexity to O(1) by using two pointers approach, but the solution provided here uses the arrays for clarity.

### Chinese

- **时间复杂度**：O(n)，其中 n 是数组的长度。我们对数组进行了三次遍历：一次填充 `left`，一次填充 `right`，一次计算总水量。
- **空间复杂度**：O(n)，用于存储 `left` 和 `right` 数组。

有一种优化方法可以使用双指针方法将空间复杂度降低到 O(1)，但这里提供的解决方案使用数组是为了清晰度。 