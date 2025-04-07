# unique_paths.md)
- 跳跃游戏 / Jump Game [LeetCode 55]

## Problem Description

## Jump Game
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

### Example 1:
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2:
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Constraints:
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`

## Solution

## Problem Explanation
The problem is to determine whether it's possible to reach the last index of a given integer array `nums` by jumping from the first index. Each element in the array represents the maximum jump length at that position.

## Step-by-Step Approach
1. **Understand the Problem**: We need to figure out if we can jump from the first index to the last index based on the jump lengths provided in the array.
2. **Identify the Key Insight**: The key insight here is that we don't need to actually jump to every index. Instead, we need to keep track of the maximum reachable index as we iterate through the array.
3. **Formulate the Approach**: We will iterate through the array from left to right. For each index, we check if it's within the maximum reachable index. If it is, we update the maximum reachable index if the current index plus its jump value is greater than the current maximum reachable index.
4. **Determine the Condition for Reaching the Last Index**: If at any point the maximum reachable index is greater than or equal to the last index of the array, we can return `True` because we've found a path to the last index.
5. **Handle the Case Where We Cannot Reach the Last Index**: If we finish iterating through the array and the maximum reachable index is still less than the last index, we return `False`.

## Python Solution
```python
def canJump(nums):
    """
    Determines whether it's possible to reach the last index of the given array by jumping from the first index.

    Args:
    nums (list): A list of integers where each element represents the maximum jump length at that position.

    Returns:
    bool: True if we can reach the last index, False otherwise.
    """
    max_reachable_index = 0
    for i, jump in enumerate(nums):
        # If the current index is beyond the max reachable index, return False
        if i > max_reachable_index:
            return False
        # Update the max reachable index
        max_reachable_index = max(max_reachable_index, i + jump)
    # If we've iterated through the entire array without returning False, we can reach the last index
    return True

# Test Cases
if __name__ == "__main__":
    # Example 1:
    nums = [2,3,1,1,4]
    print(canJump(nums))  # Expected Output: True
    
    # Example 2:
    nums = [3,2,1,0,4]
    print(canJump(nums))  # Expected Output: False
    
    # Additional Test Cases
    nums = [1]
    print(canJump(nums))  # Expected Output: True
    
    nums = [0]
    print(canJump(nums))  # Expected Output: True
    
    nums = [0,1]
    print(canJump(nums))  # Expected Output: False
    
    nums = [2,0,0]
    print(canJump(nums))  # Expected Output: True
```

## Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the `nums` array. This is because we make a single pass through the array.
- **Space Complexity**: O(1), as we only use a constant amount of space to store the `max_reachable_index` variable, regardless of the size of the input array.

## Test Cases
The provided Python solution includes several test cases to verify its correctness. These test cases cover various scenarios, including the examples given in the problem statement, as well as additional edge cases such as arrays with a single element, arrays starting with 0, and arrays where the jump is not possible to the last index.