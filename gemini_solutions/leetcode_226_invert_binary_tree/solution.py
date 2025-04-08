import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Helper for visualizing the tree (level-order)
        return f"TreeNode({self.val})"

class Solution:
    """
    Solves the Invert Binary Tree problem using recursion.
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree recursively.

        Args:
            root: The root node of the binary tree.

        Returns:
            The root node of the inverted binary tree.
        """
        # Base case: If the tree/subtree is empty, return None.
        if not root:
            return None

        # Swap the left and right children of the current node.
        # Python's tuple assignment makes this concise.
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree (which was originally the right).
        self.invertTree(root.left)
        # Recursively invert the right subtree (which was originally the left).
        self.invertTree(root.right)

        # Return the root of the modified tree.
        return root

# Helper functions for testing
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
            
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to a list representation (level-order)."""
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            # We add None placeholders initially but remove trailing Nones later
            result.append(None)
            
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
        
    return result

# --- Test Cases ---
solver = Solution()

# Example 1
root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
inverted_root1 = solver.invertTree(root1)
output1 = tree_to_list(inverted_root1)
expected1 = [4, 7, 2, 9, 6, 3, 1]
print(f"Test Case 1 Input:  [4, 2, 7, 1, 3, 6, 9]")
print(f"Test Case 1 Output: {output1}")
print(f"Test Case 1 Expected: {expected1}")
print(f"Test Case 1 Passed: {output1 == expected1}")
print("-" * 20)

# Example 2
root2 = build_tree([2, 1, 3])
inverted_root2 = solver.invertTree(root2)
output2 = tree_to_list(inverted_root2)
expected2 = [2, 3, 1]
print(f"Test Case 2 Input:  [2, 1, 3]")
print(f"Test Case 2 Output: {output2}")
print(f"Test Case 2 Expected: {expected2}")
print(f"Test Case 2 Passed: {output2 == expected2}")
print("-" * 20)

# Example 3
root3 = build_tree([])
inverted_root3 = solver.invertTree(root3)
output3 = tree_to_list(inverted_root3)
expected3 = []
print(f"Test Case 3 Input:  []")
print(f"Test Case 3 Output: {output3}")
print(f"Test Case 3 Expected: {expected3}")
print(f"Test Case 3 Passed: {output3 == expected3}")
print("-" * 20)

# Custom Test Case: Single Node
root4 = build_tree([1])
inverted_root4 = solver.invertTree(root4)
output4 = tree_to_list(inverted_root4)
expected4 = [1]
print(f"Test Case 4 Input:  [1]")
print(f"Test Case 4 Output: {output4}")
print(f"Test Case 4 Expected: {expected4}")
print(f"Test Case 4 Passed: {output4 == expected4}")
print("-" * 20)

# Custom Test Case: Left Skewed
# Input:    1
#          /
#         2
#        /
#       3
root5 = build_tree([1, 2, None, 3]) 
# Expected Output: 1
#                   \
#                    2
#                     \
#                      3
inverted_root5 = solver.invertTree(root5)
output5 = tree_to_list(inverted_root5)
expected5 = [1, None, 2, None, 3]
print(f"Test Case 5 Input:  [1, 2, null, 3]")
print(f"Test Case 5 Output: {output5}")
print(f"Test Case 5 Expected: {expected5}")
print(f"Test Case 5 Passed: {output5 == expected5}")
print("-" * 20)

# Custom Test Case: Tree with missing children
# Input:    4
#          /
#         2
#        / \
#       1   3
root6 = build_tree([4, 2, None, 1, 3])
# Expected Output: 4
#                   \
#                    2
#                   / \
#                  3   1
inverted_root6 = solver.invertTree(root6)
output6 = tree_to_list(inverted_root6)
expected6 = [4, None, 2, 3, 1]
print(f"Test Case 6 Input:  [4, 2, null, 1, 3]")
print(f"Test Case 6 Output: {output6}")
print(f"Test Case 6 Expected: {expected6}")
print(f"Test Case 6 Passed: {output6 == expected6}")
print("-" * 20)

