# unique_paths.md)
- 跳跃游戏 / Jump Game [LeetCode 55]

## Problem Description

**Problem Title:** Jump Game

**Description:**  
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

**Example 1:**  
**Input:** `nums = [2,3,1,1,4]`  
**Output:** `true`  
**Explanation:**  
Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**  
**Input:** `nums = [3,2,1,0,4]`  
**Output:** `false`  
**Explanation:**  
You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

**Constraints:**  
- `1 <= nums.length <= 10^4`  
- `0 <= nums[i] <= 10^5`

## Solution

### Explanation of the Problem
The problem is to determine if you can reach the last index of an array starting from the first index, where each element in the array represents the maximum number of steps you can jump forward from that position. For example, if you're at index `i` and `nums[i] = 3`, you can jump to index `i+1`, `i+2`, or `i+3`.

### Approach
The key insight is to keep track of the farthest index you can reach at any point in the array. Here's the step-by-step approach:

1. **Initialize the farthest reachable index**: Start with `max_reach = 0`, which represents the farthest index you can reach initially (before any jumps).
2. **Iterate through the array**: For each index `i` in the array:
   - If `i` exceeds `max_reach`, it means you cannot reach index `i` (and thus cannot reach the end), so return `false`.
   - Update `max_reach` to be the maximum of `max_reach` and `i + nums[i]` (the farthest you can jump from the current position).
   - If `max_reach` is already at or beyond the last index, return `true`.
3. **Final check**: If you finish the loop without returning, check if `max_reach` is at least the last index.

### Solution Code
```python
def canJump(nums):
    max_reach = 0
    n = len(nums)
    for i in range(n):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True
    return max_reach >= n - 1

# Test cases
print(canJump([2,3,1,1,4]))  # Output: True
print(canJump([3,2,1,0,4]))  # Output: False
print(canJump([0]))          # Output: True (already at the last index)
print(canJump([1,0,1,0]))    # Output: False
print(canJump([2,0,0]))      # Output: True
```

### Time and Space Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the array. We traverse the array once.
- **Space Complexity**: O(1), as we only use a constant amount of extra space (variables `max_reach` and `i`).

### Test Cases
1. **Example 1**: `nums = [2,3,1,1,4]`  
   - **Explanation**: From index 0, you can jump to index 1 or 2. Jumping to 1 allows a jump of 3 to reach the last index.  
   - **Expected Output**: `True`

2. **Example 2**: `nums = [3,2,1,0,4]`  
   - **Explanation**: No matter how you jump, you'll get stuck at index 3 (which has a jump value of 0).  
   - **Expected Output**: `False`

3. **Single Element**: `nums = [0]`  
   - **Explanation**: You're already at the last index.  
   - **Expected Output**: `True`

4. **Unreachable End**: `nums = [1,0,1,0]`  
   - **Explanation**: You can jump from index 0 to 1, but then you're stuck.  
   - **Expected Output**: `False`

5. **Reachable with Zero Jumps**: `nums = [2,0,0]`  
   - **Explanation**: From index 0, you can jump to index 2 directly.  
   - **Expected Output**: `True`

This approach efficiently checks reachability by dynamically updating the farthest index you can reach, ensuring optimal performance.