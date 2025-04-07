# k_closest_elements.md)
- 旋转排序数组中的最小值 / Find Minimum in Rotated Sorted Array [LeetCode 153]

## Problem Description

**Problem 153: Find Minimum in Rotated Sorted Array**

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

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
Explanation: The original array was [0,1,2,4,5,6,7] rotated 4 times.
```

**Example 3:**

```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Solution

### Explanation of the Problem

We are given a sorted array that has been rotated between 1 and n times, where n is the length of the array. The rotation means that the last element of the original sorted array is moved to the front, and this operation is performed multiple times. The array contains unique elements, and our task is to find the minimum element in this rotated sorted array efficiently, i.e., in O(log n) time.

### Approach
To solve this problem, we can use a modified binary search approach. The key observation is that in a rotated sorted array, the minimum element is the point where the order of elements changes from increasing to decreasing or where the next element is smaller than the current one. Here’s the step-by-step approach:

1. **Initialize Pointers**: Start with two pointers, `left` at the beginning (0) and `right` at the end (n-1) of the array.
2. **Binary Search**: While `left` < `right`:
   - Calculate the middle index `mid`.
   - Compare the element at `mid` with the element at `right`:
     - If `nums[mid] > nums[right]`, the minimum must be in the right half (since the array is rotated, and the right half contains smaller elements). Move `left` to `mid + 1`.
     - Else, the minimum is in the left half or at `mid`. Move `right` to `mid`.
3. **Termination**: When `left` equals `right`, it points to the minimum element.

This approach efficiently narrows down the search space by half in each iteration, adhering to the O(log n) time complexity requirement.

### Solution Code
```python
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Test cases
print(findMin([3,4,5,1,2]))      # Output: 1
print(findMin([4,5,6,7,0,1,2]))  # Output: 0
print(findMin([11,13,15,17]))    # Output: 11
print(findMin([1]))              # Output: 1
print(findMin([2,1]))            # Output: 1
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(log n), where n is the number of elements in the array. This is because we are using binary search, which halves the search space in each iteration.
- **Space Complexity**: O(1), as we are using a constant amount of extra space regardless of the input size.

### Test Cases
1. **Example 1**: 
   - Input: `[3,4,5,1,2]`
   - Output: `1` (The original array was `[1,2,3,4,5]` rotated 3 times.)
2. **Example 2**: 
   - Input: `[4,5,6,7,0,1,2]`
   - Output: `0` (The original array was `[0,1,2,4,5,6,7]` rotated 4 times.)
3. **Example 3**: 
   - Input: `[11,13,15,17]`
   - Output: `11` (The original array was `[11,13,15,17]` rotated 4 times.)
4. **Single Element**: 
   - Input: `[1]`
   - Output: `1` (Only one element, which is the minimum.)
5. **Two Elements**: 
   - Input: `[2,1]`
   - Output: `1` (The array is rotated once, so the minimum is 1.)

These test cases cover various scenarios including no rotation, rotation at different positions, and edge cases with minimal array sizes.