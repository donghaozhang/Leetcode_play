# binary_tree_paths.md)
- 平衡二叉树 / Balanced Binary Tree [LeetCode 110]

## Problem Description

## Problem Description

### Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

#### Example 1:
```
    3
   / \
  9  20
     /  \
    15   7
```
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `true`

#### Example 2:
```
     1
    / \
   2   2
  / \
 3   3
/ \
4   4
```
**Input:** `root = [1,2,2,3,3,null,null,4,4]`
**Output:** `false`

#### Example 3:
**Input:** `root = []`
**Output:** `true`

#### Constraints:
* The number of nodes in the tree is in the range `[0, 5000]`.
* `-10^4 <= Node.val <= 10^4`

## Solution

**Problem Explanation**

The problem requires determining whether a given binary tree is height-balanced. A binary tree is considered height-balanced if the absolute difference between the heights of its left and right subtrees does not exceed 1 for any node in the tree.

### Key Insights

* To check if a binary tree is height-balanced, we need to calculate the height of its left and right subtrees for every node.
* A binary tree is height-balanced if the absolute difference between the heights of its left and right subtrees does not exceed 1.
* We can use a recursive approach to calculate the height of the subtrees and check if the tree is height-balanced.

### Step-by-Step Approach

1. **Define a helper function to calculate the height of a subtree**: This function will recursively calculate the height of a subtree. If the subtree is not height-balanced, it will return -1.
2. **Check if the current tree is height-balanced**: Calculate the heights of the left and right subtrees. If the absolute difference between their heights exceeds 1, return -1.
3. **Recursively check the left and right subtrees**: If the current tree is height-balanced, recursively check if the left and right subtrees are height-balanced.
4. **Return the result**: If the current tree and its subtrees are height-balanced, return true; otherwise, return false.

### Python Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            """Return the height of the subtree rooted at node if it's balanced; otherwise, return -1."""
            if node is None:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1

# Helper function to create a binary tree from a list
def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1:
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    print(solution.isBalanced(root1))  # Expected output: True
    
    # Example 2:
    root2 = create_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(solution.isBalanced(root2))  # Expected output: False
    
    # Example 3:
    root3 = create_tree([])
    print(solution.isBalanced(root3))  # Expected output: True
```

### Time and Space Complexity Analysis

* **Time complexity**: O(n), where n is the number of nodes in the binary tree. We visit each node once.
* **Space complexity**: O(h), where h is the height of the binary tree. This is the maximum depth of the recursion call stack. In the worst case (when the tree is skewed), h = n. In the average case (when the tree is balanced), h = log(n).

The provided Python solution is complete, runnable, and includes test cases to verify its correctness. It uses a recursive approach to check if a binary tree is height-balanced and calculates the height of the subtrees. The time and space complexity analysis is also provided.