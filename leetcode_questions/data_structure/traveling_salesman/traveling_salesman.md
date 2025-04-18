# 旅行商问题 (TSP)

## 题目描述
给定n个城市和城市之间的距离矩阵，求从起点出发，访问每个城市恰好一次并返回起点的最短路径长度。
- 距离矩阵中的 -1 表示两个城市之间不可达
- 距离矩阵不一定对称（即从城市i到j的距离可能不等于从j到i的距离）

## 示例
输入:
```
n = 4
distances = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]
```
输出: 11

## 解题思路

### 状态压缩DP
1. **状态表示**
   - 使用二进制表示已访问城市集合
   - dp[state][city] 表示当前状态的最短路径

2. **状态转移**
   - 从当前城市尝试访问未访问的城市
   - 更新最短路径长度
   - 记忆化搜索避免重复计算

### 实现细节
```python
def dfs(state, curr):
    if state == (1 << n) - 1:  # 所有城市都已访问
        return distances[curr][0]  # 返回到起点的距离
        
    for next_city in range(n):
        if not visited[next_city]:
            # 尝试访问next_city
            min_dist = min(min_dist, 
                         dfs(state | (1 << next_city), next_city) + 
                         distances[curr][next_city])
```

## 复杂度分析
- 时间复杂度：O(n^2 * 2^n)
  - 状态数：2^n * n
  - 每个状态转移：O(n)
- 空间复杂度：O(n * 2^n)
  - 需要存储所有状态

## 优化策略
1. **剪枝优化**
   - 提前判断不可达情况
   - 利用三角不等式
   - 记录已知的上下界

2. **启发式搜索**
   - 贪心选择下一个城市
   - 使用最小生成树估计下界
   - 分支限界法

## 应用场景
1. 物流配送路线规划
2. 电路板钻孔优化
3. 网络布线优化
4. 机器人路径规划

## 相关变种
1. **多旅行商问题**
   - 多个起点
   - 容量限制
   - 时间窗口约束

2. **其他约束**
   - 必经点约束
   - 优先级约束
   - 时间限制

## 常见错误
1. 忽略不可达情况
2. 状态转移错误
3. 边界条件处理
4. 内存溢出

## 相关问题
1. 哈密顿回路
2. 最短路径
3. 欧拉回路
4. 中国邮递员问题

## 扩展思考
1. **近似算法**
   - 贪心算法
   - 2-opt优化
   - 遗传算法
   - 蚁群算法

2. **问题变种**
   - 多旅行商问题
   - 带时间窗的TSP
   - 带容量限制的TSP
   - 非对称TSP 