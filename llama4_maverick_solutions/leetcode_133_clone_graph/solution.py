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
