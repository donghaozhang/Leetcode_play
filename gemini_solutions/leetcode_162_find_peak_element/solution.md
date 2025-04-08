# search_rotated.md)
- 寻找峰值元素 / Find Peak Element [LeetCode 162]

## Problem Description

Content could not be retrieved due to API limitations. Please try again later.

## Solution

Okay, let's break down the "Find Peak Element" problem (LeetCode 162).

### 1. Explanation of the Problem

You are given an integer array `nums`. Your task is to find a **peak element** and return its **index**.

A peak element is defined as an element that is **strictly greater** than its immediate neighbors.

The problem statement also specifies two important conditions:
1.  The array may contain multiple peaks; in such cases, returning the index of **any** peak is sufficient.
2.  You can imagine that `nums[-1] = nums[n] = -∞` (negative infinity), where `n` is the length of the array. This means:
    *   If the first element `nums[0]` is greater than `nums[1]`, then `nums[0]` is considered a peak.
    *   If the last element `nums[n-1]` is greater than `nums[n-2]`, then `nums[n-1]` is considered a peak.

Finally, the problem requires a solution with **O(log n)** time complexity, which strongly suggests using binary search.

**Example:**

*   `nums = [1, 2, 3, 1]`
    *   `3` is a peak element because `3 > 2` and `3 > 1`.
    *   The index of `3` is `2`. So, the function should return `2`.
*   `nums = [1, 2, 1, 3, 5, 6, 4]`
    *   `2` is a peak element (index `1`).
    *   `6` is a peak element (index `5`).
    *   Returning either `1` or `5` is acceptable.

### 2. Step-by-Step Approach

The key insight is that we can use binary search because of the nature of peaks and the implicit boundary conditions.

1.  **Initialization:** Set two pointers, `left = 0` and `right = n - 1`, where `n` is the length of the array `nums`. These pointers define the current search space `[left, right]`.

2.  **Binary Search Loop:** Continue the search as long as `left < right`. This condition ensures we haven't narrowed down the search space to a single element yet.

3.  **Calculate Midpoint:** Calculate the middle index `mid = left + (right - left) // 2`. Using this formula avoids potential integer overflow compared to `(left + right) // 2`.

4.  **Compare `nums[mid]` with its Right Neighbor `nums[mid+1]`:**
    *   **Case 1: `nums[mid] < nums[mid+1]`**
        *   This means the numbers are increasing at index `mid`. `nums[mid]` cannot be a peak because its right neighbor is larger.
        *   However, this upward trend implies that a peak *must* exist somewhere to the right of `mid` (either `nums[mid+1]` itself is a peak, or the trend continues upwards until it eventually drops, creating a peak further right). The `-infinity` boundary at `nums[n]` guarantees a peak will be found on the right side.
        *   Therefore, we can safely discard the left half including `mid`, and update `left = mid + 1`.
    *   **Case 2: `nums[mid] > nums[mid+1]`**
        *   This means the numbers are decreasing at index `mid`. `nums[mid]` *could* be a peak (if `nums[mid] > nums[mid-1]`, or if `mid == 0`).
        *   Even if `nums[mid]` is not a peak itself (because `nums[mid-1] > nums[mid]`), the downward slope at `mid` guarantees that a peak *must* exist somewhere to the left of or at `mid`. The `-infinity` boundary at `nums[-1]` guarantees a peak will be found on this side.
        *   Therefore, we can safely discard the right half *after* `mid`, and update `right = mid`. We keep `mid` in the search space because it might be the peak itself.

5.  **Termination:** The loop terminates when `left == right`. At this point, the search space has been narrowed down to a single index. Because we maintained the invariant that a peak always exists within the `[left, right]` range, this final index `left` (or `right`) must be the index of a peak element.

6.  **Return:** Return `left` (or `right`).

**Why does this work?**
The comparison `nums[mid]` vs `nums[mid+1]` effectively tells us which direction has the "potential" for a peak. If `nums[mid] < nums[mid+1]`, we are on an "upslope", so the peak must be further up (to the right). If `nums[mid] > nums[mid+1]`, we are on a "downslope" (or at the peak itself), meaning a peak must be at `mid` or to its left. The binary search systematically eliminates half of the remaining search space in each step, guaranteeing an O(log n) time complexity. The boundary conditions ensure that a peak always exists.

### 3. Python Solution

