# 序列重构

## 题目描述
判断给定的序列是否是唯一的拓扑序。给定一个序列org和一些子序列seqs，判断org是否是seqs的唯一重构序列。
重构序列必须包含seqs中的所有子序列，并且是唯一满足这个条件的序列。

## 示例
输入:
```
org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
```
输出: true
解释: [1,2,3]是唯一一个可以被重构的序列。

## 解题思路

### BFS + 唯一性检查
1. **核心思想**
   - 使用BFS进行拓扑排序
   - 确保每一步只有一个选择
   - 验证生成的序列与目标序列匹配

2. **实现细节**
```python
def is_unique_sequence(org, seqs):
    # 构建图和入度表
    graph = defaultdict(set)
    indegrees = defaultdict(int)
    
    # 构建依赖关系
    for seq in seqs:
        for i in range(len(seq) - 1):
            if seq[i + 1] not in graph[seq[i]]:
                graph[seq[i]].add(seq[i + 1])
                indegrees[seq[i + 1]] += 1
    
    # BFS检查唯一性
    queue = deque([x for x in values if indegrees[x] == 0])
    index = 0
    
    while queue:
        if len(queue) != 1:  # 关键检查：确保每步只有一个选择
            return False
        # ... 处理当前节点
```

## 复杂度分析
- 时间复杂度：O(V + E)，其中V是节点数，E是边数
- 空间复杂度：O(V + E)，用于存储图和入度表

### 复杂度分析详解
1. **时间复杂度**
   - 构建图：O(E)
   - BFS遍历：O(V + E)
   - 唯一性检查：O(V)

2. **空间复杂度**
   - 邻接表：O(E)
   - 入度表：O(V)
   - 队列：O(V)

## 代码实现要点
1. 正确构建图结构
2. 检查队列大小确保唯一性
3. 验证序列完整性
4. 处理特殊情况

## 常见错误
1. 未检查队列大小
2. 图构建错误
3. 未处理自环
4. 未验证所有节点

## 优化策略
1. 提前检测无效情况
2. 使用集合优化查找
3. 减少内存使用
4. 优化图的表示

## 相关题目
1. 拓扑排序
2. 课程表
3. 外星词典
4. 验证序列 