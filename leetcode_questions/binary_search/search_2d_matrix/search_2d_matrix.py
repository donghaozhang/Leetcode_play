def search_matrix(matrix, target):
    """
    :param matrix: List[List[int]]
    :param target: int
    :return: bool
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Test cases
def run_tests():
    # Test Case 1: Example from problem description
    matrix1 = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    assert search_matrix(matrix1, 3) == True, "Test Case 1 Failed: Target 3 should be found"
    
    # Test Case 2: Target not in matrix
    assert search_matrix(matrix1, 13) == False, "Test Case 2 Failed: Target 13 should not be found"
    
    # Test Case 3: Target at beginning of matrix
    assert search_matrix(matrix1, 1) == True, "Test Case 3 Failed: Target 1 should be found"
    
    # Test Case 4: Target at end of matrix
    assert search_matrix(matrix1, 50) == True, "Test Case 4 Failed: Target 50 should be found"
    
    # Test Case 5: Empty matrix
    assert search_matrix([], 1) == False, "Test Case 5 Failed: Empty matrix should return False"
    
    # Test Case 6: Matrix with empty rows
    assert search_matrix([[]], 1) == False, "Test Case 6 Failed: Matrix with empty rows should return False"
    
    # Test Case 7: Matrix with a single element
    assert search_matrix([[5]], 5) == True, "Test Case 7 Failed: Target 5 should be found in single element matrix"
    assert search_matrix([[5]], 6) == False, "Test Case 8 Failed: Target 6 should not be found in single element matrix"
    
    print("All test cases passed!")

if __name__ == "__main__":
    run_tests() 