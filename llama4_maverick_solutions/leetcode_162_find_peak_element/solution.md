# search_rotated.md)
- 寻找峰值元素 / Find Peak Element [LeetCode 162]

## Problem Description

## Problem Description

### Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any** of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`.

You must write an algorithm that runs in `O(log n)` time.

#### Example 1:

**Input:** `nums = [1,2,3,1]`
**Output:** `2`
**Explanation:** `3` is a peak element and your function should return the index number `2`.

#### Example 2:

**Input:** `nums = [1,2,1,3,5,6,4]`
**Output:** `5`
**Explanation:** Your function can return either index number `1` where the peak element is `2`, or index number `5` where the peak element is `6`.

#### Constraints:

* `1 <= nums.length <= 1000`
* `-2^31 <= nums[i] <= 2^31 - 1`
* `nums[i] != nums[i + 1]` for all valid `i`.

## Solution

## Problem Explanation

The problem requires finding a peak element in a given integer array `nums` and returning its index. A peak element is defined as an element that is strictly greater than its neighbors. The array is assumed to be surrounded by negative infinity, i.e., `nums[-1] = nums[n] = -∞`. The algorithm should run in `O(log n)` time complexity.

## Step-by-Step Approach

1. **Understand the Problem**: The task is to find the index of any peak element in the array. A peak element is greater than its neighbors.
2. **Identify Key Constraints**:
   - The array length is between 1 and 1000.
   - Each element in the array is a 32-bit integer.
   - No two adjacent elements are equal.
   - The algorithm must run in `O(log n)` time.
3. **Choose an Algorithm**: Given the `O(log n)` constraint, a binary search algorithm is suitable. Binary search is typically used for finding an element in a sorted array, but it can be adapted for this problem.
4. **Adapt Binary Search for Peak Element**:
   - Compare the middle element with its next element.
   - If the middle element is greater than the next, there must be a peak on the left side (including the middle element), so we continue the search on the left half.
   - If the middle element is less than the next, there must be a peak on the right side (since `nums[n] = -∞`), so we continue the search on the right half.
5. **Handle Edge Cases**: The array has at least one element, and the edges are considered to be surrounded by negative infinity.

## Python Solution

```python
def findPeakElement(nums):
    """
    Finds the index of a peak element in the given array.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The index of a peak element.

    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # If the middle element is less than the next one, 
        # then there must be a peak on the right side.
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        # If the middle element is greater than or equal to the next one, 
        # then there must be a peak on the left side (including mid).
        else:
            right = mid
    return left

# Test Cases
if __name__ == "__main__":
    # Example 1
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))  # Expected Output: 2

    # Example 2
    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))  # Expected Output: 1 or 5

    # Edge Case: Single Element
    nums = [5]
    print(findPeakElement(nums))  # Expected Output: 0

    # Edge Case: Increasing Array
    nums = [1, 2, 3, 4, 5]
    print(findPeakElement(nums))  # Expected Output: 4

    # Edge Case: Decreasing Array
    nums = [5, 4, 3, 2, 1]
    print(findPeakElement(nums))  # Expected Output: 0
```

## Time and Space Complexity Analysis

- **Time Complexity**: `O(log n)`, where `n` is the number of elements in `nums`. This is because with each comparison, we effectively halve the search space.
- **Space Complexity**: `O(1)`, as we only use a constant amount of space to store the indices and do not use any data structures that scale with the input size.

## Test Cases

The provided Python solution includes several test cases to verify its correctness:
- Example 1: `nums = [1, 2, 3, 1]`
- Example 2: `nums = [1, 2, 1, 3, 5, 6, 4]`
- Edge Case: Single Element `nums = [5]`
- Edge Case: Increasing Array `nums = [1, 2, 3, 4, 5]`
- Edge Case: Decreasing Array `nums = [5, 4, 3, 2, 1]`

These test cases cover various scenarios, including the examples given in the problem statement and some edge cases to ensure the solution is robust.