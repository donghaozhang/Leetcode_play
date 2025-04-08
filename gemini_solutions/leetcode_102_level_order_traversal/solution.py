import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level order traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the node values
            at a specific level, from left to right.
        """
        result = []
        if not root:
            return result # Return empty list for an empty tree

        # Use a deque (double-ended queue) for efficient appends and poplefts
        queue = collections.deque([root])

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            current_level_values = []

            # Process all nodes at the current level
            for _ in range(level_size):
                # Dequeue the node from the front
                current_node = queue.popleft()
                current_level_values.append(current_node.val)

                # Enqueue children for the next level
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            # Add the collected values for the current level to the result
            result.append(current_level_values)

        return result

# Helper function to build a tree from a list (for testing)
# LeetCode's representation: [3, 9, 20, null, null, 15, 7]
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()

        # Process left child
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes):
             # Process right child
            if nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1

    return root

# Helper function to print tree level order (for verifying build_tree)
def print_level_order(root: Optional[TreeNode]):
    sol = Solution()
    print(sol.levelOrder(root))

# --- Test Cases ---
solver = Solution()

# Test Case 1: Example 1
print("Test Case 1: Example 1")
root1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Input Tree (visualized by level order):")
print_level_order(root1)
output1 = solver.levelOrder(root1)
expected1 = [[3], [9, 20], [15, 7]]
print(f"Output: {output1}")
print(f"Expected: {expected1}")
print(f"Pass: {output1 == expected1}\n")

# Test Case 2: Example 2
print("Test Case 2: Example 2")
root2 = build_tree([1])
print(f"Input Tree (visualized by level order):")
print_level_order(root2)
output2 = solver.levelOrder(root2)
expected2 = [[1]]
print(f"Output: {output2}")
print(f"Expected: {expected2}")
print(f"Pass: {output2 == expected2}\n")

# Test Case 3: Example 3 (Empty Tree)
print("Test Case 3: Example 3 (Empty Tree)")
root3 = build_tree([])
print(f"Input Tree (visualized by level order):")
print_level_order(root3)
output3 = solver.levelOrder(root3)
expected3 = []
print(f"Output: {output3}")
print(f"Expected: {expected3}")
print(f"Pass: {output3 == expected3}\n")

# Test Case 4: Left-Skewed Tree
print("Test Case 4: Left-Skewed Tree")
root4 = build_tree([1, 2, None, 3, None, 4, None])
print(f"Input Tree (visualized by level order):")
print_level_order(root4)
output4 = solver.levelOrder(root4)
expected4 = [[1], [2], [3], [4]]
print(f"Output: {output4}")
print(f"Expected: {expected4}")
print(f"Pass: {output4 == expected4}\n")

# Test Case 5: Right-Skewed Tree
print("Test Case 5: Right-Skewed Tree")
root5 = build_tree([1, None, 2, None, 3, None, 4])
print(f"Input Tree (visualized by level order):")
print_level_order(root5)
output5 = solver.levelOrder(root5)
expected5 = [[1], [2], [3], [4]]
print(f"Output: {output5}")
print(f"Expected: {expected5}")
print(f"Pass: {output5 == expected5}\n")

# Test Case 6: Complete Binary Tree
print("Test Case 6: Complete Binary Tree")
root6 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(f"Input Tree (visualized by level order):")
print_level_order(root6)
output6 = solver.levelOrder(root6)
expected6 = [[1], [2, 3], [4, 5, 6, 7]]
print(f"Output: {output6}")
print(f"Expected: {expected6}")
print(f"Pass: {output6 == expected6}\n")

