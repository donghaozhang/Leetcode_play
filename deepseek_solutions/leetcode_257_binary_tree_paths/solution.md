# level_order_traversal.md)

### 其他树问题
- 二叉树路径 / Binary Tree Paths [LeetCode 257]

## Problem Description

Here is the full description of LeetCode problem #257 "Binary Tree Paths":

---

Given the `root` of a binary tree, return all root-to-leaf paths in **any order**.

A **leaf** is a node with no children.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg)

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Example 2:**

```
Input: root = [1]
Output: ["1"]
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 100]`.
- `-100 <= Node.val <= 100`

--- 

Let me know if you'd like any clarification or assistance with solving this problem!

## Solution

### Explanation of the Problem

The problem requires us to find all root-to-leaf paths in a binary tree and return them as strings in the format "root->child->...->leaf". A leaf is defined as a node with no children (both left and right are null). The order of the paths in the output doesn't matter.

For example, in the first example:
- The tree has root 1, left child 2 (which has a right child 5), and right child 3.
- The paths are:
  - 1 -> 2 -> 5
  - 1 -> 3
- These are returned as ["1->2->5", "1->3"].

### Approach
To solve this problem, we can use a Depth-First Search (DFS) approach to traverse the tree. As we traverse, we keep track of the current path from the root to the current node. When we reach a leaf node (a node with no children), we add the current path to our result list.

1. **Initialize**: Start with an empty list to store the result paths.
2. **DFS Traversal**: Traverse the tree recursively:
   - If the current node is a leaf (both left and right children are null), add the current path to the result.
   - Otherwise, recursively traverse the left and right children, appending the current node's value to the path before moving to the children.
3. **Path Construction**: Construct the path string by joining node values with "->".

### Solution Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        def dfs(node, path, res):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
            dfs(node.left, path, res)
            dfs(node.right, path, res)
            path.pop()
        
        res = []
        dfs(root, [], res)
        return res
```

### Explanation
- **TreeNode Class**: Defines the structure of a binary tree node with `val`, `left`, and `right` attributes.
- **binaryTreePaths Function**: This function initializes the result list and starts the DFS traversal.
- **DFS Helper Function**: 
  - **Base Case**: If the node is `None`, return immediately.
  - **Path Construction**: The current node's value is added to the path list as a string.
  - **Leaf Check**: If the node is a leaf (no left or right children), the current path is joined into a string and added to the result list.
  - **Recursive Traversal**: The function recursively processes the left and right children. After processing both children, the current node's value is removed from the path (backtracking) to maintain the correct path for other branches.
- **Result Handling**: The result list, containing all root-to-leaf paths, is returned.

### Time and Space Complexity
- **Time Complexity**: O(N), where N is the number of nodes in the tree. Each node is visited exactly once.
- **Space Complexity**: O(H), where H is the height of the tree. This accounts for the recursion stack. In the worst case (a skewed tree), this is O(N), but for a balanced tree, it's O(log N).

### Test Cases
```python
# Test Case 1
# Tree:
#     1
#    / \
#   2   3
#    \
#     5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root1))  # Expected: ["1->2->5", "1->3"]

# Test Case 2
# Tree:
#     1
root2 = TreeNode(1)
print(Solution().binaryTreePaths(root2))  # Expected: ["1"]

# Test Case 3
# Tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root3))  # Expected: ["1->2->4", "1->2->5", "1->3"]

# Test Case 4: Empty Tree (shouldn't happen per constraints, but handled)
root4 = None
print(Solution().binaryTreePaths(root4))  # Expected: []

# Test Case 5: Single path
# Tree:
#     1
#    /
#   2
#  /
# 3
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.left.left = TreeNode(3)
print(Solution().binaryTreePaths(root5))  # Expected: ["1->2->3"]
```

These test cases cover various scenarios, including a simple tree, a single node, a more complex tree with multiple leaves, and edge cases like an empty tree (though the constraints say the tree has at least one node). The solution efficiently handles all these cases.