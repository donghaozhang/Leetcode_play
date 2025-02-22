# 僵尸矩阵

## 题目描述
给定一个二维网格，其中：
- 0 表示人类
- 1 表示僵尸
- 2 表示墙

每天，僵尸可以感染上、下、左、右四个方向相邻的人类。求所有人类被感染需要多少天。
如果无法感染所有人类，返回 -1。

## 示例
输入:
```
[
    [0, 1, 2, 0, 0],
    [1, 0, 0, 2, 1],
    [0, 1, 0, 0, 0]
]
```
输出: 2
解释: 需要2天才能感染所有人类。

## 解题思路

### 矩阵BFS
1. **核心思想**
   - 使用BFS同时从所有僵尸位置开始扩散
   - 记录感染过程中的天数
   - 统计是否所有人类都被感染

2. **实现细节**
```python
def zombie_in_matrix(grid):
    rows, cols = len(grid), len(grid[0])
    humans = 0
    queue = deque()
    
    # 初始化
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                humans += 1
            elif grid[i][j] == 1:
                queue.append((i, j, 0))
    
    # BFS过程
    while queue:
        row, col, day = queue.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 0):
                grid[new_row][new_col] = 1
                humans -= 1
                queue.append((new_row, new_col, day + 1))
```

## 复杂度分析
- 时间复杂度：O(M × N)，其中M和N是矩阵的行数和列数
- 空间复杂度：O(M × N)，用于存储队列

### 复杂度分析详解
1. **时间复杂度**
   - 初始化遍历：O(M × N)
   - BFS过程：O(M × N)
   - 每个位置最多被访问一次

2. **空间复杂度**
   - 队列存储：O(M × N)
   - 原地修改矩阵，不需要额外空间

## 代码实现要点
1. 正确统计人类数量
2. 同时处理多个起始点
3. 记录感染天数
4. 处理边界情况

## 常见错误
1. 未检查边界条件
2. 忘记统计人类数量
3. 天数计算错误
4. 未处理无法感染情况

## 优化策略
1. 提前检测特殊情况
2. 使用方向数组简化代码
3. 原地修改减少空间使用
4. 优化队列操作

## 相关题目
1. 岛屿数量
2. 腐烂的橘子
3. 矩阵中的最短路径
4. 墙与门 