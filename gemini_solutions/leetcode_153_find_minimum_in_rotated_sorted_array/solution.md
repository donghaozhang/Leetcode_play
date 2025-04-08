# k_closest_elements.md)
- 旋转排序数组中的最小值 / Find Minimum in Rotated Sorted Array [LeetCode 153]

## Problem Description

```markdown
### 153. Find Minimum in Rotated Sorted Array

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

*   `[4,5,6,7,0,1,2]` if it was rotated `4` times.
*   `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**

```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

**Example 3:**

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 5000`
*   `-5000 <= nums[i] <= 5000`
*   All the integers of `nums` are **unique**.
*   `nums` is sorted and rotated between `1` and `n` times.
```

## Solution

Okay, let's break down the "Find Minimum in Rotated Sorted Array" problem (LeetCode 153).

**1. Explanation of the Problem**

Imagine you have a sorted array of unique numbers, like `[1, 2, 3, 4, 5]`. This array is then "rotated" some number of times. Rotating means taking the last element and moving it to the front.

*   Rotate `[1, 2, 3, 4, 5]` once: `[5, 1, 2, 3, 4]`
*   Rotate `[1, 2, 3, 4, 5]` three times: `[3, 4, 5, 1, 2]`

The result is an array that consists of two sorted subarrays. For example, in `[3, 4, 5, 1, 2]`, the subarrays are `[3, 4, 5]` and `[1, 2]`. The key property is that every element in the first subarray is greater than every element in the second subarray.

The goal is to find the smallest element in this rotated array efficiently. Since the original array was sorted, the minimum element is the one that "breaks" the ascending order due to the rotation. It will be the element that is smaller than its predecessor (or the first element if the array wasn't rotated much).

The constraint that the algorithm must run in O(log n) time strongly suggests using a binary search approach.

**2. Step-by-Step Approach**

We can adapt binary search to find the minimum element. The core idea is to determine which side of the midpoint (`mid`) the minimum element lies on.

1.  **Initialization:**
    *   Set two pointers, `left = 0` and `right = n - 1`, where `n` is the length of the array `nums`.
    *   These pointers define the current search space `[left, right]`.

2.  **Binary Search Loop:**
    *   Continue the search as long as `left < right`. When `left == right`, the search space has shrunk to a single element, which must be the minimum.
    *   Calculate the middle index: `mid = left + (right - left) // 2`. This prevents potential integer overflow compared to `(left + right) // 2`.
    *   **Comparison Logic:** Compare `nums[mid]` with `nums[right]`. This comparison helps us determine if `mid` is in the "left" (larger values) part or the "right" (smaller values) part of the rotated array.
        *   **Case 1: `nums[mid] > nums[right]`**
            *   This means the minimum element *must* be in the right half of the current search space, specifically *after* `mid`. Why? Because `nums[mid]` is larger than the element at the end of the current range (`nums[right]`), indicating that the "drop" (where the minimum element is) occurs somewhere between `mid + 1` and `right`.
            *   Therefore, we discard the left half including `mid`: `left = mid + 1`.
        *   **Case 2: `nums[mid] < nums[right]`**
            *   This means `nums[mid]` *could* be the minimum element, or the minimum element is to the *left* of `mid`. The elements from `mid` to `right` are in ascending order. The minimum cannot be in the range `(mid, right]`.
            *   Therefore, we discard the right half *after* `mid`, but keep `mid` as a potential candidate: `right = mid`.
        *   **Case 3: `nums[mid] == nums[right]`**
            *   Since the problem states all elements are *unique*, and our loop condition is `left < right`, `mid` will always be strictly less than `right` (unless `left = right - 1`, where `mid = left`). In either scenario, if `nums[mid] == nums[right]`, it would imply duplicate elements, which contradicts the problem statement. So, this case won't happen with unique elements.

3.  **Termination:**
    *   The loop terminates when `left == right`. At this point, `left` (or `right`) points to the index of the minimum element.

4.  **Return Value:**
    *   Return `nums[left]`.

**Example Walkthrough (`nums = [4, 5, 6, 7, 0, 1, 2]`)**

