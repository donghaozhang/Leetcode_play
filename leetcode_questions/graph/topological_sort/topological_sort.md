# 拓扑排序

## 题目描述
给定一个有向图，输出任意一个拓扑排序序列。拓扑排序是一个图中所有节点的线性排序，使得对于图中的每一条有向边(u, v)，节点u在排序中都出现在节点v之前。

## 示例
输入:
```
  1 -> 2 -> 4
  |    |
  v    v
  3 -> 5
```
输出: [1, 2, 3, 4, 5] 或其他有效的拓扑排序

## 解题思路

### BFS + 入度表法
1. **核心思想**
   - 计算每个节点的入度
   - 将入度为0的节点加入队列
   - 逐步删除入度为0的节点及其出边

2. **实现细节**
```python
def topological_sort(graph):
    # 计算入度
    indegrees = defaultdict(int)
    for node in graph:
        for neighbor in node.neighbors:
            indegrees[neighbor] += 1
    
    # BFS
    queue = deque([node for node in graph if indegrees[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in node.neighbors:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
```

## 复杂度分析
- 时间复杂度：O(V + E)，其中V是节点数，E是边数
- 空间复杂度：O(V)，用于存储入度表和队列

### 复杂度分析详解
1. **时间复杂度**
   - 构建入度表：O(E)
   - BFS遍历：O(V + E)
   - 每个节点和边只会被处理一次

2. **空间复杂度**
   - 入度表：O(V)
   - 队列：最大O(V)
   - 结果数组：O(V)

## 应用：课程表问题
1. **问题描述**
   - 给定课程总数和依赖关系
   - 判断是否可以完成所有课程
   - 本质是检测图中是否有环

2. **解决方案**
```python
def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegrees[course] += 1
    
    queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
    count = 0
    
    while queue:
        course = queue.popleft()
        count += 1
        for dependent in graph[course]:
            indegrees[dependent] -= 1
            if indegrees[dependent] == 0:
                queue.append(dependent)
    
    return count == numCourses
```

## 代码实现要点
1. 正确计算入度
2. 维护入度变化
3. 处理孤立节点
4. 检测环的存在

## 常见错误
1. 入度计算错误
2. 未处理所有边
3. 未检测环
4. 队列使用错误

## 优化策略
1. 使用邻接表存储图
2. 提前检测特殊情况
3. 减少不必要的遍历
4. 使用DFS的替代实现

## 相关题目
1. 课程表
2. 课程表II
3. 外星词典
4. 任务调度 