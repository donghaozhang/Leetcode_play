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

