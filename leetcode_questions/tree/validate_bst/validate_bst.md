# Validate Binary Search Tree

## Problem Description
Given a binary tree, determine if it is a valid binary search tree (BST).

A binary search tree is defined as:
1. The left subtree of a node contains only nodes with values less than the node's value
2. The right subtree of a node contains only nodes with values greater than the node's value
3. Both the left and right subtrees must also be binary search trees

## Examples
Input:
```
    5
   / \
  3   7
 / \ / \
1  4 6  8
```
Output: true

Input:
```
    5
   / \
  3   7
 / \ / \
1  4 2  8
```
Output: false
Explanation: Node 7's left child (2) is less than the root node value (5)

## Solution Approach

### Recursive Range Validation
1. **Core Idea**
   - Maintain a valid value range for each node
   - Recursively validate each node
   - Pass range constraints top-down

2. **Implementation Details**
```python
def validate(node, min_val, max_val):
    if not node:
        return True
        
    if node.val <= min_val or node.val >= max_val:
        return False
        
    return validate(node.left, min_val, node.val) and \
           validate(node.right, node.val, max_val)
```

### Inorder Traversal Method (Optional)
1. **Core Idea**
   - BST inorder traversal produces a sorted sequence
   - Keep track of the previous node's value
   - Verify if the sequence maintains ascending order

## Complexity Analysis
- Time Complexity: O(N), each node is visited once
- Space Complexity: O(H), where H is the height of the tree (recursive stack depth)

## Implementation Key Points
1. Correctly maintain value ranges
2. Handle empty node cases
3. Consider boundary values
4. Avoid integer overflow

## Common Mistakes
1. Only validating against parent nodes
2. Not considering equality cases
3. Incorrect range validation
4. Ignoring empty tree cases

## Optimization Strategies
1. Iterative implementation
2. Inorder traversal optimization
3. Early return for invalid cases
4. Special value handling

## Related Problems
1. Lowest Common Ancestor in a BST
2. Kth Smallest Element in a BST
3. Successor in BST
4. Recover BST

---

# 验证二叉搜索树

## 题目描述
给定一个二叉树，判断其是否是一个有效的二叉搜索树（BST）。

二叉搜索树定义：
1. 节点的左子树只包含小于当前节点的数
2. 节点的右子树只包含大于当前节点的数
3. 所有左子树和右子树自身必须也是二叉搜索树

## 示例
输入:
```
    5
   / \
  3   7
 / \ / \
1  4 6  8
```
输出: true

输入:
```
    5
   / \
  3   7
 / \ / \
1  4 2  8
```
输出: false
解释: 节点7的左子节点2小于根节点5

## 解题思路

### 递归验证范围
1. **核心思想**
   - 维护每个节点的有效值范围
   - 递归验证每个节点
   - 自顶向下传递范围约束

2. **实现细节**
```python
def validate(node, min_val, max_val):
    if not node:
        return True
        
    if node.val <= min_val or node.val >= max_val:
        return False
        
    return validate(node.left, min_val, node.val) and \
           validate(node.right, node.val, max_val)
```

### 中序遍历法（可选）
1. **核心思想**
   - BST的中序遍历是升序序列
   - 记录前一个节点的值
   - 验证是否保持升序

## 复杂度分析
- 时间复杂度：O(N)，每个节点访问一次
- 空间复杂度：O(H)，H是树的高度，递归栈深度

## 代码实现要点
1. 正确维护值范围
2. 处理空节点情况
3. 考虑边界值
4. 避免整数溢出

## 常见错误
1. 只验证与父节点的关系
2. 未考虑相等的情况
3. 范围判断错误
4. 忽略空树情况

## 优化策略
1. 使用迭代实现
2. 中序遍历优化
3. 提前返回无效情况
4. 处理特殊值

## 相关题目
1. 二叉搜索树的最近公共祖先
2. 二叉搜索树的第k小元素
3. 二叉搜索树的后继者
4. 恢复二叉搜索树 