# 最长上升子序列问题解析

## 问题描述
给定一个整数数组 `nums`，求其中最长的严格递增子序列（Longest Increasing Subsequence, LIS）。  
例如：
- 输入: `[4, 5, 6, 1, 2, 3, 5]`
- 输出: `[1, 2, 3, 5]`

说明：  
返回的子序列要求满足严格递增，并且元素在原数组中的相对顺序不变。

## 解题思路

### 动态规划方法
1. **状态定义**  
   令 `dp[i]` 表示以 `nums[i]` 结尾的最长上升子序列的长度。  
   同时维护一个数组 `prev[i]`，记录构成该子序列的前一个元素的索引，以便后续重构子序列。

2. **状态转移**  
   对于每个元素 `nums[i]`，遍历其之前的所有元素 `nums[j]`（`0 ≤ j < i`）：  
   - 如果 `nums[j] < nums[i]`，则可以尝试将 `nums[i]`接到以 `nums[j]`结尾的子序列后面，更新状态：  
     ```
     if dp[j] + 1 > dp[i]:
         dp[i] = dp[j] + 1
         prev[i] = j
     ```
     
3. **结果重构**  
   遍历 `dp` 数组找出最大的值对应的索引，再利用 `prev` 数组反向重构最长上升子序列，然后翻转顺序得到最终结果。

### 时间和空间复杂度
- **时间复杂度：** O(n²)
- **空间复杂度：** O(n)

## 示例说明
对于输入 `[4, 5, 6, 1, 2, 3, 5]`：
- 动态规划计算后，最长上升子序列为 `[1, 2, 3, 5]`，长度为 4，是所有严格递增子序列中最长的。 