import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Constructing the tree: [1, null, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_example2(self):
        # Empty tree
        root = None
        self.assertEqual(self.solution.postorderTraversal(root), [])

    def test_example3(self):
        # Tree with one node: [1]
        root = TreeNode(1)
        self.assertEqual(self.solution.postorderTraversal(root), [1])

    def test_balanced_tree(self):
        # Constructing a balanced tree: [1, 2, 3]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [2, 3, 1])

if __name__ == "__main__":
    unittest.main()
