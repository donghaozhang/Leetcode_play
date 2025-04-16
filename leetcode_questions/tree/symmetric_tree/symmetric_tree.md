# Symmetric Tree / 对称二叉树 [LeetCode 101]

## Problem / 问题

### English

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example 1:**
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
Input: root = [1,2,2,3,4,4,3]
Output: true

**Example 2:**
```
    1
   / \
  2   2
   \   \
   3    3
```
Input: root = [1,2,2,null,3,null,3]
Output: false

**Constraints:**
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

### 中文

给你一个二叉树的根节点 root，检查它是否轴对称。

**示例 1：**
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
输入：root = [1,2,2,3,4,4,3]
输出：true

**示例 2：**
```
    1
   / \
  2   2
   \   \
   3    3
```
输入：root = [1,2,2,null,3,null,3]
输出：false

**约束条件：**
- 树中的节点数目范围：[1, 1000]
- -100 <= Node.val <= 100

## Solution / 解决方案

### English

This problem can be solved using both recursive and iterative approaches.

#### Recursive Approach

The intuition is to check if the left subtree is a mirror reflection of the right subtree:
1. Two trees are a mirror reflection of each other if:
   - Their root nodes have the same value
   - The left subtree of one tree is the mirror reflection of the right subtree of the other tree

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

#### Iterative Approach

We can also solve this problem iteratively using a queue:
1. Initialize a queue with the left and right subtrees of the root
2. For each pair of nodes we dequeue:
   - If both are null, continue
   - If one is null and the other is not, return false
   - If their values don't match, return false
   - Enqueue the left child of the left subtree with the right child of the right subtree
   - Enqueue the right child of the left subtree with the left child of the right subtree

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(n) in the worst case

### 中文

这个问题可以使用递归和迭代两种方法解决。

#### 递归方法

直观上，我们需要检查左子树是否是右子树的镜像反射：
1. 两棵树互为镜像反射，需要满足：
   - 它们的根节点具有相同的值
   - 一棵树的左子树是另一棵树的右子树的镜像反射

时间复杂度：O(n)，其中 n 是树中节点的数量
空间复杂度：O(h)，其中 h 是树的高度（由于递归栈）

#### 迭代方法

我们也可以使用队列通过迭代方式解决这个问题：
1. 用根节点的左右子树初始化队列
2. 对于每一对出队的节点：
   - 如果两者都为空，继续
   - 如果一个为空而另一个不为空，返回 false
   - 如果它们的值不匹配，返回 false
   - 将左子树的左子节点与右子树的右子节点入队
   - 将左子树的右子节点与右子树的左子节点入队

时间复杂度：O(n)，其中 n 是树中节点的数量
空间复杂度：最坏情况下为 O(n) 