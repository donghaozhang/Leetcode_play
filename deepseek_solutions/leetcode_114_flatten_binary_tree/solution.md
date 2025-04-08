# lowest_common_ancestor.md)
- 二叉树展开为链表 / Flatten Binary Tree [LeetCode 114]

## Problem Description

Here is the full description of LeetCode problem #114, "Flatten Binary Tree to Linked List":

---

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **pre-order traversal** of the binary tree.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg)

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

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (with `O(1)` extra space)?

--- 

Let me know if you'd like any clarification or additional details!

## Solution

### Explanation of the Problem
We need to flatten a binary tree into a linked list in-place, following the pre-order traversal order. The "linked list" should use the `right` child pointer to point to the next node and set the `left` child pointer to `null`. 

For example, given the tree:
```
    1
   / \
  2   5
 / \   \
3   4   6
```
The flattened linked list should be:
```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

### Approach
1. **Recursive Approach (Post-Order Traversal):** 
   - The idea is to flatten the left and right subtrees recursively, then adjust the pointers to form the linked list.
   - For the current node, after flattening the left and right subtrees, we move the flattened left subtree to the right of the current node, and then append the flattened right subtree to the end of the left subtree.
   - This approach requires O(n) time and O(h) space (due to recursion stack), where h is the height of the tree.

2. **Iterative Approach (Using a Stack):**
   - We can use a stack to simulate the pre-order traversal iteratively. For each node, we push the right child first, then the left child onto the stack. Then, we set the right child to the top of the stack and the left child to null.
   - This approach also takes O(n) time and O(n) space (due to the stack).

3. **Morris Traversal (O(1) Space):**
   - The Morris traversal approach allows us to flatten the tree in O(1) space by modifying the tree as we traverse it.
   - For each node, if it has a left child, we find the rightmost node in the left subtree (which is the predecessor in in-order traversal), then set its right child to the current node's right child. Then, we move the left child to the right and set the left child to null.
   - This approach runs in O(n) time and O(1) space.

### Solution Code (Python)
Here, I'll provide the recursive and Morris traversal solutions.

#### Recursive Solution
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Save the right subtree
        right_subtree = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        root.left = None
        
        # Find the end of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Append the original right subtree
        current.right = right_subtree
```

#### Morris Traversal Solution
```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Rewire the connections
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            
            # Move to the next node
            current = current.right
```

### Time and Space Complexity
- **Recursive Solution:**
  - Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
  - Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), it's O(n).

- **Morris Traversal Solution:**
  - Time Complexity: O(n). Each node is visited at most twice (once when locating the predecessor and once when moving to the right).
  - Space Complexity: O(1). We only use a few pointers and no additional data structures.

### Test Cases
```python
# Helper function to print the flattened tree (linked list)
def print_flattened(root):
    res = []
    while root:
        res.append(root.val)
        root = root.right
    print(res)

# Test Case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)
Solution().flatten(root1)
print_flattened(root1)  # Expected: [1, 2, 3, 4, 5, 6]

# Test Case 2
root2 = None
Solution().flatten(root2)
print_flattened(root2)  # Expected: []

# Test Case 3
root3 = TreeNode(0)
Solution().flatten(root3)
print_flattened(root3)  # Expected: [0]
```

### Explanation of Test Cases
1. **Test Case 1:** A balanced tree that flattens to `1 -> 2 -> 3 -> 4 -> 5 -> 6`.
2. **Test Case 2:** An empty tree remains empty.
3. **Test Case 3:** A single node tree flattens to itself.

Both solutions correctly flatten the tree in-place, with the Morris traversal being more space-efficient.