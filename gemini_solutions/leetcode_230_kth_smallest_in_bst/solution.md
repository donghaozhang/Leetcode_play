# flatten_binary_tree.md)
- BST中第k小的元素 / Kth Smallest in BST [LeetCode 230]

## Problem Description

```markdown
## 230. Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`, return the `k`th smallest value **(1-indexed)** of all the values of the nodes in the tree.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints:**

*   The number of nodes in the tree is `n`.
*   `1 <= k <= n <= 10^4`
*   `0 <= Node.val <= 10^4`

**Follow up:** If the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently, how would you optimize?
```

## Solution

Okay, let's break down the "Kth Smallest Element in a BST" problem.

**1. Explanation of the Problem**

We are given a Binary Search Tree (BST) and an integer `k`. A BST has the property that for any given node, all values in its left subtree are smaller than the node's value, and all values in its right subtree are larger. Our goal is to find the value of the node which is the *k*-th smallest among all node values in the entire tree. The problem uses 1-based indexing, meaning the absolute smallest value is the 1st smallest, the next smallest is the 2nd smallest, and so on.

**2. Step-by-Step Approach**

The key property of a BST that helps us here is that an **in-order traversal** visits the nodes in ascending order of their values.

*   **In-order Traversal:** Visit left subtree -> Visit current node -> Visit right subtree.

If we perform an in-order traversal and keep track of the nodes visited, the *k*-th node we visit will contain the *k*-th smallest value.

We can implement this using either recursion or iteration. The iterative approach using a stack is often preferred as it avoids potential recursion depth limits and explicitly manages the traversal state.

**Iterative In-order Traversal Approach:**

1.  Initialize an empty stack to store nodes.
2.  Initialize a pointer `current` to the `root` node.
3.  Initialize a counter `count` to 0.
4.  Start a loop that continues as long as `current` is not `None` or the `stack` is not empty.
    a.  **Go Left:** While `current` is not `None`, push `current` onto the `stack` and move `current` to its left child (`current = current.left`). This pushes all the leftmost nodes onto the stack.
    b.  **Visit Node:** Once `current` becomes `None`, it means we've reached the leftmost node (or the leftmost node of a right subtree). Pop the top node from the `stack`. Let this node be `node_visited`.
    c.  Increment the `count`.
    d.  **Check k:** If `count` equals `k`, we have found the *k*-th smallest node. Return `node_visited.val`.
    e.  **Go Right:** Move `current` to the right child of the visited node (`current = node_visited.right`). This prepares the loop to process the right subtree in the next iteration.

This process effectively simulates the in-order traversal. By stopping and returning the value when the count reaches `k`, we find the desired element without necessarily traversing the entire tree (if `k` is smaller than the total number of nodes `n`).

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

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th smallest element in a Binary Search Tree using iterative in-order traversal.

        Args:
            root: The root node of the BST.
            k: The index (1-based) of the desired smallest element.

        Returns:
            The value of the k-th smallest element.
        """
        stack = []
        current = root
        count = 0

        while current or stack:
            # 1. Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # 2. Visit the node popped from the stack (in-order)
            #    This node is the next smallest in the sequence.
            current = stack.pop()
            count += 1

            # 3. Check if this is the k-th node visited
            if count == k:
                return current.val

            # 4. Move to the right subtree to continue the in-order traversal
            current = current.right

        # This part should theoretically not be reached if 1 <= k <= n
        return -1 # Or raise an error

# Helper function to build a BST from a list (level-order) for testing
def build_bst_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()

        # Process left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i >= len(values):
            break

        # Process right child
        if values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# --- Test Cases ---
solver = Solution()

# Example 1
root1 = build_bst_from_list([3, 1, 4, None, 2])
k1 = 1
expected1 = 1
result1 = solver.kthSmallest(root1, k1)
print(f"Test Case 1: Input root=[3,1,4,null,2], k={k1}")
print(f"Expected: {expected1}")
print(f"Result: {result1}")
print(f"Pass: {result1 == expected1}\n")

# Example 2
root2 = build_bst_from_list([5, 3, 6, 2, 4, None, None, 1])
k2 = 3
expected2 = 3
result2 = solver.kthSmallest(root2, k2)
print(f"Test Case 2: Input root=[5,3,6,2,4,null,null,1], k={k2}")
print(f"Expected: {expected2}")
print(f"Result: {result2}")
print(f"Pass: {result2 == expected2}\n")

# Additional Test Case 1: k = n (largest element)
root3 = build_bst_from_list([5, 3, 6, 2, 4, None, None, 1]) # n = 6
k3 = 6
expected3 = 6
result3 = solver.kthSmallest(root3, k3)
print(f"Test Case 3: Input root=[5,3,6,2,4,null,null,1], k={k3}")
print(f"Expected: {expected3}")
print(f"Result: {result3}")
print(f"Pass: {result3 == expected3}\n")

# Additional Test Case 2: Skewed tree
root4 = build_bst_from_list([1, None, 2, None, 3, None, 4, None, 5]) # n = 5
k4 = 4
expected4 = 4
result4 = solver.kthSmallest(root4, k4)
print(f"Test Case 4: Input root=[1,null,2,null,3,null,4,null,5], k={k4}")
print(f"Expected: {expected4}")
print(f"Result: {result4}")
print(f"Pass: {result4 == expected4}\n")

# Additional Test Case 3: Single node tree
root5 = build_bst_from_list([1]) # n = 1
k5 = 1
expected5 = 1
result5 = solver.kthSmallest(root5, k5)
print(f"Test Case 5: Input root=[1], k={k5}")
print(f"Expected: {expected5}")
print(f"Result: {result5}")
print(f"Pass: {result5 == expected5}\n")
```

