import math # Not strictly needed, but good practice

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Searches for a target value in an m x n matrix with sorted rows
        and the first element of each row greater than the last of the previous row.

        Args:
            matrix: The m x n integer matrix.
            target: The integer value to search for.

        Returns:
            True if the target is found, False otherwise.
        """
        # Handle edge cases: empty matrix or matrix with empty rows
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # Initialize binary search boundaries for the conceptual 1D array
        low = 0
        high = m * n - 1 # Index of the last element

        while low <= high:
            # Calculate the middle index in the conceptual 1D array
            # Using low + (high - low) // 2 prevents potential integer overflow
            mid_idx = low + (high - low) // 2

            # Convert the 1D index back to 2D matrix coordinates
            row = mid_idx // n
            col = mid_idx % n

            # Get the value at the middle position
            mid_val = matrix[row][col]

            # Perform comparison
            if mid_val == target:
                return True  # Target found
            elif mid_val < target:
                # Target is in the upper half (larger values)
                low = mid_idx + 1
            else: # mid_val > target
                # Target is in the lower half (smaller values)
                high = mid_idx - 1

        # Target not found after the loop finishes
        return False

# --- Test Cases ---
solver = Solution()

# Example 1
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(f"Matrix: {matrix1}, Target: {target1}, Found: {solver.searchMatrix(matrix1, target1)}") # Expected: True

# Example 2
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(f"Matrix: {matrix2}, Target: {target2}, Found: {solver.searchMatrix(matrix2, target2)}") # Expected: False

# Custom Test Cases
# Target at the beginning
target3 = 1
print(f"Matrix: {matrix1}, Target: {target3}, Found: {solver.searchMatrix(matrix1, target3)}") # Expected: True

# Target at the end
target4 = 60
print(f"Matrix: {matrix1}, Target: {target4}, Found: {solver.searchMatrix(matrix1, target4)}") # Expected: True

# Target in the middle
target5 = 11
print(f"Matrix: {matrix1}, Target: {target5}, Found: {solver.searchMatrix(matrix1, target5)}") # Expected: True

# Target smaller than min
target6 = 0
print(f"Matrix: {matrix1}, Target: {target6}, Found: {solver.searchMatrix(matrix1, target6)}") # Expected: False

# Target larger than max
target7 = 70
print(f"Matrix: {matrix1}, Target: {target7}, Found: {solver.searchMatrix(matrix1, target7)}") # Expected: False

# Target between rows but not present
target8 = 8
print(f"Matrix: {matrix1}, Target: {target8}, Found: {solver.searchMatrix(matrix1, target8)}") # Expected: False

# Single row matrix
matrix9 = [[1, 2, 3, 4]]
target9 = 3
print(f"Matrix: {matrix9}, Target: {target9}, Found: {solver.searchMatrix(matrix9, target9)}") # Expected: True

# Single column matrix
matrix10 = [[1], [10], [23]]
target10 = 10
print(f"Matrix: {matrix10}, Target: {target10}, Found: {solver.searchMatrix(matrix10, target10)}") # Expected: True

# Single element matrix (found)
matrix11 = [[5]]
target11 = 5
print(f"Matrix: {matrix11}, Target: {target11}, Found: {solver.searchMatrix(matrix11, target11)}") # Expected: True

# Single element matrix (not found)
matrix12 = [[5]]
target12 = 6
print(f"Matrix: {matrix12}, Target: {target12}, Found: {solver.searchMatrix(matrix12, target12)}") # Expected: False

# Empty matrix
matrix13 = []
target13 = 1
print(f"Matrix: {matrix13}, Target: {target13}, Found: {solver.searchMatrix(matrix13, target13)}") # Expected: False

# Matrix with empty row (handled by initial check)
matrix14 = [[]]
target14 = 1
# Note: This case technically violates constraints (1 <= n), but the code handles it.
# If the constraints were strictly followed, this test wouldn't be needed.
# Let's assume valid inputs per constraints, but the check is robust.
# If matrix = [[]] was possible, the check `if not matrix or not matrix[0]:` would catch it.
# For a valid matrix like [[1],[2]], target = 0:
matrix15 = [[1],[2]]
target15 = 0
print(f"Matrix: {matrix15}, Target: {target15}, Found: {solver.searchMatrix(matrix15, target15)}") # Expected: False

