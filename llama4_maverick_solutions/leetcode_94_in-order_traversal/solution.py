import unittest

class TestInorderTraversal(unittest.TestCase):
    def test_example1(self):
        # Construct the binary tree: [4,2,5,1,3]
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1, 2, 3, 4, 5])

    def test_example2(self):
        # Construct the binary tree: [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1, 3, 2])

    def test_example3(self):
        # Empty tree
        root = None

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [])

    def test_single_node(self):
        # Single node tree
        root = TreeNode(1)

        solution = Solution()
        self.assertEqual(solution.inorderTraversal(root), [1])

if __name__ == "__main__":
    unittest.main()
