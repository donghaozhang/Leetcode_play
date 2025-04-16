# Merge Intervals / 合并区间 [LeetCode 56]

## Problem / 问题

### English

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Example 1:**
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

**Example 2:**
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Constraints:**
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

### 中文

给出一个区间的集合，请合并所有重叠的区间。`intervals[i] = [starti, endi]`

**示例 1：**
```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例 2：**
```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 被视为重叠区间。
```

**约束条件：**
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

## Solution / 解决方案

### English

This problem can be solved using a sorting-based approach:

1. Sort the intervals based on their start times (first element of each interval)
2. Initialize an empty result list
3. Iterate through the sorted intervals:
   - If the result list is empty or the current interval does not overlap with the last interval in the result list, add the current interval to the result list
   - If the current interval overlaps with the last interval in the result list, merge them by updating the end time of the last interval in the result list

The key insight is that after sorting, any overlapping intervals will be adjacent to each other. Two intervals `[a, b]` and `[c, d]` overlap if and only if `c <= b`, assuming `a <= c` (which is guaranteed by sorting).

#### Time Complexity
- Sorting the intervals: O(n log n)
- Iterating through the sorted intervals: O(n)
- Overall: O(n log n), where n is the number of intervals

#### Space Complexity
- O(n) for the result list (not counting the input)

### 中文

这个问题可以使用基于排序的方法解决：

1. 根据区间的起始时间（每个区间的第一个元素）对区间进行排序
2. 初始化一个空的结果列表
3. 遍历排序后的区间：
   - 如果结果列表为空或当前区间与结果列表中的最后一个区间不重叠，则将当前区间添加到结果列表中
   - 如果当前区间与结果列表中的最后一个区间重叠，则通过更新结果列表中最后一个区间的结束时间来合并它们

关键的洞察是，排序后，任何重叠的区间将彼此相邻。两个区间 `[a, b]` 和 `[c, d]` 重叠当且仅当 `c <= b`，假设 `a <= c`（这通过排序保证）。

#### 时间复杂度
- 排序区间：O(n log n)
- 遍历排序后的区间：O(n)
- 总体：O(n log n)，其中 n 是区间的数量

#### 空间复杂度
- O(n) 用于结果列表（不计算输入） 