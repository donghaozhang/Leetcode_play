# 图是否是树

## 题目描述
给定n个节点（标号从0到n-1）和一个无向边列表，判断这个图是否是一棵树。

树的定义：
1. 连通（所有节点都相连）
2. 无环（任意两点之间只有一条路径）

## 示例
输入:
```
n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
```
输出: true
解释: 这是一棵有效的树，所有节点都连通且没有环。

## 解题思路

### 方法一：BFS + 连通性检查
1. **核心思想**
   - 检查边数是否为n-1
   - 使用BFS检查连通性
   - 如果满足以上条件则是树

2. **实现细节**
```python
def is_valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
        
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    queue = deque([0])
    visited.add(0)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited) == n
```

### 方法二：并查集
1. **核心思想**
   - 检查边数是否为n-1
   - 使用并查集检测环
   - 合并过程中如果发现已连通则有环

2. **实现细节**
```python
def is_valid_tree_union_find(n, edges):
    if len(edges) != n - 1:
        return False
    
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False
        parent[root_x] = root_y
        return True
    
    return all(union(u, v) for u, v in edges)
```

## 复杂度分析
1. **BFS方法**
   - 时间复杂度：O(V + E)
   - 空间复杂度：O(V)

2. **并查集方法**
   - 时间复杂度：O(E * α(N))，其中α是阿克曼函数的反函数
   - 空间复杂度：O(V)

## 代码实现要点
1. 检查边数条件
2. 构建无向图
3. 检查连通性
4. 检测环的存在

## 常见错误
1. 未检查边数
2. 忽略连通性检查
3. 未处理无向边
4. 并查集实现错误

## 优化策略
1. 路径压缩
2. 提前返回
3. 使用邻接表
4. 优化并查集实现

## 相关题目
1. 冗余连接
2. 连通分量的数量
3. 最小生成树
4. 树的直径 