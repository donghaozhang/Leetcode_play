def unique_paths(m, n):
    """
    计算从左上角到右下角的不同路径数
    :param m: int，矩阵的行数
    :param n: int，矩阵的列数
    :return: int，不同路径的总数
    """
    if m <= 0 or n <= 0:
        return 0
        
    # dp[i][j] 表示到达位置(i,j)的不同路径数
    dp = [[1] * n for _ in range(m)]
    
    # 对每个位置，路径数等于从上面来的路径数加上从左边来的路径数
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

def unique_paths_optimized(m, n):
    """
    使用一维数组优化空间的解法
    :param m: int，矩阵的行数
    :param n: int，矩阵的列数
    :return: int，不同路径的总数
    """
    if m <= 0 or n <= 0:
        return 0
        
    # 只使用一行，每次更新这一行
    dp = [1] * n
    
    # 对每一行
    for i in range(1, m):
        # 从左到右更新
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]

def test_unique_paths():
    # 测试用例1：基本情况
    assert unique_paths(3, 3) == 6, f"Expected 6, but got {unique_paths(3, 3)}"
    assert unique_paths_optimized(3, 3) == 6, f"Expected 6, but got {unique_paths_optimized(3, 3)}"
    
    # 测试用例2：1x1的网格
    assert unique_paths(1, 1) == 1, f"Expected 1, but got {unique_paths(1, 1)}"
    assert unique_paths_optimized(1, 1) == 1, f"Expected 1, but got {unique_paths_optimized(1, 1)}"
    
    # 测试用例3：1xn的网格
    assert unique_paths(1, 7) == 1, f"Expected 1, but got {unique_paths(1, 7)}"
    assert unique_paths_optimized(1, 7) == 1, f"Expected 1, but got {unique_paths_optimized(1, 7)}"
    
    # 测试用例4：mx1的网格
    assert unique_paths(7, 1) == 1, f"Expected 1, but got {unique_paths(7, 1)}"
    assert unique_paths_optimized(7, 1) == 1, f"Expected 1, but got {unique_paths_optimized(7, 1)}"
    
    # 测试用例5：较大的网格
    assert unique_paths(3, 7) == 28, f"Expected 28, but got {unique_paths(3, 7)}"
    assert unique_paths_optimized(3, 7) == 28, f"Expected 28, but got {unique_paths_optimized(3, 7)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_unique_paths() 