# preorder_traversal.py)
  - 中序遍历 / In-order Traversal [LeetCode 94]

## Problem Description

Here is the full description of LeetCode problem #94, "Binary Tree Inorder Traversal":

---

Given the `root` of a binary tree, return the *inorder traversal* of its nodes' values.

**Example 1:**

![inorder_1](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,3,2]
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

## Solution

### Explanation of the Problem
The problem requires performing an **inorder traversal** of a binary tree and returning the values of the nodes in the order they are visited. In an inorder traversal, the nodes are visited in the following order:
1. Traverse the left subtree.
2. Visit the root node.
3. Traverse the right subtree.

This traversal method is commonly used to retrieve the nodes in non-decreasing order in a binary search tree (BST). However, the problem applies to any binary tree, not necessarily a BST.

### Approach
There are two primary approaches to solve this problem:
1. **Recursive Approach**: This is straightforward and leverages the call stack to keep track of the nodes. The function recursively processes the left subtree, then the root, and finally the right subtree.
2. **Iterative Approach**: This uses an explicit stack to simulate the call stack of the recursive approach. The idea is to push all left children onto the stack until there are no more left children, then pop the stack to process the node, and then move to the right child.

### Solution Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # Iterative approach using stack
        res = []
        stack = []
        current = root
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            # Current must be None at this point
            current = stack.pop()
            res.append(current.val)
            # Now visit the right subtree
            current = current.right
        return res

# Test cases
def test_inorder_traversal():
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root1) == [1, 3, 2]

    # Example 2
    root2 = None
    assert Solution().inorderTraversal(root2) == []

    # Example 3
    root3 = TreeNode(1)
    assert Solution().inorderTraversal(root3) == [1]

    # Additional test case: left-heavy tree
    root4 = TreeNode(3)
    root4.left = TreeNode(1)
    root4.left.right = TreeNode(2)
    assert Solution().inorderTraversal(root4) == [1, 2, 3]

    print("All test cases pass")

test_inorder_traversal()
```

### Explanation
1. **Iterative Approach**:
   - **Initialization**: Start with an empty result list and an empty stack. The `current` node is set to the root of the tree.
   - **Traversal**:
     - **Left Subtree**: Push all left children of the current node onto the stack until there are no more left children. This ensures that the leftmost node is processed first.
     - **Process Node**: Once the leftmost node is reached, pop it from the stack, add its value to the result list, and move to its right child.
     - **Right Subtree**: If the right child exists, repeat the process for the right subtree. This ensures the inorder sequence (left-root-right).
   - **Termination**: The loop continues until both the stack is empty and the `current` node is `None`, indicating all nodes have been processed.

2. **Complexity Analysis**:
   - **Time Complexity**: O(n), where n is the number of nodes in the tree. Each node is visited exactly once.
   - **Space Complexity**: O(n) in the worst case (when the tree is a linear chain, i.e., each node has only a left child), as the stack will hold all nodes.

### Test Cases
- **Example 1**: A tree with root 1, right child 2, and left child of 2 being 3. The inorder traversal should be [1, 3, 2].
- **Example 2**: An empty tree should return an empty list.
- **Example 3**: A single node tree returns [1].
- **Additional Test Case**: A left-heavy tree to ensure the traversal correctly processes left, root, and right nodes in order.

This solution efficiently handles the inorder traversal iteratively, addressing the follow-up challenge to avoid recursion.