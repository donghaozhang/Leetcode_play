# level_order_traversal.md)

### 其他树问题
- 二叉树路径 / Binary Tree Paths [LeetCode 257]

## Problem Description

```markdown
## 257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in **any order**.

A **leaf** is a node with no children.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/12/binary-tree-paths-diagram.jpg)
```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Example 2:**

```
Input: root = [1]
Output: ["1"]
```

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 100]`.
*   `-100 <= Node.val <= 100`
```

## Solution

Okay, let's break down the LeetCode problem 257: Binary Tree Paths.

**1. Explanation of the Problem**

The problem asks us to find all possible paths starting from the root node and ending at any leaf node in a given binary tree. A leaf node is defined as a node that has no children (neither a left child nor a right child). We need to return these paths as a list of strings. Each string should represent a single path, with the values of the nodes in the path separated by "->". The order in which the paths are returned doesn't matter.

**Example:**

For the tree `[1, 2, 3, null, 5]`:
*   Node 1 is the root.
*   Node 2 is the left child of 1.
*   Node 3 is the right child of 1.
*   Node 5 is the right child of 2.
*   Nodes 5 and 3 are leaf nodes.

The paths from the root (1) to the leaves are:
*   1 -> 2 -> 5
*   1 -> 3

So the output should be `["1->2->5", "1->3"]`.

**2. Step-by-Step Approach**

This problem is a classic application of tree traversal, specifically Depth-First Search (DFS), because we need to explore paths from the root down to the leaves.

Here's a recursive DFS approach:

1.  **Initialization:**
    *   Create an empty list `results` to store the final path strings.
    *   If the input `root` is `None`, return the empty `results` list.

2.  **Recursive Helper Function (DFS):**
    *   Define a helper function, say `find_paths(node, current_path)`, where:
        *   `node` is the current node being visited.
        *   `current_path` is a list storing the values of the nodes encountered so far on the path from the root to the *parent* of the current `node`.

3.  **Inside the Helper Function:**
    *   **Append Current Node:** Add the value of the current `node` (converted to a string) to the `current_path` list.
    *   **Check for Leaf:** Determine if the current `node` is a leaf node (i.e., `node.left` is `None` and `node.right` is `None`).
        *   If it *is* a leaf node:
            *   We have found a complete root-to-leaf path.
            *   Join the elements in `current_path` with "->" to form the path string.
            *   Add this path string to the `results` list.
            *   Return (stop exploring this branch).
        *   If it *is not* a leaf node:
            *   **Explore Left Child:** If `node.left` exists, recursively call `find_paths(node.left, current_path)`.
            *   **Explore Right Child:** If `node.right` exists, recursively call `find_paths(node.right, current_path)`.
    *   **Backtrack:** After the recursive calls for the children (or after processing a leaf node), *remove* the current node's value from the `current_path` list. This is crucial for backtracking. It ensures that when we return from exploring a child, the `current_path` is correctly restored to the state it was in at the parent node, allowing us to explore other branches (like the right sibling) correctly.

4.  **Initial Call:** Start the process by calling the helper function with the `root` node and an empty initial path: `find_paths(root, [])`.

5.  **Return Result:** After the initial call completes, return the `results` list.

**Alternative (Slightly Cleaner Recursive Approach):**

Instead of passing the path *up to the parent*, pass the path *including the current node* as a string being built.

1.  **Initialization:** `results = []`. If `root` is `None`, return `[]`.
2.  **Helper Function:** `find_paths(node, path_str)`
3.  **Inside Helper:**
    *   Append `node.val` to `path_str`. If `path_str` wasn't empty, add "->" first.
    *   **Check Leaf:** If `node` is a leaf, add `path_str` to `results` and return.
    *   **Recurse:**
        *   If `node.left`: `find_paths(node.left, path_str + "->")`
        *   If `node.right`: `find_paths(node.right, path_str + "->")`
    *   (No explicit backtracking needed here as strings are immutable, and new strings are created for recursive calls).

Let's stick with the first approach (using a list and backtracking) as it's often more efficient for modifications than repeated string concatenation.

