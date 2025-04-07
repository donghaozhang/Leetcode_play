# combination_sum.md)
- 二叉搜索树迭代器 / BST Iterator [LeetCode 173]

## Problem Description

Here is the full description of LeetCode problem #173, "Binary Search Tree Iterator":

---

Implement the `BSTIterator` class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- `boolean hasNext()` Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

**Example 1:**

![BST iterator diagram](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)

```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 15, true, 9, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return true
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return true
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return true
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return false
```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10^5]`.
- `0 <= Node.val <= 10^6`
- At most `10^5` calls will be made to `hasNext`, and `next`.

**Follow up:**

- Could you implement `next()` and `hasNext()` to run in average `O(1)` time and use `O(h)` memory, where `h` is the height of the tree?

--- 

Let me know if you'd like any clarification or additional details!

## Solution

### Explanation of the Problem

The problem requires implementing an iterator for a Binary Search Tree (BST) that traverses the tree in in-order. The iterator should support two main operations:
1. `next()`: Returns the next smallest number in the BST.
2. `hasNext()`: Returns whether there are more elements to traverse.

The challenge is to ensure that these operations are efficient, especially given the constraints where the tree can have up to 10^5 nodes and up to 10^5 calls to these methods.

### Approach
To efficiently implement the BST iterator, we can simulate the in-order traversal using a stack. The in-order traversal of a BST yields nodes in ascending order. The stack helps in keeping track of the nodes to be visited next, allowing us to break down the traversal into smaller steps controlled by `next()` and `hasNext()`.

1. **Initialization (Constructor)**: Start by pushing all the leftmost nodes into the stack. This sets up the stack to have the smallest element at the top, which will be the first element returned by `next()`.
2. **next()**: The top of the stack is the next smallest element. After popping it, we need to push all the leftmost nodes of the right subtree of the popped node to maintain the in-order sequence.
3. **hasNext()**: Simply check if the stack is not empty. If it's not empty, there are more elements to traverse.

This approach ensures that each node is pushed and popped exactly once, making the average time complexity of `next()` and `hasNext()` O(1) per operation. The space complexity is O(h), where h is the height of the tree, as the stack will hold at most h nodes at any time (one node from each level of the tree).

### Solution Code
```python
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
```

### Explanation of the Code
1. **TreeNode Class**: Defines the structure of a BST node with `val`, `left`, and `right` attributes.
2. **BSTIterator Class**:
   - **__init__**: Initializes the stack and pushes all leftmost nodes starting from the root.
   - **_leftmost_inorder**: Helper method to push all left children of a node onto the stack.
   - **next**: Pops the top node from the stack (next smallest), processes its right subtree by pushing all leftmost nodes of the right child, and returns the node's value.
   - **hasNext**: Checks if the stack is non-empty.
3. **Test Function**: Constructs the BST from the example, initializes the iterator, and verifies each operation against expected results.

This approach efficiently handles the in-order traversal step-by-step, meeting the O(1) average time complexity for `next()` and `hasNext()`, and O(h) space complexity.