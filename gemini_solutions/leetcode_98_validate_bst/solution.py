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
