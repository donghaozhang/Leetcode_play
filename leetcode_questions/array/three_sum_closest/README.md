# 3Sum Closest [LeetCode 16]

## Problem Overview
Given an array of integers and a target value, find three integers in the array that sum closest to the target.

## Files
- [three_sum_closest.py](three_sum_closest.py) - Implementation of the solution
- [three_sum_closest.md](three_sum_closest.md) - Detailed explanation of the problem and solution

## Quick Example
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum of [-1,2,1] is 2, which is closest to target 1.
```

## Solution Approach
We use a sorting-based two-pointer technique to efficiently find the closest sum:

1. Sort the array
2. For each potential first element, use two pointers to find the other two elements
3. Track the sum that is closest to the target
4. Early termination if we find an exact match to the target

## Time and Space Complexity
- Time Complexity: O(n²) - where n is the length of the input array
- Space Complexity: O(1) - excluding space used by the sorting algorithm

## LeetCode Link
[3Sum Closest - LeetCode Problem 16](https://leetcode.com/problems/3sum-closest/) 