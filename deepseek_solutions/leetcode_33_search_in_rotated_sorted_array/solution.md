# find_minimum_rotated.md)
- 搜索旋转排序数组 / Search in Rotated Sorted Array [LeetCode 33]

## Problem Description

**33. Search in Rotated Sorted Array**

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**
```
Input: nums = [1], target = 0
Output: -1
```

**Constraints:**
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Solution

### Problem Explanation
The problem involves searching for a target value in a rotated sorted array. The array was originally sorted in ascending order but has been rotated at some pivot point. The rotation means that the array is divided into two sorted subarrays. For example, `[4,5,6,7,0,1,2]` is a rotated version of `[0,1,2,4,5,6,7]` rotated at pivot index 3. The challenge is to find the target value in this rotated array efficiently, with a time complexity of O(log n), which suggests using a binary search approach.

### Approach
1. **Binary Search in Rotated Sorted Array**: The key observation is that even though the array is rotated, one half of the array (either the left or right half from the mid-point) will always be sorted. We can leverage this property to determine which half to search for the target.
2. **Determine the Sorted Half**: For each midpoint during the binary search:
   - If the left half (from `low` to `mid`) is sorted, check if the target lies within this range. If it does, search the left half; otherwise, search the right half.
   - If the right half (from `mid` to `high`) is sorted, check if the target lies within this range. If it does, search the right half; otherwise, search the left half.
3. **Adjust Search Range**: Based on the above checks, adjust the `low` and `high` pointers to narrow down the search space until the target is found or the search space is exhausted.

### Solution Code
```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Else the right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Test cases
print(search([4,5,6,7,0,1,2], 0))  # Output: 4
print(search([4,5,6,7,0,1,2], 3))  # Output: -1
print(search([1], 0))               # Output: -1
print(search([1,3], 3))             # Output: 1
print(search([5,1,3], 5))           # Output: 0
```

### Explanation
1. **Initialization**: The binary search starts with `low` set to the start of the array and `high` set to the end.
2. **Mid Calculation**: For each iteration, the midpoint `mid` is calculated.
3. **Target Check**: If the element at `mid` is the target, return `mid`.
4. **Left Half Check**: If the left half (from `low` to `mid`) is sorted, check if the target lies within this range. If yes, adjust `high` to `mid - 1`; otherwise, adjust `low` to `mid + 1`.
5. **Right Half Check**: If the right half (from `mid` to `high`) is sorted, check if the target lies within this range. If yes, adjust `low` to `mid + 1`; otherwise, adjust `high` to `mid - 1`.
6. **Termination**: If the loop exits without finding the target, return `-1`.

### Time and Space Complexity
- **Time Complexity**: O(log n) because each iteration reduces the search space by half, similar to standard binary search.
- **Space Complexity**: O(1) as no additional space is used apart from a few variables.

### Test Cases
1. **Example 1**: Search for `0` in `[4,5,6,7,0,1,2]` returns `4` because `0` is at index 4.
2. **Example 2**: Search for `3` in `[4,5,6,7,0,1,2]` returns `-1` because `3` is not present.
3. **Single Element**: Search for `0` in `[1]` returns `-1` as `0` is not present.
4. **Two Elements**: Search for `3` in `[1,3]` returns `1` as `3` is at index 1.
5. **Rotated Small Array**: Search for `5` in `[5,1,3]` returns `0` as `5` is at index 0.