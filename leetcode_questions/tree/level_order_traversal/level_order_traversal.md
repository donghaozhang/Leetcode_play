# Binary Tree Level Order Traversal

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

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
Output: [[3],[9,20],[15,7]]

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

## Approach: Breadth-First Search (BFS)

The key to level order traversal is to process nodes level by level. We can use a Breadth-First Search (BFS) approach with a queue data structure:

1. Start by adding the root node to a queue.
2. While the queue is not empty:
   a. Get the number of nodes at the current level (the current queue size).
   b. Process all nodes at the current level by dequeuing them one by one.
   c. For each node, add its value to the current level's result.
   d. Enqueue all of its children (left and right) for processing in the next level.
   e. After processing all nodes at the current level, add the level's result to the final result.

This ensures that we process nodes level by level, from left to right.

## Solution

```python
def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    # Handle empty tree case
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    # BFS traversal
    while queue:
        # Number of nodes at current level
        level_size = len(queue)
        level_values = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            # Add children to queue for next level processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add current level values to result
        result.append(level_values)
    
    return result
```

## Time Complexity

- O(n): We visit each node exactly once, where n is the number of nodes in the tree.

## Space Complexity

- O(n): In the worst case, the queue will contain all nodes in the last level of the tree, which could be up to n/2 nodes (in a complete binary tree).

## Alternative Approaches

### Two Queue Approach

Instead of tracking the level size, we can use two queues:
- One for the current level's nodes
- Another for the next level's nodes

```python
def level_order_two_queues(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    current_queue = [root]
    
    while current_queue:
        next_queue = []
        level_values = []
        
        for node in current_queue:
            level_values.append(node.val)
            
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
                
        result.append(level_values)
        current_queue = next_queue
    
    return result
```

### Dummy Node Separator Approach

We can use a dummy node (None) as a level separator:

```python
def level_order_dummy_node(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    level_values = []
    queue = deque([root, None])  # None as level separator
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            result.append(level_values)
            level_values = []
            if queue:  # If there are more nodes to process
                queue.append(None)
            continue
            
        level_values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

### Recursive Approach

Though less common for level order traversal, we can also use recursion:

```python
def level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    
    def traverse(node, level):
        if not node:
            return
        
        # If this is a new level, add an empty list
        if len(result) <= level:
            result.append([])
            
        # Add the current node value
        result[level].append(node.val)
        
        # Recurse on children
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)
    
    traverse(root, 0)
    return result
```

## Applications

- Level order traversal is particularly useful for problems involving tree width, finding specific levels, or zigzag traversal
- It's often used for serializing and deserializing binary trees
- It's the basis for algorithms that need to process trees in a breadth-first manner 