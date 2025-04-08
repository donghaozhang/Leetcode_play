# word_ladder_ii.md)
- 克隆图 / Clone Graph [LeetCode 133]

## Problem Description

```markdown
## 133. Clone Graph

Given a reference of a node in a **connected** undirected graph.

Return a **deep copy** (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**Adjacency list** is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

**Input:** adjList = [[2,4],[1,3],[2,4],[1,3]]
**Output:** [[2,4],[1,3],[2,4],[1,3]]
**Explanation:** There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

**Input:** adjList = [[]]
**Output:** [[]]
**Explanation:** Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

**Example 3:**

**Input:** adjList = []
**Output:** []
**Explanation:** This an empty graph, it does not have any nodes.

**Constraints:**

*   The number of nodes in the graph is in the range `[0, 100]`.
*   `1 <= Node.val <= 100`
*   `Node.val` is unique for each node.
*   There are no repeated edges and no self-loops in the graph.
*   The Graph is connected and all nodes can be visited starting from the given node.
```

## Solution

Okay, let's break down the "Clone Graph" problem.

**1. Explanation of the Problem**

The task is to create a "deep copy" of a given undirected graph. We are given a reference to one node in this graph. A deep copy means we need to create entirely new `Node` objects for the cloned graph. Each new node should have the same value (`val`) as its corresponding original node. Furthermore, the connections (neighbors) between the new nodes must mirror the connections in the original graph. If original node A is connected to original node B, then the newly created clone of A must be connected to the newly created clone of B, and vice-versa. We need to return the reference to the clone of the *starting* node provided as input.

**Key Challenges:**

*   **Avoiding Infinite Loops:** Graphs can have cycles. If we naively traverse and clone, we might get stuck in an infinite loop.
*   **Ensuring Uniqueness:** We must ensure that each node in the original graph corresponds to exactly *one* node in the cloned graph. If node A is a neighbor of both B and C, the clone of A should be the *same* object when accessed from the clone of B and the clone of C.

**2. Step-by-Step Approach**

We can solve this using either Breadth-First Search (BFS) or Depth-First Search (DFS). The core idea for both is to keep track of the nodes we've already visited and cloned to avoid redundant work and infinite loops. A hash map (dictionary in Python) is ideal for this, mapping original nodes to their corresponding cloned nodes.

**Approach using BFS (Iterative):**

1.  **Initialization:**
    *   Handle the edge case: If the input `node` is `None`, return `None`.
    *   Create a dictionary `cloned_nodes_map` to store the mapping from original nodes to their clones: `{original_node: cloned_node}`.
    *   Create a queue (e.g., `collections.deque`) for the BFS traversal.
    *   Clone the starting node: Create a new `Node` with `node.val` but an empty `neighbors` list for now. Let's call it `start_clone`.
    *   Add the mapping for the starting node to the map: `cloned_nodes_map[node] = start_clone`.
    *   Add the original starting `node` to the queue.

2.  **BFS Traversal:**
    *   While the queue is not empty:
        *   Dequeue an original node, let's call it `current_orig`.
        *   Get its corresponding clone from the map: `current_clone = cloned_nodes_map[current_orig]`.
        *   Iterate through each `neighbor_orig` in `current_orig.neighbors`:
            *   **Check if neighbor is cloned:** Look up `neighbor_orig` in `cloned_nodes_map`.
                *   **If not found:** This means we haven't encountered this neighbor yet.
                    *   Create a new clone for the neighbor: `neighbor_clone = Node(neighbor_orig.val)`.
                    *   Add the mapping to the map: `cloned_nodes_map[neighbor_orig] = neighbor_clone`.
                    *   Enqueue the original neighbor (`neighbor_orig`) so we can process its neighbors later.
                *   **If found:** Retrieve the existing clone: `neighbor_clone = cloned_nodes_map[neighbor_orig]`.
            *   **Connect the clones:** Add `neighbor_clone` to the `neighbors` list of `current_clone`.

3.  **Return Value:**
    *   After the BFS completes, the entire reachable graph structure has been cloned. Return `start_clone` (the clone of the initial input node).

**Approach using DFS (Recursive):**

