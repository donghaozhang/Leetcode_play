# preorder_traversal.py)
  - 中序遍历 / In-order Traversal [LeetCode 94]

## Problem Description

## Binary Tree Inorder Traversal
Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

### Example 1:
```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
```
### Example 2:
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```
### Example 3:
```
Input: root = []
Output: []
```

### Constraints:
* The number of nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Solution

**Problem Explanation**
=======================

The problem requires performing an in-order traversal of a given binary tree and returning the values of the nodes in the correct order. In-order traversal visits the left subtree, the current node, and then the right subtree.

**Step-by-Step Approach**
-------------------------

### Recursive Approach

1.  Define a recursive function that takes a node as input.
2.  If the node is `None`, return an empty list.
3.  Recursively traverse the left subtree and store the result.
4.  Append the value of the current node to the result.
5.  Recursively traverse the right subtree and append the result to the current result.
6.  Return the final result.

### Iterative Approach

1.  Initialize an empty stack to store nodes and an empty list to store the result.
2.  Start with the root node.
3.  While the current node is not `None` or the stack is not empty:
    *   If the current node is not `None`, push it to the stack and move to its left child.
    *   If the current node is `None`, pop a node from the stack, append its value to the result, and move to its right child.
4.  Return the result.

**Python Solution**
-------------------

### Recursive Solution

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        """Recursive solution for in-order traversal."""
        def traverse(node: TreeNode) -> list[int]:
            if node is None:
                return []
            return traverse(node.left) + [node.val] + traverse(node.right)

        return traverse(root)
```

### Iterative Solution

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        """Iterative solution for in-order traversal."""
        result = []
        stack = []
        current = root

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result
```

**Time and Space Complexity Analysis**
--------------------------------------

*   **Recursive Solution:**
    *   Time complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
    *   Space complexity: O(n) due to the recursive call stack in the worst case (when the tree is skewed).
*   **Iterative Solution:**
    *   Time complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
    *   Space complexity: O(n) due to the explicit stack used to store nodes in the worst case (when the tree is skewed).

**Test Cases**
--------------

```python
import unittest

class TestInorderTraversal(unittest.TestCase):
    def test_example1(self):
        # Construct the binary tree: [4,2,5,1,3]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1, 2, 3, 4, 5])

    def test_example2(self):
        # Construct the binary tree: [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1, 3, 2])

    def test_example3(self):
        # Empty tree
        root = None

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [])

    def test_single_node(self):
        # Single node tree
        root = TreeNode(1)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1])

if __name__ == "__main__":
    unittest.main()
```

You can run these test cases to verify the correctness of the provided solutions. Both the recursive and iterative solutions should pass all the test cases.