# minimum_subtree.md)
- 最近公共祖先 / Lowest Common Ancestor [LeetCode 236]

## Problem Description

```markdown
## 236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```
*(Image of the tree for Example 1 would typically be here on LeetCode)*

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```
*(Image of the tree for Example 2 would typically be here on LeetCode)*

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 10^5]`.
*   `-10^9 <= Node.val <= 10^9`.
*   All `Node.val` are **unique**.
*   `p != q`.
*   `p` and `q` will exist in the tree.
```

## Solution

Okay, let's break down the Lowest Common Ancestor (LCA) problem.

**1. Explanation of the Problem**

Given a binary tree and two specific nodes, `p` and `q`, that are guaranteed to be present in the tree, we need to find their "lowest common ancestor". The LCA is the deepest node in the tree that has both `p` and `q` as descendants. An important clarification is that a node is considered a descendant of itself.

*   If `p` is an ancestor of `q`, then `p` is the LCA.
*   If `q` is an ancestor of `p`, then `q` is the LCA.
*   Otherwise, the LCA is the node where the paths from the root to `p` and `q` diverge.

**2. Step-by-Step Approach (Recursive DFS)**

The most intuitive and common approach uses recursion (Depth First Search). The core idea is to search for `p` and `q` in the left and right subtrees of the current node.

1.  **Base Cases:**
    *   If the current node (`root`) is `None`, it means we've reached the end of a branch without finding `p` or `q`. Return `None`.
    *   If the current node (`root`) is equal to `p` or `q`, we have found one of the target nodes. Since a node can be its own ancestor, this node could potentially be the LCA (if the other target node is found in its subtree). We return the current `root`.

2.  **Recursive Step:**
    *   Recursively call the function on the left child: `left_result = lowestCommonAncestor(root.left, p, q)`. This call will return `p`, `q`, their LCA if both are in the left subtree, or `None`.
    *   Recursively call the function on the right child: `right_result = lowestCommonAncestor(root.right, p, q)`. This does the same for the right subtree.

3.  **Combine Results:** Now, analyze the results from the left and right recursive calls:
    *   **If `left_result` is not `None` AND `right_result` is not `None`:** This means `p` was found in one subtree (e.g., left) and `q` was found in the other subtree (e.g., right). The current `root` is the first node that connects these two subtrees. Therefore, the current `root` is the LCA. Return `root`.
    *   **If `left_result` is not `None` (and `right_result` is `None`):** This implies that both `p` and `q` must be in the left subtree (or `p` or `q` *is* the node returned by `left_result`). The LCA must also be in the left subtree. The value returned by `left_result` (which could be `p`, `q`, or their LCA found lower down) is the correct result to propagate upwards. Return `left_result`.
    *   **If `right_result` is not `None` (and `left_result` is `None`):** Similar to the previous case, but for the right subtree. Return `right_result`.
    *   **If both `left_result` and `right_result` are `None`:** Neither `p` nor `q` (nor their LCA) was found in the left or right subtrees starting from this `root`. Return `None`.

This recursive process effectively searches the tree. When the recursion unwinds, the first node that receives non-`None` results from *both* its left and right recursive calls is the LCA. If one node is an ancestor of the other, the ancestor node will be returned as soon as it's encountered in the base case, and this result will be propagated up the call stack.

**3. Python Solution**

```python
# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        # Helper for printing node value during testing
        return f"Node({self.val})"

class Solution:
    """
    Solves the Lowest Common Ancestor problem using recursive DFS.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor of two nodes p and q in a binary tree.

        Args:
            root: The root node of the binary tree.
            p: The first target node.
            q: The second target node.

        Returns:
            The lowest common ancestor node.
        """
        # Base case 1: If root is None, we can't find anything.
        if not root:
            return None

        # Base case 2: If root is p or q, then this node is a potential LCA
        # (or we've found one of the nodes).
        if root == p or root == q:
            return root

        # Recursively search in the left and right subtrees.
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # Process the results from left and right subtrees:
        # Case 1: p found in one subtree, q found in the other.
        # This means the current 'root' is the LCA.
        if left_lca and right_lca:
            return root

        # Case 2: Both p and q are in the left subtree OR
        #         p or q was found in the left subtree (and the other is deeper) OR
        #         the LCA was found in the left subtree.
        # In any of these sub-cases, the result from the left subtree is the answer
        # to propagate up. Same logic applies if only right_lca is not None.
        return left_lca if left_lca else right_lca

# Helper functions for testing
def build_tree(nodes):
    """Builds a binary tree from a list representation (level-order)."""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [(root, 0)] # Store node and its index in the list
    
    while queue:
        current_node, current_index = queue.pop(0)
        
        left_child_index = 2 * current_index + 1
        if left_child_index < len(nodes) and nodes[left_child_index] is not None:
            current_node.left = TreeNode(nodes[left_child_index])
            queue.append((current_node.left, left_child_index))
            
        right_child_index = 2 * current_index + 2
        if right_child_index < len(nodes) and nodes[right_child_index] is not None:
            current_node.right = TreeNode(nodes[right_child_index])
            queue.append((current_node.right, right_child_index))
            
    return root

