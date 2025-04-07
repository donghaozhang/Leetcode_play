# inorder_traversal.py)
  - 后序遍历 / Post-order Traversal [LeetCode 145]

## Problem Description

## Problem Description

### Binary Tree Postorder Traversal
#### Problem #145

Given the `root` of a binary tree, return _the postorder traversal of its nodes' values_.

**Example 1:**
```
Input: root = [1,null,2,3]
Output: [3,2,1]
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

* The number of the nodes in the tree is in the range `[0, 100]`.
* `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Solution

## Problem Explanation

The problem requires performing a postorder traversal on a given binary tree and returning the values of the nodes in the correct order. Postorder traversal visits the left subtree, then the right subtree, and finally the root node.

## Step-by-Step Approach

1. **Understand Postorder Traversal**: Postorder traversal visits nodes in the following order: left subtree, right subtree, and then the root. This can be achieved recursively or iteratively.

2. **Recursive Approach**: 
   - Traverse the left subtree.
   - Traverse the right subtree.
   - Visit the root node.

3. **Iterative Approach**: To solve it iteratively, we can use a stack to mimic the recursive call stack. However, since we need to visit the root after its children, we have to be careful about the order in which we push nodes onto the stack and process them.

4. **Using Two Stacks**: One way to achieve postorder traversal iteratively is by using two stacks. The first stack is used to store nodes to be processed, and the second stack is used to store the result in reverse postorder (root, right, left). We then pop from the second stack to get the postorder traversal.

5. **Using One Stack**: Another iterative method involves using one stack and keeping track of the last visited node to determine whether we are returning from the left or right subtree.

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
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def traverse(node):
            if node is None:
                return []
            return traverse(node.left) + traverse(node.right) + [node.val]
        
        return traverse(root)
```

### Iterative Solution Using Two Stacks

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        return stack2[::-1]
```

### Iterative Solution Using One Stack

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        
        result = []
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        
        return result
```

## Time and Space Complexity Analysis

- **Recursive Solution**: 
  - Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
  - Space Complexity: O(n) due to the recursive call stack in the worst case (when the tree is skewed).

- **Iterative Solution Using Two Stacks**:
  - Time Complexity: O(n), as we visit each node once.
  - Space Complexity: O(n), for storing nodes in the two stacks.

- **Iterative Solution Using One Stack**:
  - Time Complexity: O(n), as each node is pushed and popped from the stack once.
  - Space Complexity: O(n), for the stack.

## Test Cases

To verify the correctness of the solutions, we can use the following test cases:

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
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_example2(self):
        # Empty tree
        root = None
        self.assertEqual(self.solution.postorderTraversal(root), [])

    def test_example3(self):
        # Tree with one node: [1]
        root = TreeNode(1)
        self.assertEqual(self.solution.postorderTraversal(root), [1])

    def test_balanced_tree(self):
        # Constructing a balanced tree: [1, 2, 3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [2, 3, 1])

if __name__ == "__main__":
    unittest.main()
```

These test cases cover various scenarios, including an empty tree, a tree with one node, and trees with multiple nodes, ensuring the solutions are robust.