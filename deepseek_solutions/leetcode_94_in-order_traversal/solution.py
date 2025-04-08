# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # Iterative approach using stack
        res = []
        stack = []
        current = root
        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left
            # Current must be None at this point
            current = stack.pop()
            res.append(current.val)
            # Now visit the right subtree
            current = current.right
        return res

# Test cases
def test_inorder_traversal():
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root1) == [1, 3, 2]

    # Example 2
    root2 = None
    assert Solution().inorderTraversal(root2) == []

    # Example 3
    root3 = TreeNode(1)
    assert Solution().inorderTraversal(root3) == [1]

    # Additional test case: left-heavy tree
    root4 = TreeNode(3)
    root4.left = TreeNode(1)
    root4.left.right = TreeNode(2)
    assert Solution().inorderTraversal(root4) == [1, 2, 3]

    print("All test cases pass")

test_inorder_traversal()
