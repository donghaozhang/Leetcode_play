def shortest_path(grid):
    """
    计算骑士从左上角到右下角的最短路径，使用滚动数组优化空间
    :param grid: List[List[bool]]，True表示可以走，False表示障碍
    :return: int，最短路径长度，如果无法到达返回-1
    """
    if not grid or not grid[0] or not grid[0][0]:
        return -1
        
    m, n = len(grid), len(grid[0])
    
    # 骑士可以走的四种方式（向右移动）
    MOVES = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
    
    # 使用两个数组进行滚动
    # dp[i][j] 表示从起点到位置(i,j)的最短路径
    dp = [[float('inf')] * n for _ in range(2)]
    dp[0][0] = 0  # 起点
    
    # 按列进行动态规划
    for j in range(1, n):
        # 当前列使用 curr，上一列使用 prev
        curr = j % 2
        prev = 1 - curr
        
        # 重置当前列
        for i in range(m):
            dp[curr][i] = float('inf')
        
        # 对当前列的每个位置计算最短路径
        for i in range(m):
            if not grid[i][j]:  # 如果是障碍，跳过
                continue
                
            # 检查所有可能的前一步位置
            for di, dj in MOVES:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < j:  # 注意j而不是n
                    if grid[prev_i][prev_j]:
                        dp[curr][i] = min(dp[curr][i], dp[prev % 2][prev_i] + 1)
    
    # 检查是否能到达终点
    result = dp[(n-1) % 2][m-1]
    return result if result != float('inf') else -1

def test_shortest_path():
    # 测试用例1：基本情况
    grid1 = [
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ]
    assert shortest_path(grid1) == 3, f"Expected 3, but got {shortest_path(grid1)}"
    
    # 测试用例2：有障碍
    grid2 = [
        [True, True, True],
        [True, False, True],
        [True, True, True]
    ]
    assert shortest_path(grid2) == 3, f"Expected 3, but got {shortest_path(grid2)}"
    
    # 测试用例3：无法到达
    grid3 = [
        [True, False, True],
        [False, False, True],
        [True, True, True]
    ]
    assert shortest_path(grid3) == -1, f"Expected -1, but got {shortest_path(grid3)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_shortest_path() 