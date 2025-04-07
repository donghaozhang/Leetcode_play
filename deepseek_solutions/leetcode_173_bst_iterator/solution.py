class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Test cases
def test_bst_iterator():
    # Construct the BST from the example
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    
    iterator = BSTIterator(root)
    operations = [
        ("next", 3),
        ("next", 7),
        ("hasNext", True),
        ("next", 15),
        ("hasNext", True),
        ("next", 9),
        ("hasNext", True),
        ("next", 20),
        ("hasNext", False)
    ]
    
    for op, expected in operations:
        if op == "next":
            assert iterator.next() == expected, f"Failed {op}: expected {expected}"
        elif op == "hasNext":
            assert iterator.hasNext() == expected, f"Failed {op}: expected {expected}"
    print("All test cases passed!")

test_bst_iterator()
