# preorder_traversal.py)
  - 中序遍历 / In-order Traversal [LeetCode 94]

## Problem Description

```markdown
# 94. Binary Tree Inorder Traversal

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Example 1:**

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```
*(Image representation of the tree for Example 1 would typically be here on LeetCode)*

**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?
```

## Solution

Okay, let's break down the Binary Tree Inorder Traversal problem (LeetCode 94).

**1. Explanation of the Problem**

The goal is to traverse a given binary tree and return a list containing the values of its nodes, visited in "inorder" sequence. Inorder traversal follows a specific pattern for any given node:

1.  Visit the entire left subtree.
2.  Visit the node itself.
3.  Visit the entire right subtree.

This process is applied recursively to every node in the tree. For example, when visiting the left subtree, the same inorder pattern (left, root, right) is applied within that subtree.

**2. Step-by-Step Approach**

We'll cover both the recursive and iterative approaches as requested.

**A) Recursive Approach**

This approach directly mirrors the definition of inorder traversal.

1.  **Base Case:** If the current node is `None`, do nothing and return.
2.  **Recursive Step (Left):** Recursively call the inorder traversal function on the left child of the current node.
3.  **Process Node (Root):** Add the value of the current node to the result list.
4.  **Recursive Step (Right):** Recursively call the inorder traversal function on the right child of the current node.

We'll need a helper function to manage the recursion and pass the result list along.

**B) Iterative Approach (Using a Stack)**

The iterative approach simulates the recursion using an explicit stack to keep track of nodes to visit later.

1.  **Initialization:**
    *   Create an empty list `result` to store the node values.
    *   Create an empty stack `stack` to store nodes.
    *   Initialize a pointer `current` to the `root` of the tree.
2.  **Traversal Loop:** Continue looping as long as `current` is not `None` OR the `stack` is not empty. This condition ensures we process all nodes.
3.  **Go Left:** While `current` is not `None`:
    *   Push the `current` node onto the `stack`. (We need to visit this node *after* its left subtree).
    *   Move `current` to its left child (`current = current.left`).
4.  **Process Node:** Once `current` becomes `None` (meaning we've gone as far left as possible), it's time to process the node at the top of the stack.
    *   Pop the top node from the `stack`. Let's call it `node`.
    *   Add `node.val` to the `result` list. (This is the "Visit the node itself" step).
5.  **Go Right:** Move `current` to the right child of the popped node (`current = node.right`). This sets up the traversal for the right subtree.
6.  **Repeat:** The loop continues. If the new `current` (the right child) is not `None`, the inner "Go Left" loop (step 3) will push it and its left descendants onto the stack. If the new `current` is `None`, the outer loop will simply pop the next node from the stack (step 4).
7.  **Termination:** The loop ends when `current` is `None` and the `stack` is empty, meaning all nodes have been processed.
8.  **Return:** Return the `result` list.

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
    # --- Recursive Approach ---
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal using recursion.
        Time Complexity: O(N), where N is the number of nodes. Each node is visited once.
        Space Complexity: O(H), where H is the height of the tree. This is due to the
                         recursion stack depth. In the worst case (skewed tree), H = N.
                         In the best case (balanced tree), H = log N.
        """
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return

        # 1. Traverse left subtree
        self._inorder_helper(node.left, result)

        # 2. Visit root node
        result.append(node.val)

        # 3. Traverse right subtree
        self._inorder_helper(node.right, result)


    # --- Iterative Approach ---
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal using iteration and a stack.
        Time Complexity: O(N), where N is the number of nodes. Each node is pushed
                         and popped from the stack exactly once.
        Space Complexity: O(H), where H is the height of the tree. This is the maximum
                          size the stack can reach. In the worst case (skewed tree),
                          H = N. In the best case (balanced tree), H = log N.
        """
        result = []
        stack = []
        current = root

        while current is not None or stack:
            # Traverse to the leftmost node
            while current is not None:
                stack.append(current)
                current = current.left

            # Current is None at this point. Pop the last node visited before going left.
            # This is the node to be processed now (inorder: Left -> *Root* -> Right)
            current = stack.pop()
            result.append(current.val)

            # Move to the right subtree
            current = current.right

        return result

# Helper function to build a tree from a list (for testing)
# LeetCode style level order representation with 'null' for missing nodes
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
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

        if i >= len(nodes):
            break

        # Process right child
        if nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1

    return root

# Helper function to print tree level order (for verification)
def print_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            # Don't add 'None' for nodes that don't exist beyond the last level
            # But we need a way to represent structure, let's refine this slightly
            # for accurate representation matching LeetCode input format.
            # This simple print might not perfectly replicate LC input for sparse trees.
             pass # Simplified for basic verification
    return result # This basic print isn't perfect for LC representation, but shows nodes


# --- Test Cases ---
solver = Solution()

# Example 1: root = [1,null,2,3] -> Inorder: [1, 3, 2]
print("--- Test Case 1 ---")
root1 = build_tree([1, None, 2, 3])
print(f"Tree (Level Order approx): {print_tree(root1)}")
result_rec1 = solver.inorderTraversal_recursive(root1)
result_iter1 = solver.inorderTraversal(root1)
print(f"Input: [1, null, 2, 3]")
print(f"Recursive Output: {result_rec1}")
print(f"Iterative Output: {result_iter1}")
assert result_rec1 == [1, 3, 2]
assert result_iter1 == [1, 3, 2]
print("Passed!")

# Example 2: root = [] -> Inorder: []
print("\n--- Test Case 2 ---")
root2 = build_tree([])
print(f"Tree (Level Order approx): {print_tree(root2)}")
result_rec2 = solver.inorderTraversal_recursive(root2)
result_iter2 = solver.inorderTraversal(root2)
print(f"Input: []")
print(f"Recursive Output: {result_rec2}")
print(f"Iterative Output: {result_iter2}")
assert result_rec2 == []
assert result_iter2 == []
print("Passed!")

# Example 3: root = [1] -> Inorder: [1]
print("\n--- Test Case 3 ---")
root3 = build_tree([1])
print(f"Tree (Level Order approx): {print_tree(root3)}")
result_rec3 = solver.inorderTraversal_recursive(root3)
result_iter3 = solver.inorderTraversal(root3)
print(f"Input: [1]")
print(f"Recursive Output: {result_rec3}")
print(f"Iterative Output: {result_iter3}")
assert result_rec3 == [1]
assert result_iter3 == [1]
print("Passed!")

# Additional Test Case: More complex tree
#       4
#      / \
#     2   5
#    / \   \
#   1   3   6
# Inorder: [1, 2, 3, 4, 5, 6]
print("\n--- Test Case 4 ---")
root4 = build_tree([4, 2, 5, 1, 3, None, 6])
# Note: print_tree helper is basic, won't show 'None' correctly here
print(f"Tree (Level Order approx): {print_tree(root4)}")
result_rec4 = solver.inorderTraversal_recursive(root4)
result_iter4 = solver.inorderTraversal(root4)
print(f"Input: [4, 2, 5, 1, 3, null, 6]")
print(f"Recursive Output: {result_rec4}")
print(f"Iterative Output: {result_iter4}")
assert result_rec4 == [1, 2, 3, 4, 5, 6]
assert result_iter4 == [1, 2, 3, 4, 5, 6]
print("Passed!")

# Additional Test Case: Left-skewed tree
#       3
#      /
#     2
#    /
#   1
# Inorder: [1, 2, 3]
print("\n--- Test Case 5 ---")
root5 = build_tree([3, 2, None, 1])
print(f"Tree (Level Order approx): {print_tree(root5)}")
result_rec5 = solver.inorderTraversal_recursive(root5)
result_iter5 = solver.inorderTraversal(root5)
print(f"Input: [3, 2, null, 1]")
print(f"Recursive Output: {result_rec5}")
print(f"Iterative Output: {result_iter5}")
assert result_rec5 == [1, 2, 3]
assert result_iter5 == [1, 2, 3]
print("Passed!")

# Additional Test Case: Right-skewed tree
#   1
#    \
#     2
#      \
#       3
# Inorder: [1, 2, 3]
print("\n--- Test Case 6 ---")
root6 = build_tree([1, None, 2, None, 3])
print(f"Tree (Level Order approx): {print_tree(root6)}")
result_rec6 = solver.inorderTraversal_recursive(root6)
result_iter6 = solver.inorderTraversal(root6)
print(f"Input: [1, null, 2, null, 3]")
print(f"Recursive Output: {result_rec6}")
print(f"Iterative Output: {result_iter6}")
assert result_rec6 == [1, 2, 3]
assert result_iter6 == [1, 2, 3]
print("Passed!")
```

**4. Test Cases**

The code above includes the following test cases:

1.  **Example 1:** `[1, null, 2, 3]` -> `[1, 3, 2]` (Basic right-heavy case)
2.  **Example 2:** `[]` -> `[]` (Empty tree)
3.  **Example 3:** `[1]` -> `[1]` (Single node tree)
4.  **Complex Tree:** `[4, 2, 5, 1, 3, null, 6]` -> `[1, 2, 3, 4, 5, 6]` (More balanced tree)
5.  **Left-Skewed Tree:** `[3, 2, null, 1]` -> `[1, 2, 3]` (Worst-case for stack depth)
6.  **Right-Skewed Tree:** `[1, null, 2, null, 3]` -> `[1, 2, 3]` (Another skewed case)

These test cases cover the examples provided, edge cases (empty, single node), and different tree structures (balanced, skewed) to ensure the robustness of both the recursive and iterative solutions. The `build_tree` helper function allows for easy creation of trees from LeetCode-style list representations.