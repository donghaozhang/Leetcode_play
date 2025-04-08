# lowest_common_ancestor.md)
- 二叉树展开为链表 / Flatten Binary Tree [LeetCode 114]

## Problem Description

```markdown
## 114. Flatten Binary Tree to Linked List

Given the `root` of a binary tree, flatten the tree into a "linked list":

*   The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
*   The "linked list" should be in the same order as a **pre-order traversal** of the binary tree.

**Example 1:**

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [0]
Output: [0]
```

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 2000]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?
```

## Solution

Okay, let's break down the "Flatten Binary Tree to Linked List" problem.

**1. Explanation of the Problem**

The goal is to take a given binary tree and rearrange its nodes in-place so that it forms a structure resembling a linked list. This "linked list" uses the `right` child pointer of the `TreeNode` to point to the next node in the sequence, and the `left` child pointer of every node must be set to `null`. The order of the nodes in this flattened structure must be the same as the pre-order traversal of the original binary tree.

*   **Pre-order Traversal:** Visit Node -> Visit Left Subtree -> Visit Right Subtree.
*   **Flattened Structure:** Node1 -> Node2 -> Node3 -> ... where `Node1.right` points to `Node2`, `Node2.right` points to `Node3`, etc., and `NodeX.left` is always `null`.

**Example:**

Original Tree:
```
      1
     / \
    2   5
   / \   \
  3   4   6
```

Pre-order Traversal: `1, 2, 3, 4, 5, 6`

Flattened Tree (Linked List Structure):
```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

**2. Step-by-Step Approach (O(1) Space - Iterative)**

This approach modifies the tree in-place without using recursion explicitly (avoiding O(H) stack space) or extra lists (avoiding O(N) space). It's inspired by the Morris Traversal concept.

1.  Initialize a pointer `curr` to the `root` of the tree.
2.  While `curr` is not `null`:
    a.  Check if `curr` has a left child (`curr.left`).
        i.  **If it does:**
            1.  Find the rightmost node in the left subtree of `curr`. Let's call this `predecessor`. Start from `curr.left` and keep moving right (`predecessor = predecessor.right`) until you find a node whose `right` child is `null`. This `predecessor` is the last node visited in the pre-order traversal of the left subtree.
            2.  Make the original right subtree of `curr` (`curr.right`) the right child of the `predecessor`. (`predecessor.right = curr.right`). This effectively links the end of the flattened left subtree to the start of the right subtree.
            3.  Move the entire left subtree of `curr` to become the right child of `curr`. (`curr.right = curr.left`).
            4.  Set the left child of `curr` to `null`. (`curr.left = None`). This satisfies the requirement of the flattened structure.
        ii. **If it does not** have a left child (`curr.left` is `null`):
            1.  This means `curr` is already in the correct position relative to its (non-existent) left subtree. We simply need to move to the next node in the pre-order sequence, which is its right child.
    b.  Move `curr` to its right child (`curr = curr.right`). This advances to the next node to be processed, which is either the node that was originally `curr.left` (if step 2.a.i was executed) or the node that was originally `curr.right` (if step 2.a.ii was executed).
3.  The loop terminates when `curr` becomes `null`, meaning the entire tree has been processed and flattened.

**Alternative Recursive Approach (O(N) Space due to stack):**

A common recursive approach uses a reverse pre-order traversal (Right -> Left -> Node).

1.  Maintain a global or class-level variable `prev` initialized to `None`. This `prev` will point to the previously processed node (which will become the `right` child of the current node).
2.  Define a recursive function `flatten_recursive(node)`:
    a.  Base Case: If `node` is `None`, return.
    b.  Recursively call `flatten_recursive(node.right)`.
    c.  Recursively call `flatten_recursive(node.left)`.
    d.  Process the current `node`:
        i.  Set `node.right = prev`.
        ii. Set `node.left = None`.
        iii. Update `prev = node`.
3.  Start the process by calling `flatten_recursive(root)`.

While conceptually simpler, this uses O(H) space for the recursion stack, where H is the height of the tree (O(N) in the worst case), violating the O(1) space follow-up constraint.

**3. Python Solution (O(1) Space - Iterative)**

