# 3Sum [LeetCode 15]

## Problem Overview
Given an array of integers, find all unique triplets that sum to zero.

## Files
- [three_sum.py](three_sum.py) - Implementation of the solution
- [three_sum.md](three_sum.md) - Detailed explanation of the problem and solution

## Quick Example
```
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Solution Approach
We use a sorting-based two-pointer technique to efficiently find all valid triplets:

1. Sort the array
2. For each potential first element, use two pointers to find pairs that complete the triplet
3. Handle duplicates by skipping repeated values
4. Use the sorted nature of the array to optimize the search

## Time and Space Complexity
- Time Complexity: O(n²) - where n is the length of the input array
- Space Complexity: O(1) - excluding the output array

## LeetCode Link
[3Sum - LeetCode Problem 15](https://leetcode.com/problems/3sum/) 