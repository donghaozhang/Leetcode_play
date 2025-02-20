def longest_increasing_continuous_subsequence2(matrix):
    """
    计算矩阵中最长连续递增子序列的长度
    :param matrix: List[List[int]]，输入矩阵
    :return: int，最长连续递增子序列的长度
    """
    if not matrix or not matrix[0]:
        return 0
        
    m, n = len(matrix), len(matrix[0])
    # dp[i][j] 表示以 matrix[i][j] 结尾的最长连续递增子序列长度
    dp = [[0] * n for _ in range(m)]
    
    # 四个方向的移动
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(i, j, visited):
        """使用记忆化搜索计算以(i,j)结尾的最长连续递增子序列长度"""
        if dp[i][j] != 0:  # 已经计算过
            return dp[i][j]
            
        max_len = 1  # 至少包含自己
        
        # 检查四个方向
        for di, dj in DIRECTIONS:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                max_len = max(max_len, dfs(ni, nj, visited) + 1)
                
        dp[i][j] = max_len
        return max_len
    
    # 从每个点开始搜索
    result = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j, visited))
            
    return result

def test_longest_increasing_continuous_subsequence2():
    # 测试用例1：基本情况
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert longest_increasing_continuous_subsequence2(matrix1) == 9, \
        f"Expected 9, but got {longest_increasing_continuous_subsequence2(matrix1)}"
    
    # 测试用例2：有下降的情况
    matrix2 = [
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]
    assert longest_increasing_continuous_subsequence2(matrix2) == 6, \
        f"Expected 6, but got {longest_increasing_continuous_subsequence2(matrix2)}"
    
    # 测试用例3：空矩阵
    assert longest_increasing_continuous_subsequence2([]) == 0, \
        "Expected 0 for empty matrix"
    
    # 测试用例4：1x1矩阵
    matrix4 = [[1]]
    assert longest_increasing_continuous_subsequence2(matrix4) == 1, \
        f"Expected 1, but got {longest_increasing_continuous_subsequence2(matrix4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_longest_increasing_continuous_subsequence2() 