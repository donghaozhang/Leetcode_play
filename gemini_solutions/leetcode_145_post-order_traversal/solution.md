# inorder_traversal.py)
  - 后序遍历 / Post-order Traversal [LeetCode 145]

## Problem Description

```markdown
# 145. Binary Tree Postorder Traversal

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

**Example 1:**

```
Input: root = [1,null,2,3]
Output: [3,2,1]
```
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg" style="width: 127px; height: 183px;">

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

Okay, let's break down the Binary Tree Postorder Traversal problem.

**1. Explanation of the Problem**

The problem asks us to traverse a given binary tree and return a list containing the values of the nodes visited in a specific order called "postorder". Postorder traversal follows these steps for any given node:

1.  Traverse the left subtree completely (postorder).
2.  Traverse the right subtree completely (postorder).
3.  Visit the node itself (add its value to the list).

This "Left -> Right -> Root" pattern is applied recursively throughout the tree.

**Example:**

For the tree `[1, null, 2, 3]`:

```
    1
     \
      2
     /
    3
```

1.  Start at root `1`. Go left (null).
2.  Go right to node `2`.
3.  From node `2`, go left to node `3`.
4.  From node `3`, go left (null).
5.  From node `3`, go right (null).
6.  Visit node `3`. Add `3` to the list. Result: `[3]`
7.  Return to node `2`. Left subtree (`3`) is done.
8.  From node `2`, go right (null).
9.  Visit node `2`. Add `2` to the list. Result: `[3, 2]`
10. Return to node `1`. Left subtree (null) is done. Right subtree (`2`) is done.
11. Visit node `1`. Add `1` to the list. Result: `[3, 2, 1]`

The final postorder traversal is `[3, 2, 1]`.

**2. Step-by-Step Approach**

We'll cover both the recursive and iterative solutions as requested.

**A. Recursive Approach**

This approach directly mirrors the definition of postorder traversal.

1.  **Base Case:** If the current node is `None`, return (do nothing).
2.  **Recursive Step 1:** Recursively call the postorder function on the left child of the current node.
3.  **Recursive Step 2:** Recursively call the postorder function on the right child of the current node.
4.  **Process Node:** Add the value of the current node to the result list.

We need a helper function to manage the recursion and pass the result list along.

**B. Iterative Approach (Using a Modified Preorder)**

A common iterative technique for postorder traversal involves modifying the preorder traversal (Root -> Left -> Right).

1.  **Modified Preorder:** Perform a traversal in the order: Root -> Right -> Left.
2.  **Reverse:** Reverse the result obtained from the modified preorder traversal. The reversed sequence will be Left -> Right -> Root, which is the desired postorder traversal.

**Steps for Iterative (Modified Preorder + Reverse):**

1.  Initialize an empty list `result` to store the final postorder sequence.
2.  Initialize an empty list `nodes` to store the intermediate (Root -> Right -> Left) sequence.
3.  Initialize an empty stack and push the `root` node onto it (if the tree is not empty).
4.  **Loop:** While the stack is not empty:
    a.  Pop a node (`current`) from the stack.
    b.  Add the `current` node's value to the *beginning* of the `result` list (or add to the end of `nodes` and reverse `nodes` later). Let's use the latter approach for clarity. Add `current.val` to `nodes`.
    c.  Push the *left* child of `current` onto the stack (if it exists).
    d.  Push the *right* child of `current` onto the stack (if it exists). **Note:** We push left then right, so that when popping, the right child is processed *before* the left child, achieving the Root -> Right -> Left order.
5.  **Final Step:** After the loop finishes, the `nodes` list contains the values in Root -> Right -> Left order. Reverse the `nodes` list to get the final postorder result. Return the reversed list.

**Alternative Iterative Approach (Using One Stack and Tracking)**

This method is more complex but avoids the final reversal step. It simulates the recursion more closely by keeping track of the last visited node.

1. Initialize an empty `stack`, an empty `result` list, and `last_visited = None`.
2. Push the `root` onto the `stack`.
3. While the `stack` is not empty:
    a. Peek at the top node (`peek_node = stack[-1]`).
    b. Check if we should visit the children or process the `peek_node`:
       i. If `peek_node` is a leaf (`peek_node.left is None and peek_node.right is None`) OR
       ii. If the last visited node was the right child (`last_visited == peek_node.right`) OR
       iii. If the last visited node was the left child and there's no right child (`last_visited == peek_node.left and peek_node.right is None`):
          - Pop the node: `node = stack.pop()`.
          - Append `node.val` to `result`.
          - Update `last_visited = node`.
       iv. Else (need to visit children):
          - If `peek_node.right` exists, push it onto the stack.
          - If `peek_node.left` exists, push it onto the stack.
          - **Important Correction:** This logic is tricky. A better way for the one-stack approach without reversal is:
             1. Initialize `stack`, `result`, `last_node_visited = None`, `node = root`.
             2. Loop while `stack` or `node` is not empty/null:
                a. While `node` is not `None`:
                   Push `node` onto `stack`.
                   `node = node.left` (Go as far left as possible).
                b. `peek_node = stack[-1]` (Peek at the stack top).
                c. If `peek_node.right` exists and `last_node_visited != peek_node.right`:
                   `node = peek_node.right` (Move to the right child to explore it).
                d. Else (right child doesn't exist or has been visited):
                   Pop `peek_node` from `stack`.
                   Append `peek_node.val` to `result`.
                   `last_node_visited = peek_node`.
                   `node = None` (Set node to None so we continue processing from the stack).
             3. Return `result`.

We will implement the **Modified Preorder + Reverse** method as it's generally considered more straightforward for iterative postorder.

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

    def __repr__(self):
        # Helper for printing tree nodes during testing
        return f"TreeNode({self.val})"

# Helper function to build a tree from a list (Level Order)
# For example: [1, None, 2, 3] -> Tree structure shown in Example 1
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        current_node = queue.popleft()
        
        # Process left child
        if nodes[i] is not None:
            left_child = TreeNode(nodes[i])
            current_node.left = left_child
            queue.append(left_child)
        i += 1
        
        if i >= len(nodes):
            break
            
        # Process right child
        if nodes[i] is not None:
            right_child = TreeNode(nodes[i])
            current_node.right = right_child
            queue.append(right_child)
        i += 1
        
    return root

class Solution:
    """
    Solves the Binary Tree Postorder Traversal problem (LeetCode 145).
    """
    
    # --- Recursive Solution ---
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal using recursion.
        """
        result = []
        self._postorder_helper(root, result)
        return result

    def _postorder_helper(self, node: Optional[TreeNode], result: List[int]):
        """
        Helper recursive function for postorder traversal.
        """
        if node is None:
            return
        
        # 1. Traverse left subtree
        self._postorder_helper(node.left, result)
        
        # 2. Traverse right subtree
        self._postorder_helper(node.right, result)
        
        # 3. Visit the node itself
        result.append(node.val)

    # --- Iterative Solution (Modified Preorder + Reverse) ---
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postorder traversal using an iterative approach
        (Modified Preorder + Reverse).
        """
        if not root:
            return []

        stack = [root]
        nodes_reversed_postorder = [] # Stores nodes in Root -> Right -> Left order

        while stack:
            node = stack.pop()
            nodes_reversed_postorder.append(node.val)
            
            # Push left child first, then right child
            # So that right child is processed before left child (LIFO)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        # Reverse the list to get the actual postorder (Left -> Right -> Root)
        return nodes_reversed_postorder[::-1]

    # --- Main function (defaults to iterative as per follow-up) ---
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Main entry point, uses the iterative solution.
        """
        return self.postorderTraversalIterative(root)
        # return self.postorderTraversalRecursive(root) # Or use recursive


# --- Complexity Analysis ---
# Recursive Solution:
#   - Time Complexity: O(N), where N is the number of nodes in the tree. Each node is visited exactly once.
#   - Space Complexity: O(H), where H is the height of the tree. This is for the recursion call stack. 
#     In the worst case (a skewed tree), H can be N, leading to O(N) space. 
#     For a balanced tree, H is O(log N).

# Iterative Solution (Modified Preorder + Reverse):
#   - Time Complexity: O(N). Each node is pushed onto and popped from the stack once (O(N)). 
#     Appending to the intermediate list takes O(N). Reversing the list takes O(N). Total: O(N).
#   - Space Complexity: O(N). The stack can hold up to O(N) nodes in the worst case (skewed tree). 
#     The `nodes_reversed_postorder` list also stores N values. Total: O(N).


# --- Test Cases ---
solver = Solution()

# Example 1: root = [1,null,2,3] -> Output: [3,2,1]
root1 = build_tree([1, None, 2, 3])
print("Test Case 1:")
print(f"Input Tree (constructed from list): {root1.val if root1 else None}, L:{root1.left}, R:{root1.right.val if root1 and root1.right else None}, R->L:{root1.right.left.val if root1 and root1.right and root1.right.left else None}")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root1)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root1)}")
print("-" * 20)

# Example 2: root = [] -> Output: []
root2 = build_tree([])
print("Test Case 2:")
print(f"Input Tree (constructed from list): None")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root2)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root2)}")
print("-" * 20)

# Example 3: root = [1] -> Output: [1]
root3 = build_tree([1])
print("Test Case 3:")
print(f"Input Tree (constructed from list): {root3.val if root3 else None}")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root3)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root3)}")
print("-" * 20)

# Additional Test Case: More complex tree
# root = [3, 9, 20, null, null, 15, 7] -> Output: [9, 15, 7, 20, 3]
#       3
#      / \
#     9  20
#       /  \
#      15   7
root4 = build_tree([3, 9, 20, None, None, 15, 7])
print("Test Case 4:")
print(f"Input Tree (constructed from list): [3, 9, 20, None, None, 15, 7]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root4)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root4)}")
print("-" * 20)

# Additional Test Case: Left-skewed tree
# root = [1, 2, null, 3, null, 4, null] -> Output: [4, 3, 2, 1]
#       1
#      /
#     2
#    /
#   3
#  /
# 4
root5 = build_tree([1, 2, None, 3, None, 4, None])
print("Test Case 5:")
print(f"Input Tree (constructed from list): [1, 2, None, 3, None, 4, None]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root5)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root5)}")
print("-" * 20)

# Additional Test Case: Right-skewed tree
# root = [1, null, 2, null, 3, null, 4] -> Output: [4, 3, 2, 1]
#       1
#        \
#         2
#          \
#           3
#            \
#             4
root6 = build_tree([1, None, 2, None, 3, None, 4])
print("Test Case 6:")
print(f"Input Tree (constructed from list): [1, None, 2, None, 3, None, 4]")
print(f"Recursive Output: {solver.postorderTraversalRecursive(root6)}")
print(f"Iterative Output: {solver.postorderTraversalIterative(root6)}")
print("-" * 20)
```

