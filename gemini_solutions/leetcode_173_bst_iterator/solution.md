# combination_sum.md)
- 二叉搜索树迭代器 / BST Iterator [LeetCode 173]

## Problem Description

```markdown
## 173. Binary Search Tree Iterator

Implement the `BSTIterator` class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

*   `BSTIterator(TreeNode root)` Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
*   `boolean hasNext()` Returns `true` if there exists a number in the traversal

## Solution

Okay, let's break down the BST Iterator problem (LeetCode 173).

**1. Explanation of the Problem**

The problem asks us to create a class, `BSTIterator`, that acts like an iterator for a Binary Search Tree (BST). An iterator allows us to traverse through a collection of elements one by one. Specifically, this iterator should return the nodes of the BST in *in-order* sequence.

*   **In-order Traversal:** For any node, we first visit its left subtree, then the node itself, and finally its right subtree. For a BST, this traversal visits the nodes in ascending order of their values.
*   **Iterator Methods:**
    *   `__init__(self, root)`: The constructor takes the root of the BST and initializes the iterator. The problem statement mentions initializing a pointer to a "non-existent number smaller than any element," but in practice, we just need to set up the state to be ready to return the *first* (smallest) element upon the initial `next()` call.
    *   `next(self)`: Returns the next smallest value in the BST.
    *   `hasNext(self)`: Returns `True` if there are more elements to iterate over, and `False` otherwise.

The key challenge is to implement `next()` and `hasNext()` efficiently, ideally without traversing the entire tree upfront and storing all elements (which would take O(N) space). We want a more "lazy" approach where we find the next element only when requested.

**2. Step-by-Step Approach (Controlled Iteration using a Stack)**

The standard iterative in-order traversal algorithm uses a stack. We can adapt this algorithm to maintain the iterator's state.

1.  **Initialization (`__init__`)**:
    *   Create an empty stack. This stack will store the nodes we need to visit.
    *   To prepare for the first `next()` call (which should return the smallest element), we need to find the leftmost node in the tree.
    *   Start from the `root`. Keep pushing the current node onto the stack and moving to its left child until we reach a `None` node. The node at the top of the stack after this process will be the smallest element in the BST. Let's encapsulate this logic in a helper function, say `_push_left(node)`.

2.  **Helper Function (`_push_left(node)`)**:
    *   Takes a `node` as input.
    *   While the `node` is not `None`:
        *   Push the `node` onto the stack.
        *   Move to the `node`'s left child (`node = node.left`).

3.  **`hasNext()`**:
    *   The iteration has more elements if and only if the stack is *not* empty.
    *   Return `True` if the stack has elements, `False` otherwise.

4.  **`next()`**:
    *   The next node to visit (the smallest remaining one) is currently at the top of the stack.
    *   Pop this node from the stack. Let's call it `smallest_node`.
    *   The value to return is `smallest_node.val`.
    *   *Crucially*, before returning, we need to prepare the stack for the *subsequent* `next()` call. According to in-order traversal, after visiting `smallest_node`, the next node to visit is the smallest node in its *right* subtree.
    *   Take the right child of `smallest_node` (`smallest_node.right`). If it exists, call the `_push_left` helper function on this right child to push it and all its left descendants onto the stack. This ensures the stack's top element is the next node in the in-order sequence.
    *   Return `smallest_node.val`.

**Why this works:** The stack always holds a path from the root (or a relevant subtree root) down the left branches towards the *next* node that should be visited in the in-order sequence. When we pop a node (`smallest_node`), we've "visited" it. The next node is found by exploring the right subtree of `smallest_node` and finding its leftmost element (which is handled by calling `_push_left` on `smallest_node.right`).

**3. Python Solution**

```python
import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

