# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the tree is empty, return None
        if not root:
            return None
        
        # If the current node is one of the given nodes, return the current node
        if root == p or root == q:
            return root
        
        # Recursively search for p and q in the left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are found in different subtrees, the current node is the LCA
        if left_lca and right_lca:
            return root
        
        # If both p and q are found in the left subtree, the LCA is in the left subtree
        if left_lca:
            return left_lca
        
        # If both p and q are found in the right subtree, the LCA is in the right subtree
        if right_lca:
            return right_lca
        
        # If neither p nor q is found in the left or right subtree, return None
        return None

def main():
    # Create the binary tree for Example 1
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   0
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node 5
    q = root.right  # Node 1
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 3

    # Create the binary tree for Example 2
    # Same as Example 1
    p = root.left  # Node 5
    q = root.left.right.right  # Node 4
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 5

    # Create the binary tree for Example 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    p = root  # Node 1
    q = root.left  # Node 2
    lca = solution.lowestCommonAncestor(root, p, q)
    print("LCA of nodes {} and {} is {}".format(p.val, q.val, lca.val))  # Output: 1

if __name__ == "__main__":
    main()