1.  **Initialization:**
    *   Handle the edge case: If the input `node` is `None`, return `None`.
    *   Create a dictionary `cloned_nodes_map` (accessible across recursive calls, e.g., passed as an argument or defined in an outer scope) to store the mapping: `{original_node: cloned_node}`.

2.  **Recursive Function `dfs_clone(original_node)`:**
    *   **Base Case / Memoization:** If `original_node` is already in `cloned_nodes_map`, return the existing clone `cloned_nodes_map[original_node]`.
    *   **Create Clone:** Create a new `Node` with `original_node.val` but an empty `neighbors` list. Let's call it `new_clone`.
    *   **Store Mapping:** Add the mapping `cloned_nodes_map[original_node] = new_clone`. **Crucially, do this *before* the recursive calls** to handle cycles correctly.
    *   **Process Neighbors:** Iterate through each `neighbor_orig` in `original_node.neighbors`:
        *   Recursively call `cloned_neighbor = dfs_clone(neighbor_orig)`. This will either return an existing clone or create a new one.
        *   Add `cloned_neighbor` to the `neighbors` list of `new_clone`.
    *   **Return Value:** Return `new_clone`.

3.  **Initial Call:**
    *   Call the recursive function starting with the input `node`: `return dfs_clone(node)`.

Both BFS and DFS achieve the same result. BFS is often slightly easier to reason about iteratively, while DFS can be more concise recursively.

**3. Python Solution**

