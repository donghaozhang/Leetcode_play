# Top K Frequent Elements / 前 K 个高频元素 [LeetCode 347]

## Problem / 问题

### English

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

**Follow up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

### 中文

给你一个整数数组 `nums` 和一个整数 `k`，请你返回其中出现频率前 `k` 高的元素。你可以按任意顺序返回答案。

**示例 1：**
```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

**示例 2：**
```
输入: nums = [1], k = 1
输出: [1]
```

**约束条件：**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k 的取值范围是 [1, 数组中不相同的元素的数量]。
- 题目数据保证答案唯一。

**进阶：** 你所设计算法的时间复杂度必须优于 O(n log n)，其中 n 是数组大小。

## Solution / 解决方案

### English

There are several approaches to solve this problem efficiently:

#### Approach 1: Heap (Min Heap)

This approach uses a min heap to track the k most frequent elements:

1. Count the frequency of each element in the array
2. Use a min heap to keep track of the k elements with the highest frequencies
3. For each element-frequency pair:
   - Add it to the heap
   - If heap size exceeds k, remove the element with the lowest frequency

Time Complexity:
- Building the frequency map: O(n)
- Heap operations: O(n log k) because we perform at most n heap operations, each taking O(log k) time
- Overall: O(n log k)

Space Complexity: O(n) for the frequency map and O(k) for the heap

#### Approach 2: Bucket Sort

We can use bucket sort to achieve O(n) time complexity:

1. Count the frequency of each element
2. Create n+1 buckets where bucket[i] contains all elements that appear exactly i times
3. Iterate through the buckets from high frequency to low, collecting elements until we have k elements

Time Complexity: O(n) where n is the size of the input array
Space Complexity: O(n) for the frequency map and buckets

#### Approach 3: Quickselect

We can also use the quickselect algorithm to find the k most frequent elements:

1. Count the frequency of each element
2. Use quickselect to find the kth most frequent element
3. Return all elements with frequency greater than or equal to the kth element's frequency

Time Complexity: O(n) on average, O(n²) in the worst case
Space Complexity: O(n)

### 中文

有几种高效解决这个问题的方法：

#### 方法一：堆（最小堆）

这种方法使用最小堆来跟踪频率最高的 k 个元素：

1. 统计数组中每个元素的频率
2. 使用最小堆来跟踪频率最高的 k 个元素
3. 对于每个元素-频率对：
   - 将其添加到堆中
   - 如果堆的大小超过 k，移除频率最低的元素

时间复杂度：
- 构建频率映射：O(n)
- 堆操作：O(n log k)，因为我们最多执行 n 次堆操作，每次操作需要 O(log k) 时间
- 总体：O(n log k)

空间复杂度：O(n) 用于频率映射，O(k) 用于堆

#### 方法二：桶排序

我们可以使用桶排序来实现 O(n) 的时间复杂度：

1. 统计每个元素的频率
2. 创建 n+1 个桶，其中 bucket[i] 包含所有恰好出现 i 次的元素
3. 从高频率到低频率遍历桶，收集元素，直到我们有 k 个元素

时间复杂度：O(n)，其中 n 是输入数组的大小
空间复杂度：O(n) 用于频率映射和桶

#### 方法三：快速选择

我们还可以使用快速选择算法来找到前 k 个高频元素：

1. 统计每个元素的频率
2. 使用快速选择找到第 k 个高频元素
3. 返回所有频率大于或等于第 k 个元素频率的元素

时间复杂度：平均 O(n)，最坏情况 O(n²)
空间复杂度：O(n) 