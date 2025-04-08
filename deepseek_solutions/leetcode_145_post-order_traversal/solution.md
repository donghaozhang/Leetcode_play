# inorder_traversal.py)
  - 后序遍历 / Post-order Traversal [LeetCode 145]

## Problem Description

Here is the full description of LeetCode problem #145, "Binary Tree Postorder Traversal":

---

Given the `root` of a binary tree, return the postorder traversal of its nodes' values.

**Example 1:**

![postorder](https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg)

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

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

--- 

Let me know if you'd like any clarification or assistance with this problem!

## Solution

### Explanation of the Problem

The problem requires us to perform a postorder traversal on a binary tree and return the values of the nodes in the order they are visited. Postorder traversal follows the Left-Right-Root sequence, meaning:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the root node.

Given the constraints, we need to handle trees with up to 100 nodes, including edge cases like an empty tree (root is `None`).

### Approaches

#### 1. Recursive Approach
The recursive approach is straightforward:
- Traverse the left subtree recursively.
- Traverse the right subtree recursively.
- Append the root's value to the result list.

#### 2. Iterative Approach
The iterative approach is more complex and uses a stack to simulate the recursion. The key idea is:
- Use a stack to keep track of nodes.
- Push the root onto the stack.
- While the stack is not empty, pop a node and insert its value at the beginning of the result list (since postorder is L-R-Root, inserting at the beginning gives Root-Right-Left, which reversed is Left-Right-Root).
- Push the left child first, then the right child onto the stack (so right is processed before left when popping).

### Solution Code

#### Recursive Solution

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        def postorder(node, result):
            if node is None:
                return
            postorder(node.left, result)
            postorder(node.right, result)
            result.append(node.val)
        
        result = []
        postorder(root, result)
        return result
```

#### Iterative Solution

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.insert(0, node.val)  # Insert at the beginning
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result
```

### Time and Space Complexity Analysis

#### Recursive Solution
- **Time Complexity:** O(n) where n is the number of nodes in the tree. Each node is visited exactly once.
- **Space Complexity:** O(n) in the worst case (skewed tree), due to the recursion stack. For a balanced tree, it would be O(log n).

#### Iterative Solution
- **Time Complexity:** O(n) because each node is processed exactly once.
- **Space Complexity:** O(n) in the worst case, as the stack can hold all nodes if the tree is skewed.

### Test Cases

```python
# Test Case 1: Example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
assert Solution().postorderTraversal(root1) == [3, 2, 1]

# Test Case 2: Empty tree
root2 = None
assert Solution().postorderTraversal(root2) == []

# Test Case 3: Single node
root3 = TreeNode(1)
assert Solution().postorderTraversal(root3) == [1]

# Test Case 4: Full binary tree
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.right = TreeNode(5)
root4.right.left = TreeNode(6)
root4.right.right = TreeNode(7)
assert Solution().postorderTraversal(root4) == [4, 5, 2, 6, 7, 3, 1]
```

These test cases cover various scenarios including a simple tree, an empty tree, a single node tree, and a full binary tree to ensure the correctness of the solution.