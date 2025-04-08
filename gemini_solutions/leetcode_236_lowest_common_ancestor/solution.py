# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        # Helper for printing node value during testing
        return f"Node({self.val})"

class Solution:
    """
    Solves the Lowest Common Ancestor problem using recursive DFS.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor of two nodes p and q in a binary tree.

        Args:
            root: The root node of the binary tree.
            p: The first target node.
            q: The second target node.

        Returns:
            The lowest common ancestor node.
        """
        # Base case 1: If root is None, we can't find anything.
        if not root:
            return None

        # Base case 2: If root is p or q, then this node is a potential LCA
        # (or we've found one of the nodes).
        if root == p or root == q:
            return root

        # Recursively search in the left and right subtrees.
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # Process the results from left and right subtrees:
        # Case 1: p found in one subtree, q found in the other.
        # This means the current 'root' is the LCA.
        if left_lca and right_lca:
            return root

        # Case 2: Both p and q are in the left subtree OR
        #         p or q was found in the left subtree (and the other is deeper) OR
        #         the LCA was found in the left subtree.
        # In any of these sub-cases, the result from the left subtree is the answer
        # to propagate up. Same logic applies if only right_lca is not None.
        return left_lca if left_lca else right_lca

# Helper functions for testing
def build_tree(nodes):
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [(root, 0)] # Store node and its index in the list
    
    while queue:
        current_node, current_index = queue.pop(0)
        
        left_child_index = 2 * current_index + 1
        if left_child_index < len(nodes) and nodes[left_child_index] is not None:
            current_node.left = TreeNode(nodes[left_child_index])
            queue.append((current_node.left, left_child_index))
            
        right_child_index = 2 * current_index + 2
        if right_child_index < len(nodes) and nodes[right_child_index] is not None:
            current_node.right = TreeNode(nodes[right_child_index])
            queue.append((current_node.right, right_child_index))
            
    return root

def find_node(root: TreeNode, val: int) -> TreeNode:
    """Finds a node with a specific value in the tree (assumes unique values)."""
    if not root:
        return None
    if root.val == val:
        return root
    
    found_left = find_node(root.left, val)
    if found_left:
        return found_left
    
    return find_node(root.right, val)

# --- Test Cases ---
solver = Solution()

# Example 1
nodes1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root1 = build_tree(nodes1)
p1 = find_node(root1, 5)
q1 = find_node(root1, 1)
lca1 = solver.lowestCommonAncestor(root1, p1, q1)
print(f"Example 1: Tree={nodes1}, p=5, q=1")
print(f"LCA: {lca1.val if lca1 else 'Not Found'} (Expected: 3)")
print("-" * 20)

# Example 2
nodes2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root2 = build_tree(nodes2)
p2 = find_node(root2, 5)
q2 = find_node(root2, 4)
lca2 = solver.lowestCommonAncestor(root2, p2, q2)
print(f"Example 2: Tree={nodes2}, p=5, q=4")
print(f"LCA: {lca2.val if lca2 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Example 3
nodes3 = [1, 2]
root3 = build_tree(nodes3)
p3 = find_node(root3, 1)
q3 = find_node(root3, 2)
lca3 = solver.lowestCommonAncestor(root3, p3, q3)
print(f"Example 3: Tree={nodes3}, p=1, q=2")
print(f"LCA: {lca3.val if lca3 else 'Not Found'} (Expected: 1)")
print("-" * 20)

# Custom Test Case 1: Deeper nodes
nodes4 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root4 = build_tree(nodes4)
p4 = find_node(root4, 3)
q4 = find_node(root4, 5)
lca4 = solver.lowestCommonAncestor(root4, p4, q4)
print(f"Custom Test 1: Tree={nodes4}, p=3, q=5")
print(f"LCA: {lca4.val if lca4 else 'Not Found'} (Expected: 4)")
print("-" * 20)

# Custom Test Case 2: p is ancestor of q
nodes5 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root5 = build_tree(nodes5)
p5 = find_node(root5, 5)
q5 = find_node(root5, 7)
lca5 = solver.lowestCommonAncestor(root5, p5, q5)
print(f"Custom Test 2: Tree={nodes5}, p=5, q=7")
print(f"LCA: {lca5.val if lca5 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Custom Test Case 3: q is ancestor of p
nodes6 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root6 = build_tree(nodes6)
p6 = find_node(root6, 4)
q6 = find_node(root6, 5)
lca6 = solver.lowestCommonAncestor(root6, p6, q6)
print(f"Custom Test 3: Tree={nodes6}, p=4, q=5")
print(f"LCA: {lca6.val if lca6 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Custom Test Case 4: Root is LCA
nodes7 = [1, 2, 3]
root7 = build_tree(nodes7)
p7 = find_node(root7, 2)
q7 = find_node(root7, 3)
lca7 = solver.lowestCommonAncestor(root7, p7, q7)
print(f"Custom Test 4: Tree={nodes7}, p=2, q=3")
print(f"LCA: {lca7.val if lca7 else 'Not Found'} (Expected: 1)")
print("-" * 20)
