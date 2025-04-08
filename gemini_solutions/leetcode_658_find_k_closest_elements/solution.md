# search_big_sorted_array.md)
- 找到K个最接近的元素 / Find K Closest Elements [LeetCode 658]

## Problem Description

```markdown
## 658. Find K Closest Elements

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

*   `|a - x| < |b - x|`, or
*   `|a - x| == |b - x|` and `a < b`

**Example 1:**

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

**Example 2:**

```
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

**Constraints:**

*   `1 <= k <= arr.length`
*   `1 <= arr.length <= 10^4`
*   `arr` is sorted in **ascending** order.
*   `-10^4 <= arr[i], x <= 10^4`
```

## Solution

Okay, let's break down the "Find K Closest Elements" problem (LeetCode 658).

**1. Problem Explanation**

We are given a sorted array of integers `arr`, an integer `k`, and a target value `x`. Our goal is to find `k` numbers from the array that are closest to `x`. The "closeness" is defined first by the absolute difference between the number and `x`. If two numbers have the same absolute difference, the smaller number is considered closer. The final result should be a list of these `k` numbers, sorted in ascending order.

**Example:**
If `arr = [1, 2, 3, 4, 5]`, `k = 4`, `x = 3`:
- Differences from `x=3`: `|1-3|=2`, `|2-3|=1`, `|3-3|=0`, `|4-3|=1`, `|5-3|=2`
- Sorted by closeness: `3` (diff 0), `2` (diff 1), `4` (diff 1, but 2 < 4), `1` (diff 2), `5` (diff 2, but 1 < 5)
- The 4 closest are `3, 2, 4, 1`.
- Sorted result: `[1, 2, 3, 4]`

**2. Step-by-Step Approach**

The key insight is that since the input array `arr` is sorted, the `k` closest elements will always form a contiguous subarray of `arr`. Our task is to find the *starting index* of this subarray of length `k`.

Let the length of the array be `n`. A subarray of length `k` can start at any index `i` from `0` to `n-k`. We are looking for the optimal starting index, let's call it `left`. The resulting subarray will be `arr[left : left + k]`.

Consider two potential windows of size `k`: `arr[i : i + k]` and `arr[i + 1 : i + k + 1]`.
These windows differ by one element at each end: the first window includes `arr[i]` but not `arr[i+k]`, while the second includes `arr[i+k]` but not `arr[i]`.

To decide which window is "better" (contains elements closer to `x`), we only need to compare the elements that differ: `arr[i]` and `arr[i+k]`.
- If `arr[i]` is further away from `x` than `arr[i+k]`, then the window starting at `i+1` is likely better or equal.
- If `arr[i+k]` is further away from `x` than `arr[i]`, then the window starting at `i` is likely better or equal.

Let's formalize the comparison using the problem's closeness rule:
We prefer `arr[i]` over `arr[i+k]` if:
  `|arr[i] - x| < |arr[i+k] - x|`
  OR
  `|arr[i] - x| == |arr[i+k] - x|` AND `arr[i] < arr[i+k]`

This is equivalent to saying we prefer `arr[i+k]` (and thus potentially shifting the window right) if `arr[i]` is *not* preferred over `arr[i+k]`. That is, if:
  `|arr[i] - x| > |arr[i+k] - x|`
  OR
  `|arr[i] - x| == |arr[i+k] - x|` AND `arr[i] > arr[i+k]` (Note: `arr[i] < arr[i+k]` since the array is sorted, so the second part of this OR is impossible if the differences are equal).

So, we shift the window right (prefer `arr[i+k]`) if `|arr[i] - x| > |arr[i+k] - x|`.
Since `x - arr[i]` will be negative or zero if `arr[i] >= x`, and `arr[i+k] - x` will be positive or zero if `arr[i+k] >= x`, comparing absolute values directly can be slightly tricky with signs.

A simpler comparison: If we have the window `arr[i : i+k]`, should we keep `arr[i]` or replace it with `arr[i+k]` (effectively shifting the window to `arr[i+1 : i+k+1]`)?
We should keep `arr[i]` (and the window starting at `i`) if `x` is closer to `arr[i]` than `arr[i+k]`.
We should discard `arr[i]` in favor of `arr[i+k]` (and shift the window right) if `x` is closer to `arr[i+k]` than `arr[i]`.

Consider the distances: `dist_left = x - arr[i]` and `dist_right = arr[i+k] - x`.
- If `dist_left > dist_right`: `x` is further from `arr[i]` than `arr[i+k]` (or `x` is "more to the right" relative to the midpoint). We discard `arr[i]` and shift the window right.
- If `dist_left <= dist_right`: `x` is closer to or equidistant from `arr[i]` compared to `arr[i+k]`. We keep `arr[i]` and the current window starting position `i` is potentially optimal or the optimal one is to its left.

This condition `x - arr[i] > arr[i+k] - x` allows us to use binary search. We are searching for the optimal starting index `left` in the range `[0, n-k]`.

**Binary Search Algorithm:**
1. Initialize `low = 0` and `high = n - k`. This `[low, high]` represents the possible range for the starting index of the optimal window.
2. While `low < high`:
   a. Calculate `mid = low + (high - low) // 2`.
   b. Compare `arr[mid]` and `arr[mid+k]`. Check if we should shift the window right. Use the condition: `x - arr[mid] > arr[mid+k] - x`.
   c. If the condition is true (`x` is closer to `arr[mid+k]`): The optimal window must start at index `mid + 1` or later. So, update `low = mid + 1`.
   d. If the condition is false (`x` is closer to or equidistant from `arr[mid]`): The optimal window could start at `mid` or even earlier. So, update `high = mid`.
