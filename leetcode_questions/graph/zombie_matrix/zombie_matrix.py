from typing import List
from collections import deque

def zombie_in_matrix(grid: List[List[int]]) -> int:
    """
    计算僵尸感染所有人需要的天数
    :param grid: List[List[int]]，矩阵，0表示人类，1表示僵尸，2表示墙
    :return: int，感染所有人需要的天数，如果无法感染所有人则返回-1
    """
    if not grid or not grid[0]:
        return -1
        
    rows, cols = len(grid), len(grid[0])
    humans = 0  # 记录人类数量
    queue = deque()  # 存储僵尸位置
    
    # 统计人类数量并找到所有僵尸的初始位置
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                humans += 1
            elif grid[i][j] == 1:
                queue.append((i, j, 0))  # (行, 列, 天数)
    
    # 如果没有人类，直接返回0
    if humans == 0:
        return 0
    
    # BFS感染过程
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 四个方向
    days = 0
    
    while queue:
        row, col, day = queue.popleft()
        days = max(days, day)
        
        # 检查四个方向
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # 检查边界和是否是人类
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 0):
                grid[new_row][new_col] = 1  # 感染
                humans -= 1  # 减少人类数量
                queue.append((new_row, new_col, day + 1))
    
    # 检查是否所有人都被感染
    return days if humans == 0 else -1

def test_zombie_in_matrix():
    """测试僵尸感染的实现"""
    # 测试用例1：基本情况
    grid1 = [
        [0, 1, 2, 0, 0],
        [1, 0, 0, 2, 1],
        [0, 1, 0, 0, 0]
    ]
    assert zombie_in_matrix(grid1) == 2, "Should take 2 days"
    
    # 测试用例2：无法感染所有人
    grid2 = [
        [0, 1, 2, 0],
        [1, 0, 2, 0],
        [0, 1, 2, 0]
    ]
    assert zombie_in_matrix(grid2) == -1, "Should be impossible"
    
    # 测试用例3：一开始就没有人类
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert zombie_in_matrix(grid3) == 0, "Should take 0 days"
    
    # 测试用例4：单元素网格
    grid4 = [[0]]
    assert zombie_in_matrix(grid4) == -1, "Should be impossible for single human"
    
    # 测试用例5：空网格
    grid5 = []
    assert zombie_in_matrix(grid5) == -1, "Should handle empty grid"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_zombie_in_matrix() 