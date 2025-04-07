import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Constructing the tree: [1, null, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 3])

    def test_example2(self):
        # Empty tree
        root = None
        self.assertEqual(self.solution.preorderTraversal(root), [])

    def test_example3(self):
        # Tree with single node: [1]
        root = TreeNode(1)
        self.assertEqual(self.solution.preorderTraversal(root), [1])

    def test_balanced_tree(self):
        # Constructing a balanced tree: [1, 2, 3, 4, 5, 6, 7]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.preorderTraversal(root), [1, 2, 4, 5, 3, 6, 7])

if __name__ == "__main__":
    unittest.main()
