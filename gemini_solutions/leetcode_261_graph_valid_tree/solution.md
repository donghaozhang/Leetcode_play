# alien_dictionary.md)
- 图是否是树 / Graph Valid Tree [LeetCode 261]

## Problem Description

```markdown
## 261. Graph Valid Tree

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` *if the given graph is a valid tree*, and `false` *otherwise*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)
**Input:** n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)
**Input:** n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
**Output:** false

**Constraints:**

*   `1 <= n <= 2000`
*   `0 <= edges.length <= 5000`
*   `edges[i].length == 2`
*   `0 <= ai, bi < n`
*   `ai != bi`
*   There are no self-loops or repeated edges.
```

## Solution

Okay, let's break down the "Graph Valid Tree" problem.

**1. Explanation of the Problem**

The problem asks us to determine if a given graph, represented by the number of nodes (`n`) and a list of undirected edges (`edges`), forms a valid tree. A valid tree in graph theory has two key properties:

1.  **Connectivity:** All nodes in the graph must be reachable from any other node. There should be only one connected component.
2.  **Acyclicity:** The graph must not contain any cycles.

An important property derived from these two is that a tree with `n` nodes must have exactly `n - 1` edges. This property provides a quick necessary condition to check. If a graph has `n` nodes, satisfying any two of the following conditions guarantees the third, and thus confirms it's a tree:
    *   It is connected.
    *   It is acyclic.
    *   It has exactly `n - 1` edges.

**2. Step-by-Step Approach**

We can leverage the properties of a tree to devise an algorithm. Two common approaches are:

**Approach 1: Using Union-Find (Disjoint Set Union - DSU)**

This approach focuses on checking for cycles and ensuring the correct number of edges.

1.  **Check Edge Count:** A valid tree with `n` nodes must have exactly `n - 1` edges. If `len(edges) != n - 1`, the graph cannot be a tree, so return `False`.
2.  **Initialize Union-Find:** Create a Union-Find data structure for `n` nodes. Initially, each node is in its own set (component).
3.  **Process Edges:** Iterate through the `edges` list. For each edge `[u, v]`:
    *   Use the `find` operation to determine the sets (roots) that `u` and `v` belong to.
    *   If `find(u)` is the same as `find(v)`, it means `u` and `v` are already connected. Adding this edge would create a cycle. Since a tree must be acyclic, return `False`.
    *   If `find(u)` is different from `find(v)`, it means `u` and `v` are in different components. Use the `union` operation to merge the sets containing `u` and `v`.
4.  **Final Check:** If the loop completes without finding any cycles, and we already verified that there are `n - 1` edges, the graph must be connected and acyclic. Therefore, it's a valid tree. Return `True`. (Note: A graph with `n` nodes, `n-1` edges, and no cycles is guaranteed to be connected).

**Approach 2: Using Graph Traversal (BFS or DFS)**

This approach focuses on checking connectivity and the edge count.

1.  **Check Edge Count:** If `len(edges) != n - 1`, return `False`.
2.  **Handle Empty Graph/Single Node:** If `n == 0` or `n == 1`, it's generally considered a valid tree (specifically, if `n=1`, `edges` must be empty, which is `n-1` edges). The edge count check handles this.
3.  **Build Adjacency List:** Create an adjacency list representation of the graph from the `edges`.
4.  **Perform Traversal (e.g., BFS):**
    *   Initialize a `visited` set or boolean array.
    *   Initialize a queue and add a starting node (e.g., node 0) to it. Mark node 0 as visited.
    *   Keep a counter for the number of nodes visited during the traversal.
    *   While the queue is not empty:
        *   Dequeue a node `u`.
        *   Increment the visited node counter.
        *   For each neighbor `v` of `u`:
            *   If `v` has not been visited, mark it as visited and enqueue it.
5.  **Check Connectivity:** After the traversal, if the number of visited nodes equals `n`, it means the graph is connected. Since we already verified it has `n - 1` edges, it must be a tree. Return `True`. Otherwise, the graph is disconnected (a forest), so return `False`.

*Why does checking `n-1` edges and connectivity suffice?* If a graph has `n` nodes, `n-1` edges, and is connected, it cannot contain a cycle. Adding any edge to a tree creates a cycle. Removing any edge from a connected graph with `n-1` edges disconnects it.

Both approaches are valid and efficient. The Union-Find approach is often slightly cleaner for this specific problem as it directly detects cycles while implicitly ensuring connectivity through the edge count check.

**3. Python Solution (using Union-Find)**

```python
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

```

**Complexity Analysis (Union-Find Approach):**

*   **Time Complexity:** O(N + E * α(N))
    *   Initializing the Union-Find structure takes O(N) time.
    *   Iterating through the `E` edges involves `E` calls to `union`. Each `union` operation performs two `find` operations.
    *   With path compression and union by rank/size (though simple union is used here, the complexity is similar in amortized analysis), the `find` and `union` operations take nearly constant time on average, specifically O(α(N)), where α is the extremely slow-growing inverse Ackermann function.
    *   Therefore, the loop takes O(E * α(N)).
    *   The total time complexity is O(N + E * α(N)). Since for a potential tree, E = N - 1, the complexity is effectively O(N * α(N)), which is very close to O(N).
*   **Space Complexity:** O(N)
    *   We need O(N) space for the `parent` array in the Union-Find data structure.

This Union-Find based solution efficiently checks the necessary conditions for a valid tree.