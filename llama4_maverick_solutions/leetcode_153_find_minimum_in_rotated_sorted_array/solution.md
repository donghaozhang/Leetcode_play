# k_closest_elements.md)
- 旋转排序数组中的最小值 / Find Minimum in Rotated Sorted Array [LeetCode 153]

## Problem Description

## Problem Description

### Find Minimum in Rotated Sorted Array

Suppose an array of distinct numbers sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

#### Example 1:

```
Input: [3,4,5,1,2] 
Output: 1
```

#### Example 2:

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

#### Example 3:

```
Input: [1]
Output: 1
```

#### Example 4:

```
Input: [2,1]
Output: 1
```

#### Constraints:

* `1 <= nums.length <= 5000`
* `-5000 <= nums[i] <= 5000`
* All the integers of `nums` are **unique**.
* `nums` was sorted in ascending order and rotated at some pivot.

## Solution

## Problem Explanation

The problem "Find Minimum in Rotated Sorted Array" requires finding the minimum element in a sorted array that has been rotated at some unknown pivot. The input array is a list of distinct integers sorted in ascending order, which has been rotated. The task is to identify the minimum element in this rotated array.

Key constraints and edge cases:

* The array contains distinct integers.
* The array is sorted in ascending order before rotation.
* The array has been rotated at some unknown pivot.
* The length of the array is between 1 and 5000 (inclusive).
* The integers in the array are within the range -5000 to 5000 (inclusive).
* There are no duplicates in the array.

Input: A list of integers representing the rotated sorted array.
Output: The minimum element in the array.

Subtle requirements or implicit constraints:

* The array is rotated at some pivot, which means that the rotation can occur at any position in the array.
* The problem assumes that the input array is a valid rotated sorted array.

## Step-by-Step Approach

To solve this problem, we can use a modified binary search algorithm. Here's a step-by-step breakdown of the approach:

1. **Initialize two pointers**: We start by initializing two pointers, `left` and `right`, to the beginning and end of the array, respectively.
2. **Check if the array is rotated**: We check if the array is rotated by comparing the first and last elements. If the first element is less than the last element, the array is not rotated, and we can return the first element as the minimum.
3. **Perform binary search**: We perform a binary search on the array. At each step, we calculate the midpoint `mid` and compare the element at `mid` with the element at `right`.
4. **Determine which half to continue searching**: If the element at `mid` is greater than the element at `right`, we know that the minimum element must be in the right half of the array, so we update `left` to `mid + 1`. Otherwise, we update `right` to `mid`.
5. **Repeat the process**: We repeat steps 3 and 4 until `left` and `right` converge to a single element, which is the minimum element in the array.

## Python Solution

```python
def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.

    Args:
    nums (list): A list of integers representing the rotated sorted array.

    Returns:
    int: The minimum element in the array.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Test cases
print(findMin([3, 4, 5, 1, 2]))  # Output: 1
print(findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(findMin([1]))  # Output: 1
print(findMin([2, 1]))  # Output: 1
print(findMin([5, 1, 2, 3, 4]))  # Output: 1
print(findMin([1, 2, 3, 4, 5]))  # Output: 1
```

## Time and Space Complexity Analysis

* **Time complexity**: The time complexity of this solution is O(log n), where n is the length of the input array. This is because we are using a binary search algorithm, which reduces the search space by half at each step.
* **Space complexity**: The space complexity of this solution is O(1), as we are only using a constant amount of space to store the `left`, `right`, and `mid` indices.

## Test Cases

The provided test cases cover various scenarios, including:

* Rotated arrays with the minimum element at different positions.
* Arrays with a single element.
* Arrays that are not rotated (i.e., the minimum element is at the beginning).

These test cases help verify that the solution works correctly for different inputs.