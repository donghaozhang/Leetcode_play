# word_ladder_ii.md)
- 克隆图 / Clone Graph [LeetCode 133]

## Problem Description

### Problem Description

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

#### Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.

#### Example 1:

![graph](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

**Input:**  
`adjList = [[2,4],[1,3],[2,4],[1,3]]`  

**Output:**  
`[[2,4],[1,3],[2,4],[1,3]]`  

**Explanation:**  
There are 4 nodes in the graph.  
- 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).  
- 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).  
- 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).  
- 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).  

#### Example 2:

![graph2](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

**Input:**  
`adjList = [[]]`  

**Output:**  
`[[]]`  

**Explanation:**  
Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.  

#### Example 3:

**Input:**  
`adjList = []`  

**Output:**  
`[]`  

**Explanation:**  
This an empty graph, it does not have any nodes.  

#### Constraints:

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

## Solution

### Problem Explanation
The problem requires us to create a deep copy of a connected undirected graph. A deep copy means that we need to create new nodes for all the nodes in the original graph and set up the same neighbor relationships as in the original graph. The graph is represented using nodes where each node has a value and a list of its neighboring nodes.

### Approach
1. **Understand the Graph Structure**: The graph is undirected, meaning if node A has node B as a neighbor, then node B must also have node A as a neighbor.
2. **Handle Edge Cases**: If the input node is null, return null. If the graph is empty, return an empty list.
3. **Breadth-First Search (BFS) or Depth-First Search (DFS)**: We can use either BFS or DFS to traverse the original graph and create copies of each node. We'll use a hash map to keep track of the original nodes and their corresponding copies to avoid cycles and redundant copies.
4. **Clone Nodes and Neighbors**: For each node encountered during traversal, if it hasn't been cloned yet, create a new clone and add it to the hash map. Then, recursively or iteratively clone all its neighbors and set up the neighbor relationships in the cloned nodes.

### Solution Code
```python
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None
    
    # Dictionary to save the visited nodes and their clones
    visited = {}
    
    # Queue for BFS
    queue = deque([node])
    
    # Clone the first node
    visited[node] = Node(node.val, [])
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in current_node.neighbors:
            if neighbor not in visited:
                # Clone the neighbor and add to visited
                visited[neighbor] = Node(neighbor.val, [])
                queue.append(neighbor)
            # Add the cloned neighbor to the current node's clone neighbors
            visited[current_node].neighbors.append(visited[neighbor])
    
    return visited[node]

# Test cases
def test_cloneGraph():
    # Helper function to create a graph from adjacency list
    def createGraph(adjList):
        if not adjList:
            return None
        nodes = {}
        for i in range(1, len(adjList)+1):
            nodes[i] = Node(i)
        for i in range(1, len(adjList)+1):
            neighbors = adjList[i-1]
            for neighbor in neighbors:
                nodes[i].neighbors.append(nodes[neighbor])
        return nodes[1]
    
    # Helper function to convert graph to adjacency list
    def graphToAdjList(node):
        if not node:
            return []
        adj_dict = {}
        visited = set()
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current.val in visited:
                continue
            visited.add(current.val)
            neighbors = []
            for neighbor in current.neighbors:
                neighbors.append(neighbor.val)
                if neighbor.val not in visited:
                    queue.append(neighbor)
            adj_dict[current.val] = neighbors
        adj_list = []
        for i in range(1, len(adj_dict)+1):
            adj_list.append(adj_dict[i])
        return adj_list
    
    # Test case 1: Example 1
    adjList1 = [[2,4],[1,3],[2,4],[1,3]]
    node1 = createGraph(adjList1)
    cloned_node1 = cloneGraph(node1)
    assert graphToAdjList(cloned_node1) == adjList1
    
    # Test case 2: Example 2 (single node with no neighbors)
    adjList2 = [[]]
    node2 = createGraph(adjList2)
    cloned_node2 = cloneGraph(node2)
    assert graphToAdjList(cloned_node2) == adjList2
    
    # Test case 3: Empty graph
    adjList3 = []
    node3 = createGraph(adjList3)
    cloned_node3 = cloneGraph(node3)
    assert graphToAdjList(cloned_node3) == adjList3
    
    print("All test cases pass")

test_cloneGraph()
```

### Explanation
1. **Node Class**: The `Node` class is defined with a value and a list of neighbors.
2. **cloneGraph Function**: This function uses BFS to traverse the original graph. It maintains a `visited` dictionary to map original nodes to their clones. For each node, it checks all neighbors, clones them if not already cloned, and adds them to the clone's neighbor list.
3. **Test Cases**: The test cases verify the correctness of the solution by comparing the adjacency list of the cloned graph with the original. The helper functions `createGraph` and `graphToAdjList` convert between adjacency lists and graph node structures for testing purposes.

### Time and Space Complexity
- **Time Complexity**: O(N + M), where N is the number of nodes and M is the number of edges. Each node and edge is processed exactly once.
- **Space Complexity**: O(N), due to the storage required for the `visited` dictionary and the queue, which can hold up to N nodes in the worst case.