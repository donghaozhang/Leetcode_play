# minimum_subtree.md)
- 最近公共祖先 / Lowest Common Ancestor [LeetCode 236]

## Problem Description

## Problem Description

### Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

#### Example 1:

```
      3
     / \
    5   1
   / \   \
  6   2   0
     / \
    7   4
```

Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 1`
Output: `3`
Explanation: The LCA of nodes 5 and 1 is 3.

#### Example 2:

```
      3
     / \
    5   1
   / \   \
  6   2   0
     / \
    7   4
```

Input: `root = [3,5,1,6,2,0,8,null,null,7,4]`, `p = 5`, `q = 4`
Output: `5`
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

#### Example 3:

Input: `root = [1,2]`, `p = 1`, `q = 2`
Output: `1`

#### Constraints:

* The number of nodes in the tree is in the range `[2, 10^5]`.
* `-10^9 <= Node.val <= 10^9`
* All `Node.val` are **unique**.
* `p != q`
* `p` and `q` will exist in the tree.

## Solution

## Problem Explanation

The problem requires finding the lowest common ancestor (LCA) of two given nodes in a binary tree. The LCA is defined as the lowest node that has both nodes as descendants, where a node can be a descendant of itself.

## Step-by-Step Approach

1. **Understand the Problem**: We need to find the LCA of two nodes in a binary tree.
2. **Identify the Approach**: We can solve this problem using a recursive approach. The idea is to traverse the tree and find the LCA by checking if the current node is one of the given nodes or if it has both nodes as descendants in its left and right subtrees.
3. **Base Cases**:
   - If the tree is empty (`root` is `None`), return `None`.
   - If the current node is one of the given nodes (`p` or `q`), return the current node.
4. **Recursive Case**:
   - Recursively search for `p` and `q` in the left and right subtrees of the current node.
   - If both `p` and `q` are found in different subtrees, the current node is the LCA.
   - If both `p` and `q` are found in the left subtree, the LCA is in the left subtree.
   - If both `p` and `q` are found in the right subtree, the LCA is in the right subtree.
   - If neither `p` nor `q` is found in the left or right subtree, return `None`.
5. **Handle Edge Cases**: The problem statement guarantees that `p` and `q` exist in the tree and are distinct.

## Python Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the tree is empty, return None
        if not root:
            return None
        
        # If the current node is one of the given nodes, return the current node
        if root == p or root == q:
            return root
        
        # Recursively search for p and q in the left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are found in different subtrees, the current node is the LCA
        if left_lca and right_lca:
            return root
        
        # If both p and q are found in the left subtree, the LCA is in the left subtree
        if left_lca:
            return left_lca
        
        # If both p and q are found in the right subtree, the LCA is in the right subtree
        if right_lca:
            return right_lca
        
        # If neither p nor q is found in the left or right subtree, return None
        return None

def main():
    # Create the binary tree for Example 1
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   0
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node 5
    q = root.right  # Node 1
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 3

    # Create the binary tree for Example 2
    # Same as Example 1
    p = root.left  # Node 5
    q = root.left.right.right  # Node 4
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 5

    # Create the binary tree for Example 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    p = root  # Node 1
    q = root.left  # Node 2
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 1

if __name__ == "__main__":
    main()
```

## Time and Space Complexity Analysis

*   **Time Complexity**: O(N), where N is the number of nodes in the binary tree. In the worst case, we visit each node once.
*   **Space Complexity**: O(H), where H is the height of the binary tree. This is due to the recursive call stack. In the worst case (when the tree is skewed), H = N. In the average case (when the tree is balanced), H = log(N).

## Test Cases

The provided Python solution includes test cases for Examples 1, 2, and 3. You can run the `main` function to verify the correctness of the solution. Additional test cases can be added to cover more scenarios.