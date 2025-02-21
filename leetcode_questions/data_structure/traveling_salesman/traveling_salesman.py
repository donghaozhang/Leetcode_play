from typing import List
import sys

def traveling_salesman(n: int, distances: List[List[int]]) -> int:
    """
    解决旅行商问题
    :param n: int，城市数量
    :param distances: List[List[int]]，城市间距离矩阵
    :return: int，最短路径长度
    """
    # 使用位运算表示状态，(1 << n) - 1 表示所有城市都已访问
    ALL_VISITED = (1 << n) - 1
    
    # dp[state][city] 表示从city出发，访问state中未访问的城市，并返回起点的最短距离
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    def solve(state: int, current: int) -> int:
        """
        递归求解TSP
        :param state: int，当前已访问城市的状态（位表示）
        :param current: int，当前所在城市
        :return: int，最短路径长度
        """
        # 所有城市都已访问，返回到起点的距离
        if state == ALL_VISITED:
            return distances[current][0]
        
        # 如果已经计算过这个状态，直接返回
        if dp[state][current] != float('inf'):
            return dp[state][current]
        
        # 尝试访问每个未访问的城市
        for next_city in range(n):
            # 如果next_city已经在state中，跳过
            if state & (1 << next_city):
                continue
            
            # 计算经过next_city的路径长度
            distance = distances[current][next_city] + \
                      solve(state | (1 << next_city), next_city)
            
            # 更新最短距离
            dp[state][current] = min(dp[state][current], distance)
        
        return dp[state][current]
    
    # 从城市0开始，初始状态为只访问了城市0
    return solve(1, 0)

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
    # 测试用例1：基本情况
    n1 = 4
    distances1 = [
        [0, 1, 2, 3],
        [1, 0, 4, 5],
        [2, 4, 0, 6],
        [3, 5, 6, 0]
    ]
    expected1 = 11  # 0 -> 1 -> 2 -> 3 -> 0
    assert traveling_salesman(n1, distances1) == expected1
    assert traveling_salesman_iterative(n1, distances1) == expected1
    
    # 测试用例2：小规模
    n2 = 3
    distances2 = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    expected2 = 6  # 0 -> 1 -> 2 -> 0
    assert traveling_salesman(n2, distances2) == expected2
    assert traveling_salesman_iterative(n2, distances2) == expected2
    
    # 测试用例3：对称距离
    n3 = 4
    distances3 = [
        [0, 2, 2, 2],
        [2, 0, 2, 2],
        [2, 2, 0, 2],
        [2, 2, 2, 0]
    ]
    expected3 = 8  # 所有路径长度相同
    assert traveling_salesman(n3, distances3) == expected3
    assert traveling_salesman_iterative(n3, distances3) == expected3
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_traveling_salesman() 