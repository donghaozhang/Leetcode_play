# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root)

    def flatten_helper(self, root: TreeNode) -> TreeNode:
        # Base case: if the tree is empty, return None
        if not root:
            return None
        
        # Recursively flatten the left and right subtrees
        left_tail = self.flatten_helper(root.left)
        right_tail = self.flatten_helper(root.right)
        
        # If the left subtree is not empty, we need to re-arrange the nodes
        if root.left:
            # Append the right subtree after the left subtree
            left_tail.right = root.right
            # Move the left subtree to the right of the root
            root.right = root.left
            # Set the left child of the root to None
            root.left = None
        
        # Return the tail of the flattened tree rooted at 'root'
        return right_tail if right_tail else left_tail if left_tail else root

# Helper function to print the flattened linked list
def print_flattened(root):
    while root:
        print(root.val, end=" ")
        root = root.right
    print()

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    solution.flatten(root1)
    print("Test case 1:")
    print_flattened(root1)  # Expected output: 1 2 3 4 5 6

    # Test case 2: Empty tree
    root2 = None
    solution.flatten(root2)
    print("Test case 2:")
    print_flattened(root2)  # Expected output: (empty line)

    # Test case 3: Single node tree
    root3 = TreeNode(0)
    solution.flatten(root3)
    print("Test case 3:")
    print_flattened(root3)  # Expected output: 0
