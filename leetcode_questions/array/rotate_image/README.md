# Rotate Image [LeetCode 48]

## Problem Overview
Rotate an n x n 2D matrix representing an image by 90 degrees clockwise in-place.

## Files
- [rotate_image.py](rotate_image.py) - Implementation of the solution
- [rotate_image.md](rotate_image.md) - Detailed explanation of the problem and solution

## Quick Example
```
Input:          Output:
1 2 3           7 4 1
4 5 6     →     8 5 2
7 8 9           9 6 3
```

## Solution Approach
The problem is solved in two steps:

1. Transpose the matrix (swap elements across the main diagonal)
2. Reverse each row of the transposed matrix

This approach allows us to rotate the matrix in-place without allocating additional space.

## Time and Space Complexity
- Time Complexity: O(n²) - Each element is visited a constant number of times
- Space Complexity: O(1) - The rotation is performed in-place

## LeetCode Link
[Rotate Image - LeetCode Problem 48](https://leetcode.com/problems/rotate-image/) 