from typing import List, Set, Dict
from collections import deque

class UndirectedGraphNode:
    """无向图节点"""
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def search_nearest_node(graph: List[UndirectedGraphNode], values: Dict[UndirectedGraphNode, int], 
                       node: UndirectedGraphNode, target: int) -> UndirectedGraphNode:
    """
    搜索图中值最接近target的节点
    :param graph: List[UndirectedGraphNode]，图的所有节点
    :param values: Dict[UndirectedGraphNode, int]，每个节点对应的值
    :param node: UndirectedGraphNode，起始节点
    :param target: int，目标值
    :return: UndirectedGraphNode，值最接近target的节点
    """
    if not graph or not node:
        return None
    
    # BFS搜索
    queue = deque([node])
    visited = {node}
    nearest_node = node
    min_diff = abs(values[node] - target)
    
    while queue:
        curr = queue.popleft()
        curr_diff = abs(values[curr] - target)
        
        # 更新最接近的节点
        if curr_diff < min_diff or \
           (curr_diff == min_diff and values[curr] < values[nearest_node]):
            min_diff = curr_diff
            nearest_node = curr
        
        # 访问邻居节点
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
                # 检查邻居节点是否更接近target
                neighbor_diff = abs(values[neighbor] - target)
                if neighbor_diff < min_diff or \
                   (neighbor_diff == min_diff and values[neighbor] < values[nearest_node]):
                    min_diff = neighbor_diff
                    nearest_node = neighbor
    
    return nearest_node

def test_search_nearest_node():
    """测试搜索最近节点的实现"""
    # 测试用例1：基本图
    #  1 -- 2 -- 3
    #  |    |
    #  4 -- 5
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node4 = UndirectedGraphNode(4)
    node5 = UndirectedGraphNode(5)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3, node5]
    node3.neighbors = [node2]
    node4.neighbors = [node1, node5]
    node5.neighbors = [node2, node4]
    
    graph = [node1, node2, node3, node4, node5]
    values = {
        node1: 3,
        node2: 5,
        node3: 7,
        node4: 1,
        node5: 2
    }
    
    # 测试用例1：查找最接近4的节点
    result1 = search_nearest_node(graph, values, node1, 4)
    assert result1 == node1, "Should find node with value 3"
    
    # 测试用例2：查找最接近6的节点
    result2 = search_nearest_node(graph, values, node1, 6)
    assert result2 == node2, "Should find node with value 5"
    
    # 测试用例3：相同差值时选择较小值
    result3 = search_nearest_node(graph, values, node1, 0)
    assert result3 == node4, "Should find node with value 1"
    
    # 测试用例4：空图
    assert search_nearest_node([], {}, None, 1) is None, \
        "Should handle empty graph"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_search_nearest_node() 