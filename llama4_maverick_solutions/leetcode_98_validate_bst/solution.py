class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, node):
        if node is None:
            return True
        
        # Traverse left subtree
        if not self.inorder(node.left):
            return False
        
        # Check if current node's value is greater than the previous node's value
        if self.prev is not None and node.val <= self.prev.val:
            return False
        
        # Update previous node
        self.prev = node
        
        # Traverse right subtree
        return self.inorder(node.right)

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
    root1 = create_tree([2, 1, 3])
    print(solution.isValidBST(root1))  # Expected output: True
    
    # Example 2:
    root2 = create_tree([5, 1, 4, None, None, 3, 6])
    print(solution.isValidBST(root2))  # Expected output: False
    
    # Test case with a single node
    root3 = create_tree([1])
    print(solution.isValidBST(root3))  # Expected output: True
    
    # Test case with an empty tree
    root4 = create_tree([])
    print(solution.isValidBST(root4))  # Expected output: True (considering an empty tree as a valid BST for this implementation)
