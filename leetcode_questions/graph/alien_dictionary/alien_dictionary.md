# 外星文字典

## 题目描述
有一种外星文字典，其中的字母顺序未知。给定一个按照字典序排序的单词列表，推导出这种外星文字典中字母的顺序。
要求返回字典序最小的有效拓扑序。

## 示例
输入:
```
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
```
输出: "wertf"
解释: 从单词的排序中可以推导出字母顺序 w < e < r < t < f

## 解题思路

### 最小堆 + 拓扑排序
1. **核心思想**
   - 使用最小堆保证字典序最小
   - 从相邻单词提取顺序关系
   - 通过拓扑排序构建结果

2. **实现细节**
```python
def alien_dictionary(words):
    # 构建图和入度表
    graph = defaultdict(set)
    indegrees = defaultdict(int)
    
    # 提取顺序关系
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
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
```

## 复杂度分析
- 时间复杂度：O(V + E + VlogV)，其中V是字符数，E是边数
- 空间复杂度：O(V + E)，用于存储图和堆

### 复杂度分析详解
1. **时间复杂度**
   - 构建图：O(N * K)，N是单词数，K是最长单词长度
   - 堆操作：O(VlogV)
   - 总体：O(NK + VlogV)

2. **空间复杂度**
   - 邻接表：O(E)
   - 入度表：O(V)
   - 最小堆：O(V)

## 代码实现要点
1. 正确提取字符顺序
2. 使用最小堆维护顺序
3. 处理特殊情况
4. 检测无效序列

## 常见错误
1. 未检查前缀违规
2. 图构建错误
3. 未处理环
4. 未返回最小字典序

## 优化策略
1. 提前检测无效情况
2. 优化字符提取
3. 减少堆操作
4. 优化图的表示

## 相关题目
1. 拓扑排序
2. 课程表
3. 字典序排列
4. 最小字典序 