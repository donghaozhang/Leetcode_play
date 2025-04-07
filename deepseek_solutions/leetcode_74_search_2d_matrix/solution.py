def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3
print(searchMatrix(matrix1, target1))  # Output: True

matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target2 = 13
print(searchMatrix(matrix2, target2))  # Output: False

matrix3 = []
target3 = 0
print(searchMatrix(matrix3, target3))  # Output: False

matrix4 = [[1]]
target4 = 1
print(searchMatrix(matrix4, target4))  # Output: True

matrix5 = [[1, 1]]
target5 = 2
print(searchMatrix(matrix5, target5))  # Output: False
