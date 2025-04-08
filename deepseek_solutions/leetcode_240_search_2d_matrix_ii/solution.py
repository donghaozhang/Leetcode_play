def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from the top-right corner
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down
    
    return False

# Test cases
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target1 = 5
print(searchMatrix(matrix1, target1))  # Expected output: True

target2 = 20
print(searchMatrix(matrix1, target2))  # Expected output: False

matrix2 = [[-5]]
target3 = -5
print(searchMatrix(matrix2, target3))  # Expected output: True

matrix3 = [[1, 1]]
target4 = 2
print(searchMatrix(matrix3, target4))  # Expected output: False
