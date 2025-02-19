from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        """
        计算骑士从起点到终点的最短路径长度（只能向右移动）
        
        参数:
            grid: 棋盘，0 表示可以走，1 表示障碍
            source: 起始位置 [x, y]
            destination: 目标位置 [x, y]
        返回:
            到达目标位置的最少步数，如果无法到达则返回 -1
        """
        if not grid or not grid[0]:
            return -1
            
        m, n = len(grid), len(grid[0])
        start_row, start_col = source
        end_row, end_col = destination
        
        # 如果终点在起点左边，不可能到达
        if end_col < start_col:
            return -1
            
        # 如果起点就是终点，直接返回 0
        if source == destination:
            return 0
            
        # 骑士可以移动的 4 个方向（只能向右）
        DIRECTIONS = [
            (1, -2),  # 右1上2
            (1, 2),   # 右1下2
            (2, -1),  # 右2上1
            (2, 1)    # 右2下1
        ]
        
        def is_valid(x: int, y: int) -> bool:
            """检查位置是否在棋盘内且不是障碍"""
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 0
        
        # 使用 BFS 搜索最短路径
        queue = deque([(start_row, start_col, 0)])  # (x, y, steps)
        
        while queue:
            curr_x, curr_y, steps = queue.popleft()
            
            # 尝试 4 个可能的移动方向
            for dx, dy in DIRECTIONS:
                next_x, next_y = curr_x + dx, curr_y + dy
                
                # 如果到达目标位置，返回步数
                if [next_x, next_y] == destination:
                    return steps + 1
                
                # 如果新位置合法，加入队列
                if is_valid(next_x, next_y):
                    # 标记为已访问（将格子设为障碍）
                    grid[next_x][next_y] = 1
                    queue.append((next_x, next_y, steps + 1))
        
        # 无法到达目标位置
        return -1


# 测试代码
def test_knight_shortest_path():
    solution = Solution()
    
    # 测试用例 1
    grid1 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    assert solution.shortestPath(grid1, [2,0], [2,2]) == 2, "测试用例 1 失败"
    
    # 测试用例 2：起点等于终点
    grid2 = [[0]]
    assert solution.shortestPath(grid2, [0,0], [0,0]) == 0, "测试用例 2 失败"
    
    # 测试用例 3：无法到达（终点在起点左边）
    grid3 = [[0,0]]
    assert solution.shortestPath(grid3, [0,1], [0,0]) == -1, "测试用例 3 失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_knight_shortest_path() 