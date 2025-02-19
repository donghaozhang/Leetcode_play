from collections import deque
from typing import List, Set, Tuple

class Solution:
    def shortestPath(self, source: List[int], destination: List[int]) -> int:
        """
        计算骑士从起点到终点的最短路径长度
        
        参数:
            source: 起始位置 [x, y]
            destination: 目标位置 [x, y]
        返回:
            到达目标位置的最少步数，如果无法到达则返回 -1
        """
        # 骑士的 8 个可能移动方向
        DIRECTIONS = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]
        
        def is_valid(x: int, y: int, visited: Set[Tuple[int, int]]) -> bool:
            """检查位置是否合法且未访问过"""
            # 这里假设棋盘大小为 8x8，可以根据实际需求调整
            return (0 <= x < 8 and 0 <= y < 8 and 
                   (x, y) not in visited)
        
        # 将起点和终点转换为元组，方便处理
        start = tuple(source)
        end = tuple(destination)
        
        # 如果起点就是终点，直接返回 0
        if start == end:
            return 0
            
        # 使用 BFS 搜索最短路径
        queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
        visited = {start}
        
        while queue:
            curr_x, curr_y, steps = queue.popleft()
            
            # 尝试 8 个可能的移动方向
            for dx, dy in DIRECTIONS:
                next_x, next_y = curr_x + dx, curr_y + dy
                
                # 如果到达目标位置，返回步数
                if (next_x, next_y) == end:
                    return steps + 1
                
                # 如果新位置合法且未访问过，加入队列
                if is_valid(next_x, next_y, visited):
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, steps + 1))
        
        # 无法到达目标位置
        return -1


# 测试代码
def test_knight_shortest_path():
    solution = Solution()
    
    # 测试用例 1：需要 2 步
    assert solution.shortestPath([0, 0], [2, 1]) == 2, "测试用例 1 失败"
    
    # 测试用例 2：起点等于终点
    assert solution.shortestPath([0, 0], [0, 0]) == 0, "测试用例 2 失败"
    
    # 测试用例 3：需要 4 步
    assert solution.shortestPath([0, 0], [7, 7]) == 6, "测试用例 3 失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_knight_shortest_path() 