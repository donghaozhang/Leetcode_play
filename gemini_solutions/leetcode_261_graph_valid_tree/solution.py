import collections

class UnionFind:
    """A class implementing the Union-Find (Disjoint Set Union) data structure."""
    def __init__(self, n):
        # Initialize parent array: each node is its own parent initially.
        self.parent = list(range(n))
        # Optional: Keep track of the number of disjoint sets.
        self.num_sets = n

    def find(self, i):
        """Find the root of the set containing element i with path compression."""
        if self.parent[i] == i:
            return i
        # Path compression: make the node point directly to the root.
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """Merge the sets containing elements i and j.
           Returns True if a union was performed (i and j were in different sets).
           Returns False if i and j were already in the same set (cycle detected)."""
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by making root_i point to root_j (can be optimized with union by rank/size)
            self.parent[root_i] = root_j
            # Decrement the number of disjoint sets.
            self.num_sets -= 1
            return True
        else:
            # i and j are already in the same set, adding this edge creates a cycle.
            return False

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """
        Determines if a given graph is a valid tree using Union-Find.

        Args:
            n: The number of nodes (labeled 0 to n-1).
            edges: A list of edges, where each edge is [u, v].

        Returns:
            True if the graph is a valid tree, False otherwise.
        """
        # --- Condition 1: A tree with n nodes must have exactly n - 1 edges ---
        # Handles cases like n=0 (not possible by constraints), n=1 (needs 0 edges).
        if len(edges) != n - 1:
            return False

        # --- Condition 2: The graph must be acyclic ---
        # We use Union-Find to detect cycles.
        # If the graph has n-1 edges and is acyclic, it must also be connected.

        uf = UnionFind(n)

        for u, v in edges:
            # If union returns False, u and v were already connected,
            # meaning adding this edge creates a cycle.
            if not uf.union(u, v):
                return False

        # --- Final Check (Implicit) ---
        # If we processed all n-1 edges without finding a cycle,
        # the graph is acyclic and has the correct number of edges.
        # This implies it's also connected (because a forest with n nodes
        # and n-1 edges must consist of exactly one tree).
        # An explicit connectivity check could be `return uf.num_sets == 1`,
        # but it's redundant given the edge count check.
        return True

# --- Test Cases ---
solver = Solution()

# Example 1: Valid Tree
n1 = 5
edges1 = [[0,1],[0,2],[0,3],[1,4]]
print(f"Input: n = {n1}, edges = {edges1}")
print(f"Output: {solver.validTree(n1, edges1)}") # Expected: True

# Example 2: Cycle Present
n2 = 5
edges2 = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(f"\nInput: n = {n2}, edges = {edges2}")
print(f"Output: {solver.validTree(n2, edges2)}") # Expected: False

# Test Case 3: Disconnected Graph (Fails edge count check)
n3 = 4
edges3 = [[0,1], [2,3]]
print(f"\nInput: n = {n3}, edges = {edges3}")
print(f"Output: {solver.validTree(n3, edges3)}") # Expected: False (len(edges) != n-1)

# Test Case 4: Single Node
n4 = 1
edges4 = []
print(f"\nInput: n = {n4}, edges = {edges4}")
print(f"Output: {solver.validTree(n4, edges4)}") # Expected: True

# Test Case 5: Two Nodes, One Edge
n5 = 2
edges5 = [[0,1]]
print(f"\nInput: n = {n5}, edges = {edges5}")
print(f"Output: {solver.validTree(n5, edges5)}") # Expected: True

# Test Case 6: Disconnected Graph with n-1 edges (Should be caught by cycle check or connectivity check)
# This specific case is impossible if acyclic. If it has n-1 edges and is disconnected, it must be acyclic (a forest).
# If it has n-1 edges and has a cycle, it must also be disconnected.
# The Union-Find approach correctly handles this.
# Example: n=5, edges=[[0,1],[1,2],[0,2],[3,4]] -> Cycle [0,1,2], disconnected node 3,4
n6 = 5
edges6 = [[0,1],[1,2],[0,2],[3,4]] # len(edges) == n-1 = 4
print(f"\nInput: n = {n6}, edges = {edges6}")
print(f"Output: {solver.validTree(n6, edges6)}") # Expected: False (cycle detected at [0,2])

# Test Case 7: Empty graph (n=0 is not allowed by constraints, but if it were)
# n7 = 0
# edges7 = []
# print(f"\nInput: n = {n7}, edges = {edges7}")
# print(f"Output: {solver.validTree(n7, edges7)}") # Expected: True (by convention, maybe?)

# Test Case 8: Graph with correct edge count but disconnected
# This case is caught by the edge count check if the number of components > 1.
# If len(edges) == n-1, and the graph is disconnected, it must be acyclic.
# The Union-Find approach works because if it's disconnected after processing n-1 edges without cycles,
# it would imply num_sets > 1. However, the logic relies on: n-1 edges + acyclic => connected.
n8 = 5
edges8 = [[0,1],[0,2],[3,4]] # len(edges) = 3, n-1 = 4
print(f"\nInput: n = {n8}, edges = {edges8}")
print(f"Output: {solver.validTree(n8, edges8)}") # Expected: False (fails edge count check)

