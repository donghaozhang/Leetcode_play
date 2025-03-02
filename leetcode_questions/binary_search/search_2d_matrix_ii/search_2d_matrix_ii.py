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

# 测试用例
if __name__ == "__main__":
    # 测试用例1：示例矩阵
    matrix1 = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    
    print("测试矩阵1:")
    print(f"搜索 5: {search_matrix(matrix1, 5)}")     # 应返回 True
    print(f"搜索 20: {search_matrix(matrix1, 20)}")   # 应返回 False
    print(f"搜索 1: {search_matrix(matrix1, 1)}")     # 应返回 True (左上角)
    print(f"搜索 30: {search_matrix(matrix1, 30)}")   # 应返回 True (右下角)
    print(f"搜索 0: {search_matrix(matrix1, 0)}")     # 应返回 False (小于所有元素)
    print(f"搜索 35: {search_matrix(matrix1, 35)}")   # 应返回 False (大于所有元素)
    
    # 测试用例2：空矩阵
    matrix2 = []
    print("\n测试矩阵2 (空矩阵):")
    print(f"搜索 1: {search_matrix(matrix2, 1)}")     # 应返回 False
    
    # 测试用例3：只有一个元素的矩阵
    matrix3 = [[5]]
    print("\n测试矩阵3 (单元素矩阵):")
    print(f"搜索 5: {search_matrix(matrix3, 5)}")     # 应返回 True
    print(f"搜索 6: {search_matrix(matrix3, 6)}")     # 应返回 False 