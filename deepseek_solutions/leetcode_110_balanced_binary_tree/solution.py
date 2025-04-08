class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1

# Test cases
def test_isBalanced():
    solution = Solution()
    
    # Example 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert solution.isBalanced(root1) == True
    
    # Example 2: Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    assert solution.isBalanced(root2) == False
    
    # Example 3: Empty tree
    root3 = None
    assert solution.isBalanced(root3) == True
    
    # Additional test case: Single node
    root4 = TreeNode(1)
    assert solution.isBalanced(root4) == True
    
    # Additional test case: Left-heavy unbalanced
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    assert solution.isBalanced(root5) == False
    
    print("All test cases pass")

test_isBalanced()
