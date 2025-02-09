# Longest Increasing Subsequence (LIS) Explained in Python

This document explains the concept of the **Longest Increasing Subsequence (LIS)** problem and demonstrates a Python implementation using **Dynamic Programming**.

---

## Problem Statement

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

## Algorithm Explanation

The dynamic programming approach works as follows:

1. **Initialization:**
   - Create an array `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. Initialize this array with 1s (each element can form a subsequence of length 1 by itself).
   - Create an array `prev` to store the index of the previous element in the subsequence. Initialize all positions with `-1`.

2. **Dynamic Programming Transition:**
   - For each element at index `i`, consider all previous indices `j` (where `j < i`).
   - If `nums[j]` is less than `nums[i]` and appending `nums[i]` extends a longer subsequence (`dp[j] + 1 > dp[i]`), update `dp[i]` and record `j` in `prev[i]`.

3. **Reconstructing the Subsequence:**
   - Identify the index (`max_index`) corresponding to the maximum value in `dp`.
   - Backtrack using the `prev` array to reconstruct the subsequence and then reverse it to maintain the correct order.

---

## Python Implementation

Below is the Python code that implements the above approach:

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

## Running the Code

To run the code, execute the following command in your terminal:

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

## Conclusion

This implementation demonstrates how to solve the Longest Increasing Subsequence problem using a dynamic programming approach. It efficiently calculates both the length and the actual increasing subsequence from the input sequence. 