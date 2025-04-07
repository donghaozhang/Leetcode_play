# flatten_binary_tree.md)
- BST中第k小的元素 / Kth Smallest in BST [LeetCode 230]

## Problem Description

## 230. Kth Smallest Element in a BST

<p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the </em><code>k<sup>th</sup></code><em> smallest element in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?</p>

## Solution

## Problem Explanation
The problem requires finding the kth smallest element in a given binary search tree (BST). A BST is a tree data structure in which each node has at most two children (i.e., left child and right child) and each node represents a value. For any given node, all elements in its left subtree are less than the node, and all elements in its right subtree are greater than the node.

## Step-by-Step Approach
To solve this problem, we can follow these steps:
1. **Understand the properties of a BST**: In a BST, an in-order traversal (left -> root -> right) visits nodes in ascending order. This property can be utilized to find the kth smallest element.
2. **Perform in-order traversal**: Traverse the BST in-order and keep track of the number of nodes visited.
3. **Identify the kth smallest element**: When the count of visited nodes equals k, the current node's value is the kth smallest element.
4. **Handle edge cases**: Ensure that k is within the valid range (1 to the number of nodes in the BST).

## Python Solution
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = None
        self.inorder(root, k)
        return self.result

    def inorder(self, node, k):
        if node is None or self.result is not None:
            return
        self.inorder(node.left, k)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.inorder(node.right, k)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    k1 = 1
    print("Test case 1:", solution.kthSmallest(root1, k1))  # Expected output: 1

    # Test case 2:
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    k2 = 3
    print("Test case 2:", solution.kthSmallest(root2, k2))  # Expected output: 3
```

## Time and Space Complexity Analysis
*   **Time complexity**: O(n), where n is the number of nodes in the BST. In the worst case, we might need to traverse all nodes.
*   **Space complexity**: O(h), where h is the height of the BST. This is due to the recursive call stack. In the worst case (when the BST is skewed), h = n. However, for a balanced BST, h = log(n).

## Follow-up: Optimizing for Frequent Queries
To optimize the solution for frequent queries on a dynamic BST (i.e., with insert and delete operations), we can use a data structure that maintains the count of nodes in each subtree, such as an **Augmented BST**. By storing the size of the left subtree in each node, we can navigate to the kth smallest element more efficiently.

Here's a high-level approach:
1.  **Augment the BST nodes**: Store the size of the left subtree in each node.
2.  **Update the size during insert and delete operations**: When inserting or deleting a node, update the size of the affected nodes.
3.  **Use the size information to find the kth smallest element**: Compare k with the size of the left subtree to decide whether to go left or right during the traversal.

By using an Augmented BST, we can achieve O(h) time complexity for finding the kth smallest element, where h is the height of the BST. For a balanced BST, this results in O(log n) time complexity.