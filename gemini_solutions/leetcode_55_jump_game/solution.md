# unique_paths.md)
- 跳跃游戏 / Jump Game [LeetCode 55]

## Problem Description

```markdown
## 55. Jump Game

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

**Example 1:**

**Input:** nums = [2,3,1,1,4]
**Output:** true
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

**Input:** nums = [3,2,1,0,4]
**Output:** false
**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

**Constraints:**

*   `1 <= nums.length <= 10^4`
*   `0 <= nums[i] <= 10^5`
```

## Solution

Okay, let's break down the Jump Game problem (LeetCode 55).

**1. Explanation of the Problem**

You're given an array `nums` where each element `nums[i]` represents the *maximum* number of steps you can jump forward from that position (index `i`). You start at the first index (index 0). The goal is to determine if you can reach the very last index of the array by making a sequence of valid jumps. You can choose to jump fewer steps than the maximum allowed at any position.

**Example:**
*   `nums = [2, 3, 1, 1, 4]`
    *   Start at index 0 (`nums[0] = 2`). You can jump 1 step (to index 1) or 2 steps (to index 2).
    *   If you jump to index 1 (`nums[1] = 3`), you can jump 1, 2, or 3 steps. Jumping 3 steps takes you to index 1 + 3 = 4, which is the last index. So, it's possible. Output: `true`.
*   `nums = [3, 2, 1, 0, 4]`
    *   Start at index 0 (`nums[0] = 3`). You can jump to index 1, 2, or 3.
    *   No matter which path you take (e.g., 0 -> 1 -> 3, or 0 -> 2 -> 3, or 0 -> 3), you will eventually land on index 3.
    *   At index 3, `nums[3] = 0`. You cannot jump anywhere from here. You are stuck and cannot reach the last index (index 4). Output: `false`.

**2. Step-by-Step Approach (Greedy Algorithm)**

The most efficient way to solve this problem is using a greedy approach. The core idea is to keep track of the farthest index you can possibly reach at any point as you iterate through the array.

1.  **Initialization:**
    *   Let `n` be the length of the `nums` array.
    *   Initialize a variable `max_reach = 0`. This variable will store the maximum index we can reach from the starting position (index 0) or any index visited so far.

2.  **Iteration:**
    *   Iterate through the array with an index `i` from 0 up to `n - 1`.
    *   **Reachability Check:** At each index `i`, first check if `i > max_reach`.
        *   If `i` is greater than `max_reach`, it means the current index `i` is beyond the farthest point we could possibly reach based on previous jumps. Therefore, we are stuck and cannot reach index `i`, let alone the end of the array. Return `false`.
    *   **Update Maximum Reach:** If the current index `i` is reachable (i.e., `i <= max_reach`), calculate the potential new maximum reach from this position: `i + nums[i]`. Update `max_reach` to be the maximum of its current value and this new potential reach: `max_reach = max(max_reach, i + nums[i])`. This ensures `max_reach` always holds the farthest index accessible from the start up to the current index `i`.
    *   **Early Exit (Optimization):** After updating `max_reach`, check if `max_reach >= n - 1`.
        *   If `max_reach` is greater than or equal to the last index (`n - 1`), it means we have found a way to reach or surpass the end of the array. We can immediately return `true`.

3.  **Completion:**
    *   If the loop finishes without returning `false` (meaning we never got stuck) and without the early exit `return true` being triggered (which it logically should if the end is reachable), it implies that we successfully processed all indices up to `n-1` while always maintaining `i <= max_reach`. This inherently means the last index was reachable. The `return true` inside the loop optimization correctly handles all successful cases. For completeness, if the loop structure allowed exiting without returning, the logical conclusion would be `true`.

**3. Python Solution**