```python
import collections

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    # Helper function for testing: Convert graph starting from this node to adjList
    def to_adj_list(self):
        adj = {}
        q = collections.deque([self])
        visited = {self}
        while q:
            curr = q.popleft()
            # Ensure node value is used as key and neighbors are sorted for consistent output
            adj[curr.val] = sorted([n.val for n in curr.neighbors])
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        # Convert map to list based on node values 1 to N
        max_val = 0
        if adj:
             max_val = max(adj.keys())
        
        adj_list_result = []
        for i in range(1, max_val + 1):
             if i in adj:
                 adj_list_result.append(adj[i])
             else:
                 # Handle disconnected nodes if necessary, though problem statement says connected
                 # For consistency with test case format, add empty list if node exists but wasn't reached
                 # or if the graph has gaps in node values (which shouldn't happen based on constraints)
                 pass # Assuming connected graph and contiguous node values 1..N

        # If the graph starts from a node not 1, or is empty
        if not adj_list_result and self.val > 0:
             # Single node graph case
             if not self.neighbors:
                 return [[self.val]] if not adj else [adj.get(self.val, [])]
             # More complex cases might need adjustments based on exact test format requirements

        # Adjust for 1-based indexing representation if needed by sorting keys
        sorted_adj = {}
        for i in sorted(adj.keys()):
            sorted_adj[i] = adj[i]

        # Final list representation
        final_list = []
        if not sorted_adj:
            if self.val == 0 and not self.neighbors: # Handle truly empty node case if needed
                 return [] if self.val == 0 else [[]] # Adjust based on how empty graph is represented
            elif self.val != 0: # Single node case
                 return [[]]


        for i in range(1, max(sorted_adj.keys()) + 1):
             final_list.append(sorted_adj.get(i, [])) # Use get for safety

        return final_list


    # Helper function to build graph from adjList for testing
    @staticmethod
    def from_adj_list(adjList):
        if not adjList:
            return None
        
        nodes = {}
        # Create all nodes first
        for i in range(len(adjList)):
            node_val = i + 1
            nodes[node_val] = Node(node_val)
            
        # Add neighbors
        for i in range(len(adjList)):
            node_val = i + 1
            current_node = nodes[node_val]
            neighbor_vals = adjList[i]
            for neighbor_val in neighbor_vals:
                if neighbor_val in nodes:
                    current_node.neighbors.append(nodes[neighbor_val])
                    
        return nodes.get(1) # Return the first node (val=1)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Clones a graph using Breadth-First Search (BFS).
        """
        if not node:
            return None

        # Dictionary to map original nodes to their clones
        cloned_nodes_map = {}

        # Queue for BFS, storing original nodes to visit
        queue = collections.deque([node])

        # Clone the starting node and add it to the map
        # We create the clone with the correct value but initially empty neighbors
        cloned_nodes_map[node] = Node(node.val, [])

        while queue:
            # Get the next original node to process
            current_orig = queue.popleft()
            # Get its corresponding clone (which must exist in the map)
            current_clone = cloned_nodes_map[current_orig]

            # Process neighbors of the original node
            for neighbor_orig in current_orig.neighbors:
                # Check if the neighbor has already been cloned
                if neighbor_orig not in cloned_nodes_map:
                    # If not, clone it and add to map
                    neighbor_clone = Node(neighbor_orig.val, [])
                    cloned_nodes_map[neighbor_orig] = neighbor_clone
                    # Add the original neighbor to the queue to process later
                    queue.append(neighbor_orig)
                else:
                    # If already cloned, just get the reference from the map
                    neighbor_clone = cloned_nodes_map[neighbor_orig]

                # Add the cloned neighbor to the neighbors list of the current cloned node
                current_clone.neighbors.append(neighbor_clone)

        # Return the clone of the starting node
        return cloned_nodes_map[node]

    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        """
        Clones a graph using Depth-First Search (DFS) - Recursive approach.
        """
        cloned_nodes_map = {} # Use a dictionary for memoization

        def dfs_clone(original_node):
            if not original_node:
                return None
            
            # If node already cloned, return the existing clone
            if original_node in cloned_nodes_map:
                return cloned_nodes_map[original_node]

            # Clone the node (without neighbors initially)
            new_clone = Node(original_node.val, [])
            
            # IMPORTANT: Add to map *before* recursive calls to handle cycles
            cloned_nodes_map[original_node] = new_clone

            # Recursively clone neighbors and add them to the new clone's list
            if original_node.neighbors:
                for neighbor_orig in original_node.neighbors:
                    cloned_neighbor = dfs_clone(neighbor_orig)
                    new_clone.neighbors.append(cloned_neighbor)
            
            return new_clone

        return dfs_clone(node)


# --- Test Cases ---

solver = Solution()

# Helper function to compare two graphs represented by adjLists
def compare_graphs(adjList1, adjList2):
    return adjList1 == adjList2

# Test Case 1: Example 1
adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
print(f"Test Case 1: Input adjList = {adjList1}")
graph1_orig = Node.from_adj_list(adjList1)
graph1_cloned_bfs = solver.cloneGraph(graph1_orig)
graph1_cloned_dfs = solver.cloneGraphDFS(graph1_orig)
output_bfs1 = graph1_cloned_bfs.to_adj_list() if graph1_cloned_bfs else []
output_dfs1 = graph1_cloned_dfs.to_adj_list() if graph1_cloned_dfs else []
print(f"BFS Output adjList: {output_bfs1}")
print(f"DFS Output adjList: {output_dfs1}")
print(f"Result Matches Expected (BFS): {compare_graphs(output_bfs1, adjList1)}")
print(f"Result Matches Expected (DFS): {compare_graphs(output_dfs1, adjList1)}")
print("-" * 20)

# Test Case 2: Single Node
adjList2 = [[]]
print(f"Test Case 2: Input adjList = {adjList2}")
graph2_orig = Node.from_adj_list(adjList2)
graph2_cloned_bfs = solver.cloneGraph(graph2_orig)
graph2_cloned_dfs = solver.cloneGraphDFS(graph2_orig)
# Adjusting expected output for single node based on helper function logic
expected_output2 = [[]] # A single node with val 1 and no neighbors
output_bfs2 = graph2_cloned_bfs.to_adj_list() if graph2_cloned_bfs else []
output_dfs2 = graph2_cloned_dfs.to_adj_list() if graph2_cloned_dfs else []
print(f"BFS Output adjList: {output_bfs2}")
print(f"DFS Output adjList: {output_dfs2}")
print(f"Result Matches Expected (BFS): {compare_graphs(output_bfs2, expected_output2)}")
print(f"Result Matches Expected (DFS): {compare_graphs(output_dfs2, expected_output2)}")
print("-" * 20)


# Test Case 3: Empty Graph
adjList3 = []
print(f"Test Case 3: Input adjList = {adjList3}")
graph3_orig = Node.from_adj_list(adjList3) # This will be None
graph3_cloned_bfs = solver.cloneGraph(graph3_orig)
graph3_cloned_dfs = solver.cloneGraphDFS(graph3_orig)
output_bfs3 = graph3_cloned_bfs.to_adj_list() if graph3_cloned_bfs else []
output_dfs3 = graph3_cloned_dfs.to_adj_list() if graph3_cloned_dfs else []
print(f"BFS Output adjList: {output_bfs3}")
print(f"DFS Output adjList: {output_dfs3}")
print(f"Result Matches Expected (BFS): {compare_graphs(output_bfs3, adjList3)}") # [] == [] -> True
print(f"Result Matches Expected (DFS): {compare_graphs(output_dfs3, adjList3)}") # [] == [] -> True
print("-" * 20)

# Test Case 4: Two nodes connected
adjList4 = [[2], [1]]
print(f"Test Case 4: Input adjList = {adjList4}")
graph4_orig = Node.from_adj_list(adjList4)
graph4_cloned_bfs = solver.cloneGraph(graph4_orig)
graph4_cloned_dfs = solver.cloneGraphDFS(graph4_orig)
output_bfs4 = graph4_cloned_bfs.to_adj_list() if graph4_cloned_bfs else []
output_dfs4 = graph4_cloned_dfs.to_adj_list() if graph4_cloned_dfs else []
print(f"BFS Output adjList: {output_bfs4}")
print(f"DFS Output adjList: {output_dfs4}")
print(f"Result Matches Expected (BFS): {compare_graphs(output_bfs4, adjList4)}")
print(f"Result Matches Expected (DFS): {compare_graphs(output_dfs4, adjList4)}")
print("-" * 20)

# Test Case 5: Line graph
adjList5 = [[2], [1, 3], [2]]
print(f"Test Case 5: Input adjList = {adjList5}")
graph5_orig = Node.from_adj_list(adjList5)
graph5_cloned_bfs = solver.cloneGraph(graph5_orig)
graph5_cloned_dfs = solver.cloneGraphDFS(graph5_orig)
output_bfs5 = graph5_cloned_bfs.to_adj_list() if graph5_cloned_bfs else []
output_dfs5 = graph5_cloned_dfs.to_adj_list() if graph5_cloned_dfs else []
print(f"BFS Output adjList: {output_bfs5}")
print(f"DFS Output adjList: {output_dfs5}")
print(f"Result Matches Expected (BFS): {compare_graphs(output_bfs5, adjList5)}")
print(f"Result Matches Expected (DFS): {compare_graphs(output_dfs5, adjList5)}")
print("-" * 20)
```

