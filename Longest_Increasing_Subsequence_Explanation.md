# Longest Increasing Subsequence (LIS) Explained in Python

## 中文讲解

### 问题描述
给定一个数列，目标是找到一个严格递增的子序列。这个子序列可以通过删除原数列中的一些元素（但保持剩余元素的顺序不变）得到。

**例如：**

对于序列：

```
[10, 9, 2, 5, 3, 7, 101, 18]
```

最长的递增子序列为：

```
[2, 5, 7, 101]
```

其长度为 4。

---

### 算法解析
使用动态规划的方法解决此问题，主要分为三步：

1. **初始化：**
   - 构造数组 `dp`，其中 `dp[i]` 表示以第 i 个元素结尾的最长递增子序列的长度，初始时每个值均为 1。
   - 构造数组 `prev` 用于记录每个元素在子序列中的前驱索引，初始均为 -1。

2. **状态转移：**
   - 对于每个元素，遍历其前面的所有元素。如果满足 `nums[j] < nums[i]` 并且 `dp[j] + 1 > dp[i]`，则更新 `dp[i]` 并记录 `prev[i] = j`。

3. **重构子序列：**
   - 找到 `dp` 数组中最大值对应的索引 `max_index`，
   - 使用 `prev` 数组回溯获得完整的最长递增子序列，然后将其反转以获得正确顺序。

---

### Python 实现
该实现思路与上述相同，具体代码请参考下面的代码示例：

```python
#!/usr/bin/env python

def longest_increasing_subsequence(nums):
    """Return the longest increasing subsequence from the list of numbers."""
    if not nums:
        return []
    n = len(nums)
    # dp[i] will be the length of the subsequence ending at index i
    dp = [1] * n
    # prev[i] will store the index of the previous element in the subsequence
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in dp
    max_index = 0
    for i in range(n):
        if dp[i] > dp[max_index]:
            max_index = i

    # Reconstruct the subsequence using prev array
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    lis.reverse()
    return lis


if __name__ == '__main__':
    # Example usage
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    lis = longest_increasing_subsequence(nums)
    print("Input sequence:", nums)
    print("Longest increasing subsequence:", lis)
    print("Length of subsequence:", len(lis))
```

---

### 运行方法
在终端中执行以下命令运行代码：

```bash
python Leetcode_play/longest_increasing_subsequence.py
```

期望输出：

```
Input sequence: [10, 9, 2, 5, 3, 7, 101, 18]
Longest increasing subsequence: [2, 5, 7, 101]
Length of subsequence: 4
```

---

### 小结
本例使用动态规划方法解决了最长递增子序列问题，能够高效地得到最长子序列及其长度。

---

## English Explanation

### Problem Statement
Given a sequence of numbers, the goal is to find the longest subsequence that is strictly increasing. A subsequence is a sequence derived from the original sequence by deleting some or no elements without changing the order of the remaining elements.

**Example:**

For the sequence:

```
[10, 9, 2, 5, 3, 7, 101, 18]
```

The longest increasing subsequence is:

```
[2, 5, 7, 101]
```

with a length of 4.

---

### Algorithm Explanation
The dynamic programming approach works as follows:

1. **Initialization:**
   - Create an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. Initialize this array with 1s.
   - Create an array `prev` to store the index of the previous element in the subsequence, initialized with `-1`.

2. **Dynamic Programming Transition:**
   - For each element at index `i`, loop over previous indices `j` (where `j < i`). 
   - If `nums[j]` is less than `nums[i]` and `dp[j] + 1 > dp[i]`, update `dp[i]` and record `prev[i] = j`.

3. **Reconstructing the Subsequence:**
   - Identify the index (`max_index`) corresponding to the maximum value in `dp`.
   - Backtrack using the `prev` array to reconstruct the full subsequence, then reverse it for the correct order.

---

### Python Implementation
Refer to the code snippet above.

---

### Running the Code
To run the code, execute:

```bash
python Leetcode_play/longest_increasing_subsequence.py
```

Expected output:

```
Input sequence: [10, 9, 2, 5, 3, 7, 101, 18]
Longest increasing subsequence: [2, 5, 7, 101]
Length of subsequence: 4
```

---

### Conclusion
This implementation demonstrates how to solve the Longest Increasing Subsequence problem using a dynamic programming approach. It efficiently calculates both the length and the actual increasing subsequence from the input sequence. 