# postorder_traversal.py)
- 层序遍历 / Level Order Traversal [LeetCode 102]

## Problem Description

```markdown
## 102. Binary Tree Level Order Traversal

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```
Input: root = []
Output: []
```

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 2000]`.
*   `-1000 <= Node.val <= 1000`
```

## Solution

Okay, let's break down the Binary Tree Level Order Traversal problem (LeetCode 102).

**1. Explanation of the Problem**

The goal is to traverse a given binary tree level by level, starting from the root. For each level, we need to collect the values of the nodes from left to right. The final output should be a list where each element is another list containing the node values for a specific level.

For instance, if the tree looks like this:

```
    3
   / \
  9  20
    /  \
   15   7
```

*   Level 0 has the node `3`.
*   Level 1 has nodes `9` and `20` (from left to right).
*   Level 2 has nodes `15` and `7` (from left to right).

The expected output is `[[3], [9, 20], [15, 7]]`.

**2. Step-by-Step Approach**

This problem is a classic application of Breadth-First Search (BFS). BFS naturally explores the tree level by level. We can use a queue data structure to keep track of the nodes to visit.

1.  **Initialization:**
    *   Create an empty list `result` which will store the final list of levels.
    *   If the input `root` is `None` (empty tree), return the empty `result` list immediately.
    *   Initialize a queue (e.g., `collections.deque` in Python) and add the `root` node to it.

2.  **Level-by-Level Traversal:**
    *   Start a loop that continues as long as the queue is not empty.
    *   Inside the loop, determine the number of nodes currently in the queue. This number represents the count of nodes at the *current* level (`level_size = len(queue)`).
    *   Create an empty list `current_level_values` to store the values of the nodes at the current level.
    *   Iterate `level_size` times (to process exactly all nodes at the current level):
        *   Dequeue a node from the front of the queue (`current_node = queue.popleft()`).
        *   Add the value of the dequeued node (`current_node.val`) to the `current_level_values` list.
        *   If the `current_node` has a left child, enqueue the left child (`queue.append(current_node.left)`).
        *   If the `current_node` has a right child, enqueue the right child (`queue.append(current_node.right)`).
    *   After the inner loop finishes (meaning all nodes for the current level have been processed), append the `current_level_values` list to the `result` list.

3.  **Termination:**
    *   The outer loop terminates when the queue becomes empty, indicating that all nodes in the tree have been visited.

4.  **Return:**
    *   Return the `result` list containing the level order traversal.

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level order traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the node values
            at a specific level, from left to right.
        """
        result = []
        if not root:
            return result # Return empty list for an empty tree

        # Use a deque (double-ended queue) for efficient appends and poplefts
        queue = collections.deque([root])

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            current_level_values = []

            # Process all nodes at the current level
            for _ in range(level_size):
                # Dequeue the node from the front
                current_node = queue.popleft()
                current_level_values.append(current_node.val)

                # Enqueue children for the next level
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            # Add the collected values for the current level to the result
            result.append(current_level_values)

        return result

# Helper function to build a tree from a list (for testing)
# LeetCode's representation: [3, 9, 20, null, null, 15, 7]
def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()

        # Process left child
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes):
             # Process right child
            if nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1

    return root

# Helper function to print tree level order (for verifying build_tree)
def print_level_order(root: Optional[TreeNode]):
    sol = Solution()
    print(sol.levelOrder(root))

# --- Test Cases ---
solver = Solution()

# Test Case 1: Example 1
print("Test Case 1: Example 1")
root1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Input Tree (visualized by level order):")
print_level_order(root1)
output1 = solver.levelOrder(root1)
expected1 = [[3], [9, 20], [15, 7]]
print(f"Output: {output1}")
print(f"Expected: {expected1}")
print(f"Pass: {output1 == expected1}\n")

# Test Case 2: Example 2
print("Test Case 2: Example 2")
root2 = build_tree([1])
print(f"Input Tree (visualized by level order):")
print_level_order(root2)
output2 = solver.levelOrder(root2)
expected2 = [[1]]
print(f"Output: {output2}")
print(f"Expected: {expected2}")
print(f"Pass: {output2 == expected2}\n")

# Test Case 3: Example 3 (Empty Tree)
print("Test Case 3: Example 3 (Empty Tree)")
root3 = build_tree([])
print(f"Input Tree (visualized by level order):")
print_level_order(root3)
output3 = solver.levelOrder(root3)
expected3 = []
print(f"Output: {output3}")
print(f"Expected: {expected3}")
print(f"Pass: {output3 == expected3}\n")

# Test Case 4: Left-Skewed Tree
print("Test Case 4: Left-Skewed Tree")
root4 = build_tree([1, 2, None, 3, None, 4, None])
print(f"Input Tree (visualized by level order):")
print_level_order(root4)
output4 = solver.levelOrder(root4)
expected4 = [[1], [2], [3], [4]]
print(f"Output: {output4}")
print(f"Expected: {expected4}")
print(f"Pass: {output4 == expected4}\n")

# Test Case 5: Right-Skewed Tree
print("Test Case 5: Right-Skewed Tree")
root5 = build_tree([1, None, 2, None, 3, None, 4])
print(f"Input Tree (visualized by level order):")
print_level_order(root5)
output5 = solver.levelOrder(root5)
expected5 = [[1], [2], [3], [4]]
print(f"Output: {output5}")
print(f"Expected: {expected5}")
print(f"Pass: {output5 == expected5}\n")

# Test Case 6: Complete Binary Tree
print("Test Case 6: Complete Binary Tree")
root6 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(f"Input Tree (visualized by level order):")
print_level_order(root6)
output6 = solver.levelOrder(root6)
expected6 = [[1], [2, 3], [4, 5, 6, 7]]
print(f"Output: {output6}")
print(f"Expected: {expected6}")
print(f"Pass: {output6 == expected6}\n")

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. Each node is visited (enqueued and dequeued) exactly once. Processing each node (adding value, checking children) takes constant time.
*   **Space Complexity:** O(W), where W is the maximum width of the binary tree. In the worst case (a complete binary tree), the last level can contain up to N/2 nodes. So, the maximum space required by the queue is proportional to the maximum number of nodes at any level. In the worst case, this is O(N). The `result` list also stores all N node values, contributing O(N) space. Therefore, the overall space complexity is O(N).

**4. Test Cases (Included in the Python code above)**

1.  **Example 1:** `root = [3, 9, 20, null, null, 15, 7]` -> `[[3], [9, 20], [15, 7]]`
2.  **Example 2:** `root = [1]` -> `[[1]]`
3.  **Example 3 (Empty Tree):** `root = []` -> `[]`
4.  **Left-Skewed Tree:** `root = [1, 2, null, 3, null, 4, null]` -> `[[1], [2], [3], [4]]`
5.  **Right-Skewed Tree:** `root = [1, null, 2, null, 3, null, 4]` -> `[[1], [2], [3], [4]]`
6.  **Complete Binary Tree:** `root = [1, 2, 3, 4, 5, 6, 7]` -> `[[1], [2, 3], [4, 5, 6, 7]]`

The provided Python code includes these test cases and helper functions to build the tree from a list representation and verify the output.