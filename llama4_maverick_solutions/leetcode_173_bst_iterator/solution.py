class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Initializes an object of the BSTIterator class.
        
        :param root: The root of the BST.
        """
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        """
        Pushes the given node and all its left children onto the stack.
        
        :param node: The node to start pushing from.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns the next element in the in-order traversal.
        
        :return: The next element in the in-order traversal.
        """
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        Checks if there exists a next element in the in-order traversal.
        
        :return: True if there exists a next element, False otherwise.
        """
        return len(self.stack) > 0

# Test cases
def main():
    # Create a sample BST:       7
    #                           / \
    #                          3   15
    #                             /  \
    #                            9    20
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)
    print(iterator.next())     # Output: 3
    print(iterator.next())     # Output: 7
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 9
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 15
    print(iterator.hasNext())  # Output: True
    print(iterator.next())     # Output: 20
    print(iterator.hasNext())  # Output: False

if __name__ == "__main__":
    main()
