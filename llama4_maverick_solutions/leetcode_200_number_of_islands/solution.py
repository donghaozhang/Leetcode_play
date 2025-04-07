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
