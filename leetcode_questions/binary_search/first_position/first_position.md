# First Position of Target

## Description
Find the first position of the target value in a sorted array. Return -1 if the target does not exist.

## Example
Input: nums = [1, 2, 3, 3, 3, 4, 5], target = 3
Output: 2 (The first position of 3)

## Solution
Use a variant of binary search:
1. Initialize left and right pointers
2. Use the method of exiting when the left and right pointers are adjacent
3. When the middle value is greater than or equal to the target value, shrink the right boundary
4. Finally check the left and right boundaries

### Complexity Analysis
- Time complexity: O(log n)
- Space complexity: O(1)

## Key Points for Code Implementation
1. Use left + 1 < right as the loop condition
2. Correctly handle boundary conditions
3. Check the left boundary first and then the right boundary
4. Handle the case where the target value does not exist
