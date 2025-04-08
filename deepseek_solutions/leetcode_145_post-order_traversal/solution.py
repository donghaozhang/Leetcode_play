# Test Case 1: Example 1
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
assert Solution().postorderTraversal(root1) == [3, 2, 1]

# Test Case 2: Empty tree
root2 = None
assert Solution().postorderTraversal(root2) == []

# Test Case 3: Single node
root3 = TreeNode(1)
assert Solution().postorderTraversal(root3) == [1]

# Test Case 4: Full binary tree
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.right = TreeNode(5)
root4.right.left = TreeNode(6)
root4.right.right = TreeNode(7)
assert Solution().postorderTraversal(root4) == [4, 5, 2, 6, 7, 3, 1]
