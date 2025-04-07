# merge_k_sorted_arrays.md)
- 丑数 II / Ugly Number II [LeetCode 264]

## Problem Description

Here is the full description of LeetCode problem #264, "Ugly Number II":

---

**Medium**

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return the `nth` **ugly number**.

**Example 1:**

```
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
```

**Example 2:**

```
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
```

**Constraints:**

- `1 <= n <= 1690`

---

## Solution

### Problem Explanation:
An **ugly number** is defined as a positive integer whose prime factors are only 2, 3, and 5. The sequence of ugly numbers starts with 1, followed by numbers like 2, 3, 4, 5, 6, 8, 9, 10, 12, etc. The challenge is to find the nth ugly number in this sequence efficiently.

### Approach:
1. **Dynamic Programming with Pointers**:
   - **Initialization**: Start with the first ugly number, which is 1.
   - **Pointers**: Maintain three pointers (or indices) for the multiples of 2, 3, and 5. These pointers will keep track of the positions in the ugly number list where multiplying by 2, 3, or 5 can produce the next smallest ugly number.
   - **Generate Next Ugly Number**: At each step, the next ugly number is the minimum of the multiples of 2, 3, and 5 at their respective pointers. Update the pointer(s) that contributed to this minimum value to move to the next position.
   - **Avoid Duplicates**: If multiple pointers produce the same minimum value, increment all those pointers to avoid duplicate entries in the list.

### Solution Code:
```python
def nthUglyNumber(n: int) -> int:
    ugly = [1]
    i2 = i3 = i5 = 0  # pointers for 2, 3, 5
    for _ in range(1, n):
        next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        ugly.append(next_ugly)
        if next_ugly == ugly[i2] * 2:
            i2 += 1
        if next_ugly == ugly[i3] * 3:
            i3 += 1
        if next_ugly == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]

# Test cases
print(nthUglyNumber(10))  # Output: 12
print(nthUglyNumber(1))   # Output: 1
```

### Explanation:
1. **Initialization**: The list `ugly` starts with `[1]`, the first ugly number.
2. **Pointers**: `i2`, `i3`, and `i5` are initialized to 0, pointing to the first element of the `ugly` list.
3. **Loop**: For each subsequent number from 1 to n-1:
   - Calculate the next ugly number as the minimum of `ugly[i2]*2`, `ugly[i3]*3`, and `ugly[i5]*5`.
   - Append this minimum value to the `ugly` list.
   - Increment the pointer(s) that contributed to this minimum value to ensure the next multiplication yields a larger ugly number.
4. **Result**: After filling the list up to the nth element, return the last element of the list, which is the nth ugly number.

### Time and Space Complexity:
- **Time Complexity**: O(n). Each iteration computes the next ugly number in constant time, and the loop runs n-1 times.
- **Space Complexity**: O(n). The `ugly` list stores n elements.

### Test Cases:
1. **Input**: `n = 10`  
   **Output**: `12`  
   **Explanation**: The 10th ugly number in the sequence [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is 12.

2. **Input**: `n = 1`  
   **Output**: `1`  
   **Explanation**: The first ugly number is 1 by definition.

This approach efficiently generates the nth ugly number by leveraging dynamic programming and careful pointer management to avoid duplicates and ensure the correct order.