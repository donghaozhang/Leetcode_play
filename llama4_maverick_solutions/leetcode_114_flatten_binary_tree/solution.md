# lowest_common_ancestor.md)
- 二叉树展开为链表 / Flatten Binary Tree [LeetCode 114]

## Problem Description

## Problem Description

### Flatten Binary Tree to Linked List

Given the `root` of a binary tree, flatten the tree into a "linked list":

* The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
* The "linked list" should be in the same order as a [**pre-order** traversal](https://en.wikipedia.org/wiki/Tree_traversal#Pre-order,_NLR) of the binary tree.

#### Example 1:
```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

#### Example 2:
```
Input: root = []
Output: []
```

#### Example 3:
```
Input: root = [0]
Output: [0]
```

#### Constraints:

* The number of nodes in the tree is in the range `[0, 2000]`.
* `-100 <= Node.val <= 100`

**Follow up:** Can you flatten the tree in-place (i.e., without allocating new nodes)?

## Solution

## Problem Explanation
The problem requires flattening a binary tree into a linked list in-place, where the linked list is formed using the same `TreeNode` class. The `right` child pointer should point to the next node in the list, and the `left` child pointer should always be `null`. The order of the linked list should be the same as a pre-order traversal of the binary tree.

## Step-by-Step Approach
1. **Understand the Problem**: The task is to transform a given binary tree into a linked list in-place, following the pre-order traversal order.
2. **Identify the Constraints**: The number of nodes in the tree is between 0 and 2000, and the node values are within the range -100 to 100.
3. **Choose an Approach**: To solve this problem in-place without using extra space for the linked list nodes, we can use a recursive or iterative approach that rearranges the nodes as per the pre-order traversal.
4. **Pre-order Traversal**: The pre-order traversal visits the current node, then recursively traverses the left subtree, and finally the right subtree. We need to flatten the tree such that the left subtree of every node becomes null, and the right subtree is the pre-order traversal of the original left and right subtrees.
5. **Flattening the Tree**: We will use a recursive approach to flatten the tree. For each node, we will first flatten its left and right subtrees. Then, we will append the flattened left subtree to the right of the current node and append the flattened right subtree after the flattened left subtree.

## Python Solution

```python
# Definition for a binary tree node.
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
        self.flatten_helper(root)

    def flatten_helper(self, root: TreeNode) -> TreeNode:
        # Base case: if the tree is empty, return None
        if not root:
            return None
        
        # Recursively flatten the left and right subtrees
        left_tail = self.flatten_helper(root.left)
        right_tail = self.flatten_helper(root.right)
        
        # If the left subtree is not empty, we need to re-arrange the nodes
        if root.left:
            # Append the right subtree after the left subtree
            left_tail.right = root.right
            # Move the left subtree to the right of the root
            root.right = root.left
            # Set the left child of the root to None
            root.left = None
        
        # Return the tail of the flattened tree rooted at 'root'
        return right_tail if right_tail else left_tail if left_tail else root

# Helper function to print the flattened linked list
def print_flattened(root):
    while root:
        print(root.val, end=" ")
        root = root.right
    print()

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1:
    #       1
    #      / \
    #     2   5
    #    / \   \
    #   3   4   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(6)
    solution.flatten(root1)
    print("Test case 1:")
    print_flattened(root1)  # Expected output: 1 2 3 4 5 6

    # Test case 2: Empty tree
    root2 = None
    solution.flatten(root2)
    print("Test case 2:")
    print_flattened(root2)  # Expected output: (empty line)

    # Test case 3: Single node tree
    root3 = TreeNode(0)
    solution.flatten(root3)
    print("Test case 3:")
    print_flattened(root3)  # Expected output: 0
```

## Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the number of nodes in the binary tree. This is because we visit each node once.
- **Space Complexity**: O(h), where h is the height of the binary tree. This is due to the recursive call stack. In the worst case (when the tree is skewed), h = n, making the space complexity O(n). In the best case (when the tree is balanced), h = log(n), making the space complexity O(log n).

## Test Cases
The provided Python solution includes test cases to verify its correctness. These test cases cover different scenarios, including a regular binary tree, an empty tree, and a tree with a single node.