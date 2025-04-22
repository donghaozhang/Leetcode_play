# Serialize and Deserialize Binary Tree

## Problem

Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a data structure into a sequence of bits that can be stored or transmitted. Deserialization is the process of reconstructing the original data structure from the serialized form.

The algorithm should:
1. Convert a binary tree to a string representation
2. Reconstruct the original tree from the string
3. Handle null nodes appropriately
4. Match LeetCode's serialization format

## Examples

**Example 1:**
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Tree structure:
    1
   / \
  2   3
     / \
    4   5
```

**Example 2:**
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000

## Approach: Level Order Traversal

The solution uses level order traversal (BFS) to serialize and deserialize the tree. Here's how it works:

1. **Serialization**:
   - Use a queue to traverse the tree level by level
   - For each node:
     - If node exists, append its value
     - If node is null, append empty string
   - Join all values with commas

2. **Deserialization**:
   - Split the string by commas to get node values
   - Use a queue to build the tree level by level
   - For each non-null value, create a new node
   - Connect nodes according to their positions

### Key Components:

1. **TreeNode Class**:
   ```python
   class TreeNode:
       def __init__(self, x):
           self.val = x
           self.left = None
           self.right = None
   ```

2. **Codec Class**:
   ```python
   class Codec:
       def serialize(self, root: Optional[TreeNode]) -> str:
           if not root:
               return ""
           flat_bt = []
           queue = deque([root])
           while queue:
               node = queue.popleft()
               if node:
                   flat_bt.append(str(node.val))
                   queue.append(node.left)
                   queue.append(node.right)
               else:
                   flat_bt.append("")
           return ",".join(flat_bt)

       def deserialize(self, data: str) -> Optional[TreeNode]:
           if not data:
               return None
           flat_bt = data.split(",")
           root = TreeNode(int(flat_bt[0]))
           queue = deque([root])
           i = 1
           while queue:
               node = queue.popleft()
               if i < len(flat_bt) and flat_bt[i]:
                   node.left = TreeNode(int(flat_bt[i]))
                   queue.append(node.left)
               i += 1
               if i < len(flat_bt) and flat_bt[i]:
                   node.right = TreeNode(int(flat_bt[i]))
                   queue.append(node.right)
               i += 1
           return root
   ```

## Complexity Analysis

- **Time Complexity**:
  - Serialization: O(n), where n is the number of nodes
  - Deserialization: O(n), where n is the number of nodes
  - Both operations visit each node exactly once

- **Space Complexity**:
  - Serialization: O(n) for the queue and result string
  - Deserialization: O(n) for the queue and reconstructed tree
  - Overall: O(n) for both operations

## Why This Approach Works

1. **Completeness**:
   - Level order traversal captures the complete tree structure
   - Null nodes are explicitly represented
   - Preserves the hierarchical relationship between nodes

2. **Efficiency**:
   - Linear time complexity
   - Minimal space overhead
   - Simple string manipulation

3. **Robustness**:
   - Handles empty trees
   - Handles single node trees
   - Handles unbalanced trees
   - Preserves node values exactly

## Example Walkthrough

For the example tree [1,2,3,null,null,4,5]:

1. **Serialization**:
   - Start with root (1)
   - Queue: [1]
   - Process 1: append "1", enqueue 2 and 3
   - Queue: [2,3]
   - Process 2: append "2", enqueue null and null
   - Queue: [3,null,null]
   - Process 3: append "3", enqueue 4 and 5
   - Queue: [null,null,4,5]
   - Process nulls: append ""
   - Process 4: append "4", enqueue null and null
   - Process 5: append "5", enqueue null and null
   - Result: "1,2,3,,,4,5"

2. **Deserialization**:
   - Split string: ["1","2","3","","","4","5"]
   - Create root (1)
   - Queue: [1]
   - Process 1: create left (2) and right (3)
   - Queue: [2,3]
   - Process 2: skip null children
   - Process 3: create left (4) and right (5)
   - Queue: [4,5]
   - Process 4 and 5: skip null children
   - Result: Original tree reconstructed 