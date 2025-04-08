# bst_iterator.md)
- 全排列 / Permutations [LeetCode 46]

## Problem Description

## 46. Permutations

**Medium**

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

**Example 2:**

**Input:** nums = [0,1]
**Output:** [[0,1],[1,0]]

**Example 3:**

**Input:** nums = [1]
**Output:** [[1]]

**Constraints:**

*   `1 <= nums.length <= 6`
*   `-10 <= nums[i] <= 10`
*   All the integers of `nums` are **unique**.

## Solution

Okay, let's break down the LeetCode problem "Permutations" (Number 46).

## 1. Explanation of the Problem

The problem asks us to find all possible unique orderings (permutations) of a given list of distinct integers. For example, if the input is `[1, 2, 3]`, we need to generate all the ways these three numbers can be arranged: `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`. The input numbers are guaranteed to be unique.

## 2. Step-by-Step Approach

This problem is a classic example where **backtracking** is a suitable algorithm. Backtracking involves exploring all possible candidates and abandoning ("backtracking") a path as soon as it's determined that it cannot lead to a valid solution.

Here's how we can apply backtracking to generate permutations:

1.  **Initialization:**
    *   Start with an empty current permutation.
    *   Keep track of which numbers from the input array `nums` have already been used in the current permutation. A boolean array `used` of the same size as `nums` is efficient for this.
    *   Maintain a list `results` to store all the complete permutations found.

2.  **Recursive Function (Backtrack Helper):**
    *   **Base Case:** If the length of the `current_permutation` equals the length of the original `nums` array, it means we have formed a complete permutation. Add a *copy* of the `current_permutation` to the `results` list and return.
    *   **Recursive Step:** Iterate through each number `nums[i]` in the original input array.
        *   **Check:** If `nums[i]` has *not* been used yet (i.e., `used[i]` is `False`):
            *   **Choose:** Mark `nums[i]` as used (`used[i] = True`) and add it to the `current_permutation`.
            *   **Explore:** Make a recursive call to the backtrack function to continue building the permutation from this new state.
            *   **Unchoose (Backtrack):** After the recursive call returns (meaning all permutations starting with the current prefix have been explored), undo the choice. Remove `nums[i]` from the `current_permutation` (`current_permutation.pop()`) and mark it as unused (`used[i] = False`). This allows us to explore other possibilities where `nums[i]` is placed later in the permutation or not used at the current level.

3.  **Final Result:** After the initial call to the backtrack function completes, the `results` list will contain all possible permutations. Return `results`.

**Example Walkthrough (`nums = [1, 2, 3]`):**

```
permute([1, 2, 3])
  backtrack(current=[], used=[F, F, F])
    i = 0 (num = 1): used[0]=T, current=[1]
      backtrack(current=[1], used=[T, F, F])
        i = 0 (num = 1): used[0] is T, skip
        i = 1 (num = 2): used[1]=T, current=[1, 2]
          backtrack(current=[1, 2], used=[T, T, F])
            i = 0 (num = 1): used[0] is T, skip
            i = 1 (num = 2): used[1] is T, skip
            i = 2 (num = 3): used[2]=T, current=[1, 2, 3]
              backtrack(current=[1, 2, 3], used=[T, T, T])
                len(current) == 3 -> Base Case! Add [1, 2, 3] to results. Return.
            current.pop() -> [1, 2], used[2]=F
          Return.
        current.pop() -> [1], used[1]=F
        i = 2 (num = 3): used[2]=T, current=[1, 3]
          backtrack(current=[1, 3], used=[T, F, T])
            i = 0 (num = 1): used[0] is T, skip
            i = 1 (num = 2): used[1]=F, used[1]=T, current=[1, 3, 2]
              backtrack(current=[1, 3, 2], used=[T, T, T])
                len(current) == 3 -> Base Case! Add [1, 3, 2] to results. Return.
            current.pop() -> [1, 3], used[1]=F
            i = 2 (num = 3): used[2] is T, skip
          Return.
        current.pop() -> [1], used[2]=F
      Return.
    current.pop() -> [], used[0]=F
    i = 1 (num = 2): used[1]=T, current=[2]
      backtrack(current=[2], used=[F, T, F])
        ... (generates [2, 1, 3] and [2, 3, 1]) ...
    current.pop() -> [], used[1]=F
    i = 2 (num = 3): used[2]=T, current=[3]
      backtrack(current=[3], used=[F, F, T])
        ... (generates [3, 1, 2] and [3, 2, 1]) ...
    current.pop() -> [], used[2]=F
  Return results.
```

## 3. Python Solution

