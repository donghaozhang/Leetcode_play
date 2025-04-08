from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

# Test cases
def test_levelOrder():
    # Test case 1: Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert Solution().levelOrder(root1) == [[3], [9, 20], [15, 7]]
    
    # Test case 2: Example 2
    root2 = TreeNode(1)
    assert Solution().levelOrder(root2) == [[1]]
    
    # Test case 3: Example 3
    root3 = None
    assert Solution().levelOrder(root3) == []
    
    # Additional test case: Single left child
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    assert Solution().levelOrder(root4) == [[1], [2]]
    
    # Additional test case: Single right child
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    assert Solution().levelOrder(root5) == [[1], [2]]
    
    print("All test cases pass")

test_levelOrder()
