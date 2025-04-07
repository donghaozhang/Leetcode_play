# word_ladder_ii.md)
- 克隆图 / Clone Graph [LeetCode 133]

## Problem Description

## Problem Description

### Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

### Example 1:

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

### Example 2:

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list as the node 1 has no neighbors.
```

### Example 3:

```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

### Example 4:

```
Input: adjList = [[2],[1]]
Output: [[2],[1]]
```

### Constraints:

* The number of nodes in the graph is in the range `[0, 100]`.
* `Node.val` is unique for each node.
* There are no repeated edges and no self-loops in the graph.
* The Graph is connected and all nodes can be visited starting from the given node.

## Solution

## Problem Explanation

The problem requires creating a deep copy (clone) of a given connected undirected graph. The graph is represented using a reference to one of its nodes. The task is to return a deep copy of the graph, ensuring that all nodes and their connections are replicated.

## Step-by-Step Approach

1. **Understand the Graph Representation**: The graph is represented using nodes, where each node contains a value (`val`) and a list of its neighbors (`neighbors`).

2. **Choose a Traversal Method**: To clone the graph, we need to traverse it. We can use either Breadth-First Search (BFS) or Depth-First Search (DFS) for this purpose. Here, we'll use DFS because it's more straightforward for recursive implementations.

3. **Use a Data Structure to Keep Track of Cloned Nodes**: To avoid cloning nodes multiple times and to handle cycles, we'll use a dictionary (`visited`) to store the nodes we've already cloned. The key will be the original node, and the value will be its clone.

4. **Clone Nodes and Their Neighbors Recursively**:
   - For each node, check if it's already been cloned. If so, return its clone.
   - If not, create a clone of the node.
   - Recursively clone its neighbors and update the clone's neighbors list.

5. **Return the Clone of the Given Node**: The entry point of our cloning process is the given node. We return its clone, which is the entry point to the cloned graph.

## Python Solution

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
```

## Time and Space Complexity Analysis

- **Time Complexity**: O(N + M), where N is the number of nodes and M is the number of edges. We visit each node once and iterate over its neighbors.
- **Space Complexity**: O(N), for storing the cloned nodes in the `visited` dictionary. The recursion stack can also go up to O(N) in the case of a skewed graph (essentially a linked list).

## Test Cases

To verify the solution, we can use the provided examples:

1. `adjList = [[2,4],[1,3],[2,4],[1,3]]`
2. `adjList = [[]]` (a single node with no neighbors)
3. `adjList = []` (an empty graph)
4. `adjList = [[2],[1]]` (two nodes connected to each other)

We need to construct the graph from the adjacency list and then call the `cloneGraph` method. After cloning, we should compare the original and cloned graphs to ensure they are identical in structure but distinct in terms of node objects.

```python
def printGraph(node):
    visited = set()
    queue = [node]
    visited.add(node)
    result = []
    while queue:
        current = queue.pop(0)
        neighbors_val = [n.val for n in current.neighbors]
        result.append([current.val, neighbors_val])
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Example usage
if __name__ == "__main__":
    # Creating nodes for the first example
    nodes = [Node(i) for i in range(1, 5)]
    nodes[0].neighbors = [nodes[1], nodes[3]]
    nodes[1].neighbors = [nodes[0], nodes[2]]
    nodes[2].neighbors = [nodes[1], nodes[3]]
    nodes[3].neighbors = [nodes[0], nodes[2]]
    
    solution = Solution()
    cloned_node = solution.cloneGraph(nodes[0])
    print("Original Graph:", printGraph(nodes[0]))
    print("Cloned Graph:", printGraph(cloned_node))
```

This test case constructs a graph, clones it, and then prints both the original and cloned graphs to verify that the cloning was successful.