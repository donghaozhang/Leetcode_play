# minimum_subtree.md)
- 最近公共祖先 / Lowest Common Ancestor [LeetCode 236]

## Problem Description

Here is the full description of LeetCode problem #236, "Lowest Common Ancestor of a Binary Tree":

---

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

**Constraints:**

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

---

## Solution

### Problem Explanation
The problem requires finding the lowest common ancestor (LCA) of two given nodes in a binary tree. The LCA is the lowest node in the tree that has both nodes as descendants (where a node can be a descendant of itself). 

For example, in the first example, the LCA of nodes 5 and 1 is 3 because 3 is the lowest node that has both 5 and 1 as descendants. In the second example, the LCA of 5 and 4 is 5 because 5 is an ancestor of itself and also an ancestor of 4.

### Approach
1. **Recursive Traversal**: We can perform a recursive post-order traversal of the tree. The idea is to search for the nodes `p` and `q` in the left and right subtrees.
2. **Base Cases**:
   - If the current node is `None`, return `None`.
   - If the current node is either `p` or `q`, return the current node.
3. **Recursive Cases**:
   - Recursively search the left and right subtrees.
   - If both left and right recursive calls return non-null values, it means the current node is the LCA.
   - If only one of the recursive calls returns a non-null value, return that value (indicating that one of the nodes was found in that subtree).
   - If both return `None`, return `None`.

### Solution Code
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right

# Test cases
def build_tree(arr, p_val, q_val):
    if not arr:
        return None, None, None
    nodes = [None if val is None else TreeNode(val) for val in arr]
    root = nodes[0]
    p_node = None
    q_node = None
    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
            if node.val == p_val:
                p_node = node
            if node.val == q_val:
                q_node = node
    return root, p_node, q_node

# Example 1
arr1 = [3,5,1,6,2,0,8,None,None,7,4]
root1, p1, q1 = build_tree(arr1, 5, 1)
sol = Solution()
print(sol.lowestCommonAncestor(root1, p1, q1).val)  # Output: 3

# Example 2
arr2 = [3,5,1,6,2,0,8,None,None,7,4]
root2, p2, q2 = build_tree(arr2, 5, 4)
print(sol.lowestCommonAncestor(root2, p2, q2).val)  # Output: 5

# Example 3
arr3 = [1,2]
root3, p3, q3 = build_tree(arr3, 1, 2)
print(sol.lowestCommonAncestor(root3, p3, q3).val)  # Output: 1
```

### Explanation
1. **TreeNode Class**: Defines the structure of a binary tree node.
2. **Solution Class**: Contains the method `lowestCommonAncestor` which implements the recursive approach to find the LCA.
3. **build_tree Function**: Helper function to construct a binary tree from a list and locate nodes `p` and `q` based on their values.
4. **Test Cases**: 
   - **Example 1**: The LCA of nodes 5 and 1 is 3.
   - **Example 2**: The LCA of nodes 5 and 4 is 5.
   - **Example 3**: The LCA of nodes 1 and 2 is 1.

### Time and Space Complexity
- **Time Complexity**: O(N), where N is the number of nodes in the tree. In the worst case, we might visit all nodes.
- **Space Complexity**: O(H), where H is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), the space complexity is O(N).

This approach efficiently finds the LCA by leveraging recursive traversal and checking for the presence of nodes `p` and `q` in the subtrees.