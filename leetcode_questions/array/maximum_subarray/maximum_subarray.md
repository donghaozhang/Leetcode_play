# Maximum Subarray

## Problem Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A **subarray** is a contiguous part of an array.

## Examples

**Example 1:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Example 2:**
```
Input: nums = [1]
Output: 1
```

**Example 3:**
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Approaches

### 1. Kadane's Algorithm (Dynamic Programming)

Kadane's algorithm is a dynamic programming approach that efficiently solves the Maximum Subarray problem in O(n) time.

#### Key Idea
The algorithm maintains two variables:
1. `max_ending_here`: the maximum sum of a subarray ending at the current position
2. `max_so_far`: the maximum sum seen so far (the answer we're looking for)

At each position, we have two choices:
- Start a new subarray at the current element
- Extend the existing subarray by including the current element

#### Implementation

```python
def max_subarray_kadane(nums):
    if not nums:
        return 0
        
    max_so_far = nums[0]
    max_ending_here = nums[0]
    
    for i in range(1, len(nums)):
        # Choose between extending previous subarray or starting new one
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        # Update global maximum
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far
```

#### Time and Space Complexity
- Time Complexity: O(n) where n is the length of the array
- Space Complexity: O(1) as we only use a constant amount of extra space

### 2. Divide and Conquer Approach

The divide and conquer approach splits the array into halves, finds the maximum subarray in each half, and also finds the maximum subarray that crosses the middle. The result is the maximum of these three possibilities.

#### Key Idea
For any subarray, the maximum sum subarray must be one of:
1. Entirely in the left half
2. Entirely in the right half
3. Crossing the middle (parts in both left and right halves)

#### Implementation

```python
def max_subarray_divide_conquer(nums):
    if not nums:
        return 0
        
    def max_crossing_subarray(nums, left, mid, right):
        # Find maximum subarray ending at mid (left part)
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
            
        # Find maximum subarray starting at mid+1 (right part)
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
            
        # Return sum of best left and right parts
        return left_sum + right_sum
    
    def divide_conquer(nums, left, right):
        # Base case: single element
        if left == right:
            return nums[left]
            
        mid = (left + right) // 2
        
        # Case 1: Maximum subarray in left half
        left_max = divide_conquer(nums, left, mid)
        
        # Case 2: Maximum subarray in right half
        right_max = divide_conquer(nums, mid + 1, right)
        
        # Case 3: Maximum subarray crossing midpoint
        cross_max = max_crossing_subarray(nums, left, mid, right)
        
        # Return the maximum of the three
        return max(left_max, right_max, cross_max)
    
    return divide_conquer(nums, 0, len(nums) - 1)
```

#### Time and Space Complexity
- Time Complexity: O(n log n) due to the recursive calls
- Space Complexity: O(log n) for the recursion stack

### 3. Tracking Indices of the Maximum Subarray

This extension of Kadane's algorithm tracks the start and end indices of the maximum subarray.

#### Implementation

```python
def max_subarray_with_indices(nums):
    if not nums:
        return 0, -1, -1
        
    max_so_far = nums[0]
    max_ending_here = nums[0]
    start = 0
    end = 0
    current_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > max_ending_here + nums[i]:
            # Start a new subarray
            max_ending_here = nums[i]
            current_start = i
        else:
            # Extend the existing subarray
            max_ending_here = max_ending_here + nums[i]
            
        if max_ending_here > max_so_far:
            # Update the best subarray found so far
            max_so_far = max_ending_here
            start = current_start
            end = i
            
    return max_so_far, start, end
```

## Follow-up Questions

1. **Can you implement a solution with O(n) time complexity?**
   - Yes, Kadane's algorithm achieves O(n) time complexity.

2. **What if the array contains all negative numbers?**
   - The algorithm will work correctly and return the maximum (which will be the least negative number).

3. **What if we need to handle an empty array?**
   - We can return 0 for an empty array or throw an exception, depending on requirements.

## Related Problems

- Maximum Circular Subarray
- Maximum Product Subarray
- Longest Increasing Subsequence 