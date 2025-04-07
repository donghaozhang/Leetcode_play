# tree_traversal.md)
  - 先序遍历 / Pre-order Traversal [LeetCode 144]

## Problem Description

## Problem Description

### Binary Tree Preorder Traversal
#### Problem #144

Given the `root` of a binary tree, return _the preorder traversal of its nodes' values_.

**Example 1:**
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```
**Example 2:**
```
Input: root = []
Output: []
```
**Example 3:**
```
Input: root = [1]
Output: [1]
```

**Constraints:**

* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Solution

## Problem Explanation

The problem requires performing a pre-order traversal on a given binary tree and returning the values of the nodes in the order they are visited. Pre-order traversal visits the current node before its child nodes, following the order: root, left subtree, right subtree.

## Step-by-Step Approach

1. **Understand Pre-order Traversal**: In pre-order traversal, we first visit the root node, then traverse the left subtree, and finally the right subtree.
   
2. **Recursive Approach**: The recursive solution is straightforward. We define a function that visits the current node and then recursively calls itself on the left and right children of the node.

3. **Iterative Approach**: For the iterative solution, we use a stack to mimic the recursive call stack. We start by pushing the root node onto the stack. Then, we enter a loop where we pop a node from the stack, visit it, and push its right and left children (if they exist) onto the stack in that order. This ensures that we visit the left subtree before the right subtree.

## Python Solution

### Recursive Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """Recursive solution for pre-order traversal."""
        def traverse(node: TreeNode) -> list[int]:
            if not node:
                return []
            return [node.val] + traverse(node.left) + traverse(node.right)
        
        return traverse(root)
```

### Iterative Solution

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        """Iterative solution for pre-order traversal."""
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Push right child first so it's processed after the left child
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
```

## Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of nodes in the binary tree, since we visit each node once.
- **Space Complexity**:
  - For the recursive solution, O(H), where H is the height of the binary tree, due to the recursive call stack. In the worst case (when the tree is skewed), H = N, so the space complexity can be O(N).
  - For the iterative solution, O(N) in the worst case when the tree is skewed, as we might need to store all nodes in the stack.

## Test Cases

To verify the solution, we can use the following test cases:

```python
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Constructing the tree: [1, null, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 3])

    def test_example2(self):
        # Empty tree
        root = None
        self.assertEqual(self.solution.preorderTraversal(root), [])

    def test_example3(self):
        # Tree with single node: [1]
        root = TreeNode(1)
        self.assertEqual(self.solution.preorderTraversal(root), [1])

    def test_balanced_tree(self):
        # Constructing a balanced tree: [1, 2, 3, 4, 5, 6, 7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 4, 5, 3, 6, 7])

if __name__ == "__main__":
    unittest.main()
```

These test cases cover various scenarios, including an empty tree, a tree with a single node, and more complex tree structures, ensuring the solution is robust and correct.