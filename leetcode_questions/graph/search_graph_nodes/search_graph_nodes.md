# 搜索图中节点

## 题目描述
给定一个无向图，一个起始节点，以及每个节点对应的值，找到距离目标值target最近的节点。
如果有多个节点的值与target的差值相同，返回值较小的那个节点。

## 示例
输入:
```
{1,2,3,4,5}, // 节点
{3,5,7,1,2}, // 对应的值
1,           // 起始节点
4            // 目标值
```
输出: 1
解释: 差值为1的节点有1(|3-4|=1)和5(|5-4|=1)，返回值较小的节点1。

## 解题思路

### BFS + 最近值更新
1. **核心思想**
   - 使用BFS遍历图
   - 维护当前找到的最接近target的节点
   - 遇到更接近的节点时更新结果

2. **实现细节**
```python
def search_nearest_node(graph, values, node, target):
    queue = deque([node])
    visited = {node}
    nearest_node = node
    min_diff = abs(values[node] - target)
    
    while queue:
        curr = queue.popleft()
        curr_diff = abs(values[curr] - target)
        
        # 更新最接近的节点
        if curr_diff < min_diff or \
           (curr_diff == min_diff and values[curr] < values[nearest_node]):
            min_diff = curr_diff
            nearest_node = curr
            
        # 访问邻居节点
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## 复杂度分析
- 时间复杂度：O(V + E)，其中V是节点数，E是边数
- 空间复杂度：O(V)，用于存储访问集合和队列

### 复杂度分析详解
1. **时间复杂度**
   - BFS遍历：O(V + E)
   - 值比较：O(1)
   - 总体：O(V + E)

2. **空间复杂度**
   - 访问集合：O(V)
   - 队列：O(V)
   - 总体：O(V)

## 代码实现要点
1. 正确实现BFS遍历
2. 维护最近值更新
3. 处理相等差值情况
4. 处理边界条件

## 常见错误
1. 未处理空图情况
2. 忘记更新最近节点
3. 未考虑相等差值
4. 访问集合使用错误

## 优化策略
1. 提前返回
2. 优化差值计算
3. 减少不必要的比较
4. 使用更高效的数据结构

## 相关题目
1. 最近公共祖先
2. 单词接龙
3. 二叉搜索树中最接近的值
4. 图的最短路径 