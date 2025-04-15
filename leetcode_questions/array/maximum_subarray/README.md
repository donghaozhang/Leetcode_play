# Maximum Subarray

## Problem Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Example
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

## Solutions
- [Problem Explanation](maximum_subarray.md) - Detailed explanation of the problem and different approaches
- [Implementation](maximum_subarray.py) - Python implementation with multiple approaches:
  - Kadane's Algorithm (O(n) time, O(1) space)
  - Divide and Conquer (O(n log n) time, O(log n) space)
  - Tracking Indices (Finding the exact subarray)

## Related Problems

- Maximum Circular Subarray 
- Maximum Product Subarray
- Maximum Subarray Sum with One Deletion

## Key Algorithms

- **Kadane's Algorithm** - A dynamic programming solution that finds the maximum subarray sum in O(n) time and O(1) space.
- **Divide and Conquer** - An alternative approach that divides the array into halves and finds the maximum subarray crossing the midpoint.

## LeetCode Link

[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## Examples

**Example 1:**

Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
Output: `6`
Explanation: The subarray `[4,-1,2,1]` has the largest sum 6.

**Example 2:**

Input: `nums = [1]`
Output: `1`
Explanation: The subarray `[1]` has the largest sum 1.

**Example 3:**

Input: `nums = [5,4,-1,7,8]`
Output: `23`
Explanation: The subarray `[5,4,-1,7,8]` has the largest sum 23.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Approach

This problem is solved using Kadane's algorithm, which is a dynamic programming approach. The algorithm maintains two variables: `current_sum` (the maximum sum ending at the current position) and `max_sum` (the maximum sum found so far). For each element, we decide whether to include it in the current subarray or start a new subarray beginning with this element.

Time Complexity: O(n)
Space Complexity: O(1)

## Related LeetCode Problem

This problem is equivalent to [LeetCode 53 - Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 