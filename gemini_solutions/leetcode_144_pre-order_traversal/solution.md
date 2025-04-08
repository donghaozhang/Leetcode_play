# tree_traversal.md)
  - 先序遍历 / Pre-order Traversal [LeetCode 144]

## Problem Description

```markdown
### 144. Binary Tree Preorder Traversal

Given the `root` of a binary tree, return the *preorder traversal* of its nodes' values.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/15/preorder_1.png)

**Input:** root = [1,null,2,3]
**Output:** [1,2,3]

**Example 2:**

**Input:** root = []
**Output:** []

**Example 3:**

**Input:** root = [1]
**Output:** [1]

**Example 4:**

![](https://assets.leetcode.com/uploads/2020/09/15/preorder_2.png)

**Input:** root = [1,2]
**Output:** [1,2]

**Example 5:**

![](https://assets.leetcode.com/uploads/2020/09/15/preorder_3.png)

**Input:** root = [1,null,2]
**Output:** [1,2]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?
```

## Solution

Okay, let's break down the Binary Tree Preorder Traversal problem.

**1. Explanation of the Problem**

The problem asks us to traverse a given binary tree and return a list containing the values of the nodes visited in "preorder". Preorder traversal follows a specific sequence:

1.  **Visit** the current node (add its value to the list).
2.  Recursively traverse the **left** subtree.
3.  Recursively traverse the **right** subtree.

We need to implement this traversal and return the resulting list of node values. The problem also specifically asks for an iterative solution as a follow-up, since the recursive one is considered straightforward.

**2. Step-by-Step Approach (Iterative)**

The recursive approach directly mirrors the definition: visit the root, recurse left, recurse right.

For the iterative approach, we need to simulate the recursion's call stack using an explicit stack data structure.

1.  **Initialization:**
    *   Create an empty list `result` to store the node values.
    *   Create an empty stack (e.g., a Python list) to keep track of nodes to visit.
    *   If the `root` node is `None`, the tree is empty, so return the empty `result` list.

2.  **Start Traversal:**
    *   Push the `root` node onto the stack.

3.  **Processing Loop:**
    *   While the stack is not empty:
        *   **Pop** a node from the top of the stack. Let's call it `current_node`.
        *   **Visit:** Add the `current_node.val` to the `result` list. This is the "Visit" step of preorder.
        *   **Push Right Child (if exists):** Since a stack is Last-In, First-Out (LIFO), and we want to process the left child *before* the right child, we must push the right child onto the stack *first*. If `current_node.right` is not `None`, push it onto the stack.
        *   **Push Left Child (if exists):** Now, push the left child onto the stack. If `current_node.left` is not `None`, push it onto the stack. This ensures that the left child will be the next node popped and processed.

4.  **Return Result:**
    *   Once the stack is empty, all nodes have been visited in preorder. Return the `result` list.

**Why push Right then Left?**
Imagine the stack. When you process a node `N`, you add its value. Then you want to process `N.left` next, and *after* that, `N.right`. To achieve this with a LIFO stack, you put the thing you want to process *last* (`N.right`) onto the stack first, followed by the thing you want to process *next* (`N.left`). When you pop, `N.left` comes out first.

**3. Python Solution**

