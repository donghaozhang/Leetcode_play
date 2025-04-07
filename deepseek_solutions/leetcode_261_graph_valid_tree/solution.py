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
