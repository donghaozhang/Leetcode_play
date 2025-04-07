# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            """Return the height of the subtree rooted at node if it's balanced; otherwise, return -1."""
            if node is None:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_height(root) != -1

# Helper function to create a binary tree from a list
def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1:
    root1 = create_tree([3, 9, 20, None, None, 15, 7])
    print(solution.isBalanced(root1))  # Expected output: True
    
    # Example 2:
    root2 = create_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(solution.isBalanced(root2))  # Expected output: False
    
    # Example 3:
    root3 = create_tree([])
    print(solution.isBalanced(root3))  # Expected output: True