**4. Test Cases Verification**

*   **Test Case 1:** `root = [1, null, 2, 3]`
    *   Recursive Output: `[3, 2, 1]` (Correct)
    *   Iterative Output: `[3, 2, 1]` (Correct)
*   **Test Case 2:** `root = []`
    *   Recursive Output: `[]` (Correct)
    *   Iterative Output: `[]` (Correct)
*   **Test Case 3:** `root = [1]`
    *   Recursive Output: `[1]` (Correct)
    *   Iterative Output: `[1]` (Correct)
*   **Test Case 4:** `root = [3, 9, 20, None, None, 15, 7]`
    *   Recursive Output: `[9, 15, 7, 20, 3]` (Correct)
    *   Iterative Output: `[9, 15, 7, 20, 3]` (Correct)
*   **Test Case 5:** Left-skewed `[1, 2, None, 3, None, 4, None]`
    *   Recursive Output: `[4, 3, 2, 1]` (Correct)
    *   Iterative Output: `[4, 3, 2, 1]` (Correct)
*   **Test Case 6:** Right-skewed `[1, None, 2, None, 3, None, 4]`
    *   Recursive Output: `[4, 3, 2, 1]` (Correct)
    *   Iterative Output: `[4, 3, 2, 1]` (Correct)

The provided code includes both recursive and iterative solutions, complexity analysis, and test cases demonstrating correctness for various tree structures. The iterative solution uses the common and relatively easy-to-understand "Modified Preorder + Reverse" strategy.