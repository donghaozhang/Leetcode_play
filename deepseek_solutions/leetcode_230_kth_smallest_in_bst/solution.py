# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            # Move to the right subtree
            current = current.right
        
        return -1  # This line is theoretically unreachable if k is valid
