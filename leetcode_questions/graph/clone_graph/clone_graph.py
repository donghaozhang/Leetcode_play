from typing import Optional, Dict
from collections import deque

class Node:
    """图节点"""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    深度拷贝图
    :param node: Node，原图的某个节点
    :return: Node，新图对应的节点
    """
    if not node:
        return None
        
    # 用于存储已克隆的节点
    visited = {}
    
    def dfs(curr: Node) -> Node:
        """
        深度优先搜索克隆图
        :param curr: 当前节点
        :return: 克隆的节点
        """
        if curr in visited:
            return visited[curr]
            
        # 创建新节点
        clone = Node(curr.val)
        visited[curr] = clone
        
        # 递归克隆邻居节点
        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))
            
        return clone
    
    return dfs(node)

def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    使用BFS深度拷贝图
    :param node: Node，原图的某个节点
    :return: Node，新图对应的节点
    """
    if not node:
        return None
        
    # 创建第一个节点的拷贝
    visited = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        
        # 处理所有邻居节点
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                # 如果邻居节点未被访问，创建拷贝
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            # 建立新节点之间的连接
            visited[curr].neighbors.append(visited[neighbor])
    
    return visited[node]

def graph_to_adj_list(node: Optional[Node]) -> list:
    """将图转换为邻接表（用于测试）"""
    if not node:
        return []
        
    result = []
    visited = set()
    
    def dfs(curr: Node) -> None:
        if curr.val in visited:
            return
            
        visited.add(curr.val)
        neighbors = [n.val for n in curr.neighbors]
        result.append(neighbors)
        
        for neighbor in curr.neighbors:
            dfs(neighbor)
    
    dfs(node)
    return result

def test_clone_graph():
    """测试图的深度拷贝"""
    # 测试用例1：基本连通图
    #   1 -- 2
    #   |    |
    #   4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    # 测试DFS方法
    cloned1 = clone_graph(node1)
    assert graph_to_adj_list(cloned1) == [[2, 4], [1, 3], [2, 4], [1, 3]], \
        "Should correctly clone a basic connected graph using DFS"
    
    # 测试BFS方法
    cloned2 = clone_graph_bfs(node1)
    assert graph_to_adj_list(cloned2) == [[2, 4], [1, 3], [2, 4], [1, 3]], \
        "Should correctly clone a basic connected graph using BFS"
    
    # 测试用例2：单节点图
    single_node = Node(1)
    cloned_single = clone_graph(single_node)
    assert graph_to_adj_list(cloned_single) == [[]], \
        "Should handle single node graph"
    
    # 测试用例3：空图
    assert clone_graph(None) is None, "Should handle empty graph"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_clone_graph() 