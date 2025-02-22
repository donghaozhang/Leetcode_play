from typing import List, Set, Dict
from collections import defaultdict, deque

def find_ladders(start: str, end: str, dict_set: Set[str]) -> List[List[str]]:
    """
    找出所有从start到end的最短转换序列
    :param start: str，起始单词
    :param end: str，目标单词
    :param dict_set: Set[str]，单词字典
    :return: List[List[str]]，所有最短转换序列
    """
    # 将起始和结束单词加入字典
    dict_set.add(start)
    dict_set.add(end)
    
    # 构建图的邻接表
    graph = defaultdict(list)
    # 记录到达每个单词的最短距离
    distance = defaultdict(int)
    
    def build_graph() -> bool:
        """
        使用BFS构建图并找到最短路径
        :return: bool，是否存在路径
        """
        queue = deque([start])
        distance[start] = 0
        found = False
        
        while queue and not found:
            level_size = len(queue)
            # 记录这一层访问过的单词，避免同层重复访问
            visited = set()
            
            for _ in range(level_size):
                word = queue.popleft()
                curr_dist = distance[word]
                
                # 尝试改变每个位置的字母
                word_chars = list(word)
                for i in range(len(word)):
                    orig_char = word_chars[i]
                    
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word_chars[i] = c
                        new_word = ''.join(word_chars)
                        
                        if new_word in dict_set:
                            if new_word == end:
                                found = True
                            
                            if new_word not in distance:
                                distance[new_word] = curr_dist + 1
                                queue.append(new_word)
                                visited.add(new_word)
                                graph[word].append(new_word)
                            elif distance[new_word] == curr_dist + 1:
                                graph[word].append(new_word)
                                
                    word_chars[i] = orig_char
                    
            # 将这一层访问过的单词从字典中移除，避免重复访问
            dict_set -= visited
            
        return found
    
    def find_paths(curr: str, path: List[str], paths: List[List[str]]) -> None:
        """
        使用DFS找出所有最短路径
        :param curr: 当前单词
        :param path: 当前路径
        :param paths: 存储所有路径
        """
        if curr == end:
            paths.append(path[:])
            return
            
        for next_word in graph[curr]:
            if distance[next_word] == distance[curr] + 1:
                path.append(next_word)
                find_paths(next_word, path, paths)
                path.pop()
    
    # 如果不存在路径，直接返回空列表
    if not build_graph():
        return []
    
    # 使用DFS找出所有最短路径
    result = []
    find_paths(start, [start], result)
    return result

def test_find_ladders():
    """测试单词接龙II的实现"""
    # 测试用例1：基本情况
    start1 = "hit"
    end1 = "cog"
    dict1 = {"hot", "dot", "dog", "lot", "log", "cog"}
    expected1 = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]
    result1 = find_ladders(start1, end1, dict1)
    assert sorted(map(tuple, result1)) == sorted(map(tuple, expected1)), \
        f"Expected {expected1}, but got {result1}"
    
    # 测试用例2：无解情况
    start2 = "hit"
    end2 = "cog"
    dict2 = {"hot", "dot", "dog", "lot", "log"}
    assert find_ladders(start2, end2, dict2) == [], \
        "Should return empty list when no solution exists"
    
    # 测试用例3：单步转换
    start3 = "a"
    end3 = "c"
    dict3 = {"a", "b", "c"}
    expected3 = [["a", "c"]]
    assert find_ladders(start3, end3, dict3) == expected3, \
        f"Expected {expected3}, but got {find_ladders(start3, end3, dict3)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_ladders() 