**Complexity Analysis:**

*   **Time Complexity:** O(H + k)
    *   In the worst case (a skewed tree where the k-th element is the last one), we might visit all `n` nodes, making it O(n).
    *   In a balanced tree, the height `H` is O(log n). We traverse down to the first node (O(H)) and then visit `k` nodes in order. So, the complexity is roughly O(H + k). If `k` is small, it's efficient. If `k` is close to `n`, it approaches O(n).
*   **Space Complexity:** O(H)
    *   The space is dominated by the `stack` used for the iterative traversal. In the worst case (a skewed tree), the stack can hold up to `n` nodes, leading to O(n) space.
    *   In a balanced tree, the height `H` is O(log n), so the stack depth and space complexity will be O(log n).

**Follow-up: Optimization for Frequent Modifications and Queries**

If the BST is frequently modified (insertions/deletions) and we need to find the k-th smallest element often, the O(H + k) or O(n) query time of the in-order traversal approach becomes inefficient.

**Optimized Approach:** Augment the `TreeNode` structure to store the size of the subtree rooted at that node.

1.  **Augmented TreeNode:** Add a `count` field to each `TreeNode`, storing the total number of nodes in the subtree rooted at that node (including the node itself).
    ```python
    class AugmentedTreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.count = 1 # Initialize count to 1 (for the node itself)
    ```
2.  **Maintaining Counts:** During insertion and deletion operations, update the `count` field of all ancestor nodes affected by the change. This adds an O(H) overhead to each modification operation.
    *   **Insertion:** When inserting a node, increment the `count` of all nodes along the insertion path.
    *   **Deletion:** When deleting a node, decrement the `count` of all nodes along the path from the root to the parent of the deleted node (or the node that replaces it).
3.  **Fast K-th Smallest Query:** With the `count` information, we can find the k-th smallest element in O(H) time, similar to how selection works in a sorted array.
    *   Start at the `root`.
    *   Let `left_subtree_size = root.left.count` if `root.left` exists, otherwise `0`.
    *   Compare `k` with `left_subtree_size`:
        *   If `k <= left_subtree_size`: The k-th smallest element is in the left subtree. Recursively search for the `k`-th smallest in `root.left`.
        *   If `k == left_subtree_size + 1`: The current `root` is the k-th smallest. Return `root.val`.
        *   If `k > left_subtree_size + 1`: The k-th smallest element is in the right subtree. Recursively search for the `(k - left_subtree_size - 1)`-th smallest in `root.right`.

**Complexity (Follow-up):**

*   **Modification (Insert/Delete):** O(H) - Time to find the location and update counts up the tree.
*   **K-th Smallest Query:** O(H) - Time to traverse down a single path from the root.
*   **Space:** O(n) - To store the `count` in each of the `n` nodes.

This trade-off (slightly slower modifications for much faster queries) is beneficial when k-th smallest queries are significantly more frequent than tree modifications. Data structures like Order-Statistic Trees are based on this principle.