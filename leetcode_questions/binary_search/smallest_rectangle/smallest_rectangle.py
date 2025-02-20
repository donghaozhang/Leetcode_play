def min_area(image, x, y):
    """
    找到包含所有黑色像素的最小矩形面积
    :param image: List[List[str]]，二维矩阵，'0'表示白色像素，'1'表示黑色像素
    :param x: int，一个黑色像素点的x坐标
    :param y: int，一个黑色像素点的y坐标
    :return: int，最小矩形的面积
    """
    if not image or not image[0]:
        return 0
        
    m, n = len(image), len(image[0])
    
    def search_columns(start, end, top, bottom, check_left):
        """二分查找列的边界"""
        while start + 1 < end:
            mid = (start + end) // 2
            # 检查这一列是否有黑色像素
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
        """二分查找行的边界"""
        while start + 1 < end:
            mid = (start + end) // 2
            # 检查这一行是否有黑色像素
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
    
    # 找左边界（从左往右第一个包含1的列）
    left = search_columns(0, y, 0, m - 1, True)
    # 找右边界（从右往左第一个包含1的列）
    right = search_columns(y, n - 1, 0, m - 1, False)
    # 找上边界（从上往下第一个包含1的行）
    top = search_rows(0, x, left, right, True)
    # 找下边界（从下往上第一个包含1的行）
    bottom = search_rows(x, m - 1, left, right, False)
    
    return (right - left + 1) * (bottom - top + 1) 