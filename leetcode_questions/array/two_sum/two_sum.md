# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Solution Approach
We can solve this problem efficiently using a hash map to track the elements we've seen.

1. Create an empty hash map
2. Iterate through the array
3. For each element:
   - Calculate the complement (target - current number)
   - If the complement is in the hash map, return the indices
   - Otherwise, add the current number and its index to the hash map

### Time Complexity: O(n)
### Space Complexity: O(n)

## Follow-up
Can you come up with an algorithm that is less than O(n²) time complexity?

The hash map approach already achieves O(n) time complexity, which is better than the naive O(n²) solution of checking every pair of numbers. 