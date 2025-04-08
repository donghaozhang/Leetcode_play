# invert_binary_tree.md)
- 验证二叉搜索树 / Validate BST [LeetCode 98]

## Problem Description

```markdown
## 98. Validate Binary Search Tree

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:

*   The left subtree of a node contains only nodes with keys **less than** the node's key.
*   The right subtree of a node contains only nodes with keys **greater than** the node's key.
*   Both the left and right subtrees must also be binary search trees.

**Example 1:**

```
    2
   / \
  1   3
```

**Input:** root = [2,1,3]
**Output:** true

**Example 2:**

```
    5
   / \
  1   4
     / \
    3   6
```

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 10^4]`.
*   `-2^31 <= Node.val <= 2^31 - 1`
```

## Solution

Okay, let's break down the "Validate Binary Search Tree" problem.

**1. Explanation of the Problem**

The goal is to determine if a given binary tree follows the rules of a Binary Search Tree (BST). The rules are strict:

*   For *any* node in the tree:
    *   All values in its *entire* left subtree must be strictly *less than* the node's value.
    *   All values in its *entire* right subtree must be strictly *greater than* the node's value.
*   This property must hold true recursively for every node in the tree. Both the left and right subtrees must themselves be valid BSTs.

It's important to note the "entire subtree" part. A common mistake is to only check the immediate children (`node.left.val < node.val` and `node.right.val > node.val`). This is insufficient, as a node further down the subtree might violate the condition with respect to an ancestor higher up.

**2. Step-by-Step Approach**

There are two main effective approaches:

**Approach 1: Recursive Validation with Bounds**

1.  **Idea:** As we traverse down the tree, we maintain the valid range (minimum and maximum allowed values) for the current node. The root node has no initial bounds (or bounds from negative infinity to positive infinity).
2.  **Helper Function:** Create a recursive helper function, say `validate(node, lower_bound, upper_bound)`.
3.  **Base Case:** If `node` is `None`, it's a valid part of a BST, so return `True`.
4.  **Validation:** Check if the current `node.val` is within the allowed range:
    *   If `node.val <= lower_bound` or `node.val >= upper_bound`, it violates the BST property. Return `False`.
5.  **Recursive Calls:** If the current node is valid, recursively check its children with updated bounds:
    *   For the left child: The new `upper_bound` becomes the current `node.val` (since all nodes in the left subtree must be *less than* the current node). The `lower_bound` remains the same. Call `validate(node.left, lower_bound, node.val)`.
    *   For the right child: The new `lower_bound` becomes the current `node.val` (since all nodes in the right subtree must be *greater than* the current node). The `upper_bound` remains the same. Call `validate(node.right, node.val, upper_bound)`.
6.  **Result:** The function should return `True` only if the current node is valid *and* both recursive calls for the left and right subtrees return `True`.
7.  **Initial Call:** Start the process by calling the helper function on the root node with initial bounds representing negative and positive infinity: `validate(root, float('-inf'), float('inf'))`.

**Approach 2: In-order Traversal**

1.  **Idea:** A key property of a BST is that an in-order traversal (Left -> Root -> Right) visits the nodes in ascending sorted order.
2.  **Traversal:** Perform an in-order traversal of the tree.
3.  **Comparison:** During the traversal, keep track of the value of the previously visited node.
4.  **Validation:** For each currently visited node, compare its value with the previously visited node's value. If the current node's value is less than or equal to the previous node's value, the tree is not a valid BST. Return `False`.
5.  **Update:** If the current node's value is greater than the previous one, update the "previous value" to the current node's value and continue the traversal.
6.  **Result:** If the entire traversal completes without finding any violation, the tree is a valid BST. Return `True`.
7.  **Implementation:** This can be done recursively (passing the "previous" value state carefully, often using an instance variable or a mutable object) or iteratively using a stack. The iterative approach is often cleaner for managing the "previous value" state.

Let's implement the first approach (Recursive Validation with Bounds) as it directly reflects the BST definition.

**3. Python Solution**

```python
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Checks if a binary tree is a valid Binary Search Tree (BST)
        using recursive validation with bounds.
        """
        
        def validate(node: TreeNode | None, low: float, high: float) -> bool:
            """
            Helper function to recursively validate the subtree rooted at 'node'.
            Ensures node values are strictly between 'low' and 'high'.
            """
            # Base case: An empty tree (or subtree) is a valid BST.
            if not node:
                return True

            # Check current node's value against the bounds.
            # Note: BST definition requires strict inequality.
            if not (low < node.val < high):
                return False

            # Recursively validate the left and right subtrees with updated bounds.
            # Left subtree: Must be less than current node's value (new high).
            # Right subtree: Must be greater than current node's value (new low).
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Start the validation process from the root with infinite bounds.
        return validate(root, float('-inf'), float('inf'))

# Helper function to build a tree from a list (Level Order Traversal)
# Handles 'null' values.
def build_tree(nodes: list[int | None]) -> TreeNode | None:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current_node = queue.pop(0)
        
        # Process left child
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        
        if i >= len(nodes):
            break
            
        # Process right child
        if nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
        
    return root

# --- Test Cases ---
solver = Solution()

# Example 1: Valid BST
#     2
#    / \
#   1   3
tree1 = build_tree([2, 1, 3])
print(f"Input: [2, 1, 3], Output: {solver.isValidBST(tree1)}") # Expected: True

# Example 2: Invalid BST
#     5
#    / \
#   1   4
#      / \
#     3   6
tree2 = build_tree([5, 1, 4, None, None, 3, 6])
print(f"Input: [5, 1, 4, null, null, 3, 6], Output: {solver.isValidBST(tree2)}") # Expected: False

# Test Case 3: Invalid BST (Grandchild violates ancestor constraint)
#     10
#    /  \
#   5    15
#       /  \
#      6    20  (6 < 10, but 6 is in the right subtree of 10)
tree3 = build_tree([10, 5, 15, None, None, 6, 20])
print(f"Input: [10, 5, 15, null, null, 6, 20], Output: {solver.isValidBST(tree3)}") # Expected: False

# Test Case 4: Empty Tree
tree4 = build_tree([])
print(f"Input: [], Output: {solver.isValidBST(tree4)}") # Expected: True

# Test Case 5: Single Node
tree5 = build_tree([1])
print(f"Input: [1], Output: {solver.isValidBST(tree5)}") # Expected: True

# Test Case 6: Invalid BST (Equal values are not allowed by strict definition)
#     1
#    /
#   1
tree6 = build_tree([1, 1])
print(f"Input: [1, 1], Output: {solver.isValidBST(tree6)}") # Expected: False

# Test Case 7: Valid BST with negative numbers
#     0
#    /
#  -1
tree7 = build_tree([0, -1])
print(f"Input: [0, -1], Output: {solver.isValidBST(tree7)}") # Expected: True

# Test Case 8: Valid complex BST
#        8
#      /   \
#     3     10
#    / \      \
#   1   6      14
#      / \    /
#     4   7  13
tree8 = build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
print(f"Input: [8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13], Output: {solver.isValidBST(tree8)}") # Expected: True

# Test Case 9: Invalid complex BST (node 9 violates constraint with root 8)
#        8
#      /   \
#     3     10
#    / \      \
#   1   9      14  (9 > 8, but 9 is in the left subtree of 8)
tree9 = build_tree([8, 3, 10, 1, 9, None, 14])
print(f"Input: [8, 3, 10, 1, 9, null, 14], Output: {solver.isValidBST(tree9)}") # Expected: False

# Test Case 10: Max/Min Integer Values
# Using slightly smaller values for ease of representation, concept is the same
#       0
#      / \
# -2^31  2^31-1 (represented as large neg/pos numbers)
tree10 = build_tree([0, -2147483648, 2147483647])
print(f"Input: [0, -2^31, 2^31-1], Output: {solver.isValidBST(tree10)}") # Expected: True
```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. Each node is visited exactly once.
*   **Space Complexity:** O(H), where H is the height of the tree. This is due to the recursion stack.
    *   In the worst case (a skewed tree, like a linked list), the height H can be N, leading to O(N) space complexity.
    *   In the best case (a perfectly balanced tree), the height H is log N, leading to O(log N) space complexity.

**4. Test Cases Verification**

The provided Python code includes a `build_tree` helper function and several test cases to verify the `isValidBST` function:

*   **Example 1:** `[2, 1, 3]` - Valid BST. Output: `True`. Correct.
*   **Example 2:** `[5, 1, 4, null, null, 3, 6]` - Invalid (4 < 5 in right subtree). Output: `False`. Correct.
*   **Test Case 3:** `[10, 5, 15, null, null, 6, 20]` - Invalid (6 < 10 in right subtree). Output: `False`. Correct.
*   **Test Case 4:** `[]` - Empty tree is valid. Output: `True`. Correct.
*   **Test Case 5:** `[1]` - Single node is valid. Output: `True`. Correct.
*   **Test Case 6:** `[1, 1]` - Invalid (equal value). Output: `False`. Correct.
*   **Test Case 7:** `[0, -1]` - Valid. Output: `True`. Correct.
*   **Test Case 8:** `[8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]` - Valid complex tree. Output: `True`. Correct.
*   **Test Case 9:** `[8, 3, 10, 1, 9, null, 14]` - Invalid (9 > 8 in left subtree). Output: `False`. Correct.
*   **Test Case 10:** `[0, -2147483648, 2147483647]` - Valid with min/max int values. Output: `True`. Correct.

The solution correctly implements the recursive approach with bounds and passes the provided test cases.