3. When the loop terminates (`low == high`), `low` (or `high`) is the starting index of the desired subarray of `k` closest elements.
4. Return the slice `arr[low : low + k]`.

**3. Python Solution**

```python
import math
from typing import List

class Solution:
    """
    Finds the k closest elements to x in a sorted array arr.

    Uses binary search to find the optimal starting index of the k-element window.
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Finds k closest elements to x in the sorted array arr.

        Args:
            arr: The sorted input array.
            k: The number of closest elements to find.
            x: The target value.

        Returns:
            A list containing the k closest elements, sorted in ascending order.
        """
        n = len(arr)

        # Handle edge case where k is the entire array
        if k == n:
            return arr

        # Binary search for the optimal start index 'left' of the window [left, left + k - 1]
        # The search space for 'left' is [0, n - k]
        low = 0
        high = n - k

        while low < high:
            mid = low + (high - low) // 2
            
            # Compare the element just outside the left end (arr[mid])
            # with the element just outside the right end (arr[mid + k])
            # We want to determine if the window starting at 'mid' is better
            # than the window starting at 'mid + 1'.

            # If x is closer to arr[mid+k] than arr[mid],
            # it means we should discard arr[mid] and shift the window right.
            # The optimal window must start at mid + 1 or later.
            # Condition: x - arr[mid] > arr[mid + k] - x
            # This checks if the distance from x to arr[mid] is greater than
            # the distance from x to arr[mid+k].
            # If distances are equal, x - arr[mid] <= arr[mid+k] - x favors
            # keeping the smaller element arr[mid], hence we keep the window starting at mid.
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                # If x is closer to arr[mid] or equidistant,
                # the optimal window could start at 'mid' or earlier.
                high = mid

        # When the loop ends, 'low' is the starting index of the k closest elements
        return arr[low : low + k]

# --- Test Cases ---

def run_tests():
    sol = Solution()
    test_cases = [
        # Example 1
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        # Example 2
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        # Edge case: k = 1
        ([1, 1, 1, 10, 10, 10], 1, 9, [10]),
        # Edge case: k = length of array
        ([1, 2, 3], 3, 2, [1, 2, 3]),
        # Edge case: x smaller than all elements
        ([10, 20, 30], 2, 5, [10, 20]),
        # Edge case: x larger than all elements
        ([10, 20, 30], 2, 35, [20, 30]),
        # Tie-breaking case
        ([1, 2, 3, 4, 5], 2, 3, [2, 3]), # |2-3|=1, |3-3|=0, |4-3|=1. Closest are 3, 2. Result [2, 3]
        ([1, 2, 4, 5], 2, 3, [2, 4]), # |2-3|=1, |4-3|=1. Tie, choose smaller elements. Need k=2. Result [2, 4].
        ([1, 3, 5, 7], 2, 4, [3, 5]), # |3-4|=1, |5-4|=1. Tie, choose smaller elements. Need k=2. Result [3, 5].
        # More complex case
        ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5, [3, 3, 4]),
        # Negative numbers
        ([-5, -3, -1, 0, 2, 4], 3, -2, [-3, -1, 0]),
        ([-2, -1, 0, 1, 2], 3, 0, [-1, 0, 1]),
        # Duplicates around x
        ([1, 1, 2, 2, 2, 3, 3], 3, 2, [2, 2, 2]), # Should pick the 2s
        ([1, 1, 2, 2, 2, 3, 3], 4, 2, [1, 2, 2, 2]), # Should pick one 1 and three 2s
        ([1, 1, 2, 2, 2, 3, 3], 5, 2, [1, 1, 2, 2, 2]), # Should pick two 1s and three 2s
    ]

    for i, (arr, k, x, expected) in enumerate(test_cases):
        result = sol.findClosestElements(arr, k, x)
        print(f"Test Case {i + 1}:")
        print(f"  Input: arr={arr}, k={k}, x={x}")
        print(f"  Expected Output: {expected}")
        print(f"  Actual Output:   {result}")
        assert result == expected, f"Test Case {i + 1} Failed!"
        print("-" * 20)

    print("All test cases passed!")

# Run the tests
run_tests()

```

**4. Complexity Analysis**

*   **Time Complexity:** O(log(N - k) + k)
    *   The binary search runs on a range of size `N - k + 1`. The number of iterations is logarithmic with respect to this range size, so it's O(log(N - k)).
    *   Each comparison inside the binary search takes O(1) time.
    *   Finally, creating the result slice `arr[low : low + k]` takes O(k) time.
    *   Therefore, the total time complexity is dominated by O(log(N - k) + k). Since `k <= N`, this is often simplified to O(log N + k).

*   **Space Complexity:** O(k) or O(1)
    *   If we consider the space required for the output list, it's O(k).
    *   If we don't count the output space (as is common in complexity analysis), the algorithm uses O(1) extra space for variables like `low`, `high`, `mid`.

This binary search approach is efficient and directly leverages the sorted property of the input array.