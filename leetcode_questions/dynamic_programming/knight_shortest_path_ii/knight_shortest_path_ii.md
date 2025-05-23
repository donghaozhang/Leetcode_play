# 骑士最短路径 II（滚动数组优化）

## 题目描述
在一个 m × n 的棋盘上，骑士只能向右移动（不能向左），求从左上角到右下角的最短路径长度。骑士可以按照以下四种方式移动：
1. 向右2步，向上1步
2. 向右2步，向下1步
3. 向右1步，向上2步
4. 向右1步，向下2步

棋盘上有一些位置可能有障碍物。

## 示例
输入:
```
[
  [true, true, true],
  [true, true, true],
  [true, true, true]
]
```
输出: 3

## 解题思路

### 动态规划 + 滚动数组
由于骑士只能向右移动，我们可以按列进行动态规划，并使用滚动数组优化空间：

1. **状态定义**
   - dp[i][j] 表示从起点到位置(i,j)的最短路径长度
   - 由于只需要前一列的信息，可以用两个数组交替使用

2. **状态转移**
   原始方程：
   ```
   dp[i][j] = min{dp[i-1][j-2], dp[i+1][j-2], dp[i-2][j-1], dp[i+2][j-1]} + 1
   ```
   滚动数组优化后：
   ```
   dp[curr][i] = min{dp[prev][i-1], dp[prev][i+1], dp[prev][i-2], dp[prev][i+2]} + 1
   ```
   其中 curr = j % 2, prev = 1 - curr

3. **滚动数组实现**
   - 只保留两列数据
   - 使用 j % 2 确定当前使用哪个数组
   - 每次计算新列时，重置当前列的值

### 为什么可以使用滚动数组？
- 计算当前位置时只依赖于前一列和前两列的状态
- 计算完一列后，更早的列的信息就不再需要了
- 两个数组交替使用可以覆盖所有需要的状态

### 复杂度分析
- 时间复杂度：O(m*n)
  - 需要遍历每个格子一次
  - 每个格子的计算是O(1)
- 空间复杂度：O(m)
  - 只需要保存两列的数据
  - 相比原始方法的O(m*n)有显著改善

## 代码实现要点
1. 正确处理滚动数组的索引
2. 注意边界条件和障碍物的处理
3. 初始化时要考虑无法到达的情况
4. 每次计算新列时要重置当前列的值 