**3. Python Solution**

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Finds all root-to-leaf paths in a binary tree.
        """
        results = []
        if not root:
            return results

        # Helper function for DFS traversal
        def find_paths_recursive(node: TreeNode, current_path: List[str]):
            """
            Recursively explores paths from the current node.

            Args:
                node: The current node being visited.
                current_path: A list of node values (as strings) from the root
                              up to the current node.
            """
            # Add the current node's value to the path
            current_path.append(str(node.val))

            # Check if it's a leaf node
            if not node.left and not node.right:
                # Found a root-to-leaf path, format and add to results
                results.append("->".join(current_path))
                # Note: We still need to pop after this, so no early return here.
            else:
                # Continue DFS on children if they exist
                if node.left:
                    find_paths_recursive(node.left, current_path)
                if node.right:
                    find_paths_recursive(node.right, current_path)

            # Backtrack: remove the current node's value before returning
            # This is crucial for exploring sibling branches correctly.
            current_path.pop()

        # Start the recursion from the root with an empty path list
        find_paths_recursive(root, [])

        return results

# Helper function to build a tree from a list (Level Order Traversal)
# Handles 'None' values represented by None in the list
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [(root, 0)] # Store (node, index_in_list)
    processed_nodes = 1

    while queue and processed_nodes < len(nodes):
        current_node, current_index = queue.pop(0)

        # Process left child
        left_child_index = 2 * current_index + 1
        if left_child_index < len(nodes) and nodes[left_child_index] is not None:
            left_node = TreeNode(nodes[left_child_index])
            current_node.left = left_node
            queue.append((left_node, left_child_index))
        processed_nodes += 1

        if processed_nodes >= len(nodes):
            break

        # Process right child
        right_child_index = 2 * current_index + 2
        if right_child_index < len(nodes) and nodes[right_child_index] is not None:
            right_node = TreeNode(nodes[right_child_index])
            current_node.right = right_node
            queue.append((right_node, right_child_index))
        processed_nodes += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1
print("--- Example 1 ---")
root1 = build_tree([1, 2, 3, None, 5])
expected1 = ["1->2->5", "1->3"]
result1 = solver.binaryTreePaths(root1)
print(f"Input Tree (List): [1, 2, 3, null, 5]")
print(f"Output: {sorted(result1)}") # Sort for consistent comparison
print(f"Expected: {sorted(expected1)}")
assert sorted(result1) == sorted(expected1)
print("Passed!")

# Example 2
print("\n--- Example 2 ---")
root2 = build_tree([1])
expected2 = ["1"]
result2 = solver.binaryTreePaths(root2)
print(f"Input Tree (List): [1]")
print(f"Output: {result2}")
print(f"Expected: {expected2}")
assert result2 == expected2
print("Passed!")

# Custom Test Case 1: Empty Tree (handled by initial check)
print("\n--- Custom Test Case 1: Empty Tree ---")
root3 = build_tree([])
expected3 = []
result3 = solver.binaryTreePaths(root3)
print(f"Input Tree (List): []")
print(f"Output: {result3}")
print(f"Expected: {expected3}")
assert result3 == expected3
print("Passed!")

# Custom Test Case 2: Skewed Tree (Left)
print("\n--- Custom Test Case 2: Skewed Tree (Left) ---")
root4 = build_tree([1, 2, None, 3, None, 4, None]) # Represents 1 -> 2 -> 3 -> 4
# Note: build_tree needs careful construction for skewed trees if using level order list
# Manual construction might be clearer here:
root4_manual = TreeNode(1)
root4_manual.left = TreeNode(2)
root4_manual.left.left = TreeNode(3)
root4_manual.left.left.left = TreeNode(4)
expected4 = ["1->2->3->4"]
result4 = solver.binaryTreePaths(root4_manual)
print(f"Input Tree: 1 -> 2 -> 3 -> 4")
print(f"Output: {result4}")
print(f"Expected: {expected4}")
assert result4 == expected4
print("Passed!")

# Custom Test Case 3: Tree with multiple branches
print("\n--- Custom Test Case 3: Multiple Branches ---")
root5 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
# Leaves are: 7, 2, 13, 5, 1
expected5 = ["5->4->11->7", "5->4->11->2", "5->8->13", "5->8->4->5", "5->8->4->1"]
result5 = solver.binaryTreePaths(root5)
print(f"Input Tree (List): [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, null, 5, 1]")
print(f"Output: {sorted(result5)}")
print(f"Expected: {sorted(expected5)}")
assert sorted(result5) == sorted(expected5)
print("Passed!")

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree.
    *   We visit each node exactly once during the DFS traversal.
    *   At each leaf node, we join the path elements into a string. The sum of the lengths of all root-to-leaf paths in the worst case (a skewed tree) can be O(N^2), but in a balanced tree, it's closer to O(N log N). However, the dominant factor is visiting each node, so the overall time complexity is typically considered O(N), assuming string joining is reasonably efficient on average per path. A more precise bound considering the output size is O(N * H) in the worst case for path construction if H is the maximum path length (height).

*   **Space Complexity:**
    *   **Recursion Stack:** The depth of the recursion stack corresponds to the height of the tree, H. In the worst case (a completely skewed tree), H can be N. In the best case (a balanced tree), H is O(log N). So, the space used by the recursion stack is O(H), which is O(N) in the worst case.
    *   **`current_path` list:** This list stores the nodes along the current path. Its maximum size is also H. O(H), which is O(N) in the worst case.
    *   **`results` list:** This stores the final path strings. In the worst case (a "bushy" tree where many nodes are leaves close to the root, or a skewed tree with one long path), the total number of characters stored across all paths could be significant. For a full binary tree, there are roughly N/2 leaves, each with path length log N, giving O(N log N) space for results. For a skewed tree, there's one path of length N, giving O(N) space. The theoretical worst case for total characters could be O(N*H) or O(N^2).
    *   Combining these, the overall space complexity is dominated by the recursion stack depth and the storage for the result, leading to O(N) in the worst case for stack depth, and potentially more depending on the structure and the total length of paths stored. Often, it's simplified to O(N) considering the dominant factor in typical scenarios.

**4. Test Cases (Included in the Python code above)**

1.  **Example 1:** `root = [1, 2, 3, null, 5]` -> `["1->2->5", "1->3"]`
2.  **Example 2:** `root = [1]` -> `["1"]`
3.  **Empty Tree:** `root = []` -> `[]`
4.  **Skewed Tree:** `1 -> 2 -> 3 -> 4` -> `["1->2->3->4"]`
5.  **Complex Tree:** `[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, null, 5, 1]` -> `["5->4->11->7", "5->4->11->2", "5->8->13", "5->8->4->5", "5->8->4->1"]` (order may vary)