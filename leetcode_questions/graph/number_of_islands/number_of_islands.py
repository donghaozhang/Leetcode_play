from typing import List

def count_islands(grid: List[List[int]]) -> int:
    """
    计算岛屿数量
    :param grid: List[List[int]]，二维网格，1表示陆地，0表示水
    :return: int，岛屿数量
    """
    if not grid or not grid[0]:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(row: int, col: int) -> None:
        """
        深度优先搜索标记连通的陆地
        :param row: 当前行
        :param col: 当前列
        """
        # 检查边界和是否为陆地
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            grid[row][col] != 1):
            return
            
        # 标记已访问
        grid[row][col] = 2
        
        # 访问四个方向
        dfs(row + 1, col)  # 下
        dfs(row - 1, col)  # 上
        dfs(row, col + 1)  # 右
        dfs(row, col - 1)  # 左
    
    # 遍历网格
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # 发现新岛屿
                count += 1
                dfs(i, j)  # 标记整个岛屿
    
    # 恢复网格（可选）
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                grid[i][j] = 1
                
    return count

def test_count_islands():
    """测试岛屿数量的计算"""
    # 测试用例1：基本网格
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    assert count_islands(grid1) == 3, "Should find 3 islands"
    
    # 测试用例2：单个岛屿
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert count_islands(grid2) == 1, "Should find 1 island"
    
    # 测试用例3：无岛屿
    grid3 = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert count_islands(grid3) == 0, "Should find no islands"
    
    # 测试用例4：空网格
    grid4 = []
    assert count_islands(grid4) == 0, "Should handle empty grid"
    
    # 测试用例5：复杂形状岛屿
    grid5 = [
        [1, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 1]
    ]
    assert count_islands(grid5) == 3, "Should handle complex shapes"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_count_islands() 