# LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。每个题目都包含了详细的解题思路和 Python 实现。


## Backtracking

- 全子集 / Subsets [LintCode 17] - [题目链接](http://www.lintcode.com/problem/subsets) - [Python](leetcode_questions/backtracking/subsets/subsets.py) - [题解](leetcode_questions/backtracking/subsets/subsets.md)
```
给定一个整数数组，返回其所有可能的子集。

注意：
1. 子集中的元素必须是非降序的
2. 解集不能包含重复的子集
3. 空集是所有集合的子集

例如：
输入：[1,2,3]
输出：
[
  [],
  [1],
  [1,2],
  [1,2,3],
  [1,3],
  [2],
  [2,3],
  [3]
]

解题思路：
可以用两种方式构建搜索树：
1. 组合式搜索树：每个节点代表是否选择当前数字
2. 排列式搜索树：每层代表枚举下一个可以选择的数字
```


## Graph Search

- 单词接龙 / Word Ladder [LintCode 120] - [题目链接](https://www.lintcode.com/problem/word-ladder/) - [Python](leetcode_questions/graph_search/word_ladder/word_ladder.py) - [题解](leetcode_questions/graph_search/word_ladder/word_ladder.md)
```
给出两个单词（start和end）和一个字典，找出从start到end的最短转换序列。
规则：
1. 每次只能改变一个字母
2. 变换过程中的每个单词都必须在字典中出现
3. start可以不在字典中
4. 返回最短转换序列的长度

例如：
- start = "hit"
- end = "cog"
- dict = ["hot","dot","dog","lot","log"]
返回 5
最短转换序列是: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
```


## Math

- 快速幂 / Fast Power [LintCode 140] - [Python](leetcode_questions/math/fast_power/fast_power.py) - [题解](leetcode_questions/math/fast_power/fast_power.md)
```
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

要求时间复杂度为 O(log n)。

示例：
输入: x = 2.00000, n = 10
输出: 1024.00000

解题思路：
1. 递归方法：将指数二分，递归计算
2. 迭代方法：利用二进制思想，按位计算
```

