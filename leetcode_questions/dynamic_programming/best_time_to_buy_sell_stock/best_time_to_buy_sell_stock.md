# Best Time to Buy and Sell Stock / 买卖股票的最佳时机 [LeetCode 121]

## Problem / 问题

### English

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

**Constraints:**
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

### 中文

给定一个数组 `prices`，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
```
输入：prices = [7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**
```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**约束条件：**
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## Solution / 解决方案

### English

This problem can be solved using a simple one-pass algorithm which keeps track of the minimum price seen so far and the maximum profit that can be achieved.

#### Approach: One-Pass Algorithm

The key insight is that to maximize profit, we need to buy at the lowest price and sell at the highest price afterwards. We can solve this problem by:

1. Keeping track of the minimum price we've seen so far (`minlow`)
2. For each price, calculate the potential profit if we buy at the minimum price seen so far and sell at the current price
3. Update the maximum profit if the current potential profit is higher

#### Time Complexity
- O(n) where n is the number of prices - we only need to iterate through the array once

#### Space Complexity
- O(1) - we only use a constant amount of extra space

#### Algorithm Explanation

1. Initialize `minlow` to the first price in the array, and `profit` to 0
2. Iterate through the prices starting from the second price:
   - Update `minlow` to be the minimum of the current `minlow` and the current price
   - Update `profit` to be the maximum of the current `profit` and the difference between the current price and `minlow`
3. Return the final `profit`

The algorithm efficiently finds the maximum profit by keeping track of the lowest price seen so far and calculating the potential profit at each step. This works because we're only concerned with buying once and selling once to maximize profit.

### 中文

这个问题可以通过一个简单的一次遍历算法来解决，该算法会跟踪到目前为止看到的最低价格和可以获得的最大利润。

#### 方法：一次遍历算法

关键的见解是，要最大化利润，我们需要以最低的价格买入，并在之后以最高的价格卖出。我们可以通过以下方式解决这个问题：

1. 跟踪到目前为止我们看到的最低价格（`minlow`）
2. 对于每个价格，计算如果我们在到目前为止看到的最低价格买入并在当前价格卖出的潜在利润
3. 如果当前潜在利润更高，则更新最大利润

#### 时间复杂度
- O(n)，其中 n 是价格的数量 - 我们只需要遍历数组一次

#### 空间复杂度
- O(1) - 我们只使用常量数量的额外空间

#### 算法解释

1. 将 `minlow` 初始化为数组中的第一个价格，将 `profit` 初始化为 0
2. 从第二个价格开始遍历价格：
   - 将 `minlow` 更新为当前 `minlow` 和当前价格的最小值
   - 将 `profit` 更新为当前 `profit` 和当前价格与 `minlow` 之差的最大值
3. 返回最终的 `profit`

该算法通过跟踪到目前为止看到的最低价格并在每一步计算潜在利润，高效地找到最大利润。这之所以有效，是因为我们只关心一次买入和一次卖出以最大化利润。 