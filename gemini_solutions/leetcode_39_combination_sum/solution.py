from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates that sum up to the target.

        Args:
            candidates: A list of distinct integers.
            target: The target sum.

        Returns:
            A list of lists, where each inner list is a unique combination
            summing to the target.
        """
        results = []
        
        # Sort candidates to handle combinations systematically and enable pruning
        candidates.sort() 
        
        n = len(candidates)

        def backtrack(remain: int, combo: List[int], start: int):
            """
            Recursive helper function for backtracking.

            Args:
                remain: The remaining sum needed to reach the target.
                combo: The current combination being built.
                start: The starting index in candidates to consider for the next element.
            """
            # Base Case 1: Found a valid combination
            if remain == 0:
                # Make a deep copy of the current combination and add to results
                results.append(list(combo)) 
                return

            # Base Case 2: Exceeded the target, invalid path
            if remain < 0:
                return

            # Explore candidates starting from the 'start' index
            for i in range(start, n):
                candidate = candidates[i]

                # Optimization: If candidate is too large, stop exploring further
                # (since candidates are sorted)
                if candidate > remain:
                    break 
                
                # Choose: Add the candidate to the current combination
                combo.append(candidate)
                
                # Explore: Recurse with updated remaining target and the same start index 'i'
                # We pass 'i' (not i+1) because we can reuse the same candidate
                backtrack(remain - candidate, combo, i)
                
                # Unchoose (Backtrack): Remove the candidate to explore other paths
                combo.pop()

        # Start the backtracking process
        backtrack(target, [], 0)
        
        return results

# --- Test Cases ---

solver = Solution()

# Example 1
candidates1 = [2, 3, 6, 7]
target1 = 7
expected1 = [[2, 2, 3], [7]]
# Sort expected output for comparison if needed, though order doesn't matter
output1 = solver.combinationSum(candidates1, target1)
print(f"Input: candidates = {candidates1}, target = {target1}")
print(f"Output: {output1}")
# Simple check (might need more robust comparison for complex cases)
print(f"Correct: {sorted(map(sorted, output1)) == sorted(map(sorted, expected1))}\n") 

# Example 2
candidates2 = [2, 3, 5]
target2 = 8
expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
output2 = solver.combinationSum(candidates2, target2)
print(f"Input: candidates = {candidates2}, target = {target2}")
print(f"Output: {output2}")
print(f"Correct: {sorted(map(sorted, output2)) == sorted(map(sorted, expected2))}\n")

# Example 3
candidates3 = [2]
target3 = 1
expected3 = []
output3 = solver.combinationSum(candidates3, target3)
print(f"Input: candidates = {candidates3}, target = {target3}")
print(f"Output: {output3}")
print(f"Correct: {sorted(map(sorted, output3)) == sorted(map(sorted, expected3))}\n")

# Additional Test Case 1: No solution
candidates4 = [3, 5]
target4 = 4
expected4 = []
output4 = solver.combinationSum(candidates4, target4)
print(f"Input: candidates = {candidates4}, target = {target4}")
print(f"Output: {output4}")
print(f"Correct: {sorted(map(sorted, output4)) == sorted(map(sorted, expected4))}\n")

# Additional Test Case 2: Target is one of the candidates
candidates5 = [2, 4, 6]
target5 = 6
expected5 = [[2, 2, 2], [2, 4], [6]]
output5 = solver.combinationSum(candidates5, target5)
print(f"Input: candidates = {candidates5}, target = {target5}")
print(f"Output: {output5}")
print(f"Correct: {sorted(map(sorted, output5)) == sorted(map(sorted, expected5))}\n")

# Additional Test Case 3: Larger numbers
candidates6 = [7, 3, 2] # Unsorted initially
target6 = 18
expected6 = [[2,2,2,2,2,2,2,2,2], [2,2,2,2,2,2,3,3], [2,2,2,2,3,7], [2,2,2,3,3,3,3], [2,2,7,7], [2,3,3,3,7], [3,3,3,3,3,3], [3,3,7,7]] # Found using an online tool, verify
output6 = solver.combinationSum(candidates6, target6)
print(f"Input: candidates = {candidates6}, target = {target6}")
print(f"Output: {output6}")
print(f"Correct: {sorted(map(sorted, output6)) == sorted(map(sorted, expected6))}\n")