```python
from typing import List

class Solution:
    """
    Solves the Permutations problem using backtracking.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the input list nums.

        Args:
            nums: A list of distinct integers.

        Returns:
            A list of lists, where each inner list is a permutation of nums.
        """
        results = []
        n = len(nums)
        current_permutation = []
        used = [False] * n  # Track used elements by index

        def backtrack():
            """Helper function for recursion."""
            # Base Case: If the current permutation is complete
            if len(current_permutation) == n:
                # Add a copy of the current permutation to results
                # Must be a copy because current_permutation is modified during backtracking
                results.append(current_permutation.copy())
                return

            # Recursive Step: Try adding each unused number
            for i in range(n):
                if not used[i]:
                    # Choose: Mark the number as used and add it to the permutation
                    used[i] = True
                    current_permutation.append(nums[i])

                    # Explore: Recursively call backtrack for the next position
                    backtrack()

                    # Unchoose (Backtrack): Remove the number and mark it as unused
                    # This prepares for exploring other possibilities
                    current_permutation.pop()
                    used[i] = False

        # Start the backtracking process
        backtrack()
        return results

# --- Test Cases ---

solver = Solution()

# Example 1
nums1 = [1, 2, 3]
output1 = solver.permute(nums1)
print(f"Input: {nums1}")
print(f"Output: {output1}")
# Expected: A list containing [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] (order may vary)
# Check if the output contains the expected permutations
expected1_set = {tuple(p) for p in [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]}
output1_set = {tuple(p) for p in output1}
assert expected1_set == output1_set
print("-" * 20)

# Example 2
nums2 = [0, 1]
output2 = solver.permute(nums2)
print(f"Input: {nums2}")
print(f"Output: {output2}")
# Expected: A list containing [[0,1],[1,0]] (order may vary)
expected2_set = {tuple(p) for p in [[0,1],[1,0]]}
output2_set = {tuple(p) for p in output2}
assert expected2_set == output2_set
print("-" * 20)

# Example 3
nums3 = [1]
output3 = solver.permute(nums3)
print(f"Input: {nums3}")
print(f"Output: {output3}")
# Expected: [[1]]
expected3_set = {tuple(p) for p in [[1]]}
output3_set = {tuple(p) for p in output3}
assert expected3_set == output3_set
print("-" * 20)

# Additional Test Case
nums4 = [] # Although constraints say n>=1, let's test
output4 = solver.permute(nums4)
print(f"Input: {nums4}")
print(f"Output: {output4}")
# Expected: [[]] (One permutation of an empty list is an empty list)
expected4_set = {tuple(p) for p in [[]]}
output4_set = {tuple(p) for p in output4}
assert expected4_set == output4_set
print("-" * 20)

nums5 = [5, 4]
output5 = solver.permute(nums5)
print(f"Input: {nums5}")
print(f"Output: {output5}")
# Expected: A list containing [[5,4],[4,5]] (order may vary)
expected5_set = {tuple(p) for p in [[5,4],[4,5]]}
output5_set = {tuple(p) for p in output5}
assert expected5_set == output5_set
print("-" * 20)

```

**Complexity Analysis:**

*   **Time Complexity:** O(N * N!)
    *   There are N! possible permutations for a list of N distinct elements.
    *   For each permutation, we perform O(N) work:
        *   The recursion depth is N.
        *   At each level of recursion, the loop runs N times. Inside the loop, operations (checking `used`, appending, popping) take roughly constant time.
        *   When a permutation is complete (at a leaf node of the recursion tree), copying the `current_permutation` to `results` takes O(N) time. Since there are N! leaf nodes, this copying contributes O(N * N!).
    *   The total number of nodes in the implicit recursion tree is roughly the sum of P(N, k) for k from 0 to N, which is related to N!. The work done at each node involves an O(N) loop. So the exploration part is also roughly O(N * N!).
    *   Therefore, the overall time complexity is dominated by generating and storing the permutations, resulting in O(N * N!).

*   **Space Complexity:** O(N * N!)
    *   **Output Storage (`results`):** We need to store N! permutations, each of length N. This requires O(N * N!) space.
    *   **Auxiliary Space:**
        *   `current_permutation`: Stores up to N elements, O(N).
        *   `used` array: Stores N boolean values, O(N).
        *   Recursion Call Stack: The maximum depth of the recursion is N, so the stack uses O(N) space.
    *   The space required for the output `results` dominates the auxiliary space. Thus, the total space complexity is O(N * N!). If the problem statement asks for space complexity *excluding* the output, it would be O(N).

## 4. Test Cases

Included above within the Python solution block are test cases covering:
*   The examples provided in the problem description (`[1, 2, 3]`, `[0, 1]`, `[1]`).
*   An edge case (empty list `[]`, although the constraints specify `n >= 1`, the code handles it correctly).
*   Another simple case (`[5, 4]`).

The assertions `assert expected_set == output_set` are used to verify the correctness by comparing the set of generated permutations (converted to tuples to be hashable for set inclusion) against the set of expected permutations. This handles the fact that the order of permutations in the output list doesn't matter.