# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Helper function to print the tree in level order (for testing)
def printLevelOrder(root):
    if not root:
        print("[]")
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    print(result)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    print("Original tree (Example 1):")
    printLevelOrder(root1)
    inverted_root1 = solution.invertTree(root1)
    print("Inverted tree (Example 1):")
    printLevelOrder(inverted_root1)
    
    # Example 2
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    print("Original tree (Example 2):")
    printLevelOrder(root2)
    inverted_root2 = solution.invertTree(root2)
    print("Inverted tree (Example 2):")
    printLevelOrder(inverted_root2)
    
    # Example 3
    root3 = None
    print("Original tree (Example 3):")
    printLevelOrder(root3)
    inverted_root3 = solution.invertTree(root3)
    print("Inverted tree (Example 3):")
    printLevelOrder(inverted_root3)
