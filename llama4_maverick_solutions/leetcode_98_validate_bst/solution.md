# invert_binary_tree.md)
- 验证二叉搜索树 / Validate BST [LeetCode 98]

## Problem Description

## Problem Description
### Validate Binary Search Tree
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

* The left subtree of a node contains only nodes with keys **less than** the node's key.
* The right subtree of a node contains only nodes with keys **greater than** the node's key.
* Both the left and right subtrees must also be binary search trees.

#### Example 1:
```
    2
   / \
  1   3
```
**Input:** `root = [2,1,3]`
**Output:** `true`

#### Example 2:
```
    5
   / \
  1   4
     / \
    3   6
```
**Input:** `root = [5,1,4,null,null,3,6]`
**Output:** `false`
**Explanation:** The root node's value is 5 but its right child's value is 4.

#### Constraints:
* The number of nodes in the tree is in the range `[1, 10^4]`.
* `-2^31 <= Node.val <= 2^31 - 1`

## Solution

## Problem Explanation
The problem requires validating whether a given binary tree is a binary search tree (BST) or not. A binary search tree is a binary tree where for every node, the values in the left child are less than the node's value and the values in the right child are greater than the node's value. Both the left and right subtrees must also be binary search trees.

## Step-by-Step Approach
1. **Define the properties of a BST**: Understand that for a tree to be a BST, each node's value must be greater than all values in its left subtree and less than all values in its right subtree.
2. **Choose a traversal method**: We can validate a BST by performing an in-order traversal. In an in-order traversal, we visit the left subtree, the current node, and then the right subtree. In a BST, an in-order traversal yields a sorted sequence of node values.
3. **Check for sorted order**: During the in-order traversal, keep track of the previous node's value. If the current node's value is not greater than the previous node's value, the tree is not a BST.
4. **Handle edge cases**: Consider trees with one node or empty trees. A tree with one node is a valid BST, and an empty tree can be considered a valid BST.

## Python Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, node):
        if node is None:
            return True
        
        # Traverse left subtree
        if not self.inorder(node.left):
            return False
        
        # Check if current node's value is greater than the previous node's value
        if self.prev is not None and node.val <= self.prev.val:
            return False
        
        # Update previous node
        self.prev = node
        
        # Traverse right subtree
        return self.inorder(node.right)

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
    root1 = create_tree([2, 1, 3])
    print(solution.isValidBST(root1))  # Expected output: True
    
    # Example 2:
    root2 = create_tree([5, 1, 4, None, None, 3, 6])
    print(solution.isValidBST(root2))  # Expected output: False
    
    # Test case with a single node
    root3 = create_tree([1])
    print(solution.isValidBST(root3))  # Expected output: True
    
    # Test case with an empty tree
    root4 = create_tree([])
    print(solution.isValidBST(root4))  # Expected output: True (considering an empty tree as a valid BST for this implementation)
```

## Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the number of nodes in the tree. This is because we visit each node once during the in-order traversal.
- **Space Complexity**: O(N) in the worst case (when the tree is skewed) due to the recursive call stack. For a balanced tree, the space complexity is O(log N) due to the height of the tree.

## Test Cases
The provided Python solution includes test cases to verify its correctness:
1. Example 1 from the problem statement: A valid BST `[2, 1, 3]`.
2. Example 2 from the problem statement: An invalid BST `[5, 1, 4, None, None, 3, 6]`.
3. A tree with a single node `[1]`.
4. An empty tree `[]`.