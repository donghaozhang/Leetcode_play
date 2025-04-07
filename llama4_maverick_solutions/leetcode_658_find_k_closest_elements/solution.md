# search_big_sorted_array.md)
- 找到K个最接近的元素 / Find K Closest Elements [LeetCode 658]

## Problem Description

## 658. Find K Closest Elements

Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

*   `|a - x| < |b - x|`, or
*   `|a - x| == |b - x|` and `a < b`

### Example 1:

**Input:** arr = \[1,2,3,4,5], k = 4, x = 3
**Output:** \[1,2,3,4]

### Example 2:

**Input:** arr = \[1,2,3,4,5], k = 4, x = -1
**Output:** \[1,2,3,4]

### Constraints:

*   `1 <= k <= arr.length`
*   `1 <= arr.length <= 10^4`
*   `arr` is sorted in **ascending** order.
*   `-10^4 <= arr[i], x <= 10^4`

## Solution

## Problem Explanation

The problem requires finding the `k` closest integers to a given target `x` in a sorted integer array `arr`. The result should be sorted in ascending order. The closeness of an integer `a` to `x` is determined by the absolute difference `|a - x|`. If two integers have the same absolute difference, the smaller one is considered closer.

## Step-by-Step Approach

1. **Find the closest element to `x`**: Use binary search to find the index of the element in `arr` that is closest to `x`. If `x` is present in the array, this step will find its index. If `x` is not present, this step will find the index where `x` should be inserted to maintain the sorted order.

2. **Initialize two pointers**: Initialize two pointers, `left` and `right`, to the indices adjacent to the closest element found in step 1. The `left` pointer will be at the index of the closest element or one less than it, and the `right` pointer will be at the index one more than the closest element.

3. **Expand the window**: Compare the elements at the `left` and `right` indices and move the pointers accordingly to find the `k` closest elements. The comparison is based on the absolute difference between the elements and `x`. If the absolute difference between the element at `left` and `x` is less than or equal to the absolute difference between the element at `right` and `x`, move the `left` pointer to the left. Otherwise, move the `right` pointer to the right.

4. **Handle edge cases**: Ensure that the `left` and `right` pointers do not go out of bounds of the array.

5. **Return the result**: Once `k` closest elements are found, return them in ascending order.

## Python Solution

```python
from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # Find the index of the closest element to x using binary search
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        # Compare the absolute differences between arr[mid] and x, and arr[mid + k] and x
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    # Return the k closest elements
    return arr[left:left + k]

# Test cases
print(findClosestElements([1, 2, 3, 4, 5], 4, 3))  # Output: [1, 2, 3, 4]
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))  # Output: [1, 2, 3, 4]
print(findClosestElements([1, 5, 10, 15, 20], 3, 8))  # Output: [1, 5, 10]
print(findClosestElements([1, 2, 3, 4, 5], 2, 6))  # Output: [4, 5]
```

## Time and Space Complexity Analysis

*   **Time complexity**: The time complexity of the solution is O(log(n - k)), where n is the length of the input array `arr`. This is because we are performing a binary search on the range `[0, n - k]`.
*   **Space complexity**: The space complexity of the solution is O(1), excluding the space required for the output. We are not using any additional data structures that scale with the input size.

## Test Cases

The provided Python solution includes test cases to verify its correctness. Additional test cases can be added to cover more scenarios, such as:

*   Edge cases: `k` equals the length of `arr`, `x` is less than the smallest element in `arr`, `x` is greater than the largest element in `arr`.
*   Boundary cases: `k` is 1, `arr` contains duplicate elements.

These test cases can help ensure that the solution is robust and handles various input scenarios correctly.