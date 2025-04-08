# invert_binary_tree.md)
- 验证二叉搜索树 / Validate BST [LeetCode 98]

## Problem Description

**98. Validate Binary Search Tree**

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![bst1](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

![bst2](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Solution

### Explanation of the Problem
A Binary Search Tree (BST) is a binary tree where for each node:
- All nodes in the left subtree have values less than the node's value.
- All nodes in the right subtree have values greater than the node's value.
- Both the left and right subtrees must also be BSTs.

The task is to verify whether a given binary tree is a valid BST. The key insight is that an in-order traversal of a BST yields a strictly increasing sequence of values. If this property is violated at any point, the tree is not a BST.

### Approach
1. **In-Order Traversal**: Perform an in-order traversal (left-root-right) of the tree and check if the resulting list of values is strictly increasing. If not, the tree is not a BST.
2. **Recursive Validation with Bounds**: For each node, ensure its value lies within a valid range (initially negative and positive infinity). For the left child, the upper bound is the parent's value. For the right child, the lower bound is the parent's value. If any node violates these bounds, the tree is not a BST.

### Solution Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)
```

### Time and Space Complexity
- **Time Complexity**: O(N), where N is the number of nodes in the tree. Each node is visited exactly once.
- **Space Complexity**: O(N) in the worst case (skewed tree), due to the recursion stack. For a balanced tree, it would be O(log N).

### Test Cases
1. **Example 1**:
   - Input: `root = [2,1,3]` (Tree structure: 2 is root, left child 1, right child 3)
   - Output: `True`
   - Explanation: The left child is less than the root, and the right child is greater than the root.

2. **Example 2**:
   - Input: `root = [5,1,4,null,null,3,6]` (Tree structure: 5 is root, left child 1, right child 4; 4 has left child 3 and right child 6)
   - Output: `False`
   - Explanation: The right child of the root (4) is less than the root (5), but its left child (3) is less than 4, which is correct locally. However, 3 is less than 5, but it's in the right subtree of 5, which should only contain values greater than 5. Hence, the tree is not a BST.

3. **Single Node**:
   - Input: `root = [1]`
   - Output: `True`
   - Explanation: A single node trivially satisfies the BST properties.

4. **Invalid BST**:
   - Input: `root = [5,1,6,null,null,3,7]` (Tree structure: 5 is root, left child 1, right child 6; 6 has left child 3 and right child 7)
   - Output: `False`
   - Explanation: The value 3 is in the right subtree of 5 but is less than 5, violating BST properties.

5. **Valid BST with Negative Values**:
   - Input: `root = [-10,-20,0]` (Tree structure: -10 is root, left child -20, right child 0)
   - Output: `True`
   - Explanation: All nodes satisfy the BST properties.

### Running the Code
To test the code, you can create the tree structure using the `TreeNode` class and call the `isValidBST` method. For example:
```python
# Test Case 1
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().isValidBST(root))  # Output: True

# Test Case 2
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().isValidBST(root))  # Output: False
```

This approach efficiently checks the BST property by ensuring each node's value is within the valid range defined by its ancestors.