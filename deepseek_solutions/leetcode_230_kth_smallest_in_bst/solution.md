# flatten_binary_tree.md)
- BST中第k小的元素 / Kth Smallest in BST [LeetCode 230]

## Problem Description

Here is the full description of LeetCode problem #230, "Kth Smallest Element in a BST":

---

Given the `root` of a binary search tree (BST) and an integer `k`, return the *k<sup>th</sup>* smallest element (1-indexed) in the BST.

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Example 2:**

![Example 2](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

**Constraints:**

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

--- 

Let me know if you'd like any clarification or further assistance!

## Solution

### Problem Explanation
The problem requires finding the k-th smallest element in a Binary Search Tree (BST). A BST is a tree where each node has at most two children, and for any given node, all values in its left subtree are less than the node's value, and all values in its right subtree are greater than the node's value. The challenge is to efficiently find the k-th smallest element in this structure.

### Approach
1. **Inorder Traversal**: Since an inorder traversal (left, root, right) of a BST yields the nodes in ascending order, we can use this property to find the k-th smallest element. 
2. **Iterative Traversal**: To avoid using extra space for recursion (which could be O(n) in the worst case for a skewed tree), we can use an iterative approach with a stack to perform the inorder traversal. This allows us to stop early once we've visited the k-th element.
3. **Early Termination**: As we perform the inorder traversal, we keep a count of visited nodes. When the count reaches k, we return the current node's value, thus optimizing the solution.

### Solution Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        count = 0
        
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            # Move to the right subtree
            current = current.right
        
        return -1  # This line is theoretically unreachable if k is valid
```

### Explanation
1. **Initialization**: We start with an empty stack and set the current node to the root of the BST.
2. **Leftmost Traversal**: We traverse to the leftmost node, pushing each node onto the stack as we go. This ensures that we process nodes in ascending order.
3. **Processing Nodes**: After reaching the leftmost node, we pop it from the stack (which is the next smallest element), increment our count, and check if we've reached the k-th element. If so, we return its value.
4. **Right Subtree**: If not, we move to the right subtree of the popped node and repeat the process. This ensures that we continue the inorder traversal.
5. **Termination**: The loop terminates once we've processed the k-th smallest element, making the solution efficient with O(h) space (where h is the height of the tree) and O(k) time in the worst case.

### Test Cases
```python
# Helper function to build a tree from a list (for testing)
def build_tree(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = build_tree(lst, 2 * index + 1)
    root.right = build_tree(lst, 2 * index + 2)
    return root

# Test case 1
tree1 = build_tree([3, 1, 4, None, 2])
sol = Solution()
print(sol.kthSmallest(tree1, 1))  # Expected output: 1

# Test case 2
tree2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
print(sol.kthSmallest(tree2, 3))  # Expected output: 3

# Test case 3: single node
tree3 = build_tree([2])
print(sol.kthSmallest(tree3, 1))  # Expected output: 2

# Test case 4: left-skewed tree
tree4 = build_tree([4, 3, None, 2, None, 1])
print(sol.kthSmallest(tree4, 3))  # Expected output: 3
```

### Complexity Analysis
- **Time Complexity**: O(h + k), where h is the height of the tree. In the worst case (skewed tree), h is O(n), but on average, for a balanced BST, it's O(log n).
- **Space Complexity**: O(h) due to the stack used for the iterative inorder traversal. In the worst case, this is O(n), but O(log n) for a balanced tree.

This approach efficiently finds the k-th smallest element by leveraging the properties of BST and inorder traversal, with optimal space usage.