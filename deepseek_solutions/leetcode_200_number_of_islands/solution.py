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
