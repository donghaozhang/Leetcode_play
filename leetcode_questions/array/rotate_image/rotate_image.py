from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the image by 90 degrees (clockwise).
        Do not return anything, modify matrix in-place instead.
        
        Args:
            matrix: n x n 2D matrix representing an image
            
        Returns:
            None (matrix is modified in-place)
        """
        row_num = len(matrix)
        col_num = len(matrix[0])
        
        # Step 1: Transpose the matrix (swap elements across the main diagonal)
        for row_i in range(row_num):
            for col_i in range(row_i+1, col_num):
                matrix[row_i][col_i], matrix[col_i][row_i] = matrix[col_i][row_i], matrix[row_i][col_i]
        
        # Step 2: Reverse each row
        for row_i in range(row_num):
            matrix[row_i][0:row_num] = matrix[row_i][::-1]


def test_rotate():
    """Test the rotate function with various examples"""
    solution = Solution()
    
    # Test case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    solution.rotate(matrix1)
    assert matrix1 == expected1, f"Expected {expected1}, got {matrix1}"
    
    # Test case 2: 4x4 matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    solution.rotate(matrix2)
    assert matrix2 == expected2, f"Expected {expected2}, got {matrix2}"
    
    # Test case 3: 1x1 matrix
    matrix3 = [[1]]
    expected3 = [[1]]
    solution.rotate(matrix3)
    assert matrix3 == expected3, f"Expected {expected3}, got {matrix3}"
    
    # Test case 4: 2x2 matrix
    matrix4 = [[1, 2], [3, 4]]
    expected4 = [[3, 1], [4, 2]]
    solution.rotate(matrix4)
    assert matrix4 == expected4, f"Expected {expected4}, got {matrix4}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_rotate() 