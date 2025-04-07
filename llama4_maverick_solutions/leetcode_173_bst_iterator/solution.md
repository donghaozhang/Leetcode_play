# combination_sum.md)
- 二叉搜索树迭代器 / BST Iterator [LeetCode 173]

## Problem Description

## 173. Binary Search Tree Iterator

### Description
Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

*   `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to non-existent element before the first element in the in-order traversal.
*   `boolean hasNext()` Returns `true` if there exists a next element in the in-order traversal, and `false` otherwise.
*   `int next()` Returns the next element in the in-order traversal. It is guaranteed that there will be a next element.

### Example 1:
```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
```

### Constraints:

*   The number of nodes in the tree is in the range `[1, 10<sup>5</sup>]`.
*   `0 <= Node.val <= 10<sup>6</sup>`
*   At most `10<sup>5</sup>` calls will be made to `hasNext`, and `next`.

### Follow up:

*   You may assume that `next()` calls will always be valid. That is, there will be at least a next element when `next()` is called.

## Solution

## Problem Explanation

The problem requires implementing a Binary Search Tree (BST) iterator that performs an in-order traversal of the BST. The iterator should have two main methods: `hasNext()` and `next()`. The `hasNext()` method checks if there is a next element in the in-order traversal, and the `next()` method returns the next element in the in-order traversal.

The BST iterator is initialized with the root of the BST. The iterator should be able to handle a large number of nodes in the tree (up to 10^5) and a large number of calls to `hasNext()` and `next()` (up to 10^5).

## Step-by-Step Approach

1.  **Understanding the Problem**: The problem requires implementing an iterator for a Binary Search Tree (BST) that performs an in-order traversal.
2.  **In-Order Traversal**: Recall that an in-order traversal of a BST visits nodes in ascending order. It works by first visiting the left subtree, then the current node, and finally the right subtree.
3.  **Using a Stack for Iterative In-Order Traversal**: To implement the iterator, we can use a stack to perform an iterative in-order traversal. We start by pushing the root node and all its left children onto the stack.
4.  **Implementing `hasNext()` and `next()`**:
    *   `hasNext()`: Checks if the stack is not empty. If it's not empty, there is a next element.
    *   `next()`: Pops the top node from the stack, returns its value, and then pushes the right child of the popped node and all its left children onto the stack.
5.  **Handling Edge Cases**: The problem statement guarantees that `next()` will always be called when there is a next element, so we don't need to handle the case where `next()` is called on an empty iterator.

## Python Solution

```python
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
```

## Time and Space Complexity Analysis

*   **Time Complexity**:
    *   `__init__`: O(h), where h is the height of the BST. In the worst case (a skewed tree), h = n, where n is the number of nodes. In the average case (a balanced BST), h = log(n).
    *   `next()`: O(h) in the worst case because we might need to traverse down the height of the tree when pushing the right child and its left children onto the stack. However, amortized over all calls, the time complexity is O(1) because each node is visited exactly once.
    *   `hasNext()`: O(1) because it simply checks if the stack is empty.
*   **Space Complexity**: O(h) for storing nodes in the stack. In the worst case, h = n. In the average case, h = log(n).

The provided Python solution implements the BST iterator using a stack to perform an iterative in-order traversal. It includes test cases to verify the correctness of the implementation. The time and space complexity analysis is also provided to understand the performance characteristics of the solution.