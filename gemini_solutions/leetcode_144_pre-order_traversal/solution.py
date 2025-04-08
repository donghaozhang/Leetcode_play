import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solves the Binary Tree Preorder Traversal problem iteratively.
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative preorder traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of node values in preorder.
        """
        if not root:
            return []

        result = []
        # Use a list as a stack (LIFO)
        stack = [root]

        while stack:
            # Pop the next node to visit
            node = stack.pop()

            # Visit the node (add its value to the result)
            result.append(node.val)

            # Push the right child first (if exists) so it's processed after the left
            if node.right:
                stack.append(node.right)

            # Push the left child last (if exists) so it's processed next
            if node.left:
                stack.append(node.left)

        return result

# --- Helper function to build tree from list (for testing) ---
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes):
            # Process right child
            if nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1: root = [1,null,2,3]
# Tree structure:
#    1
#     \
#      2
#     /
#    3
root1 = build_tree([1, None, 2, 3])
expected1 = [1, 2, 3]
result1 = solver.preorderTraversal(root1)
print(f"Test Case 1: Input: [1, null, 2, 3], Output: {result1}, Expected: {expected1}")
assert result1 == expected1

# Example 2: root = []
root2 = build_tree([])
expected2 = []
result2 = solver.preorderTraversal(root2)
print(f"Test Case 2: Input: [], Output: {result2}, Expected: {expected2}")
assert result2 == expected2

# Example 3: root = [1]
root3 = build_tree([1])
expected3 = [1]
result3 = solver.preorderTraversal(root3)
print(f"Test Case 3: Input: [1], Output: {result3}, Expected: {expected3}")
assert result3 == expected3

# Example 4: root = [1, 2]
# Tree structure:
#    1
#   /
#  2
root4 = build_tree([1, 2])
expected4 = [1, 2]
result4 = solver.preorderTraversal(root4)
print(f"Test Case 4: Input: [1, 2], Output: {result4}, Expected: {expected4}")
assert result4 == expected4

# Example 5: root = [1, null, 2]
# Tree structure:
#    1
#     \
#      2
root5 = build_tree([1, None, 2])
expected5 = [1, 2]
result5 = solver.preorderTraversal(root5)
print(f"Test Case 5: Input: [1, null, 2], Output: {result5}, Expected: {expected5}")
assert result5 == expected5

# More Complex Tree: root = [3, 1, 2]
# Tree structure:
#    3
#   / \
#  1   2
root6 = build_tree([3, 1, 2])
expected6 = [3, 1, 2]
result6 = solver.preorderTraversal(root6)
print(f"Test Case 6: Input: [3, 1, 2], Output: {result6}, Expected: {expected6}")
assert result6 == expected6

# Deeper Tree: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
# Tree structure:
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1
root7 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
expected7 = [5, 4, 11, 7, 2, 8, 13, 4, 5, 1]
result7 = solver.preorderTraversal(root7)
print(f"Test Case 7: Input: [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], Output: {result7}, Expected: {expected7}")
assert result7 == expected7

print("\nAll test cases passed!")


# --- Recursive Solution (for comparison) ---
class SolutionRecursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return
        result.append(node.val)      # Visit root
        self._preorder(node.left, result)  # Traverse left
        self._preorder(node.right, result) # Traverse right

# You can uncomment the below lines to test the recursive solution as well
# solver_rec = SolutionRecursive()
# print("\n--- Testing Recursive Solution ---")
# print(f"Test Case 1 (Recursive): {solver_rec.preorderTraversal(root1)}")
# print(f"Test Case 7 (Recursive): {solver_rec.preorderTraversal(root7)}")
