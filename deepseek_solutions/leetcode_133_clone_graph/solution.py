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
