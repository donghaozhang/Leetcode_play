from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Finds all root-to-leaf paths in a binary tree.
        """
        results = []
        if not root:
            return results

        # Helper function for DFS traversal
        def find_paths_recursive(node: TreeNode, current_path: List[str]):
            """
            Recursively explores paths from the current node.

            Args:
                node: The current node being visited.
                current_path: A list of node values (as strings) from the root
                              up to the current node.
            """
            # Add the current node's value to the path
            current_path.append(str(node.val))

            # Check if it's a leaf node
            if not node.left and not node.right:
                # Found a root-to-leaf path, format and add to results
                results.append("->".join(current_path))
                # Note: We still need to pop after this, so no early return here.
            else:
                # Continue DFS on children if they exist
                if node.left:
                    find_paths_recursive(node.left, current_path)
                if node.right:
                    find_paths_recursive(node.right, current_path)

            # Backtrack: remove the current node's value before returning
            # This is crucial for exploring sibling branches correctly.
            current_path.pop()

        # Start the recursion from the root with an empty path list
        find_paths_recursive(root, [])

        return results

# Helper function to build a tree from a list (Level Order Traversal)
# Handles 'None' values represented by None in the list
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [(root, 0)] # Store (node, index_in_list)
    processed_nodes = 1

    while queue and processed_nodes < len(nodes):
        current_node, current_index = queue.pop(0)

        # Process left child
        left_child_index = 2 * current_index + 1
        if left_child_index < len(nodes) and nodes[left_child_index] is not None:
            left_node = TreeNode(nodes[left_child_index])
            current_node.left = left_node
            queue.append((left_node, left_child_index))
        processed_nodes += 1

        if processed_nodes >= len(nodes):
            break

        # Process right child
        right_child_index = 2 * current_index + 2
        if right_child_index < len(nodes) and nodes[right_child_index] is not None:
            right_node = TreeNode(nodes[right_child_index])
            current_node.right = right_node
            queue.append((right_node, right_child_index))
        processed_nodes += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1
print("--- Example 1 ---")
root1 = build_tree([1, 2, 3, None, 5])
expected1 = ["1->2->5", "1->3"]
result1 = solver.binaryTreePaths(root1)
print(f"Input Tree (List): [1, 2, 3, null, 5]")
print(f"Output: {sorted(result1)}") # Sort for consistent comparison
print(f"Expected: {sorted(expected1)}")
assert sorted(result1) == sorted(expected1)
print("Passed!")

# Example 2
print("\n--- Example 2 ---")
root2 = build_tree([1])
expected2 = ["1"]
result2 = solver.binaryTreePaths(root2)
print(f"Input Tree (List): [1]")
print(f"Output: {result2}")
print(f"Expected: {expected2}")
assert result2 == expected2
print("Passed!")

# Custom Test Case 1: Empty Tree (handled by initial check)
print("\n--- Custom Test Case 1: Empty Tree ---")
root3 = build_tree([])
expected3 = []
result3 = solver.binaryTreePaths(root3)
print(f"Input Tree (List): []")
print(f"Output: {result3}")
print(f"Expected: {expected3}")
assert result3 == expected3
print("Passed!")

# Custom Test Case 2: Skewed Tree (Left)
print("\n--- Custom Test Case 2: Skewed Tree (Left) ---")
root4 = build_tree([1, 2, None, 3, None, 4, None]) # Represents 1 -> 2 -> 3 -> 4
# Note: build_tree needs careful construction for skewed trees if using level order list
# Manual construction might be clearer here:
root4_manual = TreeNode(1)
root4_manual.left = TreeNode(2)
root4_manual.left.left = TreeNode(3)
root4_manual.left.left.left = TreeNode(4)
expected4 = ["1->2->3->4"]
result4 = solver.binaryTreePaths(root4_manual)
print(f"Input Tree: 1 -> 2 -> 3 -> 4")
print(f"Output: {result4}")
print(f"Expected: {expected4}")
assert result4 == expected4
print("Passed!")

# Custom Test Case 3: Tree with multiple branches
print("\n--- Custom Test Case 3: Multiple Branches ---")
root5 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
# Leaves are: 7, 2, 13, 5, 1
expected5 = ["5->4->11->7", "5->4->11->2", "5->8->13", "5->8->4->5", "5->8->4->1"]
result5 = solver.binaryTreePaths(root5)
print(f"Input Tree (List): [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, null, 5, 1]")
print(f"Output: {sorted(result5)}")
print(f"Expected: {sorted(expected5)}")
assert sorted(result5) == sorted(expected5)
print("Passed!")

