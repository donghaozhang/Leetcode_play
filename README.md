# LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。每个题目都包含了详细的解题思路和 Python 实现。


## Dynamic Programming

- 最长上升子序列 / Longest Increasing Subsequence - [Python](leetcode_questions/dynamic_programming/longest_increasing_subsequence/longest_increasing_subsequence.py) - [题解](leetcode_questions/dynamic_programming/longest_increasing_subsequence/longest_increasing_subsequence.md)
- 回文子串 / Palindrome Substring - Python - [题解](leetcode_questions/dynamic_programming/palindrome/palindrome_substring.md)
- 石子游戏 / Stone Game - [Python](leetcode_questions/dynamic_programming/stone_game/stone_game.py) - [题解](leetcode_questions/dynamic_programming/stone_game/stone_game.md)
- 戳气球 / Burst Balloons - [Python](leetcode_questions/dynamic_programming/burst_balloons/burst_balloons.py) - [题解](leetcode_questions/dynamic_programming/burst_balloons/burst_balloons.md)
- 三角形最小路径和 / Triangle - [Python](leetcode_questions/dynamic_programming/triangle/triangle.py) - [题解](leetcode_questions/dynamic_programming/triangle/triangle.md)
- 解码方法 / Decode Ways - [Python](leetcode_questions/dynamic_programming/decode_ways/decode_ways.py) - [题解](leetcode_questions/dynamic_programming/decode_ways/decode_ways.md)
- 复制书籍 / Copy Books - [Python](leetcode_questions/dynamic_programming/copy_books/copy_books.py) - [题解](leetcode_questions/dynamic_programming/copy_books/copy_books.md)
- 最大整除子集 / Largest Divisible Subset - [Python](leetcode_questions/dynamic_programming/largest_divisible_subset/largest_divisible_subset.py) - [题解](leetcode_questions/dynamic_programming/largest_divisible_subset/largest_divisible_subset.md)

## String Processing

- 通配符匹配 / Wildcard Matching - [Python](leetcode_questions/string_processing/wildcard_matching/wildcard_matching.py) - [题解](leetcode_questions/string_processing/wildcard_matching/wildcard_matching.md)
- 编辑距离 / Edit Distance - [Python](leetcode_questions/string_processing/edit_distance/edit_distance.py) - [题解](leetcode_questions/string_processing/edit_distance/edit_distance.md)
- 单词拆分 / Word Break - [Python](leetcode_questions/string_processing/word_break/word_break.py) - [题解](leetcode_questions/string_processing/word_break/word_break.md)

## Data Structure

- 最大栈 / Max Stack - [Python](leetcode_questions/data_structure/max_stack/max_stack.py) - [题解](leetcode_questions/data_structure/max_stack/max_stack.md)
- 用两个队列实现栈 / Stack Using Two Queues - [Python](leetcode_questions/data_structure/stack_by_two_queues/stack_by_two_queues.py) - [题解](leetcode_questions/data_structure/stack_by_two_queues/stack_by_two_queues.md)
- 用两个栈实现队列 / Queue Using Two Stacks - [Python](leetcode_questions/data_structure/queue_by_two_stacks/queue_by_two_stacks.py) - [题解](leetcode_questions/data_structure/queue_by_two_stacks/queue_by_two_stacks.md)

## Backtracking

- N皇后 II / N-Queens II - [Python](leetcode_questions/backtracking/n_queens/n_queens_ii.py)
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


## Game Theory

- Bash游戏 / Bash Game - [Python](leetcode_questions/game_theory/bash_game/bash_game.py) - [题解](leetcode_questions/game_theory/bash_game/bash_game.md)

## Graph Search

- 骑士最短路径 / Knight Shortest Path - [Python](leetcode_questions/graph_search/knight_shortest_path/knight_shortest_path.py) - [题解](leetcode_questions/graph_search/knight_shortest_path/knight_shortest_path.md)
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

