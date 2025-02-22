from typing import List
from collections import defaultdict, deque

def is_unique_sequence(org: List[int], seqs: List[List[int]]) -> bool:
    """
    判断序列是否是唯一的拓扑序
    :param org: List[int]，目标序列
    :param seqs: List[List[int]]，子序列列表
    :return: bool，是否是唯一的拓扑序
    """
    # 处理边界情况
    if not seqs:
        return not org
    
    # 构建图和入度表
    graph = defaultdict(set)
    indegrees = defaultdict(int)
    values = set()
    
    # 从子序列构建图
    for seq in seqs:
        values.update(seq)
        for i in range(len(seq) - 1):
            if seq[i] == seq[i + 1]:  # 自环
                return False
            if seq[i + 1] not in graph[seq[i]]:
                graph[seq[i]].add(seq[i + 1])
                indegrees[seq[i + 1]] += 1
    
    # 检查节点数是否匹配
    if len(values) != len(org):
        return False
    for value in org:
        if value not in values:
            return False
    
    # BFS检查拓扑序
    queue = deque([x for x in values if indegrees[x] == 0])
    index = 0
    
    while queue:
        # 如果队列中元素多于1个，说明存在多种可能的拓扑序
        if len(queue) != 1:
            return False
            
        curr = queue.popleft()
        if index == len(org) or curr != org[index]:
            return False
        index += 1
        
        # 更新邻居节点的入度
        for neighbor in graph[curr]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    return index == len(org)

def test_is_unique_sequence():
    """测试序列重构的实现"""
    # 测试用例1：唯一拓扑序
    org1 = [1, 2, 3]
    seqs1 = [[1, 2], [1, 3], [2, 3]]
    assert is_unique_sequence(org1, seqs1), \
        "Should identify unique sequence"
    
    # 测试用例2：非唯一拓扑序
    org2 = [1, 2, 3]
    seqs2 = [[1, 2], [1, 3]]
    assert not is_unique_sequence(org2, seqs2), \
        "Should identify non-unique sequence"
    
    # 测试用例3：不匹配的序列
    org3 = [1, 2, 3]
    seqs3 = [[1, 2], [2, 3], [3, 1]]
    assert not is_unique_sequence(org3, seqs3), \
        "Should identify invalid sequence with cycle"
    
    # 测试用例4：空序列
    org4 = []
    seqs4 = []
    assert is_unique_sequence(org4, seqs4), \
        "Should handle empty sequences"
    
    # 测试用例5：单元素序列
    org5 = [1]
    seqs5 = [[1]]
    assert is_unique_sequence(org5, seqs5), \
        "Should handle single element sequence"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_is_unique_sequence() 