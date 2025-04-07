# clone_graph.md)
- 岛屿数量 / Number of Islands [LeetCode 200]

## Problem Description

## Number of Islands
Given an `m x n` 2D binary grid `grid` which represents a map of `'1's` (land) and `'0's` (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Example 1:
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2:
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Constraints:
* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.

## Solution

## Problem Explanation
The problem requires counting the number of islands in a given 2D binary grid. An island is defined as a group of connected '1's (land) surrounded by '0's (water). The grid is `m x n` in size, where `1 <= m, n <= 300`, and each cell contains either '0' or '1'.

## Step-by-Step Approach
1. **Understand the Grid and Islands**: Recognize that the grid is a 2D array where '1' represents land and '0' represents water. Islands are formed by '1's connected horizontally or vertically.
   
2. **Choose a Traversal Method**: To count islands, we need to traverse the grid. Since islands are defined by connectivity, a graph traversal algorithm like Depth-First Search (DFS) is suitable.

3. **Implement DFS**:
   - When a '1' is encountered, perform a DFS to mark all connected '1's as visited.
   - Use a mechanism to mark visited cells to avoid revisiting them.

4. **Count Islands**:
   - Increment the island count each time a '1' is encountered that has not been visited yet.
   - Perform DFS from this '1' to mark all connected '1's as visited.

5. **Handle Grid Edges**:
   - Be mindful of grid boundaries to avoid index out-of-range errors during DFS.

## Python Solution

```python
def numIslands(grid):
    """
    Counts the number of islands in a given 2D binary grid.

    Args:
    grid (List[List[str]]): A 2D grid of '1's and '0's representing land and water respectively.

    Returns:
    int: The number of islands in the grid.
    """
    if not grid:
        return 0

    count = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        # Check if the current cell is within the grid and is a '1'
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
            # Mark the cell as visited by setting it to '0'
            grid[r][c] = '0'
            # Recursively visit neighboring cells
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # Found a new island, increment count and mark all connected '1's as visited
                count += 1
                dfs(r, c)

    return count

# Test Cases
if __name__ == "__main__":
    # Example 1:
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(numIslands(grid1))  # Expected Output: 1

    # Example 2:
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(numIslands(grid2))  # Expected Output: 3

    # Edge Case: Empty Grid
    grid3 = []
    print(numIslands(grid3))  # Expected Output: 0

    # Edge Case: Grid with all '0's
    grid4 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    print(numIslands(grid4))  # Expected Output: 0

    # Edge Case: Grid with all '1's
    grid5 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    print(numIslands(grid5))  # Expected Output: 1
```

## Time and Space Complexity Analysis

- **Time Complexity**: O(m*n) where m is the number of rows and n is the number of columns in the grid. This is because in the worst-case scenario (when the grid is filled with '1's), we might end up visiting every cell once.

- **Space Complexity**: O(m*n) in the worst case due to the recursive call stack used by DFS. This occurs when the grid is filled with '1's and the DFS traversal goes through all cells in the grid. However, in practice, for grids that are not fully connected, the space complexity will be less.