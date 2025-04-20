# Binary Tree Zigzag Level Order Traversal

## Problem

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

## Examples

**Example 1:**
```
    3
   / \
  9  20
    /  \
   15   7
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Explanation:
- First level (0): Traverse from left to right → [3]
- Second level (1): Traverse from right to left → [20,9]
- Third level (2): Traverse from left to right → [15,7]

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

## Approach 1: Modified BFS with Direction Toggle

This approach is a modification of the standard level order traversal with BFS. The key difference is that we toggle a flag after processing each level to determine whether to reverse the current level's values:

1. Start with a queue containing the root node and a flag to track the current direction (initialize to false).
2. While the queue is not empty:
   a. Get the number of nodes at the current level.
   b. Process all nodes at the current level by dequeuing them.
   c. Add their children to the queue for the next level.
   d. If the flag is true, reverse the current level's values.
   e. Add the level's values to the result.
   f. Toggle the flag for the next level.

## Solution 1: Iterative BFS

```python
def zigzag_level_order_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    # Flag to track direction (True means right to left)
    reverse = False
    
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
        
        # Reverse the level values if needed
        if reverse:
            level_values.reverse()
        
        result.append(level_values)
        reverse = not reverse  # Toggle the direction for the next level
    
    return result
```

## Approach 2: Recursive DFS with Level Tracking

We can also use a recursive DFS approach:

1. Use a dictionary to store values at each level.
2. For even-numbered levels, insert values at the beginning of the list for that level.
3. For odd-numbered levels, append values at the end of the list.
4. Convert the dictionary to a list of lists for the final result.

## Solution 2: Recursive DFS

```python
def zigzag_level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    level_dict = defaultdict(list)
    
    def dfs(node, level):
        if not node:
            return
        
        # Check if we need to insert at beginning (even levels) or append (odd levels)
        if level % 2 == 0:  # Even level, insert at beginning
            level_dict[level].insert(0, node.val)
        else:  # Odd level, append at end
            level_dict[level].append(node.val)
        
        # Recursively process children
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    # Start DFS
    dfs(root, 0)
    
    # Convert dictionary to list of lists
    result = []
    for i in range(len(level_dict)):
        result.append(level_dict[i])
    
    return result
```

## Time Complexity

Both approaches have the same time complexity:
- O(n): We visit each node exactly once, where n is the number of nodes in the tree.

The iterative approach may have additional O(n) operations for reversing levels, but this doesn't change the overall complexity.

## Space Complexity

- O(n): Both approaches use space proportional to the number of nodes in the tree.
  - For the iterative approach, the queue can contain at most n/2 nodes (the maximum width of the tree).
  - For the recursive approach, the call stack can go as deep as the height of the tree (O(h)), and the dictionary stores all n nodes.

## Implementation Comparison

### Iterative Approach (BFS)
- **Pros**: Follows the natural level-by-level processing, which is intuitive for a level order problem.
- **Cons**: Requires reversing arrays, which might be less efficient for very large trees.

### Recursive Approach (DFS)
- **Pros**: No need to reverse arrays; the zigzag pattern is built during traversal.
- **Cons**: Less intuitive for a level order problem, as DFS doesn't naturally visit nodes level by level.

## Related Problems

- Binary Tree Level Order Traversal
- Binary Tree Level Order Traversal II (bottom-up)
- N-ary Tree Level Order Traversal 