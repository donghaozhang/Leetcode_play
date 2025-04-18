# 石头碰撞

## 题目描述
给出 N 个石头及其大小数组，每次选 2 个石头进行碰撞，大小分别为 x, y。
碰撞之后会变成一个石头，大小变为 |x - y|。
直到石头个数 < 2 为止，问最后剩下来的石头最小是多少？

## 示例
输入: [2, 7, 4, 1, 8, 1]
输出: 1
解释: 
- 选择 7 和 8，|7-8| = 1
- 现在石头为 [2, 4, 1, 1, 1]
- 选择 2 和 4，|2-4| = 2
- 现在石头为 [2, 1, 1, 1]
- 选择 2 和 1，|2-1| = 1
- 现在石头为 [1, 1, 1]
- 选择 1 和 1，|1-1| = 0
- 现在石头为 [1]
最后剩下 1

## 解题思路

### 贪心 + 优先队列
为了使最后的石头尽可能小，我们应该：

1. **贪心策略**
   - 每次选择最大的两块石头碰撞
   - 这样可以最大程度减小石头的大小

2. **实现方法**
   - 使用最大堆（优先队列）维护石头大小
   - 每次取出最大的两块石头
   - 将碰撞后的石头放回堆中

### 为什么这样是正确的？
1. **最优性证明**
   - 如果不选最大的石头，剩下的石头会更大
   - 每次碰撞都尽可能减小最大的石头
   - 这样可以得到最小的最终结果

2. **终止条件**
   - 当石头数量小于2时停止
   - 如果还有石头，其大小就是答案
   - 如果没有石头，返回0

### 复杂度分析
- 时间复杂度：O(nlogn)
  - 建堆需要O(n)
  - 每次操作需要O(logn)
  - 最多进行n次操作
- 空间复杂度：O(n)
  - 需要存储所有石头
  - 优先队列的空间

## 代码实现要点
1. 使用最大堆（Python中用负数实现）
2. 正确处理碰撞后的石头
3. 处理边界情况（空数组，单个石头）
4. 注意返回值的处理
5. 考虑石头完全消失的情况 