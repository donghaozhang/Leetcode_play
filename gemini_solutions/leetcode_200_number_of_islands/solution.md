# clone_graph.md)
- 岛屿数量 / Number of Islands [LeetCode 200]

## Problem Description

```markdown
## 200. Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

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

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 300`
*   `grid[i][j]` is `'0'` or `'1'`.
```

## Solution

Okay, let's break down the "Number of Islands" problem (LeetCode 200).

**1. Explanation of the Problem**

The problem asks us to count the number of "islands" in a 2D grid. The grid contains '1's representing land and '0's representing water. An island is defined as a group of '1's that are connected horizontally or vertically. Any land cell ('1') not connected to another land cell horizontally or vertically forms an island of size one. We are told the grid's edges are surrounded by water, simplifying boundary conditions.

**Example:**
Imagine the grid as a map. We need to count how many separate landmasses exist. If two land cells are adjacent (up, down, left, or right), they belong to the same landmass (island).

```
["1","1","0"]  -> Two '1's connected horizontally form one island.
["1","0","1"]

["1","0","1"]  -> Three '1's, none connected, form three separate islands.
["0","0","0"]
["1","0","0"]
```

**2. Step-by-Step Approach**

The core idea is to traverse the grid and, whenever we find a land cell ('1') that we haven't visited yet as part of a previous island, we know we've found a *new* island. We then need to explore all connected land cells belonging to this *new* island and mark them as visited so we don't count them again.

We can use either Depth-First Search (DFS) or Breadth-First Search (BFS) to explore the connected land cells of an island.

**Algorithm:**

1.  Initialize `island_count = 0`.
2.  Get the dimensions of the grid: `rows = len(grid)` and `cols = len(grid[0])`. Handle the edge case of an empty grid.
3.  Iterate through each cell `(r, c)` of the grid from `r = 0` to `rows - 1` and `c = 0` to `cols - 1`.
4.  **Check for New Island:** If `grid[r][c]` is '1':
    *   This cell is part of an island. Since we are iterating systematically, if we encounter a '1', it must be the first time we are seeing *this specific* island (or a part of it we haven't explored yet).
    *   Increment `island_count` by 1.
    *   **Explore the Island:** Start a traversal (DFS or BFS) from this cell `(r, c)`. The purpose of this traversal is to find all connected '1's belonging to this island and mark them as visited. A common way to mark them is to change their value from '1' to '0' (or another marker like '#'). This prevents recounting cells of the same island.
        *   **DFS Approach:**
            *   Create a recursive function `dfs(row, col)`.
            *   **Base Cases:** If `(row, col)` is out of bounds OR `grid[row][col]` is '0' (water or already visited), return.
            *   **Mark:** Set `grid[row][col] = '0'`.
            *   **Recurse:** Call `dfs` for all four neighbors: `(row+1, col)`, `(row-1, col)`, `(row, col+1)`, `(row, col-1)`.
        *   **BFS Approach:**
            *   Create a queue and add the starting cell `(r, c)`.
            *   Mark the starting cell: `grid[r][c] = '0'`.
            *   While the queue is not empty:
                *   Dequeue a cell `(curr_r, curr_c)`.
                *   For each neighbor `(nr, nc)` of `(curr_r, curr_c)`:
                    *   If the neighbor is within bounds AND `grid[nr][nc]` is '1':
                        *   Mark the neighbor: `grid[nr][nc] = '0'`.
                        *   Enqueue the neighbor `(nr, nc)`.
5.  After iterating through all cells, the final `island_count` holds the total number of islands. Return `island_count`.

**Why does marking visited cells work?**
When we find the first '1' of an island, we start exploring. The DFS/BFS systematically visits *every* '1' connected to the starting point. By changing these '1's to '0's, we ensure that when the main loop later encounters another cell that *was* part of this island, it will now see a '0' and correctly skip it, preventing us from counting the same island multiple times.

**3. Python Solution**

We'll provide the DFS approach as it's often slightly more concise to implement recursively.

```python
from typing import List
import sys

# Increase recursion depth limit for potentially deep DFS paths
# Be cautious with this in production environments, but useful for deep grids in competitive programming.
# sys.setrecursionlimit(10000) # Usually not needed for constraints m, n <= 300

