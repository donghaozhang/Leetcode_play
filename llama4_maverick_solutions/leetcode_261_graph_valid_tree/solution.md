# alien_dictionary.md)
- 图是否是树 / Graph Valid Tree [LeetCode 261]

## Problem Description

## 261. Graph Valid Tree

Given `n` nodes labeled from `0` to `n - 1` and a list of `undirected` edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

### Example 1:

Input: `n = 5`, edges = `[[0,1], [0,2], [0,3], [1,4]]`
Output: `true`

### Example 2:

Input: `n = 5`, edges = `[[0,1], [1,2], [2,3], [1,3], [1,4]]`
Output: `false`

### Constraints:

* `n >= 0`
* No duplicate edges
* The input edges are `undirected` (i.e., `[0,1]` is the same as `[1,0]`)

## Solution

## Problem Explanation

The problem requires determining whether a given set of nodes and undirected edges form a valid tree. A valid tree is a connected graph with no cycles.

## Step-by-Step Approach

To solve this problem, we will follow these steps:

1. **Check if the number of edges is correct**: A tree with `n` nodes must have `n - 1` edges. If the number of edges is not `n - 1`, the graph is not a tree.
2. **Create an adjacency list representation of the graph**: We will use a dictionary to store the adjacency list, where each key is a node and its corresponding value is a list of its neighbors.
3. **Perform a depth-first search (DFS) or breadth-first search (BFS) traversal**: We will use BFS in this solution. The traversal will help us check if the graph is connected and if there are any cycles.
4. **Check if the graph is connected**: During the BFS traversal, we will count the number of visited nodes. If the count is equal to `n`, the graph is connected.
5. **Check for cycles**: We will use a `visited` set to keep track of visited nodes. If we encounter a node that is already visited and it's not the parent of the current node, there is a cycle.

## Python Solution

```python
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
```

## Time and Space Complexity Analysis

*   Time complexity: O(n + m), where n is the number of nodes and m is the number of edges. We iterate over the edges to create the adjacency list, and then we perform a BFS traversal that visits each node once.
*   Space complexity: O(n + m), where n is the number of nodes and m is the number of edges. We store the adjacency list, which requires O(n + m) space. The `visited` set and the BFS queue require O(n) space.