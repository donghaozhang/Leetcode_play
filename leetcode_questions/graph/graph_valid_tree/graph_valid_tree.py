from typing import List
from collections import defaultdict, deque

def is_valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    判断一个图是否是一棵树
    :param n: int，节点数量（从0到n-1）
    :param edges: List[List[int]]，边的列表
    :return: bool，是否是一棵有效的树
    """
    # 树的特性：n个节点恰好有n-1条边，且连通无环
    if len(edges) != n - 1:
        return False
        
    # 构建邻接表
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS检查连通性
    visited = set()
    queue = deque([0])  # 从节点0开始
    visited.add(0)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # 检查是否所有节点都被访问到
    return len(visited) == n

def is_valid_tree_union_find(n: int, edges: List[List[int]]) -> bool:
    """
    使用并查集判断一个图是否是一棵树
    :param n: int，节点数量
    :param edges: List[List[int]]，边的列表
    :return: bool，是否是一棵有效的树
    """
    # 树的特性：n个节点恰好有n-1条边
    if len(edges) != n - 1:
        return False
    
    # 初始化并查集
    parent = list(range(n))
    
    def find(x: int) -> int:
        """查找节点的根"""
        if parent[x] != x:
            parent[x] = find(parent[x])  # 路径压缩
        return parent[x]
    
    def union(x: int, y: int) -> bool:
        """
        合并两个节点所在的集合
        返回是否成功合并（如果已经在同一集合中则返回False）
        """
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        parent[root_x] = root_y
        return True
    
    # 尝试合并所有边
    for u, v in edges:
        if not union(u, v):  # 如果已经连通，说明有环
            return False
    
    return True

def test_is_valid_tree():
    """测试图是否是有效的树"""
    # 测试用例1：有效的树
    n1 = 5
    edges1 = [[0,1], [0,2], [0,3], [1,4]]
    assert is_valid_tree(n1, edges1), "Should identify valid tree"
    assert is_valid_tree_union_find(n1, edges1), "Should identify valid tree (union find)"
    
    # 测试用例2：有环
    n2 = 4
    edges2 = [[0,1], [1,2], [2,3], [1,3]]
    assert not is_valid_tree(n2, edges2), "Should detect cycle"
    assert not is_valid_tree_union_find(n2, edges2), "Should detect cycle (union find)"
    
    # 测试用例3：不连通
    n3 = 4
    edges3 = [[0,1], [2,3]]
    assert not is_valid_tree(n3, edges3), "Should detect disconnected components"
    assert not is_valid_tree_union_find(n3, edges3), "Should detect disconnected components (union find)"
    
    # 测试用例4：单节点
    n4 = 1
    edges4 = []
    assert is_valid_tree(n4, edges4), "Should handle single node"
    assert is_valid_tree_union_find(n4, edges4), "Should handle single node (union find)"
    
    # 测试用例5：边数错误
    n5 = 4
    edges5 = [[0,1], [1,2], [2,3], [3,0], [0,2]]
    assert not is_valid_tree(n5, edges5), "Should detect wrong number of edges"
    assert not is_valid_tree_union_find(n5, edges5), "Should detect wrong number of edges (union find)"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_is_valid_tree() 