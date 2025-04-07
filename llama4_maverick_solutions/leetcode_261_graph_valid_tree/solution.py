from collections import deque, defaultdict

def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    Checks if the given edges form a valid tree.

    Args:
    n (int): The number of nodes.
    edges (list[list[int]]): A list of undirected edges.

    Returns:
    bool: True if the edges form a valid tree, False otherwise.
    """
    # Check if the number of edges is correct
    if len(edges) != n - 1:
        return False

    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS traversal
    visited = set()
    queue = deque([0])
    visited.add(0)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
            # No need to check for cycles explicitly because BFS will not revisit a node if it's already visited
            # and we have already checked if the number of edges is n - 1

    # Check if the graph is connected
    return len(visited) == n


# Test cases
if __name__ == "__main__":
    print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))  # Expected output: True
    print(valid_tree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))  # Expected output: False
    print(valid_tree(0, []))  # Expected output: True
    print(valid_tree(1, []))  # Expected output: True
    print(valid_tree(2, [[0,1]]))  # Expected output: True
    print(valid_tree(2, []))  # Expected output: False
    print(valid_tree(4, [[0,1],[2,3]]))  # Expected output: False
