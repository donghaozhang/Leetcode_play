from typing import List, Optional
from collections import deque

class TreeNode:
    """Binary tree node definition"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform level order traversal of a binary tree
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        List of lists, where each inner list contains node values at a level
    """
    # Handle empty tree case
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    # BFS traversal
    while queue:
        # Number of nodes at current level
        level_size = len(queue)
        level_values = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            # Add children to queue for next level processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add current level values to result
        result.append(level_values)
    
    return result

# Test cases
if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(level_order_traversal(root1))  # Expected: [[3], [9, 20], [15, 7]]
    
    # Example 2: [1]
    root2 = TreeNode(1)
    print(level_order_traversal(root2))  # Expected: [[1]]
    
    # Example 3: []
    root3 = None
    print(level_order_traversal(root3))  # Expected: []
    
    # Additional example: Complete binary tree
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    print(level_order_traversal(root4))  # Expected: [[1], [2, 3], [4, 5, 6, 7]] 