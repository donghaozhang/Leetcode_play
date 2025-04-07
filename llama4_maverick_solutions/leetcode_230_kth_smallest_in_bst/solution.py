# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = None
        self.inorder(root, k)
        return self.result

    def inorder(self, node, k):
        if node is None or self.result is not None:
            return
        self.inorder(node.left, k)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.inorder(node.right, k)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    k1 = 1
    print("Test case 1:", solution.kthSmallest(root1, k1))  # Expected output: 1

    # Test case 2:
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    k2 = 3
    print("Test case 2:", solution.kthSmallest(root2, k2))  # Expected output: 3