class Solution:
    """
    Solves the Number of Islands problem using Depth First Search (DFS).
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a grid.

        Args:
            grid: A list of lists of strings representing the grid ('1' is land, '0' is water).

        Returns:
            The total number of islands.
        """
        if not grid or not grid[0]:
            return 0  # Handle empty grid or grid with empty rows

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            """
            Performs DFS to mark all connected land cells of an island as visited ('0').
            """
            # Base Cases: Check boundaries and if the cell is water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Mark the current cell as visited by changing it to '0'
            grid[r][c] = '0'

            # Explore all 4 adjacent cells recursively
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find a land cell ('1'), it's the start of a new island
                if grid[r][c] == '1':
                    island_count += 1
                    # Start DFS to find and mark all parts of this island
                    dfs(r, c)

        return island_count

# --- Test Cases ---
solver = Solution()

# Helper function to run tests and print results
def run_test(grid_input, expected_output):
    # Create a deep copy to avoid modifying the original test case grid
    grid_copy = [row[:] for row in grid_input]
    result = solver.numIslands(grid_copy)
    print(f"Input Grid:")
    if not grid_input:
        print("[]")
    else:
        for row in grid_input:
            print(row)
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output:   {result}")
    print(f"Test Passed:     {result == expected_output}")
    print("-" * 30)

# Test Case 1: Example 1
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
run_test(grid1, 1)

# Test Case 2: Example 2
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
run_test(grid2, 3)

# Test Case 3: Empty Grid
grid3 = []
run_test(grid3, 0)

# Test Case 4: Grid with only water
grid4 = [["0","0"],["0","0"]]
run_test(grid4, 0)

# Test Case 5: Grid with only land
grid5 = [["1","1"],["1","1"]]
run_test(grid5, 1)

# Test Case 6: Single cell island
grid6 = [["1"]]
run_test(grid6, 1)

# Test Case 7: Single cell water
grid7 = [["0"]]
run_test(grid7, 0)

# Test Case 8: Disconnected islands
grid8 = [
    ["1","0","1"],
    ["0","0","0"],
    ["1","0","1"]
]
run_test(grid8, 4)

# Test Case 9: Complex island shape
grid9 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
run_test(grid9, 1)

# Test Case 10: Long thin island (tests recursion depth potentially)
grid10 = [["1"] for _ in range(10)] + [["0"]] + [["1"] for _ in range(10)]
run_test(grid10, 2)

```

**Complexity Analysis:**

*   **Time Complexity:** O(m * n), where `m` is the number of rows and `n` is the number of columns.
    *   The outer loops iterate through each cell of the grid exactly once (m * n iterations).
    *   The DFS function visits each land cell ('1') at most once. When `dfs` is called on a cell, it marks it as '0'. Subsequent calls or checks on this cell will return immediately in O(1) time.
    *   Therefore, each cell is processed a constant number of times in total across the main loop and the DFS calls.

*   **Space Complexity:** O(m * n) in the worst case.
    *   This is primarily due to the recursion stack depth for DFS. In the worst-case scenario (e.g., a grid filled with '1's or a long snaking path of '1's), the recursion could go as deep as m * n levels before returning.
    *   If we used BFS, the space complexity would be determined by the maximum size of the queue, which can also be O(m * n) in the worst case, although often closer to O(min(m, n)) for typical island shapes.
    *   Since we modify the grid in place, we don't need an extra `visited` array, but the recursion stack/queue dominates the space complexity.

**4. Test Cases (Included in the Python code above)**

1.  **Example 1:** Standard case with one large island. (Expected: 1)
2.  **Example 2:** Multiple distinct islands. (Expected: 3)
3.  **Empty Grid:** `[]`. (Expected: 0)
4.  **All Water:** `[["0","0"],["0","0"]]`. (Expected: 0)
5.  **All Land:** `[["1","1"],["1","1"]]`. (Expected: 1)
6.  **Single Cell Land:** `[["1"]]`. (Expected: 1)
7.  **Single Cell Water:** `[["0"]]`. (Expected: 0)
8.  **Disconnected Small Islands:** `[["1","0","1"],["0","0","0"],["1","0","1"]]`. (Expected: 4)
9.  **Complex Shape Island:** `[["1","1","1"],["0","1","0"],["1","1","1"]]`. (Expected: 1)
10. **Long Thin Islands:** Tests potential recursion depth limits. (Expected: 2)