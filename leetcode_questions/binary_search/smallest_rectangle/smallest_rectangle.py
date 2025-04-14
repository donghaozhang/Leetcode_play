def min_area(image, x, y):
    """
    Find the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
    :param image: List[List[str]], 2D matrix, '0' is white pixel, '1' is black pixel
    :param x: int, the x coordinate of one of the black pixels
    :param y: int, the y coordinate of one of the black pixels
    :return: int, the area of the smallest rectangle
    """
    if not image or not image[0]:
        return 0
        
    m, n = len(image), len(image[0])
    
    def search_columns(start, end, top, bottom, check_left):
        """Binary search for column boundary"""
        while start + 1 < end:
            mid = (start + end) // 2
            # Check if this column has black pixel
            has_black = False
            for i in range(top, bottom + 1):
                if image[i][mid] == '1':
                    has_black = True
                    break
            if has_black == check_left:
                end = mid
            else:
                start = mid
        return start if check_left else end
    
    def search_rows(start, end, left, right, check_top):
        """Binary search for row boundary"""
        while start + 1 < end:
            mid = (start + end) // 2
            # Check if this row has black pixel
            has_black = False
            for j in range(left, right + 1):
                if image[mid][j] == '1':
                    has_black = True
                    break
            if has_black == check_top:
                end = mid
            else:
                start = mid
        return start if check_top else end
    
    # Find left boundary (first column containing 1 from left to right)
    left = search_columns(0, y, 0, m - 1, True)
    # Find right boundary (first column containing 1 from right to left)
    right = search_columns(y, n - 1, 0, m - 1, False)
    # Find top boundary (first row containing 1 from top to bottom)
    top = search_rows(0, x, left, right, True)
    # Find bottom boundary (first row containing 1 from bottom to top)
    bottom = search_rows(x, m - 1, left, right, False)
    
    return (right - left + 1) * (bottom - top + 1)
