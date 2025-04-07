# level_order_traversal.md)

### 其他树问题
- 二叉树路径 / Binary Tree Paths [LeetCode 257]

## Problem Description

## 257. Binary Tree Paths

Given the `root` of a binary tree, return all root-to-leaf paths in **any order**.

A **leaf** is a node with no children.

### Example 1:

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

### Example 2:

```
Input: root = [1]
Output: ["1"]
```

### Constraints:

* The number of nodes in the tree is in the range `[1, 100]`.
* `-100 <= Node.val <= 100`

## Solution

## Problem Explanation
The problem requires finding all root-to-leaf paths in a given binary tree. A root-to-leaf path is a path from the root node to a leaf node, where a leaf node is a node with no children.

## Step-by-Step Approach
1. **Understand the Problem**: The task is to traverse a binary tree and return all paths from the root to leaf nodes.
2. **Choose a Traversal Method**: Since we need to explore all paths from the root to leaves, a depth-first traversal (DFS) is suitable.
3. **Implement DFS**: We will use a recursive DFS approach to traverse the tree. For each node, we'll maintain a current path.
4. **Handle Leaf Nodes**: When a leaf node is encountered, the current path is added to the result list.
5. **Backtrack**: After exploring a node's children, we backtrack by removing the current node from the path.

## Python Solution

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        """
        Returns all root-to-leaf paths in a binary tree.

        :param root: The root of the binary tree.
        :return: A list of strings representing root-to-leaf paths.
        """
        def dfs(node: TreeNode, path: str) -> None:
            """
            Performs a depth-first search on the binary tree.

            :param node: The current node.
            :param path: The current path.
            """
            if not node:
                return
            
            # Update the current path
            new_path = path + str(node.val) if not path else path + "->" + str(node.val)
            
            # If the node is a leaf, add the path to the result
            if not node.left and not node.right:
                result.append(new_path)
                return
            
            # Recursively explore the left and right subtrees
            dfs(node.left, new_path)
            dfs(node.right, new_path)

        result = []
        dfs(root, "")
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: root = [1,2,3,null,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    print(solution.binaryTreePaths(root1))  # Output: ["1->2->5", "1->3"]

    # Test case 2: root = [1]
    root2 = TreeNode(1)
    print(solution.binaryTreePaths(root2))  # Output: ["1"]
```

## Time and Space Complexity Analysis

*   **Time Complexity**: O(N), where N is the number of nodes in the tree, since we visit each node once.
*   **Space Complexity**: O(N), for the recursion stack in the worst case (when the tree is skewed) and for storing the result.

## Test Cases
The provided Python solution includes test cases to verify its correctness. These test cases cover different scenarios:

*   **Test Case 1**: A binary tree with multiple nodes and a leaf node that is not a direct child of the root.
*   **Test Case 2**: A binary tree with a single node (the root itself is a leaf).

You can run the solution with these test cases to ensure it produces the expected output.