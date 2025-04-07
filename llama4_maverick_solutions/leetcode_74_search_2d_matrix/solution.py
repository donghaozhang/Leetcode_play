def searchMatrix(matrix, target):
    """
    Searches for a target value in a given m x n integer matrix.

    Args:
    matrix (list[list[int]]): A 2D list of integers sorted as described.
    target (int): The target value to search for.

    Returns:
    bool: True if the target is found, False otherwise.
    """
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

# Test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(searchMatrix(matrix1, target1))  # Expected output: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(searchMatrix(matrix2, target2))  # Expected output: False
