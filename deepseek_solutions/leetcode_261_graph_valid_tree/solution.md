# alien_dictionary.md)
- 图是否是树 / Graph Valid Tree [LeetCode 261]

## Problem Description

Here is the full description of LeetCode problem #261, "Graph Valid Tree":

---

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [a_i, b_i]` indicates that there is an undirected edge between nodes `a_i` and `b_i` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

**Example 1:**

![graph_valid_tree_1](https://assets.leetcode.com/uploads/2021/03/12/tree1-graph.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

**Example 2:**

![graph_valid_tree_2](https://assets.leetcode.com/uploads/2021/03/12/tree2-graph.jpg)

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

**Constraints:**

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= a_i, b_i < n`
- `a_i != b_i`
- There are no self-loops or repeated edges.

--- 

A tree is a connected graph with no cycles. To determine if the given graph is a valid tree, you need to ensure:
1. The graph is fully connected (i.e., there is exactly one connected component).
2. The graph contains no cycles.

## Solution

### Explanation of the Problem

A **valid tree** is defined as a connected acyclic graph. This means:
1. **Connected**: All nodes are reachable from any other node (i.e., there is exactly one connected component).
2. **Acyclic**: There are no cycles in the graph. 

Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges, we need to determine if these edges form a valid tree.

### Approach
To determine if the graph is a valid tree, we can use either **Union-Find (Disjoint Set Union, DSU)** or **Depth-First Search (DFS)**/Breadth-First Search (BFS). Here, we'll use the Union-Find approach for its efficiency and simplicity.

**Union-Find Approach**:
1. **Initialization**: Initialize each node as its own parent.
2. **Union Operations**: For each edge, find the root parents of the two nodes. If they have the same root, adding this edge would form a cycle, so return `false`. Otherwise, union the two sets.
3. **Check Connectivity**: After processing all edges, ensure there is exactly one connected component (i.e., all nodes share the same root or there is exactly one root).

### Solution Code
```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # Path compression
                u = parent[u]
            return u
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return False  # Cycle detected
            parent[root_v] = root_u
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        # Check if all nodes are connected (optional here since edges == n-1 and no cycle implies connected)
        root = find(0)
        for i in range(1, n):
            if find(i) != root:
                return False
        
        return True
```

### Time and Space Complexity Analysis
- **Time Complexity**: 
  - Initialization: O(n)
  - Each `find` operation with path compression is nearly O(1) (amortized).
  - Each `union` operation is also nearly O(1).
  - Processing all edges: O(E * α(n)), where α(n) is the inverse Ackermann function (very slow-growing, effectively constant).
  - Checking connectivity: O(n * α(n)).
  - Overall: O(n + E * α(n)) ≈ O(n + E) for practical purposes.
  
- **Space Complexity**: O(n) for the parent array.

### Test Cases
```python
# Test Case 1: Valid tree
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
assert Solution().validTree(n, edges) == True

# Test Case 2: Contains cycle
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
assert Solution().validTree(n, edges) == False

# Test Case 3: Disconnected graph
n = 4
edges = [[0,1],[2,3]]
assert Solution().validTree(n, edges) == False

# Test Case 4: Single node (trivial tree)
n = 1
edges = []
assert Solution().validTree(n, edges) == True

# Test Case 5: Two nodes, one edge
n = 2
edges = [[0,1]]
assert Solution().validTree(n, edges) == True
```

### Explanation of Test Cases
1. **Test Case 1**: Forms a valid tree with no cycles and all nodes connected.
2. **Test Case 2**: Contains a cycle (1-2-3-1), so it's not a valid tree.
3. **Test Case 3**: Disconnected (two separate components), so it's not a valid tree.
4. **Test Case 4**: A single node with no edges is trivially a valid tree.
5. **Test Case 5**: Two nodes connected by one edge form a valid tree.