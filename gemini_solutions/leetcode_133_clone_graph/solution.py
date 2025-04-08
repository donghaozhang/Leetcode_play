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
