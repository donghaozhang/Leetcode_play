def minArea(image, x, y):
    """
    Given a 2D matrix 'image' where each element is either '0' or '1'
    and a coordinate (x, y) belonging to one of the black pixels ('1'),
    this function returns the area of the smallest axis-aligned rectangle
    that encloses all black pixels.
    
    :param image: List[List[str]] - 2D matrix of characters '0' and '1'.
    :param x: int - Row index of one of the black pixels.
    :param y: int - Column index of one of the black pixels.
    :return: int - The area of the smallest enclosing rectangle.
    """
    if not image or not image[0]:
        return 0
        
    m, n = len(image), len(image[0])
    
    def colHasBlack(col):
        # Checks if a given column contains at least one black pixel.
        for i in range(m):
            if image[i][col] == '1':
                return True
        return False
    
    def rowHasBlack(row):
        # Checks if a given row contains at least one black pixel.
        # Using a simple loop over columns.
        for j in range(n):
            if image[row][j] == '1':
                return True
        return False

    # Binary search for the left boundary (smallest column index with a black pixel).
    left, right = 0, y
    while left < right:
        mid = (left + right) // 2
        if colHasBlack(mid):
            right = mid
        else:
            left = mid + 1
    min_col = left

    # Binary search for the right boundary (largest column index with a black pixel).
    left, right = y, n - 1
    while left < right:
        mid = (left + right + 1) // 2  # Bias the mid to the right.
        if colHasBlack(mid):
            left = mid
        else:
            right = mid - 1
    max_col = left

    # Binary search for the top boundary (smallest row index with a black pixel).
    top, bottom = 0, x
    while top < bottom:
        mid = (top + bottom) // 2
        if rowHasBlack(mid):
            bottom = mid
        else:
            top = mid + 1
    min_row = top

    # Binary search for the bottom boundary (largest row index with a black pixel).
    top, bottom = x, m - 1
    while top < bottom:
        mid = (top + bottom + 1) // 2  # Bias the mid to the bottom.
        if rowHasBlack(mid):
            top = mid
        else:
            bottom = mid - 1
    max_row = top

    # Calculate the area of the rectangle.
    return (max_row - min_row + 1) * (max_col - min_col + 1)

def minArea_practice(image, x, y):
    """
    Given a 2D matrix 'image' where each element is either '0' or '1'
    and a coordinate (x, y) belonging to one of the black pixels ('1'),
    this function returns the area of the smallest axis-aligned rectangle
    that encloses all black pixels.
    """
    if not image or not image[0]:
        return 0
    
    rows, cols = len(image), len(image[0])
    def colHasBlack(col):
        for i in range(rows):
            if image[i][col] == '1':
                return True
        return False    
    
    def rowHasBlack(row):
        for j in range(cols):
            if image[row][j] == '1':
                return True
        return False
    
    # Binary search for the left boundary (smallest column index with a black pixel).
    left, right = 0, y
    while left < right:
        mid = (left + right) // 2
        if colHasBlack(mid):
            right = mid
        else:
            left = mid + 1
    min_col = left

    # Binary search for the right boundary (largest column index with a black pixel).
    left, right = y, cols - 1
    while left < right:
        mid = (left + right + 1) // 2
        if colHasBlack(mid):
            left = mid
        else:
            right = mid - 1
    max_col = left

    # Binary search for the top boundary (smallest row index with a black pixel).
    top, bottom = 0, rows
    while top < bottom:
        mid = (top + bottom) // 2
        if rowHasBlack(mid):
            bottom = mid
        else:
            top = mid + 1
    min_row = top

    # Binary search for the bottom boundary (largest row index with a black pixel).
    top, bottom = x, rows - 1
    while top < bottom:
        mid = (top + bottom + 1) // 2  # Bias the mid to the bottom.
        if rowHasBlack(mid):
            top = mid
        else:
            bottom = mid - 1
    max_row = top

    min_area = (max_row - min_row + 1) * (max_col - min_col + 1)
    return min_area

