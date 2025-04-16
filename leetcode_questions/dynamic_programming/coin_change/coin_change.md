# Coin Change / 零钱兑换 [LeetCode 322]

## Problem / 问题

### English

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**
```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**
```
Input: coins = [1], amount = 0
Output: 0
```

**Constraints:**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

### 中文

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

**示例 1：**
```
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```

**示例 2：**
```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**
```
输入：coins = [1], amount = 0
输出：0
```

**约束条件：**
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Solution / 解决方案

### English

This problem is a classic dynamic programming problem, specifically an example of the "coin change" or "minimum coin" problem.

#### Approach: Dynamic Programming

We can solve this problem using dynamic programming with the following steps:

1. Define a DP array `dp` where `dp[i]` represents the minimum number of coins needed to make up amount `i`.
2. Initialize `dp[0] = 0` (no coins needed to make up amount 0) and all other values to infinity (float('inf') or amount+1).
3. Iterate through each coin denomination:
   - For each amount from the coin value to the target amount:
     - Update `dp[i] = min(dp[i], dp[i-coin] + 1)`, meaning we either use the current solution for amount `i` or use one coin of value `coin` plus the optimal solution for amount `i-coin`.
4. Return `dp[amount]` if it's not infinity (a solution exists), otherwise return -1.

#### Time Complexity
- O(amount * n) where n is the number of coin denominations

#### Space Complexity
- O(amount) for the DP array

#### Explanation of the Algorithm

The dynamic programming approach works by building solutions for smaller subproblems and then using them to solve the original problem:

1. We know that 0 coins are needed to make amount 0, so `dp[0] = 0`.
2. For each amount from 1 to the target amount, we consider using each coin:
   - If using a coin of value `coin` leads to a smaller number of total coins, we update our solution.
   - This means we're deciding whether to include this coin in our solution.
3. By the time we reach `dp[amount]`, we have found the minimum number of coins needed.

A key insight is that this is a "minimum" problem, where for each amount, we're finding the minimum number of coins needed.

### 中文

这个问题是一个经典的动态规划问题，特别是"零钱兑换"或"最少硬币"问题的例子。

#### 方法：动态规划

我们可以使用动态规划通过以下步骤解决这个问题：

1. 定义一个 DP 数组 `dp`，其中 `dp[i]` 表示凑成金额 `i` 所需的最少硬币数。
2. 初始化 `dp[0] = 0`（不需要硬币就能凑成金额 0）并将所有其他值设为无穷大（float('inf') 或 amount+1）。
3. 遍历每种硬币面额：
   - 对于从硬币面值到目标金额的每个金额：
     - 更新 `dp[i] = min(dp[i], dp[i-coin] + 1)`，意思是我们要么使用当前的金额 `i` 的解决方案，要么使用一枚面值为 `coin` 的硬币加上金额 `i-coin` 的最优解决方案。
4. 如果 `dp[amount]` 不是无穷大（存在解决方案），则返回它，否则返回 -1。

#### 时间复杂度
- O(amount * n)，其中 n 是硬币面额的数量

#### 空间复杂度
- O(amount) 用于 DP 数组

#### 算法解释

动态规划方法通过构建更小子问题的解决方案，然后使用它们来解决原始问题：

1. 我们知道凑成金额 0 需要 0 个硬币，所以 `dp[0] = 0`。
2. 对于从 1 到目标金额的每个金额，我们考虑使用每枚硬币：
   - 如果使用面值为 `coin` 的硬币能够导致更少的总硬币数，我们就更新解决方案。
   - 这意味着我们正在决定是否在解决方案中包含这枚硬币。
3. 当我们达到 `dp[amount]` 时，我们已经找到了所需的最少硬币数。

关键的见解是这是一个"最小"问题，对于每个金额，我们都在寻找所需的最少硬币数。 