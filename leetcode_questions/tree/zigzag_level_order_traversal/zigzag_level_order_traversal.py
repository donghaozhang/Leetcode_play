from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    """Binary tree node definition"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform zigzag level order traversal of a binary tree using BFS
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        List of lists, where each inner list contains node values at a level in zigzag order
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    # Flag to track direction (True means right to left)
    reverse = False
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level values if needed
        if reverse:
            level_values.reverse()
        
        result.append(level_values)
        reverse = not reverse  # Toggle the direction for the next level
    
    return result

def zigzag_level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform zigzag level order traversal using recursion and a dictionary
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        List of lists, where each inner list contains node values at a level in zigzag order
    """
    level_dict = defaultdict(list)
    
    def dfs(node, level):
        if not node:
            return
        
        # Check if we need to insert at beginning (even levels) or append (odd levels)
        if level % 2 == 0:  # Even level, insert at beginning
            level_dict[level].insert(0, node.val)
        else:  # Odd level, append at end
            level_dict[level].append(node.val)
        
        # Recursively process children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    # Start DFS
    dfs(root, 0)
    
    # Convert dictionary to list of lists
    result = []
    for i in range(len(level_dict)):
        result.append(level_dict[i])
    
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
    
    print("Iterative approach (Example 1):")
    print(zigzag_level_order_iterative(root1))  # Expected: [[3], [20, 9], [15, 7]]
    
    print("Recursive approach (Example 1):")
    print(zigzag_level_order_recursive(root1))  # Expected: [[3], [20, 9], [15, 7]]
    
    # Example 2: [1]
    root2 = TreeNode(1)
    print("\nIterative approach (Example 2):")
    print(zigzag_level_order_iterative(root2))  # Expected: [[1]]
    
    print("Recursive approach (Example 2):")
    print(zigzag_level_order_recursive(root2))  # Expected: [[1]]
    
    # Example 3: []
    root3 = None
    print("\nIterative approach (Example 3):")
    print(zigzag_level_order_iterative(root3))  # Expected: []
    
    print("Recursive approach (Example 3):")
    print(zigzag_level_order_recursive(root3))  # Expected: []
    
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
    
    print("\nIterative approach (Additional example):")
    print(zigzag_level_order_iterative(root4))  # Expected: [[1], [3, 2], [4, 5, 6, 7]]
    
    print("Recursive approach (Additional example):")
    print(zigzag_level_order_recursive(root4))  # Expected: [[1], [3, 2], [4, 5, 6, 7]] 