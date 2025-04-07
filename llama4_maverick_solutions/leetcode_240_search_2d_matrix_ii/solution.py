def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix sorted row-wise and column-wise.

    Args:
    matrix (list[list[int]]): A 2D list of integers sorted row-wise and column-wise.
    target (int): The target value to be searched.

    Returns:
    bool: True if the target is found, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# Test cases
if __name__ == "__main__":
    # Example 1
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: True

    # Example 2
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    print(searchMatrix(matrix, target))  # Expected output: False

    # Edge case: Empty matrix
    matrix = []
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: False

    # Edge case: Matrix with a single element
    matrix = [[5]]
    target = 5
    print(searchMatrix(matrix, target))  # Expected output: True
