def search_matrix(matrix, target):
    """
    在每行每列都排序的矩阵中搜索目标值
    :param matrix: List[List[int]]，每行每列都是排序的矩阵
    :param target: int，要搜索的目标值
    :return: bool，矩阵中是否存在目标值
    """
    if not matrix or not matrix[0]:
        return False
        
    rows, cols = len(matrix), len(matrix[0])
    # 从右上角开始搜索
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            # 当前值太大，排除这一列
            col -= 1
        else:
            # 当前值太小，排除这一行
            row += 1
            
    return False 