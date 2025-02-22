from typing import List
import sys

def traveling_salesman(n: int, distances: List[List[int]]) -> int:
    """
    解决旅行商问题，找到访问所有城市的最短路径长度
    :param n: int，城市数量
    :param distances: List[List[int]]，城市间距离矩阵
    :return: int，最短路径长度
    """
    # 使用状态压缩DP
    # dp[state][city] 表示已访问城市集合为state，当前在city的最短路径
    dp = {}
    
    def dfs(state: int, curr: int) -> int:
        """
        递归+记忆化搜索
        :param state: int，已访问城市的状态（二进制表示）
        :param curr: int，当前所在城市
        :return: int，最短路径长度
        """
        if state == (1 << n) - 1:  # 所有城市都已访问
            return distances[curr][0] if distances[curr][0] != -1 else sys.maxsize
            
        state_key = (state, curr)
        if state_key in dp:
            return dp[state_key]
            
        min_dist = sys.maxsize
        for next_city in range(n):
            if state & (1 << next_city) or distances[curr][next_city] == -1:
                continue
                
            dist = dfs(state | (1 << next_city), next_city)
            if dist != sys.maxsize:
                min_dist = min(min_dist, dist + distances[curr][next_city])
                
        dp[state_key] = min_dist
        return min_dist
    
    # 从城市0开始，初始状态为只访问了城市0
    result = dfs(1, 0)
    return result if result != sys.maxsize else -1

def traveling_salesman_iterative(n: int, distances: List[List[int]]) -> int:
    """
    使用迭代动态规划解决旅行商问题
    :param n: int，城市数量
    :param distances: List[List[int]]，城市间距离矩阵
    :return: int，最短路径长度
    """
    ALL_VISITED = (1 << n) - 1
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    # 初始化：只访问起点的情况
    dp[1][0] = 0
    
    # 遍历所有可能的状态
    for state in range(1, 1 << n):
        for current in range(n):
            # 如果current不在当前状态中，跳过
            if not (state & (1 << current)):
                continue
            
            # 尝试从current到达每个未访问的城市
            for next_city in range(n):
                # 如果next_city已经访问过，或者是current，跳过
                if state & (1 << next_city) or current == next_city:
                    continue
                
                # 计算新状态
                new_state = state | (1 << next_city)
                # 更新到达next_city的最短距离
                dp[new_state][next_city] = min(
                    dp[new_state][next_city],
                    dp[state][current] + distances[current][next_city]
                )
    
    # 找到访问所有城市后返回起点的最短距离
    result = float('inf')
    for last_city in range(1, n):
        if dp[ALL_VISITED][last_city] != float('inf'):
            result = min(result,
                        dp[ALL_VISITED][last_city] + distances[last_city][0])
    
    return result if result != float('inf') else -1

def test_traveling_salesman():
    """测试旅行商问题的实现"""
    # 测试用例1：基本情况
    n1 = 4
    distances1 = [
        [0, 1, 2, 3],
        [1, 0, 4, 5],
        [2, 4, 0, 6],
        [3, 5, 6, 0]
    ]
    assert traveling_salesman(n1, distances1) == 11, \
        "Should find the shortest path in a simple graph"
    
    # 测试用例2：不可达情况
    n2 = 3
    distances2 = [
        [0, 1, -1],
        [1, 0, -1],
        [-1, -1, 0]
    ]
    assert traveling_salesman(n2, distances2) == -1, \
        "Should return -1 when no valid path exists"
    
    # 测试用例3：最小情况
    n3 = 2
    distances3 = [
        [0, 1],
        [1, 0]
    ]
    assert traveling_salesman(n3, distances3) == 2, \
        "Should handle minimum case correctly"
    
    # 测试用例4：非对称距离
    n4 = 3
    distances4 = [
        [0, 1, 2],
        [2, 0, 1],
        [1, 2, 0]
    ]
    result4 = traveling_salesman(n4, distances4)
    assert result4 > 0, "Should handle asymmetric distances"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_traveling_salesman() 