class BSTIterator:
    """
    Implements an iterator for in-order traversal of a BST.

    Uses a stack to simulate the recursion of in-order traversal,
    allowing for O(H) space complexity (where H is the height of the tree)
    and O(1) amortized time complexity for next() and hasNext().
    """
    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the iterator. Pushes the leftmost path onto the stack.
        """
        self.stack = []
        self._push_left(root) # Initialize stack with the path to the smallest element

    def _push_left(self, node: Optional[TreeNode]):
        """
        Helper function to push a node and all its left descendants onto the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns the next smallest number in the BST.
        - Pops the smallest node from the stack.
        - Explores the right subtree of the popped node to find the next sequence.
        """
        if not self.hasNext():
            raise StopIteration("No more elements in the BST")

        # The node at the top of the stack is the next smallest element
        smallest_node = self.stack.pop()

        # If the popped node has a right child, push the leftmost path
        # of that right child onto the stack. This sets up the stack
        # for the *next* call to next().
        if smallest_node.right:
            self._push_left(smallest_node.right)

        return smallest_node.val

    def hasNext(self) -> bool:
        """
        Returns true if there is a next smallest number, false otherwise.
        """
        # The iterator has a next element if the stack is not empty
        return len(self.stack) > 0

# Helper function to build a BST from a list (level-order)
def build_bst(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1

        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1

    return root

# --- Test Cases ---
print("--- Test Case 1: Standard BST ---")
# BST:
#     7
#    / \
#   3  15
#      / \
#     9  20
nodes1 = [7, 3, 15, None, None, 9, 20]
root1 = build_bst(nodes1)
iterator1 = BSTIterator(root1)
result1 = []
while iterator1.hasNext():
    result1.append(iterator1.next())
print(f"Input Tree (level order): {nodes1}")
print(f"In-order Traversal: {result1}")
print(f"Expected: {[3, 7, 9, 15, 20]}")
print(f"Test Passed: {result1 == [3, 7, 9, 15, 20]}")
print("-" * 20)

print("--- Test Case 2: Empty Tree ---")
nodes2 = []
root2 = build_bst(nodes2)
iterator2 = BSTIterator(root2)
result2 = []
print(f"Input Tree (level order): {nodes2}")
print(f"hasNext() initially: {iterator2.hasNext()}")
# Trying to call next() would raise StopIteration or error if not checked
try:
    val = iterator2.next() # Should not happen if hasNext is checked
    print(f"Called next() unexpectedly, got: {val}")
except StopIteration:
    print("Correctly handled empty iterator (StopIteration expected or hasNext check prevents call)")

print(f"In-order Traversal: {result2}")
print(f"Expected: {[]}")
print(f"Test Passed: {result2 == [] and not iterator2.hasNext()}")
print("-" * 20)


print("--- Test Case 3: Single Node Tree ---")
nodes3 = [1]
root3 = build_bst(nodes3)
iterator3 = BSTIterator(root3)
result3 = []
print(f"Input Tree (level order): {nodes3}")
print(f"hasNext() initially: {iterator3.hasNext()}") # Expected: True
if iterator3.hasNext():
    result3.append(iterator3.next())
    print(f"Called next(), got: {result3[-1]}") # Expected: 1
print(f"hasNext() after one call: {iterator3.hasNext()}") # Expected: False
print(f"In-order Traversal: {result3}")
print(f"Expected: {[1]}")
print(f"Test Passed: {result3 == [1] and not iterator3.hasNext()}")
print("-" * 20)

print("--- Test Case 4: Left-Skewed Tree ---")
# BST:
#     3
#    /
#   2
#  /
# 1
nodes4 = [3, 2, None, 1] # Representing level order might be tricky, let's build manually
root4 = TreeNode(3)
root4.left = TreeNode(2)
root4.left.left = TreeNode(1)
iterator4 = BSTIterator(root4)
result4 = []
while iterator4.hasNext():
    result4.append(iterator4.next())
print(f"Input Tree: Left-skewed (3 -> 2 -> 1)")
print(f"In-order Traversal: {result4}")
print(f"Expected: {[1, 2, 3]}")
print(f"Test Passed: {result4 == [1, 2, 3]}")
print("-" * 20)

print("--- Test Case 5: Right-Skewed Tree ---")
# BST:
#   1
#    \
#     2
#      \
#       3
nodes5 = [1, None, 2, None, 3] # Representing level order might be tricky, let's build manually
root5 = TreeNode(1)
root5.right = TreeNode(2)
root5.right.right = TreeNode(3)
iterator5 = BSTIterator(root5)
result5 = []
while iterator5.hasNext():
    result5.append(iterator5.next())
print(f"Input Tree: Right-skewed (1 -> 2 -> 3)")
print(f"In-order Traversal: {result5}")
print(f"Expected: {[1, 2, 3]}")
print(f"Test Passed: {result5 == [1, 2, 3]}")
print("-" * 20)

print("--- Test Case 6: Interaction Check ---")
# Same tree as Test Case 1
nodes6 = [7, 3, 15, None, None, 9, 20]
root6 = build_bst(nodes6)
iterator6 = BSTIterator(root6)
print(f"Input Tree (level order): {nodes6}")
ops_results = []
ops_results.append(f"hasNext(): {iterator6.hasNext()}") # True
ops_results.append(f"next(): {iterator6.next()}")       # 3
ops_results.append(f"next(): {iterator6.next()}")       # 7
ops_results.append(f"hasNext(): {iterator6.hasNext()}") # True
ops_results.append(f"next(): {iterator6.next()}")       # 9
ops_results.append(f"hasNext(): {iterator6.hasNext()}") # True
ops_results.append(f"next(): {iterator6.next()}")       # 15
ops_results.append(f"hasNext(): {iterator6.hasNext()}") # True
ops_results.append(f"next(): {iterator6.next()}")       # 20
ops_results.append(f"hasNext(): {iterator6.hasNext()}") # False
print("Operations and Results:")
for op_res in ops_results:
    print(op_res)
expected_ops_results = [
    "hasNext(): True", "next(): 3", "next(): 7", "hasNext(): True", "next(): 9",
    "hasNext(): True", "next(): 15", "hasNext(): True", "next(): 20", "hasNext(): False"
]
print(f"Test Passed: {ops_results == expected_ops_results}")
print("-" * 20)

```

**Complexity Analysis:**

*   **Time Complexity:**
    *   `__init__(root)`: The `_push_left` function potentially traverses down the leftmost path of the tree. In the worst case (a skewed tree), this takes O(H) time, where H is the height of the tree. In the best/average case (balanced tree), it's O(log N).
    *   `next()`: This operation involves popping one element (O(1)) and then potentially calling `_push_left` on the right child. While a single call to `next()` might take O(H) time in the worst case (if the popped node has a right child that starts a long left path), the *amortized* time complexity is O(1). This is because each node is pushed onto the stack exactly once and popped exactly once during the entire iteration over N nodes. The total time spent pushing nodes across all `next()` calls is proportional to N. Therefore, the average time per `next()` call is O(N) / N = O(1).
    *   `hasNext()`: Checking if the stack is empty takes O(1) time.

*   **Space Complexity:**
    *   The space complexity is determined by the maximum size of the stack. The stack stores nodes along a path from the root down, primarily consisting of left children. In the worst case (a skewed tree where H = N), the stack might hold up to N nodes, resulting in O(N) space. In the best and average case (a balanced BST where H = log N), the stack holds at most O(log N) nodes. Therefore, the space complexity is O(H).

This stack-based approach is generally preferred over pre-computing the entire in-order traversal into a list because it uses less space on average (O(H) vs O(N)) and performs the work incrementally ("lazily").

**4. Test Cases (Included in the Python code above)**

The provided Python code includes:

1.  A helper function `build_bst` to construct a BST from a list representation (level-order with `None` for missing nodes).
2.  Test Case 1: A standard, moderately complex BST.
3.  Test Case 2: An empty tree.
4.  Test Case 3: A tree with only a single node.
5.  Test Case 4: A left-skewed tree (worst-case height for left path).
6.  Test Case 5: A right-skewed tree (worst-case height for right path exploration).
7.  Test Case 6: Demonstrates the interaction between `hasNext` and `next` calls.

Each test case prints the input, the output traversal, the expected traversal, and whether the test passed.