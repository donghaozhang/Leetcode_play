# 最大平均值子树

## 题目描述
给定一棵二叉树，找到具有最大平均值的子树。返回该子树的根节点。
子树的平均值是子树中所有节点值的总和除以节点数。

## 示例
输入:
```
     1
    / \
   5   3
  /   / \
 4   2   6
```
输出: 节点3
解释: 节点3的子树（包含节点3、2、6）的平均值为 (3 + 2 + 6) / 3 = 3.67，是所有子树中最大的。

## 解题思路

### DFS后序遍历
1. **核心思想**
   - 使用后序遍历计算每个子树的和与节点数
   - 同时维护全局最大平均值
   - 返回子树和与节点数供父节点使用

2. **状态定义**
   - sum: 子树节点值之和
   - count: 子树节点数量
   - max_avg: 当前找到的最大平均值
   - result: 最大平均值子树的根节点

### 实现细节
```python
def dfs(node):
    if not node:
        return 0, 0
        
    left_sum, left_count = dfs(node.left)
    right_sum, right_count = dfs(node.right)
    
    curr_sum = left_sum + right_sum + node.val
    curr_count = left_count + right_count + 1
    
    curr_avg = curr_sum / curr_count
    if curr_avg > max_avg:
        max_avg = curr_avg
        result = node
        
    return curr_sum, curr_count
```

## 复杂度分析
- 时间复杂度：O(N)，每个节点只访问一次
- 空间复杂度：O(H)，H是树的高度，递归栈的深度

## 代码实现要点
1. 正确计算子树和与节点数
2. 维护全局最大平均值
3. 处理空节点情况
4. 处理负值节点

## 常见错误
1. 计算平均值时的除零错误
2. 未考虑负值节点
3. 未正确更新全局最大值
4. 子树和计算错误

## 优化策略
1. 使用元组返回多个值
2. 及早判断空节点
3. 使用nonlocal访问外部变量
4. 避免重复计算

## 相关题目
1. 二叉树的最大路径和
2. 平衡二叉树
3. 二叉树中的最大路径和
4. 统计完全二叉树节点个数 