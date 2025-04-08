class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        return left if left else right

# Test cases
def build_tree(arr, p_val, q_val):
    if not arr:
        return None, None, None
    nodes = [None if val is None else TreeNode(val) for val in arr]
    root = nodes[0]
    p_node = None
    q_node = None
    for i, node in enumerate(nodes):
        if node:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
            if node.val == p_val:
                p_node = node
            if node.val == q_val:
                q_node = node
    return root, p_node, q_node

# Example 1
arr1 = [3,5,1,6,2,0,8,None,None,7,4]
root1, p1, q1 = build_tree(arr1, 5, 1)
sol = Solution()
print(sol.lowestCommonAncestor(root1, p1, q1).val)  # Output: 3

# Example 2
arr2 = [3,5,1,6,2,0,8,None,None,7,4]
root2, p2, q2 = build_tree(arr2, 5, 4)
print(sol.lowestCommonAncestor(root2, p2, q2).val)  # Output: 5

# Example 3
arr3 = [1,2]
root3, p3, q3 = build_tree(arr3, 1, 2)
print(sol.lowestCommonAncestor(root3, p3, q3).val)  # Output: 1