```python
import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Finds a peak element in the array using binary search.

        A peak element is an element that is strictly greater than its neighbors.
        Assumes nums[-1] = nums[n] = -infinity.

        Args:
            nums: A list of integers.

        Returns:
            The index of any peak element.
        """
        n = len(nums)

        # Handle edge case: single element array
        if n == 1:
            return 0

        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            # Compare mid element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # We are on an ascending slope, peak must be to the right (mid+1 or further)
                left = mid + 1
            else:
                # We are on a descending slope (or at a peak),
                # peak must be at mid or to the left.
                # Keep mid in the search space as it could be the peak.
                right = mid

        # When the loop terminates, left == right, pointing to a peak element.
        # Why is nums[left] a peak?
        # The loop invariant ensures a peak exists in [left, right].
        # When left == right, the range has one element.
        # Consider the final state: left = right = p.
        # If we arrived here via right = mid, it means nums[mid] > nums[mid+1] (i.e., nums[p] > nums[p+1]).
        # If we arrived here via left = mid + 1, it means the previous mid was p-1, and nums[p-1] < nums[p].
        # Combining these (or handling boundary conditions using implicit -infinity), nums[p] must be a peak.
        return left

# Helper function to run test cases
def run_tests():
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 1], [2]), # Peak is 3 at index 2
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]), # Peaks are 2 (idx 1) and 6 (idx 5) - either is fine
        ([1], [0]), # Single element is a peak
        ([3, 2, 1], [0]), # Peak at the beginning
        ([1, 2, 3], [2]), # Peak at the end
        ([2, 1], [0]), # Two elements, descending
        ([1, 2], [1]), # Two elements, ascending
        ([1, 1, 1, 1], [0, 1, 2, 3]), # Any index could be argued if strictness wasn't required, but here it finds one based on slope logic
        ([6, 5, 4, 3, 2, 3, 2], [0, 5]), # Multiple peaks
    ]

    for i, (nums, expected_indices) in enumerate(test_cases):
        result = sol.findPeakElement(nums.copy()) # Use copy to avoid modifying original test case list if needed
        print(f"Test Case {i+1}:")
        print(f"  Input: nums = {nums}")
        print(f"  Expected Peak Index (one of): {expected_indices}")
        print(f"  Actual Peak Index: {result}")
        if result in expected_indices:
            # Verify if the returned index is indeed a peak
            is_peak = True
            n = len(nums)
            left_val = nums[result - 1] if result > 0 else -math.inf
            right_val = nums[result + 1] if result < n - 1 else -math.inf
            if not (nums[result] > left_val and nums[result] > right_val):
                 is_peak = False

            if is_peak:
                print(f"  Result: PASSED (Found valid peak at index {result})")
            else:
                 print(f"  Result: FAILED (Index {result} value {nums[result]} is not a peak)")

        else:
            # Check if the returned index is actually a peak, even if not listed in expected_indices
            # (only happens if multiple peaks exist and the algorithm finds a different one)
            is_peak = True
            n = len(nums)
            left_val = nums[result - 1] if result > 0 else -math.inf
            right_val = nums[result + 1] if result < n - 1 else -math.inf
            if not (nums[result] > left_val and nums[result] > right_val):
                 is_peak = False

            if is_peak:
                 print(f"  Result: PASSED (Found valid peak at index {result}, which is one of the possible peaks)")
            else:
                 print(f"  Result: FAILED (Returned index {result} is not one of the expected indices {expected_indices} AND is not a peak)")
        print("-" * 20)

# Run the tests
run_tests()
```

### 4. Complexity Analysis

*   **Time Complexity: O(log n)**
    *   The binary search algorithm divides the search space in half in each iteration.
    *   The number of iterations is proportional to the logarithm of the input size `n`.
*   **Space Complexity: O(1)**
    *   The algorithm uses only a constant amount of extra space for variables like `left`, `right`, and `mid`. No auxiliary data structures are needed.

### 5. Test Cases Verification

The provided `run_tests` function includes several test cases:

1.  `[1, 2, 3, 1]`: Peak `3` at index `2`. Expected: `2`.
2.  `[1, 2, 1, 3, 5, 6, 4]`: Peaks `2` at index `1` and `6` at index `5`. Expected: `1` or `5`. The algorithm might return either.
3.  `[1]`: Single element array. Peak `1` at index `0`. Expected: `0`.
4.  `[3, 2, 1]`: Peak `3` at index `0` (due to `nums[-1] = -inf`). Expected: `0`.
5.  `[1, 2, 3]`: Peak `3` at index `2` (due to `nums[3] = -inf`). Expected: `2`.
6.  `[2, 1]`: Peak `2` at index `0`. Expected: `0`.
7.  `[1, 2]`: Peak `2` at index `1`. Expected: `1`.
8.  `[1, 1, 1, 1]`: The problem statement says `nums[i] != nums[i+1]`, but if this constraint were relaxed, the algorithm would still find *an* index based on the comparison logic. For `[1,1,1,1]`, `nums[mid] < nums[mid+1]` is never true, so `right` keeps becoming `mid`. It will likely return index `0`. Let's assume the input adheres to the constraint `nums[i] != nums[i+1]`.
9.  `[6, 5, 4, 3, 2, 3, 2]`: Peaks `6` at index `0` and `3` at index `5`. Expected: `0` or `5`.

The test runner executes the `findPeakElement` function for each case and compares the returned index against the list of possible correct indices. It also verifies if the element at the returned index actually satisfies the peak condition using the implicit `-infinity` neighbors. The output confirms whether the solution passes each test case.