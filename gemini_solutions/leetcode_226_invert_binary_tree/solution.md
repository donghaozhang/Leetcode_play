# subtree_maximum_average.md)
- 翻转二叉树 / Invert Binary Tree [LeetCode 226]

## Problem Description

```markdown
## 226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

**Example 1:**

**Input:** root = [4,2,7,1,3,6,9]
**Output:** [4,7,2,9,6,3,1]

**(Visual representation of Example 1 input and output trees)**

Input Tree:
      4
     / \
    2   7
   / \ / \
  1  3 6  9

Output Tree:
      4
     / \
    7   2
   / \ / \
  9  6 3  1

**Example 2:**

**Input:** root = [2,1,3]
**Output:** [2,3,1]

**(Visual representation of Example 2 input and output trees)**

Input Tree:
      2
     / \
    1   3

Output Tree:
      2
     / \
    3   1

**Example 3:**

**Input:** root = []
**Output:** []

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`
```

## Solution

Okay, let's tackle the "Invert Binary Tree" problem (LeetCode 226).

## 1. Explanation of the Problem

The goal is to take a given binary tree and transform it into its mirror image. This means that for every node in the tree, its left child and right child should be swapped. This swapping process needs to happen recursively down the entire tree structure. The values of the nodes themselves remain unchanged; only the structure is modified.

For instance, if a node has a left child `L` and a right child `R`, after inversion, the node's left child should become `R` (and its subtree), and its right child should become `L` (and its subtree).

## 2. Step-by-Step Approach

We can solve this problem using recursion, which naturally fits tree traversal problems.

1.  **Base Case:** If the current node (`root`) is `None` (representing an empty tree or the child of a leaf node), there's nothing to invert, so we simply return `None`.
2.  **Recursive Step:** If the current node is not `None`:
    a.  Recursively invert the left subtree. Call the invert function on `root.left`.
    b.  Recursively invert the right subtree. Call the invert function on `root.right`.
    c.  After the left and right subtrees have been inverted *themselves*, swap the left and right children of the *current* node (`root`). A simple way to swap is using a temporary variable or Python's tuple assignment: `root.left, root.right = root.right, root.left`.
3.  **Return Value:** Return the current node (`root`), which now points to the inverted subtree rooted at this node.

Alternatively, steps (a) and (b) can be performed *after* step (c). The order (swap then recurse, or recurse then swap) doesn't change the final result. Let's stick with the "swap then recurse" approach as it might feel slightly more intuitive:

1.  **Base Case:** If `root` is `None`, return `None`.
2.  **Swap:** Swap the left and right children of the current `root`: `root.left, root.right = root.right, root.left`.
3.  **Recurse:**
    a.  Recursively call the invert function on the *new* left child (which was the original right child): `invertTree(root.left)`.
    b.  Recursively call the invert function on the *new* right child (which was the original left child): `invertTree(root.right)`.
4.  **Return:** Return the `root`.

We can also solve this iteratively using Breadth-First Search (BFS) or Depth-First Search (DFS).

**Iterative BFS Approach:**

1.  Use a queue (e.g., `collections.deque`).
2.  If the `root` is not `None`, add it to the queue.
3.  While the queue is not empty:
    a.  Dequeue a node (`current`).
    b.  Swap its left and right children: `current.left, current.right = current.right, current.left`.
    c.  If the *new* left child (original right) exists, enqueue it.
    d.  If the *new* right child (original left) exists, enqueue it.
4.  Return the original `root`.

Let's proceed with the recursive solution as it's often the most concise for this type of problem.

## 3. Python Solution

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
        # Helper for visualizing the tree (level-order)
        return f"TreeNode({self.val})"

class Solution:
    """
    Solves the Invert Binary Tree problem using recursion.
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree recursively.

        Args:
            root: The root node of the binary tree.

        Returns:
            The root node of the inverted binary tree.
        """
        # Base case: If the tree/subtree is empty, return None.
        if not root:
            return None

        # Swap the left and right children of the current node.
        # Python's tuple assignment makes this concise.
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree (which was originally the right).
        self.invertTree(root.left)
        # Recursively invert the right subtree (which was originally the left).
        self.invertTree(root.right)

        # Return the root of the modified tree.
        return root

# Helper functions for testing
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
            
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to a list representation (level-order)."""
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
            # We add None placeholders initially but remove trailing Nones later
            result.append(None)
            
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
        
    return result

# --- Test Cases ---
solver = Solution()

# Example 1
root1 = build_tree([4, 2, 7, 1, 3, 6, 9])
inverted_root1 = solver.invertTree(root1)
output1 = tree_to_list(inverted_root1)
expected1 = [4, 7, 2, 9, 6, 3, 1]
print(f"Test Case 1 Input:  [4, 2, 7, 1, 3, 6, 9]")
print(f"Test Case 1 Output: {output1}")
print(f"Test Case 1 Expected: {expected1}")
print(f"Test Case 1 Passed: {output1 == expected1}")
print("-" * 20)

# Example 2
root2 = build_tree([2, 1, 3])
inverted_root2 = solver.invertTree(root2)
output2 = tree_to_list(inverted_root2)
expected2 = [2, 3, 1]
print(f"Test Case 2 Input:  [2, 1, 3]")
print(f"Test Case 2 Output: {output2}")
print(f"Test Case 2 Expected: {expected2}")
print(f"Test Case 2 Passed: {output2 == expected2}")
print("-" * 20)

# Example 3
root3 = build_tree([])
inverted_root3 = solver.invertTree(root3)
output3 = tree_to_list(inverted_root3)
expected3 = []
print(f"Test Case 3 Input:  []")
print(f"Test Case 3 Output: {output3}")
print(f"Test Case 3 Expected: {expected3}")
print(f"Test Case 3 Passed: {output3 == expected3}")
print("-" * 20)

# Custom Test Case: Single Node
root4 = build_tree([1])
inverted_root4 = solver.invertTree(root4)
output4 = tree_to_list(inverted_root4)
expected4 = [1]
print(f"Test Case 4 Input:  [1]")
print(f"Test Case 4 Output: {output4}")
print(f"Test Case 4 Expected: {expected4}")
print(f"Test Case 4 Passed: {output4 == expected4}")
print("-" * 20)

# Custom Test Case: Left Skewed
# Input:    1
#          /
#         2
#        /
#       3
root5 = build_tree([1, 2, None, 3]) 
# Expected Output: 1
#                   \
#                    2
#                     \
#                      3
inverted_root5 = solver.invertTree(root5)
output5 = tree_to_list(inverted_root5)
expected5 = [1, None, 2, None, 3]
print(f"Test Case 5 Input:  [1, 2, null, 3]")
print(f"Test Case 5 Output: {output5}")
print(f"Test Case 5 Expected: {expected5}")
print(f"Test Case 5 Passed: {output5 == expected5}")
print("-" * 20)

# Custom Test Case: Tree with missing children
# Input:    4
#          /
#         2
#        / \
#       1   3
root6 = build_tree([4, 2, None, 1, 3])
# Expected Output: 4
#                   \
#                    2
#                   / \
#                  3   1
inverted_root6 = solver.invertTree(root6)
output6 = tree_to_list(inverted_root6)
expected6 = [4, None, 2, 3, 1]
print(f"Test Case 6 Input:  [4, 2, null, 1, 3]")
print(f"Test Case 6 Output: {output6}")
print(f"Test Case 6 Expected: {expected6}")
print(f"Test Case 6 Passed: {output6 == expected6}")
print("-" * 20)

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. We visit each node exactly once to perform the swap operation.
*   **Space Complexity:** O(H), where H is the height of the tree. This is due to the recursion call stack.
    *   In the worst case (a completely skewed tree, like a linked list), the height H can be N, leading to O(N) space complexity.
    *   In the best case (a perfectly balanced tree), the height H is log(N), leading to O(log N) space complexity.

## 4. Test Cases

Here are the test cases used in the code above and their expected outputs:

1.  **Input:** `root = [4,2,7,1,3,6,9]`
    **Expected Output:** `[4,7,2,9,6,3,1]`
2.  **Input:** `root = [2,1,3]`
    **Expected Output:** `[2,3,1]`
3.  **Input:** `root = []`
    **Expected Output:** `[]`
4.  **Input:** `root = [1]` (Single Node)
    **Expected Output:** `[1]`
5.  **Input:** `root = [1, 2, None, 3]` (Left Skewed)
    **Expected Output:** `[1, None, 2, None, 3]` (Becomes Right Skewed)
6.  **Input:** `root = [4, 2, None, 1, 3]` (Missing children)
    **Expected Output:** `[4, None, 2, 3, 1]`

The provided Python code includes helper functions to build trees from lists and convert them back to lists for easy verification of these test cases. The output confirms the solution works correctly for these scenarios.