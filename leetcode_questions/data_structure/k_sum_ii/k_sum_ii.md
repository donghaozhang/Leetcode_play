# K数之和 II

## 题目描述
给定 n 个不同的正整数，整数 k (1 <= k <= n)，以及目标数 target。在这 n 个数里面找出 k 个数，使得这 k 个数的和等于目标数 target，要求找出所有可能的 k 个数的组合。

## 示例
输入:
```
numbers = [1,2,3,4]
k = 2
target = 5
```
输出: [[1,4], [2,3]]

## 与 Combination Sum 的区别

### 1. 元素使用规则
- **Combination Sum**：每个数字可以重复使用多次
- **K Sum II**：每个数字最多只能使用一次

### 2. 组合大小限制
- **Combination Sum**：组合大小不限
- **K Sum II**：必须恰好使用 k 个数字

### 3. 剪枝策略
- **Combination Sum**：基于目标和剪枝
- **K Sum II**：可以同时基于 k 和目标和剪枝
  - 当前组合大小超过 k 时可以提前返回
  - 剩余数字不足 k 个时可以提前返回

## 解题思路

### 回溯法
1. **核心思想**
   - 从每个位置开始尝试选择数字
   - 维护当前已选数字个数和当前和
   - 同时满足 k 个数和目标和时记录结果

2. **剪枝优化**
   ```python
   def backtrack(start, curr_k, curr_sum, path):
       # 剪枝条件
       if curr_k > k:  # 使用数字过多
           return
       if curr_sum > target:  # 和超过目标
           return
       if len(numbers) - start < k - curr_k:  # 剩余数字不足
           return
       
       if curr_k == k and curr_sum == target:
           result.append(path[:])
           return
   ```

### 复杂度分析
- 时间复杂度：O(C(n,k))，其中 C(n,k) 是组合数
- 空间复杂度：O(k)，递归深度为 k

## 代码实现要点
1. 正确维护计数器(k)和当前和
2. 高效剪枝
3. 避免重复组合
4. 注意递归终止条件

## 优化可能
1. 排序后剪枝
2. 双向搜索
3. 动态规划变体
4. 位运算优化

## 应用场景
1. 投资组合选择
2. 团队人员分配
3. 资源优化配置
4. 数据分析聚类

## 常见错误
1. 剪枝条件不完整
2. 未正确处理 k 的限制
3. 组合大小判断错误
4. 重复使用数字

## 相关题目
1. K Sum
2. 3Sum
3. 4Sum
4. Combination Sum 