**Complexity Analysis:**

*   **Time Complexity:** O(N + E)
    *   N is the number of nodes, and E is the number of edges.
    *   Both BFS and DFS visit each node and each edge exactly once.
    *   Operations like dictionary lookups/insertions and queue/stack operations take O(1) time on average.
*   **Space Complexity:** O(N + E) or O(N)
    *   `cloned_nodes_map`: Stores a mapping for each node, taking O(N) space.
    *   Queue (BFS) or Recursion Stack (DFS): In the worst case (e.g., a line graph or a star graph), this can take up to O(N) space.
    *   The new graph structure itself requires O(N + E) space for the nodes and their neighbor lists.
    *   If we consider only the *auxiliary* space (excluding the space needed for the output clone), the complexity is dominated by the map and the queue/stack, which is O(N). If we include the output space, it's O(N + E).

**4. Test Cases**

*   **Empty Graph:** `adjList = []` -> Input `node` is `None`. Output should be `None`. (Covered in Test Case 3)
*   **Single Node Graph:** `adjList = [[]]` -> Input is a node with `val=1` and no neighbors. Output should be a *new* node with `val=1` and no neighbors. (Covered in Test Case 2)
*   **Two Nodes Connected:** `adjList = [[2], [1]]` -> Output should be a clone of this structure. (Covered in Test Case 4)
*   **Cycle Graph (Example 1):** `adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]` -> Output should be a clone of this structure. (Covered in Test Case 1)
*   **Line Graph:** `adjList = [[2], [1, 3], [2]]` -> Output should be a clone. (Covered in Test Case 5)
*   **Star Graph:** `adjList = [[2, 3, 4], [1], [1], [1]]` -> Output should be a clone. (Can be added as another test case if desired).

The provided Python code includes implementations for both BFS and DFS, along with helper functions to build graphs from adjacency lists and convert them back for easier testing and verification against the expected outputs. The test cases cover the scenarios mentioned above.