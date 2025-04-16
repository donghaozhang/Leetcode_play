# Binary Tree Maximum Path Sum

## Problem Description

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum **path sum** of any **non-empty** path.

## Examples

**Example 1:**
```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

**Example 2:**
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 3 * 10^4]`.
- `-1000 <= Node.val <= 1000`

## Approach

### English

This problem can be solved using depth-first search (DFS) with a recursive approach. The key insight is understanding that any path in a binary tree can be represented by a subtree rooted at a node, possibly including just one of its branches or both branches.

The algorithm follows these steps:

1. Implement a recursive helper function `max_gain(node)` that calculates the maximum path sum with the given node as the highest point.
2. At each node, calculate the maximum gain from its left and right subtrees. We take the maximum of the gain and 0 because if the gain is negative, we're better off not including that path.
3. For each node, there are two possibilities:
   - The node is part of the maximum path, but not the highest point - in this case, we can only choose one branch to continue the path upwards.
   - The node is the highest point of the maximum path - in this case, we can include both left and right branches.
4. Keep track of the maximum path sum found so far in a global variable.
5. Return the maximum path sum.

### Chinese

这个问题可以使用深度优先搜索（DFS）与递归方法解决。关键的洞察是理解二叉树中的任何路径都可以表示为以一个节点为根的子树，可能包括其中一个分支或两个分支。

算法步骤如下：

1. 实现一个递归辅助函数 `max_gain(node)`，计算以给定节点为最高点的最大路径和。
2. 在每个节点，计算其左右子树的最大增益。我们取增益和0的最大值，因为如果增益为负，我们最好不包括该路径。
3. 对于每个节点，有两种可能性：
   - 该节点是最大路径的一部分，但不是最高点 - 在这种情况下，我们只能选择一个分支向上继续路径。
   - 该节点是最大路径的最高点 - 在这种情况下，我们可以包括左右两个分支。
4. 在全局变量中跟踪迄今为止发现的最大路径和。
5. 返回最大路径和。

## Complexity Analysis

### English

- **Time Complexity**: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once.
- **Space Complexity**: O(H), where H is the height of the binary tree. This represents the maximum recursive call stack depth. In the worst case (a skewed tree), this could be O(N).

### Chinese

- **时间复杂度**：O(N)，其中 N 是二叉树中的节点数。每个节点恰好被访问一次。
- **空间复杂度**：O(H)，其中 H 是二叉树的高度。这表示最大递归调用栈深度。在最坏的情况下（偏斜树），这可能是 O(N)。 