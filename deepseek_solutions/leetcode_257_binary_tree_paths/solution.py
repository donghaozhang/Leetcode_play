# Test Case 1
# Tree:
#     1
#    / \
#   2   3
#    \
#     5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root1))  # Expected: ["1->2->5", "1->3"]

# Test Case 2
# Tree:
#     1
root2 = TreeNode(1)
print(Solution().binaryTreePaths(root2))  # Expected: ["1"]

# Test Case 3
# Tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
print(Solution().binaryTreePaths(root3))  # Expected: ["1->2->4", "1->2->5", "1->3"]

# Test Case 4: Empty Tree (shouldn't happen per constraints, but handled)
root4 = None
print(Solution().binaryTreePaths(root4))  # Expected: []

# Test Case 5: Single path
# Tree:
#     1
#    /
#   2
#  /
# 3
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.left.left = TreeNode(3)
print(Solution().binaryTreePaths(root5))  # Expected: ["1->2->3"]
