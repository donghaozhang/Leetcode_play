# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Determines if a binary tree is height-balanced using a bottom-up DFS approach.
        """

        # Helper function returns the height of the subtree if balanced,
        # otherwise returns -2 to indicate imbalance.
        def check_height(node: TreeNode | None) -> int:
            # Base case: An empty tree is balanced and has height -1
            if not node:
                return -1

            # Recursively check the left subtree
            left_height = check_height(node.left)
            # If the left subtree is unbalanced, propagate the imbalance signal
            if left_height == -2:
                return -2

            # Recursively check the right subtree
            right_height = check_height(node.right)
            # If the right subtree is unbalanced, propagate the imbalance signal
            if right_height == -2:
                return -2

            # Check the balance condition at the current node
            if abs(left_height - right_height) > 1:
                # Current node is unbalanced
                return -2
            else:
                # Current node is balanced, return its height
                return 1 + max(left_height, right_height)

        # Call the helper function starting from the root.
        # If it returns -2, the tree is unbalanced. Otherwise, it's balanced.
        return check_height(root) != -2

# Helper function to build a tree from a list (for testing)
def build_tree(nodes: list) -> TreeNode | None:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current_node = queue.pop(0)
        
        # Left child
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        
        if i < len(nodes):
            # Right child
            if nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1
            
    return root

# --- Test Cases ---
solver = Solution()

# Example 1: Balanced
tree1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Tree 1 ([3,9,20,null,null,15,7]): Balanced = {solver.isBalanced(tree1)}") # Expected: True

# Example 2: Unbalanced
tree2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(f"Tree 2 ([1,2,2,3,3,null,null,4,4]): Balanced = {solver.isBalanced(tree2)}") # Expected: False

# Example 3: Empty tree
tree3 = build_tree([])
print(f"Tree 3 ([]): Balanced = {solver.isBalanced(tree3)}") # Expected: True

# Test Case 4: Single node
tree4 = build_tree([1])
print(f"Tree 4 ([1]): Balanced = {solver.isBalanced(tree4)}") # Expected: True

# Test Case 5: Skewed tree (unbalanced)
tree5 = build_tree([1, 2, None, 3, None, 4, None])
print(f"Tree 5 ([1,2,null,3,null,4,null]): Balanced = {solver.isBalanced(tree5)}") # Expected: False

# Test Case 6: Slightly more complex balanced tree
tree6 = build_tree([1, 2, 3, 4, 5, 6, None, 8])
# Heights: 8(-1,-1)->0; 4(8,-1)->1; 5(-1,-1)->0; 2(4,5)->2; 6(-1,-1)->0; 3(6,-1)->1; 1(2,3)->3
# Balances: 8(0); 4(1); 5(0); 2(1); 6(0); 3(1); 1(1) -> Balanced
print(f"Tree 6 ([1,2,3,4,5,6,null,8]): Balanced = {solver.isBalanced(tree6)}") # Expected: True

# Test Case 7: Unbalanced at root due to height difference
tree7 = build_tree([1, 2, None, 3, None, 4, None, 5, None])
# Heights: 5(-1,-1)->0; 4(5,-1)->1; 3(4,-1)->2; 2(3,-1)->3; 1(2,None)->4
# Balances: 5(0); 4(1); 3(1); 2(1); 1(abs(3 - (-1)) = 4 > 1) -> Unbalanced
print(f"Tree 7 ([1,2,null,3,null,4,null,5,null]): Balanced = {solver.isBalanced(tree7)}") # Expected: False

# Test Case 8: Unbalanced deeper in the tree
tree8 = build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
# Heights: 4(-1,-1)->0; 3(4,-1)->1; 2(3,None)->2; 4(-1,-1)->0; 3(None,4)->1; 2(None,3)->2; 1(2,2)->3
# Balances: 4(0); 3(1); 2(1); 4(0); 3(1); 2(1); 1(abs(2-2)=0)
# Let's recheck node 2 (left): left=3(height 1), right=None(height -1). Diff=2 -> Unbalanced
print(f"Tree 8 ([1,2,2,3,null,null,3,4,null,null,4]): Balanced = {solver.isBalanced(tree8)}") # Expected: False

