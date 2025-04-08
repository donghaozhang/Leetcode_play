# postorder_traversal.py)
- 层序遍历 / Level Order Traversal [LeetCode 102]

## Problem Description

Here is the full description of LeetCode problem #102, "Binary Tree Level Order Traversal":

---

Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example 1:**

![Example 1](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

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

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

---

## Solution

### Explanation of the Problem
The problem requires performing a level order traversal of a binary tree, which means visiting all nodes level by level from top to bottom and from left to right within each level. The output should be a list of lists, where each inner list contains the values of nodes at the same level.

For example, given the tree:
```
    3
   / \
  9  20
    /  \
   15   7
```
The level order traversal would be `[[3], [9, 20], [15, 7]]`.

### Approach
1. **Breadth-First Search (BFS)**: This is the most natural approach for level order traversal. We use a queue to keep track of nodes at the current level.
2. **Process Level by Level**: For each level, we process all nodes in the queue, collect their values, and enqueue their children for the next level.
3. **Loop Until Queue is Empty**: The process continues until there are no more nodes left to process.

### Solution Code
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
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result

# Test cases
def test_levelOrder():
    # Test case 1: Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert Solution().levelOrder(root1) == [[3], [9, 20], [15, 7]]
    
    # Test case 2: Example 2
    root2 = TreeNode(1)
    assert Solution().levelOrder(root2) == [[1]]
    
    # Test case 3: Example 3
    root3 = None
    assert Solution().levelOrder(root3) == []
    
    # Additional test case: Single left child
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    assert Solution().levelOrder(root4) == [[1], [2]]
    
    # Additional test case: Single right child
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    assert Solution().levelOrder(root5) == [[1], [2]]
    
    print("All test cases pass")

test_levelOrder()
```

### Explanation
1. **Initialization**: We start by checking if the root is `None`. If it is, we return an empty list.
2. **Queue Setup**: We initialize a queue with the root node to start the BFS.
3. **Processing Levels**: For each level, we determine the number of nodes (`level_size`) in the current level. We process each node by dequeuing it, adding its value to the current level's list, and enqueuing its left and right children if they exist.
4. **Collecting Results**: After processing all nodes in the current level, the collected values are added to the result list.
5. **Termination**: The loop continues until the queue is empty, indicating all levels have been processed.

### Time and Space Complexity
- **Time Complexity**: O(N), where N is the number of nodes in the tree. Each node is processed exactly once.
- **Space Complexity**: O(N), which is the maximum size of the queue. In the worst case, the queue holds all nodes at the last level, which can be up to N/2 nodes for a balanced tree.

### Test Cases
1. **Example 1**: A balanced tree with three levels.
2. **Example 2**: A tree with only the root node.
3. **Example 3**: An empty tree.
4. **Additional Test 1**: A tree with only a left child.
5. **Additional Test 2**: A tree with only a right child.

These test cases verify the correctness of the solution for various tree structures.