```python
import collections
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Solves the Binary Tree Preorder Traversal problem iteratively.
    """
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative preorder traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of node values in preorder.
        """
        if not root:
            return []

        result = []
        # Use a list as a stack (LIFO)
        stack = [root]

        while stack:
            # Pop the next node to visit
            node = stack.pop()

            # Visit the node (add its value to the result)
            result.append(node.val)

            # Push the right child first (if exists) so it's processed after the left
            if node.right:
                stack.append(node.right)

            # Push the left child last (if exists) so it's processed next
            if node.left:
                stack.append(node.left)

        return result

# --- Helper function to build tree from list (for testing) ---
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes):
            # Process right child
            if nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1: root = [1,null,2,3]
# Tree structure:
#    1
#     \
#      2
#     /
#    3
root1 = build_tree([1, None, 2, 3])
expected1 = [1, 2, 3]
result1 = solver.preorderTraversal(root1)
print(f"Test Case 1: Input: [1, null, 2, 3], Output: {result1}, Expected: {expected1}")
assert result1 == expected1

# Example 2: root = []
root2 = build_tree([])
expected2 = []
result2 = solver.preorderTraversal(root2)
print(f"Test Case 2: Input: [], Output: {result2}, Expected: {expected2}")
assert result2 == expected2

# Example 3: root = [1]
root3 = build_tree([1])
expected3 = [1]
result3 = solver.preorderTraversal(root3)
print(f"Test Case 3: Input: [1], Output: {result3}, Expected: {expected3}")
assert result3 == expected3

# Example 4: root = [1, 2]
# Tree structure:
#    1
#   /
#  2
root4 = build_tree([1, 2])
expected4 = [1, 2]
result4 = solver.preorderTraversal(root4)
print(f"Test Case 4: Input: [1, 2], Output: {result4}, Expected: {expected4}")
assert result4 == expected4

# Example 5: root = [1, null, 2]
# Tree structure:
#    1
#     \
#      2
root5 = build_tree([1, None, 2])
expected5 = [1, 2]
result5 = solver.preorderTraversal(root5)
print(f"Test Case 5: Input: [1, null, 2], Output: {result5}, Expected: {expected5}")
assert result5 == expected5

# More Complex Tree: root = [3, 1, 2]
# Tree structure:
#    3
#   / \
#  1   2
root6 = build_tree([3, 1, 2])
expected6 = [3, 1, 2]
result6 = solver.preorderTraversal(root6)
print(f"Test Case 6: Input: [3, 1, 2], Output: {result6}, Expected: {expected6}")
assert result6 == expected6

# Deeper Tree: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
# Tree structure:
#        5
#       / \
#      4   8
#     /   / \
#    11  13  4
#   /  \    / \
#  7    2  5   1
root7 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
expected7 = [5, 4, 11, 7, 2, 8, 13, 4, 5, 1]
result7 = solver.preorderTraversal(root7)
print(f"Test Case 7: Input: [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], Output: {result7}, Expected: {expected7}")
assert result7 == expected7

print("\nAll test cases passed!")


# --- Recursive Solution (for comparison) ---
class SolutionRecursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return
        result.append(node.val)      # Visit root
        self._preorder(node.left, result)  # Traverse left
        self._preorder(node.right, result) # Traverse right

# You can uncomment the below lines to test the recursive solution as well
# solver_rec = SolutionRecursive()
# print("\n--- Testing Recursive Solution ---")
# print(f"Test Case 1 (Recursive): {solver_rec.preorderTraversal(root1)}")
# print(f"Test Case 7 (Recursive): {solver_rec.preorderTraversal(root7)}")
```

**Complexity Analysis (Iterative Solution):**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. Each node is pushed onto the stack exactly once and popped exactly once. Visiting the node and accessing its children takes constant time.
*   **Space Complexity:** O(H) in the average case and O(N) in the worst case, where H is the height of the tree. The space is determined by the maximum size of the stack.
    *   In the best case (a balanced binary tree), the height H is log N, so the space complexity is O(log N).
    *   In the worst case (a skewed tree, like a linked list), the height H is N, and the stack might hold up to N nodes (e.g., if it's skewed to the left, all nodes get pushed before popping). So the worst-case space complexity is O(N).

**4. Test Cases**

The provided Python code includes a `build_tree` helper function and several test cases:

1.  `[1, null, 2, 3]` -> `[1, 2, 3]` (Basic right-heavy)
2.  `[]` -> `[]` (Empty tree)
3.  `[1]` -> `[1]` (Single node)
4.  `[1, 2]` -> `[1, 2]` (Left child only)
5.  `[1, null, 2]` -> `[1, 2]` (Right child only)
6.  `[3, 1, 2]` -> `[3, 1, 2]` (Simple full tree)
7.  `[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]` -> `[5, 4, 11, 7, 2, 8, 13, 4, 5, 1]` (More complex tree)

These test cases cover various tree structures, including empty, single-node, skewed, and more balanced trees, ensuring the iterative solution works correctly.