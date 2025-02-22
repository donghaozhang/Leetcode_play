# 课程表 II

## 题目描述
现在你总共有 n 门课需要选，记为 0 到 n-1。在选修某些课程之前需要一些先修课程。给定课程总数和一个先决条件表，返回你为了学完所有课程所安排的学习顺序。如果不可能完成所有课程，返回一个空数组。

## 示例
输入:
```
n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
```
输出: [0,1,2,3] 或 [0,2,1,3]
解释: 总共有4门课程。要学习课程3，你应该先完成课程1和2。并且课程1和2都应该排在课程0之后。因此，一个正确的课程顺序是[0,1,2,3]。另一个正确的排序是[0,2,1,3]。

## 解题思路

### BFS + 入度表法
1. **核心思想**
   - 使用入度表记录每个课程的依赖数量
   - 从入度为0的课程开始学习
   - 逐步减少后续课程的依赖数

2. **实现细节**
```python
def find_course_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegrees = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegrees[course] += 1
    
    queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        for dependent in graph[course]:
            indegrees[dependent] -= 1
            if indegrees[dependent] == 0:
                queue.append(dependent)
    
    return order if len(order) == numCourses else []
```

## 复杂度分析
- 时间复杂度：O(V + E)，其中V是课程数，E是依赖关系数
- 空间复杂度：O(V + E)，用于存储图和入度表

### 复杂度分析详解
1. **时间复杂度**
   - 构建图和入度表：O(E)
   - BFS遍历：O(V + E)
   - 每个课程和依赖关系只处理一次

2. **空间复杂度**
   - 邻接表：O(E)
   - 入度表：O(V)
   - 队列和结果数组：O(V)

## 代码实现要点
1. 正确构建依赖关系
2. 维护入度变化
3. 检测是否可以完成所有课程
4. 保存课程学习顺序

## 常见错误
1. 依赖关系构建错误
2. 入度计算错误
3. 未检测环的存在
4. 返回结果不完整

## 优化策略
1. 使用数组代替哈希表
2. 提前检测特殊情况
3. 减少内存使用
4. 使用DFS的替代实现

## 相关题目
1. 课程表
2. 拓扑排序
3. 外星词典
4. 任务调度器 