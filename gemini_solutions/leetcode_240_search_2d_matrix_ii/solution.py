from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a value target in an m x n integer matrix matrix.
        Integers in each row are sorted left-to-right.
        Integers in each column are sorted top-to-bottom.

        Args:
            matrix: The m x n integer matrix.
            target: The integer value to search for.

        Returns:
            True if the target is found in the matrix, False otherwise.
        """
        # Handle edge cases: empty matrix or matrix with empty rows
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)       # Number of rows
        n = len(matrix[0])    # Number of columns

        # Start search from the top-right corner
        row = 0
        col = n - 1

        # Loop while the pointers are within the matrix bounds
        while row < m and col >= 0:
            current_element = matrix[row][col]

            if target == current_element:
                return True  # Target found
            elif target < current_element:
                # Target is smaller, must be to the left (if it exists)
                # Eliminate the current column
                col -= 1
            else: # target > current_element
                # Target is larger, must be below (if it exists)
                # Eliminate the current row
                row += 1

        # If the loop finishes, the target was not found
        return False

# --- Test Cases ---

solver = Solution()

# Example 1
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target1 = 5
print(f"Matrix 1:\n{matrix1}")
print(f"Target 1: {target1}, Found: {solver.searchMatrix(matrix1, target1)}") # Expected: True

# Example 2
target2 = 20
print(f"Target 2: {target2}, Found: {solver.searchMatrix(matrix1, target2)}") # Expected: False

# Edge Case: Empty matrix
matrix_empty = []
target_empty = 5
print(f"\nMatrix Empty: {matrix_empty}")
print(f"Target Empty: {target_empty}, Found: {solver.searchMatrix(matrix_empty, target_empty)}") # Expected: False

# Edge Case: Matrix with empty row (handled by initial check)
matrix_empty_row = [[]]
target_empty_row = 1
# This case is typically disallowed by constraints but good to consider
# The code handles it via `if not matrix or not matrix[0]:`
# print(f"\nMatrix Empty Row: {matrix_empty_row}")
# print(f"Target Empty Row: {target_empty_row}, Found: {solver.searchMatrix(matrix_empty_row, target_empty_row)}") # Expected: False (due to check)

# Edge Case: Single element matrix
matrix_single = [[5]]
target_single_found = 5
target_single_not_found = 3
print(f"\nMatrix Single: {matrix_single}")
print(f"Target Single Found: {target_single_found}, Found: {solver.searchMatrix(matrix_single, target_single_found)}") # Expected: True
print(f"Target Single Not Found: {target_single_not_found}, Found: {solver.searchMatrix(matrix_single, target_single_not_found)}") # Expected: False

# Edge Case: Single row matrix
matrix_row = [[1, 3, 5, 7, 9]]
target_row_found = 7
target_row_not_found = 4
print(f"\nMatrix Row: {matrix_row}")
print(f"Target Row Found: {target_row_found}, Found: {solver.searchMatrix(matrix_row, target_row_found)}") # Expected: True
print(f"Target Row Not Found: {target_row_not_found}, Found: {solver.searchMatrix(matrix_row, target_row_not_found)}") # Expected: False

# Edge Case: Single column matrix
matrix_col = [[2], [4], [6], [8]]
target_col_found = 6
target_col_not_found = 5
print(f"\nMatrix Col: {matrix_col}")
print(f"Target Col Found: {target_col_found}, Found: {solver.searchMatrix(matrix_col, target_col_found)}") # Expected: True
print(f"Target Col Not Found: {target_col_not_found}, Found: {solver.searchMatrix(matrix_col, target_col_not_found)}") # Expected: False

# Target smaller than smallest element
target_small = 0
print(f"\nTarget Small: {target_small}, Found: {solver.searchMatrix(matrix1, target_small)}") # Expected: False

# Target larger than largest element
target_large = 35
print(f"Target Large: {target_large}, Found: {solver.searchMatrix(matrix1, target_large)}") # Expected: False

# Target at top-right
target_top_right = 15
print(f"Target Top-Right: {target_top_right}, Found: {solver.searchMatrix(matrix1, target_top_right)}") # Expected: True

# Target at bottom-left
target_bottom_left = 18
print(f"Target Bottom-Left: {target_bottom_left}, Found: {solver.searchMatrix(matrix1, target_bottom_left)}") # Expected: True
