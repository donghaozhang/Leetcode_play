# find_minimum_rotated.md)
- 搜索旋转排序数组 / Search in Rotated Sorted Array [LeetCode 33]

## Problem Description

## Search in Rotated Sorted Array
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return _the index of `target` if it is in `nums`, or `-1` if it is not in `nums`_.

You must write an algorithm with an `O(log n)` runtime complexity.

### Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```
### Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```
### Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

### Constraints:
* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i] <= 10^4`
* All values of `nums` are **unique**.
* `nums` is an **ascending array** that is possibly rotated.
* `-10^4 <= target <= 10^4`

## Solution

## Problem Explanation
The problem requires finding the index of a target element in a possibly rotated sorted array. The input array is sorted in ascending order but may be rotated at an unknown pivot index. The task is to write an algorithm that can find the target element in the array with an `O(log n)` runtime complexity.

## Step-by-Step Approach
1. **Understand the Problem**: The input array is sorted but possibly rotated. We need to find a target element in this array.
2. **Identify the Rotation**: Determine if the array is rotated by comparing the first and last elements. If the first element is less than the last element, the array is not rotated.
3. **Modified Binary Search**: Use a modified binary search algorithm to find the target element. The standard binary search algorithm assumes the input array is sorted. We need to adjust it to handle the rotation.
4. **Determine the Sorted Half**: In each step of the binary search, determine which half of the array is sorted.
5. **Check if Target is in Sorted Half**: Check if the target element is within the range of the sorted half. If it is, continue the search in that half; otherwise, search in the other half.
6. **Repeat the Process**: Continue the binary search process until the target element is found or the search space is exhausted.

## Python Solution
```python
def search(nums: list[int], target: int) -> int:
    """
    Searches for a target element in a possibly rotated sorted array.

    Args:
    - nums: A list of integers sorted in ascending order but possibly rotated.
    - target: The target element to be searched.

    Returns:
    - The index of the target element if found; otherwise, -1.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the target is found, return its index
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # If the target is within the range of the left half, continue search there
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # If the target is within the range of the right half, continue search there
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    # If the target is not found, return -1
    return -1

# Test Cases
if __name__ == "__main__":
    test_cases = [
        {"nums": [4,5,6,7,0,1,2], "target": 0, "expected": 4},
        {"nums": [4,5,6,7,0,1,2], "target": 3, "expected": -1},
        {"nums": [1], "target": 0, "expected": -1},
        {"nums": [1], "target": 1, "expected": 0},
        {"nums": [2, 1], "target": 2, "expected": 0},
        {"nums": [3, 1], "target": 1, "expected": 1},
    ]
    
    for test_case in test_cases:
        result = search(test_case["nums"], test_case["target"])
        assert result == test_case["expected"], f"Expected {test_case['expected']} but got {result}"
        print(f"Test case passed: nums = {test_case['nums']}, target = {test_case['target']}, result = {result}")
```

## Time and Space Complexity Analysis
* **Time Complexity**: `O(log n)`, where `n` is the number of elements in the input array. This is because we are using a modified binary search algorithm that divides the search space in half at each step.
* **Space Complexity**: `O(1)`, as we are only using a constant amount of space to store the indices and the target element.

## Test Cases
The provided test cases cover various scenarios, including:
* A rotated array with the target element present.
* A rotated array with the target element not present.
* A non-rotated array (or an array rotated by 0 positions) with one element.
* Edge cases with small arrays.

These test cases help verify that the solution works correctly for different inputs and edge cases.