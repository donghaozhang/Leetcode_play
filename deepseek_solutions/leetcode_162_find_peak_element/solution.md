# search_rotated.md)
- 寻找峰值元素 / Find Peak Element [LeetCode 162]

## Problem Description

**Problem: Find Peak Element**

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

**Example 2:**
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

**Constraints:**
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Solution

### Explanation of the Problem
A peak element in an array is an element that is strictly greater than its neighbors. For the given problem, the array is 0-indexed, and we can assume that `nums[-1] = nums[n] = -∞`, meaning that the first and last elements can also be peaks if they are greater than their single neighbor. The problem requires us to find any peak element in the array efficiently, with a time complexity of O(log n), which suggests the use of binary search.

### Approach
1. **Binary Search Adaptation**: Since the array is not necessarily sorted, but we need O(log n) time, we can use a modified binary search. The key observation is that if an element is not a peak, then the side with the higher neighbor must contain a peak.
2. **Steps**:
   - Initialize `left` to 0 and `right` to `len(nums) - 1`.
   - While `left < right`, compute the middle index `mid`.
   - Compare `nums[mid]` with `nums[mid + 1]`:
     - If `nums[mid] < nums[mid + 1]`, the peak must be on the right side of `mid` (since `nums[n]` is -∞), so set `left = mid + 1`.
     - Otherwise, the peak is on the left side (including `mid`), so set `right = mid`.
   - When the loop ends, `left` will be pointing to a peak element because the search narrows down to the highest point in the current range.

### Solution Code
```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

# Test cases
print(findPeakElement([1, 2, 3, 1]))  # Output: 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 or 1
print(findPeakElement([1]))  # Output: 0
print(findPeakElement([1, 2]))  # Output: 1
print(findPeakElement([2, 1]))  # Output: 0
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(log n), where n is the number of elements in the array. This is because we are using binary search, which halves the search space in each iteration.
- **Space Complexity**: O(1), as we are using a constant amount of extra space for variables `left`, `right`, and `mid`.

### Test Cases
1. **Test Case 1**: `[1, 2, 3, 1]`
   - **Explanation**: The peak is at index 2 (value 3), as it is greater than its neighbors 2 and 1.
   - **Expected Output**: 2

2. **Test Case 2**: `[1, 2, 1, 3, 5, 6, 4]`
   - **Explanation**: There are two peaks: at index 1 (value 2) and index 5 (value 6). The function can return either.
   - **Possible Outputs**: 1 or 5

3. **Test Case 3**: `[1]`
   - **Explanation**: Only one element, which is considered a peak by default.
   - **Expected Output**: 0

4. **Test Case 4**: `[1, 2]`
   - **Explanation**: The peak is at index 1 (value 2), as it is greater than its left neighbor and the right neighbor is -∞.
   - **Expected Output**: 1

5. **Test Case 5**: `[2, 1]`
   - **Explanation**: The peak is at index 0 (value 2), as it is greater than its right neighbor and the left neighbor is -∞.
   - **Expected Output**: 0

These test cases cover various scenarios including single-element arrays, arrays with peaks at the beginning or end, and multiple peaks. The solution efficiently handles all these cases with O(log n) time complexity.