```python
import unittest
from typing import List

class Solution:
    """
    Solves the Jump Game problem using a greedy approach.
    Keeps track of the maximum index reachable so far.
    """
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if the last index of the array can be reached starting from index 0.

        Args:
            nums: A list of non-negative integers representing maximum jump lengths.

        Returns:
            True if the last index is reachable, False otherwise.
        """
        n = len(nums)
        # Constraints state n >= 1, so no need to check for n == 0 explicitly.
        # If n == 1, the loop runs once for i=0, max_reach becomes nums[0] >= 0 (n-1), returns True.

        max_reach = 0 # The farthest index reachable so far.

        for i in range(n):
            # If the current index 'i' is greater than the farthest index
            # we could reach up to the previous step, then 'i' is unreachable.
            if i > max_reach:
                return False 
            
            # Update the farthest index reachable by considering the jump from 'i'.
            max_reach = max(max_reach, i + nums[i])
            
            # Optimization: If our maximum reach already includes or surpasses
            # the last index, we know it's possible to reach the end.
            if max_reach >= n - 1:
                return True
                
        # This line is theoretically unreachable for n >= 1 because the loop
        # will either return False if stuck, or return True once max_reach
        # covers the last index. If n=1, it returns True in the first iteration.
        # If the problem allowed n=0, this might be needed.
        # Based on the logic, if the loop could somehow complete without returning,
        # it would imply the end was reached.
        return True # Logically consistent, though unreachable given loop structure and n>=1.

```

**Complexity Analysis:**

*   **Time Complexity:** O(n), where n is the number of elements in the `nums` array. We iterate through the array at most once.
*   **Space Complexity:** O(1). We only use a few extra variables (`n`, `max_reach`, `i`), regardless of the input size.

**4. Test Cases**

```python
# Test Suite
class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]), "Test Case 1 Failed: Example 1")

    def test_example2(self):
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]), "Test Case 2 Failed: Example 2")

    def test_single_zero(self):
        # Start and end at index 0, which is reachable.
        self.assertTrue(self.solution.canJump([0]), "Test Case 3 Failed: Single Zero") 

    def test_single_non_zero(self):
        # Start and end at index 0, which is reachable.
        self.assertTrue(self.solution.canJump([1]), "Test Case 4 Failed: Single Non-Zero") 

    def test_stuck_at_start(self):
        # From index 0, max jump is 0. Cannot move. Last index (1) is unreachable.
        self.assertFalse(self.solution.canJump([0, 1]), "Test Case 5 Failed: Stuck at Start")

    def test_simple_jump_to_end(self):
        # From index 0, jump 1 step to index 1 (last index).
        self.assertTrue(self.solution.canJump([1, 0]), "Test Case 6 Failed: Simple Jump to End")

    def test_jump_over_zero(self):
        # From index 0, can jump 2 steps to index 2 (last index).
        self.assertTrue(self.solution.canJump([2, 0, 0]), "Test Case 7 Failed: Jump Over Zero")

    def test_all_ones(self):
        # Can always jump 1 step forward, eventually reaching the end.
        self.assertTrue(self.solution.canJump([1, 1, 1, 1]), "Test Case 8 Failed: All Ones")

    def test_blocked_by_zero(self):
        # 0 -> 1 -> 2. At index 2, nums[2]=0. Cannot jump further. Last index (3) unreachable.
        self.assertFalse(self.solution.canJump([1, 1, 0, 1]), "Test Case 9 Failed: Blocked by Zero")
        
    def test_long_jump_sufficient(self):
        # From index 0, can jump up to 5 steps. Can directly reach index 5 (last index).
        self.assertTrue(self.solution.canJump([5, 0, 0, 0, 0, 0]), "Test Case 10 Failed: Long Jump Sufficient")

    def test_cannot_reach_end_complex(self):
        # 0 -> 1. At index 1, nums[1]=0. Stuck. Cannot reach index 2 or 3.
        self.assertFalse(self.solution.canJump([1, 0, 1, 0]), "Test Case 11 Failed: Cannot Reach End Complex")

    def test_large_input_true(self):
        # Array of 10000 ones, should be able to reach the end.
        self.assertTrue(self.solution.canJump([1] * 10000), "Test Case 12 Failed: Large Input True")

    def test_large_input_true_with_zero(self):
        # Array of 9999 ones followed by zero. Can reach the last index.
        self.assertTrue(self.solution.canJump([1] * 9999 + [0]), "Test Case 13 Failed: Large Input True w/ Zero")

    def test_large_input_false(self):
        # Blocked by a zero partway through.
        nums = [1] * 5000 + [0] + [1] * 4999
        self.assertFalse(self.solution.canJump(nums), "Test Case 14 Failed: Large Input False")

# To run the tests (e.g., save as 'test_jump_game.py' and run 'python -m unittest test_jump_game.py')
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```