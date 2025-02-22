from typing import List
from collections import defaultdict, deque

def find_course_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    查找课程的学习顺序（拓扑排序）
    :param numCourses: int，课程总数
    :param prerequisites: List[List[int]]，课程依赖关系
    :return: List[int]，课程学习顺序，如果不存在则返回空列表
    """
    # 构建图的邻接表和入度表
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    
    # 构建依赖关系
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegrees[course] += 1
    
    # 将所有入度为0的课程加入队列
    queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
    order = []
    
    # BFS处理课程
    while queue:
        course = queue.popleft()
        order.append(course)
        
        # 减少依赖当前课程的其他课程的入度
        for dependent in graph[course]:
            indegrees[dependent] -= 1
            if indegrees[dependent] == 0:
                queue.append(dependent)
    
    # 检查是否所有课程都被安排
    return order if len(order) == numCourses else []

def test_find_course_order():
    """测试课程顺序的查找"""
    # 测试用例1：有效的课程依赖
    #  0 -> 1 -> 3
    #  |    |
    #  v    v
    #  2 -> 4
    prerequisites1 = [[1,0], [2,0], [3,1], [4,1], [4,2]]
    result1 = find_course_order(5, prerequisites1)
    assert result1 == [0, 1, 2, 3, 4] or result1 == [0, 2, 1, 4, 3], \
        "Should find valid course order"
    
    # 测试用例2：存在环的课程依赖
    prerequisites2 = [[1,0], [0,1]]
    assert find_course_order(2, prerequisites2) == [], \
        "Should detect cycle and return empty list"
    
    # 测试用例3：无依赖的课程
    assert find_course_order(1, []) == [0], \
        "Should handle course with no prerequisites"
    
    # 测试用例4：复杂依赖关系
    prerequisites4 = [[1,0], [2,0], [3,1], [3,2]]
    result4 = find_course_order(4, prerequisites4)
    assert result4 and len(result4) == 4 and result4[0] == 0, \
        "Should handle complex dependencies"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_course_order() 