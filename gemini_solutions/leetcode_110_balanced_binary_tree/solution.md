# binary_tree_paths.md)
- 平衡二叉树 / Balanced Binary Tree [LeetCode 110]

## Problem Description

```markdown
## 110. Balanced Binary Tree

Given a binary tree, determine if it is **height-balanced**.

A **height-balanced** binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

**Example 1:**

Input: root = [3,9,20,null,null,15,7]
Output: true

**Example 2:**

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

**Example 3:**

Input: root = []
Output: true

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 5000]`.
*   `-10^4 <= Node.val <= 10^4`
```

## Solution

Okay, let's break down the "Balanced Binary Tree" problem (LeetCode 110).

**1. Explanation of the Problem**

The problem asks us to determine if a given binary tree is "height-balanced". A binary tree is height-balanced if, for *every node* in the tree, the absolute difference between the height of its left subtree and the height of its right subtree is no more than 1.

*   **Height of a Node/Subtree:** The height is typically defined as the number of edges on the longest path from that node down to a leaf node in its subtree. An empty subtree (represented by `None`) has a height of -1, and a leaf node has a height of 0.
*   **Condition:** For any node `N`, `abs(height(N.left) - height(N.right)) <= 1`. This must hold true for all nodes, not just the root.

**Example Walkthrough:**

*   **Example 1:** `[3,9,20,null,null,15,7]`
    *   Node 9: Left height = -1, Right height = -1. Diff = 0. OK. Height = 0.
    *   Node 15: Left height = -1, Right height = -1. Diff = 0. OK. Height = 0.
    *   Node 7: Left height = -1, Right height = -1. Diff = 0. OK. Height = 0.
    *   Node 20: Left height (15) = 0, Right height (7) = 0. Diff = 0. OK. Height = 1.
    *   Node 3: Left height (9) = 0, Right height (20) = 1. Diff = 1. OK. Height = 2.
    *   Since the condition holds for all nodes, the tree is balanced. Output: `true`.

*   **Example 2:** `[1,2,2,3,3,null,null,4,4]`
    *   Node 4 (left): Height = 0.
    *   Node 4 (right): Height = 0.
    *   Node 3 (left): Left height (4) = 0, Right height (4) = 0. Diff = 0. OK. Height = 1.
    *   Node 3 (right): Height = 0.
    *   Node 2 (left): Left height (3) = 1, Right height (3) = 0. Diff = 1. OK. Height = 2.
    *   Node 2 (right): Left height = -1, Right height = -1. Diff = 0. OK. Height = 0.
    *   Node 1: Left height (2) = 2, Right height (2) = 0. Diff = 2. NOT OK.
    *   Since the condition fails at the root node, the tree is not balanced. Output: `false`.

**2. Step-by-Step Approach (Optimized - Bottom-Up DFS)**

The most efficient way to solve this is using a single Depth-First Search (DFS) traversal, specifically a postorder traversal (Left, Right, Node). We can combine the height calculation and the balance check.

1.  **Helper Function:** Create a recursive helper function (e.g., `check_height`) that takes a node as input. This function will do two things:
    *   Calculate the height of the subtree rooted at the given node.
    *   Determine if this subtree is balanced.
2.  **Return Value Strategy:** To combine these two pieces of information, the helper function will return:
    *   The actual height of the subtree if it *is* balanced.
    *   A special value (e.g., -2 or any value that cannot be a valid height like -1) to indicate that an imbalance was detected *within* this subtree.
3.  **Base Case:** If the current node is `None`, it represents a balanced empty subtree with height -1. Return -1.
4.  **Recursive Calls:**
    *   Recursively call `check_height` on the left child to get its status/height (`left_height`).
    *   If `left_height` indicates imbalance (e.g., is -2), immediately return -2 to propagate the imbalance signal up the call stack. There's no need to check the right side.
    *   Recursively call `check_height` on the right child (`right_height`).
    *   If `right_height` indicates imbalance (e.g., is -2), immediately return -2.
5.  **Check Current Node's Balance:** If both recursive calls returned valid heights (meaning the left and right subtrees are themselves balanced), check the balance condition at the *current* node:
    *   Calculate `abs(left_height - right_height)`.
    *   If the difference is greater than 1, the subtree rooted at the current node is unbalanced. Return the imbalance signal (-2).
6.  **Return Height:** If the current node is balanced, calculate its height: `1 + max(left_height, right_height)`. Return this height.
7.  **Main Function:** The main `isBalanced` function will call the helper function starting from the `root`.
    *   If the helper function returns the imbalance signal (-2), the entire tree is not balanced. Return `False`.
    *   Otherwise (if it returns any other value, which would be a valid height), the tree is balanced. Return `True`.

**Why Bottom-Up?**
This approach is efficient because it calculates the height and checks the balance condition in a single pass. When processing a node, we already have the results (height and balance status) from its children. This avoids the redundant height calculations of a naive top-down approach where you might calculate the height of the same subtree multiple times.

**3. Python Solution**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Determines if a binary tree is height-balanced using a bottom-up DFS approach.
        """

        # Helper function returns the height of the subtree if balanced,
        # otherwise returns -2 to indicate imbalance.
        def check_height(node: TreeNode | None) -> int:
            # Base case: An empty tree is balanced and has height -1
            if not node:
                return -1

            # Recursively check the left subtree
            left_height = check_height(node.left)
            # If the left subtree is unbalanced, propagate the imbalance signal
            if left_height == -2:
                return -2

            # Recursively check the right subtree
            right_height = check_height(node.right)
            # If the right subtree is unbalanced, propagate the imbalance signal
            if right_height == -2:
                return -2

            # Check the balance condition at the current node
            if abs(left_height - right_height) > 1:
                # Current node is unbalanced
                return -2
            else:
                # Current node is balanced, return its height
                return 1 + max(left_height, right_height)

        # Call the helper function starting from the root.
        # If it returns -2, the tree is unbalanced. Otherwise, it's balanced.
        return check_height(root) != -2

# Helper function to build a tree from a list (for testing)
def build_tree(nodes: list) -> TreeNode | None:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current_node = queue.pop(0)
        
        # Left child
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        
        if i < len(nodes):
            # Right child
            if nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1
            
    return root

# --- Test Cases ---
solver = Solution()

# Example 1: Balanced
tree1 = build_tree([3, 9, 20, None, None, 15, 7])
print(f"Tree 1 ([3,9,20,null,null,15,7]): Balanced = {solver.isBalanced(tree1)}") # Expected: True

# Example 2: Unbalanced
tree2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print(f"Tree 2 ([1,2,2,3,3,null,null,4,4]): Balanced = {solver.isBalanced(tree2)}") # Expected: False

# Example 3: Empty tree
tree3 = build_tree([])
print(f"Tree 3 ([]): Balanced = {solver.isBalanced(tree3)}") # Expected: True

# Test Case 4: Single node
tree4 = build_tree([1])
print(f"Tree 4 ([1]): Balanced = {solver.isBalanced(tree4)}") # Expected: True

# Test Case 5: Skewed tree (unbalanced)
tree5 = build_tree([1, 2, None, 3, None, 4, None])
print(f"Tree 5 ([1,2,null,3,null,4,null]): Balanced = {solver.isBalanced(tree5)}") # Expected: False

# Test Case 6: Slightly more complex balanced tree
tree6 = build_tree([1, 2, 3, 4, 5, 6, None, 8])
# Heights: 8(-1,-1)->0; 4(8,-1)->1; 5(-1,-1)->0; 2(4,5)->2; 6(-1,-1)->0; 3(6,-1)->1; 1(2,3)->3
# Balances: 8(0); 4(1); 5(0); 2(1); 6(0); 3(1); 1(1) -> Balanced
print(f"Tree 6 ([1,2,3,4,5,6,null,8]): Balanced = {solver.isBalanced(tree6)}") # Expected: True

# Test Case 7: Unbalanced at root due to height difference
tree7 = build_tree([1, 2, None, 3, None, 4, None, 5, None])
# Heights: 5(-1,-1)->0; 4(5,-1)->1; 3(4,-1)->2; 2(3,-1)->3; 1(2,None)->4
# Balances: 5(0); 4(1); 3(1); 2(1); 1(abs(3 - (-1)) = 4 > 1) -> Unbalanced
print(f"Tree 7 ([1,2,null,3,null,4,null,5,null]): Balanced = {solver.isBalanced(tree7)}") # Expected: False

# Test Case 8: Unbalanced deeper in the tree
tree8 = build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
# Heights: 4(-1,-1)->0; 3(4,-1)->1; 2(3,None)->2; 4(-1,-1)->0; 3(None,4)->1; 2(None,3)->2; 1(2,2)->3
# Balances: 4(0); 3(1); 2(1); 4(0); 3(1); 2(1); 1(abs(2-2)=0)
# Let's recheck node 2 (left): left=3(height 1), right=None(height -1). Diff=2 -> Unbalanced
print(f"Tree 8 ([1,2,2,3,null,null,3,4,null,null,4]): Balanced = {solver.isBalanced(tree8)}") # Expected: False

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. The `check_height` function visits each node exactly once in a postorder traversal fashion. The work done at each node (comparisons, max, addition) is constant O(1).
*   **Space Complexity:** O(H), where H is the height of the tree. This is due to the recursion stack space used by the `check_height` function.
    *   In the best case (a perfectly balanced tree), H = log N, so space complexity is O(log N).
    *   In the worst case (a completely skewed tree, like a linked list), H = N, so space complexity is O(N).

**4. Test Cases (Included in the Python code above)**

1.  `[3, 9, 20, None, None, 15, 7]` -> `True` (Example 1)
2.  `[1, 2, 2, 3, 3, None, None, 4, 4]` -> `False` (Example 2)
3.  `[]` -> `True` (Example 3 - Empty tree)
4.  `[1]` -> `True` (Single node tree)
5.  `[1, 2, None, 3, None, 4, None]` -> `False` (Left-skewed, unbalanced)
6.  `[1, 2, 3, 4, 5, 6, None, 8]` -> `True` (More complex balanced tree)
7.  `[1, 2, None, 3, None, 4, None, 5, None]` -> `False` (Unbalanced at root due to large height difference)
8.  `[1, 2, 2, 3, None, None, 3, 4, None, None, 4]` -> `False` (Unbalanced deeper within the tree)