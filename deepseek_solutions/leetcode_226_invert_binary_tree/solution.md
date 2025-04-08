# subtree_maximum_average.md)
- 翻转二叉树 / Invert Binary Tree [LeetCode 226]

## Problem Description

Here is the full description of LeetCode problem #226, "Invert Binary Tree," as it appears on LeetCode:

---

Given the `root` of a binary tree, invert the tree, and return its root.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

**Example 3:**

```
Input: root = []
Output: []
```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

--- 

Let me know if you'd like any further clarification or assistance!

## Solution

### Explanation of the Problem
The problem requires us to invert a binary tree, which means swapping the left and right children of every node in the tree. This operation should be performed recursively for all nodes in the tree. The inversion should start from the root and propagate down to all the leaf nodes.

### Approach
1. **Base Case**: If the root is `None`, return `None` because an empty tree cannot be inverted.
2. **Recursive Case**: For the current node, swap its left and right children.
3. **Recursion**: Recursively invert the left subtree and the right subtree.
4. **Return the Root**: After inverting both subtrees, return the root of the now inverted tree.

This approach uses a depth-first search (DFS) strategy to traverse the tree and invert each node's children. The time complexity is O(n), where n is the number of nodes in the tree, because each node is visited exactly once. The space complexity is O(h), where h is the height of the tree, due to the recursion stack. In the worst case (a skewed tree), the space complexity becomes O(n).

### Solution Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Helper function to print the tree in level order (for testing)
def printLevelOrder(root):
    if not root:
        print("[]")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    print(result)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    print("Original tree (Example 1):")
    printLevelOrder(root1)
    inverted_root1 = solution.invertTree(root1)
    print("Inverted tree (Example 1):")
    printLevelOrder(inverted_root1)
    
    # Example 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print("Original tree (Example 2):")
    printLevelOrder(root2)
    inverted_root2 = solution.invertTree(root2)
    print("Inverted tree (Example 2):")
    printLevelOrder(inverted_root2)
    
    # Example 3
    root3 = None
    print("Original tree (Example 3):")
    printLevelOrder(root3)
    inverted_root3 = solution.invertTree(root3)
    print("Inverted tree (Example 3):")
    printLevelOrder(inverted_root3)
```

### Test Cases
1. **Example 1**:
   - Input: `[4,2,7,1,3,6,9]`
   - Output: `[4,7,2,9,6,3,1]`
   - Explanation: The left and right children of every node are swapped.

2. **Example 2**:
   - Input: `[2,1,3]`
   - Output: `[2,3,1]`
   - Explanation: The left and right children of the root are swapped.

3. **Example 3**:
   - Input: `[]`
   - Output: `[]`
   - Explanation: An empty tree remains empty after inversion.

The provided solution correctly inverts the binary tree for all test cases, demonstrating the expected behavior. The helper function `printLevelOrder` is used to print the tree in level order for verification.