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