def find_node(root: TreeNode, val: int) -> TreeNode:
    """Finds a node with a specific value in the tree (assumes unique values)."""
    if not root:
        return None
    if root.val == val:
        return root
    
    found_left = find_node(root.left, val)
    if found_left:
        return found_left
    
    return find_node(root.right, val)

# --- Test Cases ---
solver = Solution()

# Example 1
nodes1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root1 = build_tree(nodes1)
p1 = find_node(root1, 5)
q1 = find_node(root1, 1)
lca1 = solver.lowestCommonAncestor(root1, p1, q1)
print(f"Example 1: Tree={nodes1}, p=5, q=1")
print(f"LCA: {lca1.val if lca1 else 'Not Found'} (Expected: 3)")
print("-" * 20)

# Example 2
nodes2 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root2 = build_tree(nodes2)
p2 = find_node(root2, 5)
q2 = find_node(root2, 4)
lca2 = solver.lowestCommonAncestor(root2, p2, q2)
print(f"Example 2: Tree={nodes2}, p=5, q=4")
print(f"LCA: {lca2.val if lca2 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Example 3
nodes3 = [1, 2]
root3 = build_tree(nodes3)
p3 = find_node(root3, 1)
q3 = find_node(root3, 2)
lca3 = solver.lowestCommonAncestor(root3, p3, q3)
print(f"Example 3: Tree={nodes3}, p=1, q=2")
print(f"LCA: {lca3.val if lca3 else 'Not Found'} (Expected: 1)")
print("-" * 20)

# Custom Test Case 1: Deeper nodes
nodes4 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root4 = build_tree(nodes4)
p4 = find_node(root4, 3)
q4 = find_node(root4, 5)
lca4 = solver.lowestCommonAncestor(root4, p4, q4)
print(f"Custom Test 1: Tree={nodes4}, p=3, q=5")
print(f"LCA: {lca4.val if lca4 else 'Not Found'} (Expected: 4)")
print("-" * 20)

# Custom Test Case 2: p is ancestor of q
nodes5 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root5 = build_tree(nodes5)
p5 = find_node(root5, 5)
q5 = find_node(root5, 7)
lca5 = solver.lowestCommonAncestor(root5, p5, q5)
print(f"Custom Test 2: Tree={nodes5}, p=5, q=7")
print(f"LCA: {lca5.val if lca5 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Custom Test Case 3: q is ancestor of p
nodes6 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root6 = build_tree(nodes6)
p6 = find_node(root6, 4)
q6 = find_node(root6, 5)
lca6 = solver.lowestCommonAncestor(root6, p6, q6)
print(f"Custom Test 3: Tree={nodes6}, p=4, q=5")
print(f"LCA: {lca6.val if lca6 else 'Not Found'} (Expected: 5)")
print("-" * 20)

# Custom Test Case 4: Root is LCA
nodes7 = [1, 2, 3]
root7 = build_tree(nodes7)
p7 = find_node(root7, 2)
q7 = find_node(root7, 3)
lca7 = solver.lowestCommonAncestor(root7, p7, q7)
print(f"Custom Test 4: Tree={nodes7}, p=2, q=3")
print(f"LCA: {lca7.val if lca7 else 'Not Found'} (Expected: 1)")
print("-" * 20)
```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the number of nodes in the tree. In the worst case, the algorithm visits each node once during the recursive traversal.
*   **Space Complexity:** O(H), where H is the height of the tree. This space is used by the recursion call stack. In the worst case (a completely skewed tree), the height H can be equal to N, leading to O(N) space complexity. For a balanced binary tree, the height is log(N), resulting in O(log N) space complexity.

**4. Test Cases Verification**

The provided Python code includes helper functions (`build_tree`, `find_node`) and several test cases:

1.  **Example 1:** `p=5`, `q=1`. LCA is `3`. Correctly handled by finding `5` in the left subtree and `1` in the right subtree of `3`.
2.  **Example 2:** `p=5`, `q=4`. LCA is `5`. Correctly handled because `5` is found first, and the recursive call for its right subtree eventually finds `4`. The result `5` is propagated up.
3.  **Example 3:** `p=1`, `q=2`. LCA is `1`. Correctly handled because `1` (root) is `p`.
4.  **Custom Test 1:** `p=3`, `q=5`. LCA is `4`. `3` and `5` are children of `4`. The call at node `4` gets `3` from the left and `5` from the right, returning `4`.
5.  **Custom Test 2:** `p=5`, `q=7`. LCA is `5`. `5` is an ancestor of `7`. The call at node `5` returns `5` (base case). The recursive calls below `5` eventually find `7`, but the result `5` is already being propagated up.
6.  **Custom Test 3:** `p=4`, `q=5`. LCA is `5`. `5` is an ancestor of `4`. Similar logic to Custom Test 2.
7.  **Custom Test 4:** `p=2`, `q=3`. LCA is `1`. The root `1` gets `2` from its left child and `3` from its right child, returning `1`.

The test cases cover various scenarios, including the examples provided, cases where one node is an ancestor of the other, and cases where the LCA is deeper in the tree or is the root itself. The solution correctly identifies the LCA in all these scenarios.