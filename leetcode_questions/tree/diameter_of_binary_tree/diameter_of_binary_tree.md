# Diameter of Binary Tree / 二叉树的直径 [LeetCode 543]

## Problem / 问题

### English

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

**Example 1:**
```
    1
   / \
  2   3
 / \
4   5
```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

**Example 2:**
```
  1
 /
2
```
Input: root = [1,2]
Output: 1

**Constraints:**
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100

### 中文

给定一棵二叉树的根节点 `root`，返回该树的直径。

二叉树的直径是指任意两个节点之间最长路径的长度。这条路径可能经过也可能不经过根节点。

两个节点之间的路径长度由它们之间的边数表示。

**示例 1：**
```
    1
   / \
  2   3
 / \
4   5
```
输入：root = [1,2,3,4,5]
输出：3
解释：路径 [4,2,1,3] 或 [5,2,1,3] 的长度为 3。

**示例 2：**
```
  1
 /
2
```
输入：root = [1,2]
输出：1

**约束条件：**
- 树中节点数目的范围为 [1, 10^4]。
- -100 <= Node.val <= 100

## Solution / 解决方案

### English

The diameter of a binary tree is essentially the longest path between any two leaf nodes. This path can be visualized as going up from one leaf to a common ancestor, then down to another leaf. 

#### Approach: Recursive Depth-First Search (DFS)

The key insight is that for any node, the diameter that passes through it is the sum of:
- The maximum depth of its left subtree
- The maximum depth of its right subtree

To find the diameter of the entire tree, we need to find the node that gives the maximum sum of left and right subtree depths.

#### Algorithm
1. Define a recursive function `maxdepth` that calculates the maximum depth of a node
2. For each node, compute the maximum depths of its left and right subtrees
3. Update a global variable `result` to keep track of the maximum diameter found so far
4. The diameter at a node is the sum of its left and right subtree depths
5. Return the maximum depth of the current node (max of left and right + 1)

#### Time Complexity
- O(n) where n is the number of nodes in the tree, as we visit each node exactly once

#### Space Complexity
- O(h) where h is the height of the tree, due to the recursion stack

#### Key Insights
- The height of a leaf node is 0
- The diameter of a node with no children is 0
- The diameter may not pass through the root of the tree
- We need to check every node as a potential "highest point" of the diameter

### 中文

二叉树的直径本质上是任意两个叶节点之间的最长路径。这条路径可以被视为从一个叶节点向上到达一个共同祖先，然后向下到另一个叶节点。

#### 方法：递归深度优先搜索 (DFS)

关键的见解是，对于任何节点，通过它的直径是：
- 其左子树的最大深度
- 其右子树的最大深度
的总和。

要找到整棵树的直径，我们需要找到那个左右子树深度之和最大的节点。

#### 算法
1. 定义一个递归函数 `maxdepth`，计算节点的最大深度
2. 对于每个节点，计算其左右子树的最大深度
3. 更新全局变量 `result` 以跟踪到目前为止发现的最大直径
4. 节点处的直径是其左右子树深度的总和
5. 返回当前节点的最大深度（左右深度的最大值 + 1）

#### 时间复杂度
- O(n)，其中 n 是树中的节点数，因为我们恰好访问每个节点一次

#### 空间复杂度
- O(h)，其中 h 是树的高度，这是由于递归栈的开销

#### 关键见解
- 叶节点的高度为 0
- 没有子节点的节点的直径为 0
- 直径可能不经过树的根节点
- 我们需要检查每个节点作为直径的潜在"最高点" 