# Test cases
if __name__ == '__main__':
    # Test Case 1: Example from the problem statement.
    # Image format: Each inner list is a row.
    # Black pixels are at positions: (0,2), (1,1), (1,2), (2,1).
    image1 = [
        ['0', '0', '1', '0'],
        ['0', '1', '1', '0'],
        ['0', '1', '0', '0']
    ]
    x1, y1 = 0, 2  # Given coordinate for a black pixel.
    # Expected rectangle encloses rows 0 to 2 and columns 1 to 2, area = 3 * 2 = 6.
    result1 = minArea(image1, x1, y1)
    result1_practice = minArea_practice(image1, x1, y1)
    expected1 = 6
    print(f"Test Case 1: Result={result1}, Expected={expected1}, {'PASS' if result1 == expected1 else 'FAIL'}")
    assert result1 == expected1, "Test Case 1 Failed"
    print(f"Test Case 1: Result={result1_practice}, Expected={expected1}, {'PASS' if result1_practice == expected1 else 'FAIL'}")

    # Test Case 2: Single black pixel in the middle.
    image2 = [
        ['0', '0', '0'],
        ['0', '1', '0'],
        ['0', '0', '0']
    ]
    x2, y2 = 1, 1

    # Expected rectangle is just that pixel, area = 1.
    result2 = minArea(image2, x2, y2)
    result2_practice = minArea_practice(image2, x2, y2)
    expected2 = 1
    print(f"Test Case 2: Result={result2}, Expected={expected2}, {'PASS' if result2 == expected2 else 'FAIL'}")
    assert result2 == expected2, "Test Case 2 Failed"
    assert result2_practice == expected2, "Test Case 2 Failed"
    print(f"Test Case 2: Result={result2_practice}, Expected={expected2}, {'PASS' if result2_practice == expected2 else 'FAIL'}")
    
    # Test Case 3: All pixels are black.
    image3 = [
        ['1', '1'],
        ['1', '1']
    ]
    x3, y3 = 0, 1
    # The rectangle will cover the entire image, area = 2 * 2 = 4.
    result3 = minArea(image3, x3, y3)
    expected3 = 4
    print(f"Test Case 3: Result={result3}, Expected={expected3}, {'PASS' if result3 == expected3 else 'FAIL'}")
    assert result3 == expected3, "Test Case 3 Failed"
    result3_practice = minArea_practice(image3, x3, y3)
    print(f"Test Case 3: Result={result3_practice}, Expected={expected3}, {'PASS' if result3_practice == expected3 else 'FAIL'}")

    # Test Case 4: Black pixels scattered such that the bounding rectangle spans more.
    image4 = [
        ['0', '0', '1', '0', '0'],
        ['0', '0', '1', '1', '1'],
        ['0', '0', '1', '0', '0'],
        ['0', '1', '1', '0', '0']
    ]
    x4, y4 = 0, 2  # Starting at one known black pixel.
    # Black pixels occur at (0,2), (1,4), and (3,1).
    # So the minimal rectangle spans rows 0 to 3 and columns 1 to 4, area = 4 * 4 = 16.
    result4 = minArea(image4, x4, y4)
    result4_practice = minArea_practice(image4, x4, y4)
    expected4 = 16
    print(f"Test Case 4: Result={result4}, Expected={expected4}, {'PASS' if result4 == expected4 else 'FAIL'}")
    assert result4 == expected4, "Test Case 4 Failed"
    print(f"Test Case 4: Result={result4_practice}, Expected={expected4}, {'PASS' if result4_practice == expected4 else 'FAIL'}")

    # Test Case 5: Cross pattern
    image5 = [
        ['0', '1', '0'],
        ['1', '1', '1'],
        ['0', '1', '0']
    ]
    x5, y5 = 1, 1
    # The cross pattern should be enclosed by a 3x3 rectangle, area = 9
    result5 = minArea(image5, x5, y5)
    result5_practice = minArea_practice(image5, x5, y5)
    expected5 = 9
    print(f"Test Case 5: Result={result5}, Expected={expected5}, {'PASS' if result5 == expected5 else 'FAIL'}")
    assert result5 == expected5, "Test Case 5 Failed"
    print(f"Test Case 5: Result={result5_practice}, Expected={expected5}, {'PASS' if result5_practice == expected5 else 'FAIL'}")
    # Test Case 6: T pattern 
    image6 = [
        ['0', '1', '0'],
        ['0', '1', '1'],
        ['0', '1', '0']
    ]
    x6, y6 = 1, 1
    result6 = minArea(image6, x6, y6)
    result6_practice = minArea_practice(image6, x6, y6)
    expected6 = 6
    print(f"Test Case 6: Result={result6}, Expected={expected6}, {'PASS' if result6 == expected6 else 'FAIL'}")
    assert result6 == expected6, "Test Case 6 Failed"
    print(f"Test Case 6: Result={result6_practice}, Expected={expected6}, {'PASS' if result6_practice == expected6 else 'FAIL'}")
    
    # Test Case 7: 
    image7 = [
        ['0', '1', '0'],
        ['0', '1', '1'],
        ['0', '0', '0']
    ]
    x7, y7 = 1, 1
    # The cross pattern should be enclosed by a 2x2 rectangle, area = 4
    result7 = minArea(image7, x7, y7)
    result7_practice = minArea_practice(image7, x7, y7)
    expected7 = 4
    print(f"Test Case 7: Result={result7}, Expected={expected7}, {'PASS' if result7 == expected7 else 'FAIL'}")
    assert result7 == expected7, "Test Case 7 Failed"
    print(f"Test Case 7: Result={result7_practice}, Expected={expected7}, {'PASS' if result7_practice == expected7 else 'FAIL'}")

    print("\nAll test cases passed successfully!")
