# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        Inverts a binary tree.

        Args:
        root: The root of the binary tree to be inverted.

        Returns:
        The root of the inverted binary tree.
        """
        if root is None:
            return None
        
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        
        return root

def printTree(node, level=0):
    """
    Helper function to print the binary tree.

    Args:
    node: The current node being processed.
    level: The level of the current node in the tree.
    """
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.left, level + 1)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example given in the problem
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    print("Original Tree:")
    printTree(root1)
    inverted_root1 = solution.invertTree(root1)
    print("\nInverted Tree:")
    printTree(inverted_root1)

    # Test case 2: Empty tree
    root2 = None
    inverted_root2 = solution.invertTree(root2)
    assert inverted_root2 is None, "Test case 2 failed"

    # Test case 3: Tree with one node
    root3 = TreeNode(1)
    inverted_root3 = solution.invertTree(root3)
    assert inverted_root3.val == 1, "Test case 3 failed"
    assert inverted_root3.left is None, "Test case 3 failed"
    assert inverted_root3.right is None, "Test case 3 failed"

    print("\nAll test cases passed.")
