from typing import List
from collections import defaultdict
import heapq

def alien_dictionary(words: List[str]) -> str:
    """
    从字典中的单词顺序推导出字母顺序
    :param words: List[str]，按字典序排序的外星文单词列表
    :return: str，字母的排序结果（字典序最小的拓扑序）
    """
    # 处理边界情况
    if not words:
        return ""
        
    # 构建图和入度表
    graph = defaultdict(set)
    indegrees = defaultdict(int)
    chars = set(''.join(words))  # 收集所有出现的字符
    
    # 从相邻单词中提取顺序关系
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # 检查是否违反字典序
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
            
        # 找到第一个不同的字符
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegrees[c2] += 1
                break
    
    # 使用最小堆进行拓扑排序
    heap = []
    for c in chars:
        if indegrees[c] == 0:
            heapq.heappush(heap, c)
    
    result = []
    
    # 每次选择最小的字符
    while heap:
        c = heapq.heappop(heap)
        result.append(c)
        
        # 更新邻居节点的入度
        for neighbor in sorted(graph[c]):  # 按字典序处理邻居
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    # 检查是否所有字符都被使用
    return ''.join(result) if len(result) == len(chars) else ""

def test_alien_dictionary():
    """测试外星文字典的实现"""
    # 测试用例1：基本字典序
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    assert alien_dictionary(words1) == "wertf", \
        "Should find correct order"
    
    # 测试用例2：无法确定顺序
    words2 = ["z", "x", "z"]
    assert alien_dictionary(words2) == "", \
        "Should detect invalid order"
    
    # 测试用例3：单字符
    words3 = ["z", "x"]
    assert alien_dictionary(words3) == "zx", \
        "Should handle simple case"
    
    # 测试用例4：空列表
    assert alien_dictionary([]) == "", \
        "Should handle empty list"
    
    # 测试用例5：违反字典序
    words5 = ["abc", "ab"]
    assert alien_dictionary(words5) == "", \
        "Should detect prefix violation"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_alien_dictionary() 