```python
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Helper for visualizing the flattened list
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            if curr.left: # Should ideally be None after flatten
                 nodes.append(f"(L:{curr.left.val})") # Indicate error if left exists
            curr = curr.right
        return " -> ".join(nodes) if nodes else "None"

# Helper function to build a tree from a list (level-order)
def build_tree(nodes: list) -> TreeNode | None:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while i < len(nodes):
        curr = queue.popleft()
        if nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

# Helper function to represent tree structure (for debugging before flatten)
def tree_to_string(root: TreeNode | None) -> str:
    if not root:
        return "[]"
    
    nodes = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            nodes.append(str(node.val))
            # Important: Add children to queue even if None, to represent structure
            # Only stop adding children if all remaining nodes in queue are None
            # (This simple version might not perfectly match LeetCode's null representation
            # for trailing nulls, but good enough for structure check)
            queue.append(node.left)
            queue.append(node.right)
        else:
            # Only add "null" if there are potentially more nodes later
            # This part is tricky to get exactly like LeetCode's representation
            # without more complex queue management. Let's keep it simple.
             if any(n is not None for n in queue):
                 nodes.append("null")
            # pass # Avoid adding trailing nulls excessively

    # Clean up trailing nulls that might have been added
    while nodes and nodes[-1] == "null":
        nodes.pop()
        
    return "[" + ",".join(nodes) + "]"


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Flattens the binary tree in-place using O(1) extra space.
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree (predecessor)
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # --- Rewiring ---
                # 1. Connect predecessor's right to current node's right
                predecessor.right = curr.right

                # 2. Move current node's left subtree to its right
                curr.right = curr.left

                # 3. Set current node's left to None
                curr.left = None
                # --- Rewiring Done ---

            # Move to the next node in the pre-order sequence
            # This will be the node that was just moved from the left (if left existed),
            # or the original right node (if left did not exist).
            curr = curr.right

# --- Time and Space Complexity Analysis ---
# Time Complexity: O(N), where N is the number of nodes.
#   - Each node is visited as `curr` once.
#   - Finding the `predecessor` involves traversing the right spine of the left subtree.
#   - Crucially, each edge connecting a node to its right child is traversed at most twice
#     (once downwards when finding the predecessor, once downwards when `curr` moves right).
#   - Edges connecting a node to its left child are traversed once when `curr` has a left child.
#   - Therefore, the total work is proportional to the number of nodes and edges, resulting in O(N).
#
# Space Complexity: O(1).
#   - We only use a few pointers (`curr`, `predecessor`).
#   - No recursion stack is used (iterative approach).
#   - No auxiliary data structures like lists or queues are used.
#   - Modification is done in-place.

# --- Test Cases ---
solver = Solution()

# Example 1
print("--- Example 1 ---")
root1 = build_tree([1, 2, 5, 3, 4, None, 6])
print(f"Original Tree: {tree_to_string(root1)}")
solver.flatten(root1)
print(f"Flattened Tree: {root1}") # Uses the __repr__ method
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Example 2
print("\n--- Example 2 ---")
root2 = build_tree([])
print(f"Original Tree: {tree_to_string(root2)}")
solver.flatten(root2)
print(f"Flattened Tree: {root2}")
# Expected Output: None

# Example 3
print("\n--- Example 3 ---")
root3 = build_tree([0])
print(f"Original Tree: {tree_to_string(root3)}")
solver.flatten(root3)
print(f"Flattened Tree: {root3}")
# Expected Output: 0

# Additional Test Case: Left Skewed Tree
print("\n--- Test Case: Left Skewed ---")
root4 = build_tree([1, 2, None, 3, None, 4])
print(f"Original Tree: {tree_to_string(root4)}")
solver.flatten(root4)
print(f"Flattened Tree: {root4}")
# Expected Output: 1 -> 2 -> 3 -> 4

# Additional Test Case: Right Skewed Tree
print("\n--- Test Case: Right Skewed ---")
root5 = build_tree([1, None, 2, None, 3, None, 4])
print(f"Original Tree: {tree_to_string(root5)}")
solver.flatten(root5)
print(f"Flattened Tree: {root5}")
# Expected Output: 1 -> 2 -> 3 -> 4

# Additional Test Case: More Complex
print("\n--- Test Case: Complex ---")
root6 = build_tree([1, 2, 7, 3, 4, None, None, None, None, 5, 6])
# Original Structure:
#        1
#      /   \
#     2     7
#    / \
#   3   4
#      / \
#     5   6
# Pre-order: 1, 2, 3, 4, 5, 6, 7
print(f"Original Tree: {tree_to_string(root6)}")
solver.flatten(root6)
print(f"Flattened Tree: {root6}")
# Expected Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
```

**4. Test Cases Verification**

*   **Example 1:** `[1, 2, 5, 3, 4, null, 6]` -> Pre-order `1, 2, 3, 4, 5, 6`. Output: `1 -> 2 -> 3 -> 4 -> 5 -> 6`. Correct.
*   **Example 2:** `[]` -> Output: `None`. Correct.
*   **Example 3:** `[0]` -> Pre-order `0`. Output: `0`. Correct.
*   **Left Skewed:** `[1, 2, null, 3, null, 4]` -> Pre-order `1, 2, 3, 4`. Output: `1 -> 2 -> 3 -> 4`. Correct.
*   **Right Skewed:** `[1, null, 2, null, 3, null, 4]` -> Pre-order `1, 2, 3, 4`. Output: `1 -> 2 -> 3 -> 4`. Correct.
*   **Complex:** `[1, 2, 7, 3, 4, null, null, null, null, 5, 6]` -> Pre-order `1, 2, 3, 4, 5, 6, 7`. Output: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`. Correct.

The provided solution correctly implements the O(1) space iterative approach and passes the test cases.