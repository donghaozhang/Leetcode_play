# binary_tree_paths.md)
- 平衡二叉树 / Balanced Binary Tree [LeetCode 110]

## Problem Description

**110. Balanced Binary Tree**

Given a binary tree, determine if it is height-balanced.

A **height-balanced** binary tree is defined as:
- A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**
```
Input: root = []
Output: true
```

**Constraints:**
- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Solution

### Explanation of the Problem

A balanced binary tree is one where, for every node in the tree, the heights of its left and right subtrees differ by no more than 1. This property must hold for all nodes in the tree, not just the root. 

For example:
- In **Example 1**, the tree is balanced because the left subtree of the root (height 1) and the right subtree (height 2) differ by 1, and all other nodes also satisfy the condition.
- In **Example 2**, the tree is not balanced because at the node with value 2, the left subtree has a height of 2 (nodes 3 and 4), while the right subtree is missing (height 0), leading to a difference of 2, which violates the condition.

### Step-by-Step Approach

1. **Base Case**: If the tree is empty (i.e., `root` is `None`), it is balanced by definition.
2. **Height Calculation**: For each node, calculate the height of its left and right subtrees.
3. **Balance Check**: Check if the absolute difference between the heights of the left and right subtrees is more than 1. If it is, the tree is not balanced.
4. **Recursive Check**: Recursively check if both the left and right subtrees are balanced.
5. **Return Result**: The tree is balanced only if both the current node and all its subtrees are balanced.

### Solution Code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1

# Test cases
def test_isBalanced():
    solution = Solution()
    
    # Example 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution.isBalanced(root1) == True
    
    # Example 2: Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    assert solution.isBalanced(root2) == False
    
    # Example 3: Empty tree
    root3 = None
    assert solution.isBalanced(root3) == True
    
    # Additional test case: Single node
    root4 = TreeNode(1)
    assert solution.isBalanced(root4) == True
    
    # Additional test case: Left-heavy unbalanced
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    assert solution.isBalanced(root5) == False
    
    print("All test cases pass")

test_isBalanced()
```

### Time and Space Complexity Analysis

- **Time Complexity**: O(n), where n is the number of nodes in the tree. Each node is visited once to compute its height and check the balance condition.
- **Space Complexity**: O(h), where h is the height of the tree. This is due to the recursion stack, which can go up to h in the worst case (for a skewed tree, h = n; for a balanced tree, h = log n).

### Test Cases

1. **Example 1**: A balanced tree where the left and right subtrees of the root differ in height by 1.
   - Input: `[3,9,20,null,null,15,7]`
   - Output: `True`

2. **Example 2**: An unbalanced tree where the left subtree of one node has a height difference of 2.
   - Input: `[1,2,2,3,3,null,null,4,4]`
   - Output: `False`

3. **Example 3**: An empty tree.
   - Input: `[]`
   - Output: `True`

4. **Additional Test Case**: A single node tree.
   - Input: `[1]`
   - Output: `True`

5. **Additional Test Case**: A left-heavy unbalanced tree.
   - Input: `[1,2,null,3]`
   - Output: `False`

The provided solution efficiently checks the balance condition for all nodes in the tree while minimizing redundant calculations by combining the height computation and balance check in a single pass.