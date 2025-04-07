# postorder_traversal.py)
- 层序遍历 / Level Order Traversal [LeetCode 102]

## Problem Description

## Problem Description

### Binary Tree Level Order Traversal

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

#### Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

#### Example 2:

```
Input: root = [1]
Output: [[1]]
```

#### Example 3:

```
Input: root = []
Output: []
```

#### Constraints:

* The number of nodes in the tree is in the range `[0, 2000]`.
* `-1000 <= Node.val <= 1000`

## Solution

**Problem Explanation**
=======================

The problem requires performing a level order traversal on a given binary tree and returning the values of the nodes level by level from left to right.

### Key Constraints and Edge Cases

* The number of nodes in the tree is in the range `[0, 2000]`.
* The value of each node is in the range `[-1000, 1000]`.
* The input tree can be empty.
* The tree can have only one node.

### Input and Output

* Input: The root of a binary tree.
* Output: A list of lists containing the node values level by level.

**Step-by-Step Approach**
-------------------------

1. **Check if the tree is empty**: If the tree is empty (i.e., the root is `None`), return an empty list.
2. **Initialize a queue**: Create a queue to store the nodes to be processed. Enqueue the root node.
3. **Initialize the result list**: Create an empty list to store the result.
4. **Perform level order traversal**: While the queue is not empty, perform the following steps:
   * **Process the current level**: Dequeue all nodes at the current level and store their values in a list.
   * **Enqueue the next level**: Enqueue the children of the nodes at the current level.
   * **Add the current level to the result**: Add the list of values at the current level to the result list.
5. **Return the result**: Return the result list containing the node values level by level.

**Python Solution**
------------------

```python
from collections import deque
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
        Performs a level order traversal on a binary tree and returns the node values level by level.

        Args:
        root: The root of the binary tree.

        Returns:
        A list of lists containing the node values level by level.
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result

def print_tree(node: Optional[TreeNode], level: int = 0) -> None:
    """
    Prints the binary tree in a pretty format.

    Args:
    node: The current node.
    level: The current level.
    """
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)

def main() -> None:
    # Create a sample binary tree:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Binary Tree:")
    print_tree(root)

    solution = Solution()
    result = solution.levelOrder(root)
    print("Level Order Traversal:", result)

    # Test cases
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ]

    for test_case in test_cases:
        input_tree = create_tree(test_case[0])
        expected_output = test_case[1]
        actual_output = solution.levelOrder(input_tree)
        print(f"Input: {test_case[0]}, Expected: {expected_output}, Actual: {actual_output}")
        assert actual_output == expected_output, f"Test case failed: {test_case}"

def create_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Creates a binary tree from a list of values.

    Args:
    values: A list of values representing the binary tree.

    Returns:
    The root of the created binary tree.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    main()
```

**Time and Space Complexity Analysis**
--------------------------------------

* **Time complexity**: O(N), where N is the number of nodes in the tree, since we visit each node once.
* **Space complexity**: O(N), where N is the number of nodes in the tree, since in the worst case, the queue will contain N/2 nodes at the last level.

**Test Cases**
--------------

The provided Python solution includes test cases to verify its correctness. The `main` function creates a sample binary tree and performs a level order traversal using the `Solution` class. Additionally, it includes several test cases to validate the solution against expected outputs.