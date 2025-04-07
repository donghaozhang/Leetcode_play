# clone_graph.md)
- 岛屿数量 / Number of Islands [LeetCode 200]

## Problem Description

**200. Number of Islands**

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Solution

### Explanation of the Problem

The problem requires us to count the number of islands in a given 2D binary grid. An island is defined as a group of adjacent '1's (land) connected horizontally or vertically. The grid is surrounded by water, so any '1's on the edges that are connected to other '1's are part of the same island. The goal is to traverse the grid and count all such distinct islands.

### Approach
1. **Iterate through the grid**: We will go through each cell in the grid one by one.
2. **Check for land**: Whenever we encounter a '1', it signifies the start of a new island.
3. **Depth-First Search (DFS) or Breadth-First Search (BFS)**: To explore all connected '1's (land) from the current cell, marking them as visited (by setting them to '0') to avoid counting them again. This process will "sink" the entire island, ensuring it's only counted once.
4. **Increment the count**: Each time we find a new '1' and explore its entire island, we increment our island count.

### Solution Code
```python
from collections import deque

def numIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                grid[r][c] = '0'  # Mark as visited
                queue = deque()
                queue.append((r, c))
                while queue:
                    row, col = queue.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))
    return islands

# Test cases
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid1))  # Output: 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid2))  # Output: 3

grid3 = [
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(grid3))  # Output: 0

grid4 = [
    ["1","0","1","0","1"],
    ["0","1","0","1","0"],
    ["1","0","1","0","1"],
    ["0","1","0","1","0"]
]
print(numIslands(grid4))  # Output: 10
```

### Explanation of the Solution
1. **Initial Checks**: If the grid is empty, return 0 as there are no islands.
2. **Grid Traversal**: Loop through each cell in the grid. For each cell that is '1' (land), increment the island count and initiate a BFS to mark all connected '1's as visited ('0').
3. **BFS Exploration**: For each '1' found, explore its neighboring cells (up, down, left, right). If a neighboring cell is '1', mark it as '0' and add it to the queue to explore its neighbors.
4. **Result**: The count of islands is returned after processing the entire grid.

### Time and Space Complexity
- **Time Complexity**: O(m * n), where m is the number of rows and n is the number of columns. Each cell is visited once.
- **Space Complexity**: O(min(m, n)) in the worst case when the grid is filled with '1's, because the queue can grow up to the minimum of the grid's dimensions due to BFS properties.

### Test Cases
1. **Example 1**: A single large island.
2. **Example 2**: Three separate islands.
3. **Empty Grid**: No islands.
4. **Checkerboard Pattern**: Multiple small islands, each '1' is isolated.

These test cases cover various scenarios including no islands, a single island, multiple islands, and a grid with alternating land and water cells.