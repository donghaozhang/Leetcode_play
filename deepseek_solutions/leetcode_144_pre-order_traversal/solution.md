# tree_traversal.md)
  - 先序遍历 / Pre-order Traversal [LeetCode 144]

## Problem Description

Here is the full description of LeetCode problem #144, "Binary Tree Preorder Traversal":

---

**Problem #144: Binary Tree Preorder Traversal**

Given the `root` of a binary tree, return the *preorder traversal* of its nodes' values.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

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

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

--- 

The problem asks for the preorder traversal of a binary tree, where the traversal order is: root node, left subtree, right subtree. The examples and constraints are provided to clarify the input/output expectations and limits.

## Solution

### Explanation of the Problem
The problem requires performing a preorder traversal of a binary tree. In preorder traversal, we visit nodes in the following order:
1. **Root**: Process the current node.
2. **Left subtree**: Recursively traverse the left subtree.
3. **Right subtree**: Recursively traverse the right subtree.

Given the root of a binary tree, we need to return a list of node values in the order they are visited during the traversal.

### Approaches
1. **Recursive Approach**:
   - The recursive solution is straightforward. We start by processing the root node, then recursively traverse the left subtree, followed by the right subtree.
   - **Time Complexity**: O(n), where n is the number of nodes, as each node is visited exactly once.
   - **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (a skewed tree), this becomes O(n).

2. **Iterative Approach**:
   - The iterative approach uses a stack to simulate the recursion. We start by pushing the root node onto the stack. While the stack is not empty, we pop a node, process it, and push its right and left children onto the stack (right first so that left is processed first).
   - **Time Complexity**: O(n), as each node is visited exactly once.
   - **Space Complexity**: O(h), where h is the height of the tree, due to the stack usage. In the worst case, this is O(n).

### Solution Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive solution
        def recursive_helper(node, result):
            if node:
                result.append(node.val)
                recursive_helper(node.left, result)
                recursive_helper(node.right, result)
        
        result = []
        recursive_helper(root, result)
        return result

        # Uncomment below for iterative solution
        # if not root:
        #     return []
        # stack = [root]
        # result = []
        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return result
```

### Explanation
1. **Recursive Solution**:
   - The `recursive_helper` function takes a node and the result list. If the node is not `None`, it appends the node's value to the result, then recursively processes the left and right children.
   - The initial call starts with the root node, and the result list is built as the recursion progresses.

2. **Iterative Solution** (commented in the code):
   - The stack is initialized with the root node. While the stack is not empty, the top node is popped, and its value is added to the result.
   - The right child is pushed first, followed by the left child, ensuring that the left child is processed next (since stacks are LIFO).

### Test Cases
```python
# Test Case 1
# Input: root = [1,null,2,3]
# Expected Output: [1,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().preorderTraversal(root))  # Output: [1, 2, 3]

# Test Case 2
# Input: root = []
# Expected Output: []
root = None
print(Solution().preorderTraversal(root))  # Output: []

# Test Case 3
# Input: root = [1]
# Expected Output: [1]
root = TreeNode(1)
print(Solution().preorderTraversal(root))  # Output: [1]
```

### Time and Space Complexity
- **Recursive Solution**:
  - **Time Complexity**: O(n) - Each node is visited once.
  - **Space Complexity**: O(h) - Where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), it's O(n).

- **Iterative Solution**:
  - **Time Complexity**: O(n) - Each node is visited once.
  - **Space Complexity**: O(h) - Where h is the height of the tree, due to the stack. In the worst case, it's O(n).

Both approaches efficiently solve the problem, with the iterative method being preferred when avoiding recursion is necessary (e.g., deep trees causing stack overflow).