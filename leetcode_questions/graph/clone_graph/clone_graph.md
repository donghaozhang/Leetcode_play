# 克隆图

## 题目描述
给定一个无向连通图中的一个节点，返回该图的深度拷贝。图中的每个节点都包含一个值和邻居节点列表。

要求：
1. 新图和原图具有相同的结构
2. 对新图的修改不会影响原图
3. 保持节点间的连接关系

## 示例
输入:
```
     1 -- 2
     |    |
     4 -- 3
```
输出: 返回节点1的拷贝，新图具有相同的结构和连接关系

## 解题思路

### 方法一：DFS + 哈希表
1. **核心思想**
   - 使用哈希表记录已克隆的节点
   - 深度优先搜索遍历图
   - 递归克隆邻居节点

2. **实现细节**
```python
def dfs(curr):
    if curr in visited:
        return visited[curr]
        
    clone = Node(curr.val)
    visited[curr] = clone
    
    for neighbor in curr.neighbors:
        clone.neighbors.append(dfs(neighbor))
        
    return clone
```

### 方法二：BFS + 哈希表
1. **核心思想**
   - 使用队列进行层次遍历
   - 哈希表记录已克隆节点
   - 逐层建立节点连接

2. **实现细节**
```python
def clone_graph_bfs(node):
    visited = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            visited[curr].neighbors.append(visited[neighbor])
```

## 复杂度分析
- 时间复杂度：O(N + M)，N是节点数，M是边数
- 空间复杂度：O(N)，哈希表存储所有节点

## 代码实现要点
1. 正确使用哈希表避免重复克隆
2. 维护节点间的连接关系
3. 处理空图和单节点情况
4. 确保深度拷贝的独立性

## 常见错误
1. 未使用哈希表导致无限递归
2. 节点连接关系错误
3. 未处理空图情况
4. 浅拷贝而非深拷贝

## 优化策略
1. 使用迭代代替递归
2. 减少哈希表查询
3. 预分配空间
4. 处理特殊情况

## 相关题目
1. 图的遍历
2. 深拷贝链表
3. 图的连通性
4. 图的序列化与反序列化 