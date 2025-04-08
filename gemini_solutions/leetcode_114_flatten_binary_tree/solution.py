import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Helper for visualizing the flattened list
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            if curr.left: # Should ideally be None after flatten
                 nodes.append(f"(L:{curr.left.val})") # Indicate error if left exists
            curr = curr.right
        return " -> ".join(nodes) if nodes else "None"

# Helper function to build a tree from a list (level-order)
def build_tree(nodes: list) -> TreeNode | None:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        curr = queue.popleft()
        if nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

# Helper function to represent tree structure (for debugging before flatten)
def tree_to_string(root: TreeNode | None) -> str:
    if not root:
        return "[]"
    
    nodes = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            nodes.append(str(node.val))
            # Important: Add children to queue even if None, to represent structure
            # Only stop adding children if all remaining nodes in queue are None
            # (This simple version might not perfectly match LeetCode's null representation
            # for trailing nulls, but good enough for structure check)
            queue.append(node.left)
            queue.append(node.right)
        else:
            # Only add "null" if there are potentially more nodes later
            # This part is tricky to get exactly like LeetCode's representation
            # without more complex queue management. Let's keep it simple.
             if any(n is not None for n in queue):
                 nodes.append("null")
            # pass # Avoid adding trailing nulls excessively

    # Clean up trailing nulls that might have been added
    while nodes and nodes[-1] == "null":
        nodes.pop()
        
    return "[" + ",".join(nodes) + "]"


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Flattens the binary tree in-place using O(1) extra space.
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree (predecessor)
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # --- Rewiring ---
                # 1. Connect predecessor's right to current node's right
                predecessor.right = curr.right

                # 2. Move current node's left subtree to its right
                curr.right = curr.left

                # 3. Set current node's left to None
                curr.left = None
                # --- Rewiring Done ---

            # Move to the next node in the pre-order sequence
            # This will be the node that was just moved from the left (if left existed),
            # or the original right node (if left did not exist).
            curr = curr.right

# --- Time and Space Complexity Analysis ---
# Time Complexity: O(N), where N is the number of nodes.
#   - Each node is visited as `curr` once.
#   - Finding the `predecessor` involves traversing the right spine of the left subtree.
#   - Crucially, each edge connecting a node to its right child is traversed at most twice
#     (once downwards when finding the predecessor, once downwards when `curr` moves right).
#   - Edges connecting a node to its left child are traversed once when `curr` has a left child.
#   - Therefore, the total work is proportional to the number of nodes and edges, resulting in O(N).
#
# Space Complexity: O(1).
#   - We only use a few pointers (`curr`, `predecessor`).
#   - No recursion stack is used (iterative approach).
#   - No auxiliary data structures like lists or queues are used.
#   - Modification is done in-place.

# --- Test Cases ---
solver = Solution()

# Example 1
print("--- Example 1 ---")
root1 = build_tree([1, 2, 5, 3, 4, None, 6])
print(f"Original Tree: {tree_to_string(root1)}")
solver.flatten(root1)
print(f"Flattened Tree: {root1}") # Uses the __repr__ method
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Example 2
print("\n--- Example 2 ---")
root2 = build_tree([])
print(f"Original Tree: {tree_to_string(root2)}")
solver.flatten(root2)
print(f"Flattened Tree: {root2}")
# Expected Output: None

# Example 3
print("\n--- Example 3 ---")
root3 = build_tree([0])
print(f"Original Tree: {tree_to_string(root3)}")
solver.flatten(root3)
print(f"Flattened Tree: {root3}")
# Expected Output: 0

# Additional Test Case: Left Skewed Tree
print("\n--- Test Case: Left Skewed ---")
root4 = build_tree([1, 2, None, 3, None, 4])
print(f"Original Tree: {tree_to_string(root4)}")
solver.flatten(root4)
print(f"Flattened Tree: {root4}")
# Expected Output: 1 -> 2 -> 3 -> 4

# Additional Test Case: Right Skewed Tree
print("\n--- Test Case: Right Skewed ---")
root5 = build_tree([1, None, 2, None, 3, None, 4])
print(f"Original Tree: {tree_to_string(root5)}")
solver.flatten(root5)
print(f"Flattened Tree: {root5}")
# Expected Output: 1 -> 2 -> 3 -> 4

# Additional Test Case: More Complex
print("\n--- Test Case: Complex ---")
root6 = build_tree([1, 2, 7, 3, 4, None, None, None, None, 5, 6])
# Original Structure:
#        1
#      /   \
#     2     7
#    / \
#   3   4
#      / \
#     5   6
# Pre-order: 1, 2, 3, 4, 5, 6, 7
print(f"Original Tree: {tree_to_string(root6)}")
solver.flatten(root6)
print(f"Flattened Tree: {root6}")
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
