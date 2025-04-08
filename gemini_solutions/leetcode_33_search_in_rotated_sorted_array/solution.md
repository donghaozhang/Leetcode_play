# find_minimum_rotated.md)
- 搜索旋转排序数组 / Search in Rotated Sorted Array [LeetCode 33]

## Problem Description

```markdown
## 33. Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [4,5,6,7,0,1,2], target = 0
**Output:** 4

**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2], target = 3
**Output:** -1

**Example 3:**

**Input:** nums = [1], target = 0
**Output:** -1

**Constraints:**

*   `1 <= nums.length <= 5000`
*   `-10^4 <= nums[i] <= 10^4`
*   All values of `nums` are **unique**.
*   `nums` is an ascending array that is possibly rotated.
*   `-10^4 <= target <= 10^4`
```

## Solution

Okay, let's break down the "Search in Rotated Sorted Array" problem (LeetCode 33).

**1. Explanation of the Problem**

We are given an array of distinct integers that was originally sorted in ascending order. This array has then been rotated at some unknown pivot point `k`. Our goal is to find the index of a given `target` value within this rotated array. If the `target` is not present, we should return -1. The crucial constraint is that our solution must run in O(log n) time complexity, which strongly suggests using a modified binary search.

**Example:**
Original sorted array: `[0, 1, 2, 4, 5, 6, 7]`
Rotated at pivot `k=3`: `[4, 5, 6, 7, 0, 1, 2]`

If `target = 0`, the output should be `4`.
If `target = 3`, the output should be `-1`.

The key challenge is that the array is not fully sorted, but it has a specific structure: it consists of two sorted subarrays.

**2. Step-by-Step Approach**

We'll adapt the standard binary search algorithm. The core idea remains the same: maintain a search space defined by `low` and `high` pointers and repeatedly narrow it down by comparing the `target` with the middle element `nums[mid]`.

The modification comes in how we decide which half of the array to discard. Since the array isn't fully sorted, we first need to determine which part (left half `[low...mid]` or right half `[mid...high]`) *is* sorted.

1.  **Initialization:**
    *   Set `low = 0` and `high = len(nums) - 1`.

2.  **Binary Search Loop:**
    *   Continue as long as `low <= high`.
    *   Calculate the middle index: `mid = low + (high - low) // 2` (this avoids potential integer overflow).
    *   **Check for Target:** If `nums[mid] == target`, we've found it! Return `mid`.
    *   **Identify the Sorted Half:** Compare `nums[mid]` with `nums[low]`.
        *   **Case 1: `nums[low] <= nums[mid]`**
            *   This means the left half (`nums[low]` to `nums[mid]`) is sorted.
            *   Now, check if the `target` lies within this sorted left half:
                *   If `nums[low] <= target < nums[mid]`: The target *must* be in the left half. Discard the right half by setting `high = mid - 1`.
                *   Else: The target must be in the right (potentially unsorted) half. Discard the left half by setting `low = mid + 1`.
        *   **Case 2: `nums[low] > nums[mid]`**
            *   This means the rotation point is somewhere in the left half, so the *right* half (`nums[mid]` to `nums[high]`) is sorted.
            *   Now, check if the `target` lies within this sorted right half:
                *   If `nums[mid] < target <= nums[high]`: The target *must* be in the right half. Discard the left half by setting `low = mid + 1`.
                *   Else: The target must be in the left (potentially unsorted) half. Discard the right half by setting `high = mid - 1`.

3.  **Target Not Found:**
    *   If the loop finishes (i.e., `low > high`), the `target` was not found in the array. Return `-1`.

**3. Python Solution**

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Args:
            nums: A list of distinct integers, sorted and possibly rotated.
            target: The integer value to search for.

        Returns:
            The index of the target if found, otherwise -1.
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Case 1: Found the target
            if nums[mid] == target:
                return mid

            # Case 2: Left half is sorted (nums[low] to nums[mid])
            if nums[low] <= nums[mid]:
                # Check if target is within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
            # Case 3: Right half is sorted (nums[mid] to nums[high])
            else: # nums[low] > nums[mid]
                # Check if target is within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left

        # Target not found
        return -1

# --- Test Cases ---
solver = Solution()

# Example 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {solver.search(nums1, target1)}") # Expected: 4
print("-" * 20)

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {solver.search(nums2, target2)}") # Expected: -1
print("-" * 20)

# Example 3
nums3 = [1]
target3 = 0
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {solver.search(nums3, target3)}") # Expected: -1
print("-" * 20)

# Additional Test Cases
nums4 = [1]
target4 = 1
print(f"Input: nums = {nums4}, target = {target4}")
print(f"Output: {solver.search(nums4, target4)}") # Expected: 0
print("-" * 20)

nums5 = [5, 1, 3]
target5 = 5
print(f"Input: nums = {nums5}, target = {target5}")
print(f"Output: {solver.search(nums5, target5)}") # Expected: 0
print("-" * 20)

nums6 = [5, 1, 3]
target6 = 3
print(f"Input: nums = {nums6}, target = {target6}")
print(f"Output: {solver.search(nums6, target6)}") # Expected: 2
print("-" * 20)

nums7 = [3, 1]
target7 = 1
print(f"Input: nums = {nums7}, target = {target7}")
print(f"Output: {solver.search(nums7, target7)}") # Expected: 1
print("-" * 20)

nums8 = [3, 5, 1]
target8 = 3
print(f"Input: nums = {nums8}, target = {target8}")
print(f"Output: {solver.search(nums8, target8)}") # Expected: 0
print("-" * 20)

```

**Complexity Analysis:**

*   **Time Complexity: O(log n)**
    *   The algorithm uses binary search. In each iteration of the `while` loop, the search space (`high - low + 1`) is roughly halved. This logarithmic reduction in the search space leads to O(log n) time complexity, where n is the number of elements in `nums`.
*   **Space Complexity: O(1)**
    *   The algorithm uses only a fixed number of variables (`low`, `high`, `mid`) regardless of the input size. Therefore, the space complexity is constant, O(1).

**4. Test Cases**

The provided Python code includes several test cases to verify the solution:

1.  `nums = [4, 5, 6, 7, 0, 1, 2], target = 0` -> Expected: `4` (Target in the second sorted part)
2.  `nums = [4, 5, 6, 7, 0, 1, 2], target = 3` -> Expected: `-1` (Target not present)
3.  `nums = [1], target = 0` -> Expected: `-1` (Single element array, target not present)
4.  `nums = [1], target = 1` -> Expected: `0` (Single element array, target present)
5.  `nums = [5, 1, 3], target = 5` -> Expected: `0` (Target is the first element, rotation involved)
6.  `nums = [5, 1, 3], target = 3` -> Expected: `2` (Target in the second sorted part)
7.  `nums = [3, 1], target = 1` -> Expected: `1` (Two elements, target is the second)
8.  `nums = [3, 5, 1], target = 3` -> Expected: `0` (Target is the first element, rotation involved)

These test cases cover various scenarios, including finding the target in either sorted subarray, the target being the first or last element, single-element arrays, and cases where the target is not found.