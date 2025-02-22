from typing import List, Dict, Set
from collections import defaultdict, deque

class DirectedGraphNode:
    """有向图节点"""
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def topological_sort(graph: List[DirectedGraphNode]) -> List[DirectedGraphNode]:
    """
    获取图的拓扑排序
    :param graph: List[DirectedGraphNode]，图的所有节点
    :return: List[DirectedGraphNode]，拓扑排序结果
    """
    if not graph:
        return []
        
    # 计算每个节点的入度
    indegrees = defaultdict(int)
    for node in graph:
        for neighbor in node.neighbors:
            indegrees[neighbor] += 1
    
    # 将入度为0的节点加入队列
    queue = deque([node for node in graph if indegrees[node] == 0])
    result = []
    
    # BFS处理节点
    while queue:
        node = queue.popleft()
        result.append(node)
        
        # 减少邻居节点的入度
        for neighbor in node.neighbors:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else []

def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    判断课程是否可以完成（检测是否有环）
    :param numCourses: int，课程总数
    :param prerequisites: List[List[int]]，课程依赖关系
    :return: bool，是否可以完成所有课程
    """
    # 构建图的邻接表
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    
    # 构建入度表
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegrees[course] += 1
    
    # 将入度为0的课程加入队列
    queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
    count = 0
    
    # BFS处理课程
    while queue:
        course = queue.popleft()
        count += 1
        
        # 减少依赖课程的入度
        for dependent in graph[course]:
            indegrees[dependent] -= 1
            if indegrees[dependent] == 0:
                queue.append(dependent)
    
    return count == numCourses

def test_topological_sort():
    """测试拓扑排序的实现"""
    # 测试用例1：基本有向无环图
    #  1 -> 2 -> 4
    #  |    |
    #  v    v
    #  3 -> 5
    node1 = DirectedGraphNode(1)
    node2 = DirectedGraphNode(2)
    node3 = DirectedGraphNode(3)
    node4 = DirectedGraphNode(4)
    node5 = DirectedGraphNode(5)
    
    node1.neighbors = [node2, node3]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node5]
    
    result = topological_sort([node1, node2, node3, node4, node5])
    labels = [node.label for node in result]
    assert labels == [1, 2, 3, 4, 5], "Should return valid topological order"
    
    # 测试用例2：课程表问题
    assert can_finish(4, [[1,0], [2,1], [3,2]]) == True, \
        "Should detect no cycle"
    assert can_finish(2, [[1,0], [0,1]]) == False, \
        "Should detect cycle"
    
    # 测试用例3：空图
    assert topological_sort([]) == [], "Should handle empty graph"
    
    # 测试用例4：单节点图
    single_node = DirectedGraphNode(1)
    result = topological_sort([single_node])
    assert len(result) == 1 and result[0].label == 1, \
        "Should handle single node graph"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_topological_sort() 