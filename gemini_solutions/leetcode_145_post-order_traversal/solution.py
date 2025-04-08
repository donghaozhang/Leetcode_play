import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Helper for printing tree nodes during testing
        return f"TreeNode({self.val})"

# Helper function to build a tree from a list (Level Order)
# For example: [1, None, 2, 3] -> Tree structure shown in Example 1
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()
        
        # Process left child
        if nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1
        
        if i >= len(nodes):
            break
            
        # Process right child
        if nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1
        
    return root

class Solution:
    """
    Solves the Binary Tree Postorder Traversal problem (LeetCode 145).
    """
    
    # --- Recursive Solution ---
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal using recursion.
        """
        result = []
        self._postorder_helper(root, result)
        return result

    def _postorder_helper(self, node: Optional[TreeNode], result: List[int]):
        """
        Helper recursive function for postorder traversal.
        """
        if node is None:
            return
        
        # 1. Traverse left subtree
        self._postorder_helper(node.left, result)
        
        # 2. Traverse right subtree
        self._postorder_helper(node.right, result)
        
        # 3. Visit the node itself
        result.append(node.val)

    # --- Iterative Solution (Modified Preorder + Reverse) ---
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal using an iterative approach
        (Modified Preorder + Reverse).
        """
        if not root:
            return []

        stack = [root]
        nodes_reversed_postorder = [] # Stores nodes in Root -> Right -> Left order

        while stack:
            node = stack.pop()
            nodes_reversed_postorder.append(node.val)
            
            # Push left child first, then right child
            # So that right child is processed before left child (LIFO)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        # Reverse the list to get the actual postorder (Left -> Right -> Root)
        return nodes_reversed_postorder[::-1]

    # --- Main function (defaults to iterative as per follow-up) ---
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Main entry point, uses the iterative solution.
        """
        return self.postorderTraversalIterative(root)
        # return self.postorderTraversalRecursive(root) # Or use recursive


# --- Complexity Analysis ---
# Recursive Solution:
#   - Time Complexity: O(N), where N is the number of nodes in the tree. Each node is visited exactly once.
#   - Space Complexity: O(H), where H is the height of the tree. This is for the recursion call stack. 
#     In the worst case (a skewed tree), H can be N, leading to O(N) space. 
#     For a balanced tree, H is O(log N).

# Iterative Solution (Modified Preorder + Reverse):
#   - Time Complexity: O(N). Each node is pushed onto and popped from the stack once (O(N)). 
#     Appending to the intermediate list takes O(N). Reversing the list takes O(N). Total: O(N).
#   - Space Complexity: O(N). The stack can hold up to O(N) nodes in the worst case (skewed tree). 
#     The `nodes_reversed_postorder` list also stores N values. Total: O(N).


# --- Test Cases ---
solver = Solution()

# Example 1: root = [1,null,2,3] -> Output: [3,2,1]
root1 = build_tree([1, None, 2, 3])
print("Test Case 1:")
print(f"Input Tree (constructed from list): {root1.val if root1 else None}, L:{root1.left}, R:{root1.right.val if root1 and root1.right else None}, R->L:{root1.right.left.val if root1 and root1.right and root1.right.left else None}")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root1)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root1)}")
print("-" * 20)

# Example 2: root = [] -> Output: []
root2 = build_tree([])
print("Test Case 2:")
print(f"Input Tree (constructed from list): None")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root2)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root2)}")
print("-" * 20)

# Example 3: root = [1] -> Output: [1]
root3 = build_tree([1])
print("Test Case 3:")
print(f"Input Tree (constructed from list): {root3.val if root3 else None}")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root3)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root3)}")
print("-" * 20)

# Additional Test Case: More complex tree
# root = [3, 9, 20, null, null, 15, 7] -> Output: [9, 15, 7, 20, 3]
#       3
#      / \
#     9  20
#       /  \
#      15   7
root4 = build_tree([3, 9, 20, None, None, 15, 7])
print("Test Case 4:")
print(f"Input Tree (constructed from list): [3, 9, 20, None, None, 15, 7]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root4)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root4)}")
print("-" * 20)

# Additional Test Case: Left-skewed tree
# root = [1, 2, null, 3, null, 4, null] -> Output: [4, 3, 2, 1]
#       1
#      /
#     2
#    /
#   3
#  /
# 4
root5 = build_tree([1, 2, None, 3, None, 4, None])
print("Test Case 5:")
print(f"Input Tree (constructed from list): [1, 2, None, 3, None, 4, None]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root5)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root5)}")
print("-" * 20)

# Additional Test Case: Right-skewed tree
# root = [1, null, 2, null, 3, null, 4] -> Output: [4, 3, 2, 1]
#       1
#        \
#         2
#          \
#           3
#            \
#             4
root6 = build_tree([1, None, 2, None, 3, None, 4])
print("Test Case 6:")
print(f"Input Tree (constructed from list): [1, None, 2, None, 3, None, 4]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root6)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root6)}")
print("-" * 20)