1.  `left = 0`, `right = 6`
2.  `mid = 0 + (6 - 0) // 2 = 3`. `nums[mid] = nums[3] = 7`. `nums[right] = nums[6] = 2`.
3.  `nums[mid] (7) > nums[right] (2)`. Minimum is to the right of `mid`.
4.  `left = mid + 1 = 3 + 1 = 4`. Search space `[4, 6]`.
---
5.  `left = 4`, `right = 6`
6.  `mid = 4 + (6 - 4) // 2 = 4 + 1 = 5`. `nums[mid] = nums[5] = 1`. `nums[right] = nums[6] = 2`.
7.  `nums[mid] (1) < nums[right] (2)`. Minimum could be `nums[mid]` or to its left.
8.  `right = mid = 5`. Search space `[4, 5]`.
---
9.  `left = 4`, `right = 5`
10. `mid = 4 + (5 - 4) // 2 = 4 + 0 = 4`. `nums[mid] = nums[4] = 0`. `nums[right] = nums[5] = 1`.
11. `nums[mid] (0) < nums[right] (1)`. Minimum could be `nums[mid]` or to its left.
12. `right = mid = 4`. Search space `[4, 4]`.
---
13. `left = 4`, `right = 4`. Loop condition `left < right` is false. Loop terminates.
14. Return `nums[left] = nums[4] = 0`.

**3. Python Solution**

```python
from typing import List

class Solution:
    """
    Finds the minimum element in a rotated sorted array with unique elements.
    """
    def findMin(self, nums: List[int]) -> int:
        """
        Uses binary search to find the minimum element in O(log n) time.

        Args:
            nums: A list of integers representing the rotated sorted array.

        Returns:
            The minimum element in the array.
        """
        if not nums:
            # Although constraints state n >= 1, handle empty list defensively.
            return -1 # Or raise an error, depending on requirements

        n = len(nums)
        left, right = 0, n - 1

        # If the array is not rotated (or rotated n times),
        # the first element is the minimum.
        # This check is not strictly necessary for the algorithm's correctness
        # but can be a small optimization.
        # if nums[left] <= nums[right]:
        #     return nums[left]

        # Binary search loop
        while left < right:
            mid = left + (right - left) // 2

            # Compare nums[mid] with nums[right] to decide which half to search
            if nums[mid] > nums[right]:
                # Minimum element is in the right half (mid+1 to right)
                # because nums[mid] is part of the 'larger' segment
                left = mid + 1
            else: # nums[mid] < nums[right] (equality impossible due to unique elements)
                # Minimum element is potentially nums[mid] or in the left half (left to mid)
                # because nums[mid] is part of the 'smaller' segment or is the pivot
                right = mid

        # When the loop ends, left == right, and points to the minimum element
        return nums[left]

# --- Test Cases ---
solver = Solution()

# Example 1
nums1 = [3, 4, 5, 1, 2]
print(f"Input: {nums1}, Output: {solver.findMin(nums1)}") # Expected: 1

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(f"Input: {nums2}, Output: {solver.findMin(nums2)}") # Expected: 0

# Example 3: Not rotated (or rotated n times)
nums3 = [11, 13, 15, 17]
print(f"Input: {nums3}, Output: {solver.findMin(nums3)}") # Expected: 11

# Edge Case: Single element
nums4 = [1]
print(f"Input: {nums4}, Output: {solver.findMin(nums4)}") # Expected: 1

# Edge Case: Two elements, rotated
nums5 = [2, 1]
print(f"Input: {nums5}, Output: {solver.findMin(nums5)}") # Expected: 1

# Edge Case: Two elements, not rotated
nums6 = [1, 2]
print(f"Input: {nums6}, Output: {solver.findMin(nums6)}") # Expected: 1

# Larger case
nums7 = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]
print(f"Input: {nums7}, Output: {solver.findMin(nums7)}") # Expected: 1
```

**Complexity Analysis:**

*   **Time Complexity:** O(log n). The binary search algorithm halves the search space in each iteration.
*   **Space Complexity:** O(1). We only use a constant amount of extra space for variables like `left`, `right`, and `mid`.

**4. Test Cases**

Here's a breakdown of the test cases used above and why they are important:

1.  `nums = [3, 4, 5, 1, 2]` (Example 1): Standard rotated array. Tests the basic logic where the minimum is in the "second" part.
2.  `nums = [4, 5, 6, 7, 0, 1, 2]` (Example 2): Another standard case, minimum is 0.
3.  `nums = [11, 13, 15, 17]` (Example 3): Array is already sorted (no effective rotation or rotated `n` times). The minimum is the first element. The algorithm should correctly handle this.
4.  `nums = [1]`: Single element array. The loop `while left < right` won't execute, and it should correctly return `nums[0]`.
5.  `nums = [2, 1]`: Two elements, rotated. Minimum is the second element.
6.  `nums = [1, 2]`: Two elements, not rotated. Minimum is the first element.
7.  `nums = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]`: A larger example to ensure the logic scales.

These test cases cover the standard scenarios, edge cases (small arrays, no rotation), and variations in the rotation point, ensuring the solution is robust.