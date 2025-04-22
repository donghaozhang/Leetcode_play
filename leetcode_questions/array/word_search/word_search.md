# Word Search

## Problem

Given an m x n grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples

**Example 1:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Constraints

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

## Approach: Backtracking with DFS

The solution uses a backtracking approach with depth-first search (DFS) to explore all possible paths in the grid. Here's how it works:

1. For each cell in the grid, we start a search if the cell matches the first character of the word.
2. During the search, we mark the current cell as visited (using '#' to prevent revisiting).
3. We explore all four possible directions (up, down, left, right) recursively.
4. If we find a path that matches the entire word, we return true.
5. If a path doesn't work, we backtrack by restoring the original value of the cell.

### Key Components:

1. **Main Function (`exist`):**
   - Initializes the grid dimensions
   - Iterates through each cell as a potential starting point
   - Calls the backtracking function for each starting position

2. **Backtracking Function (`backtrack`):**
   - Base case: when the entire word has been matched
   - Boundary checks and character matching
   - Marks cells as visited and explores all directions
   - Restores the original value when backtracking

### Python Implementation:

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        if len(suffix) == 0:
            return True

        if (row < 0 or row == self.ROWS or 
            col < 0 or col == self.COLS or 
            self.board[row][col] != suffix[0]):
            return False

        self.board[row][col] = '#'
        
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + row_offset, col + col_offset, suffix[1:]):
                return True

        self.board[row][col] = suffix[0]
        return False
```

## Complexity Analysis

- **Time Complexity**: O(N * 3^L)
  - N is the number of cells in the board
  - L is the length of the word
  - For each cell, we explore up to 3 directions (since we can't go back to the previous cell)
  - In the worst case, we might need to explore all possible paths

- **Space Complexity**: O(L)
  - L is the length of the word
  - The space is used by the recursion stack
  - No additional space is used for storing visited cells (we modify the board in-place)

## Optimization and Follow-up

The solution can be optimized further using search pruning techniques:

1. **Early Termination**: Return immediately when a valid path is found.
2. **Character Frequency Check**: Before starting the search, check if the board contains all characters in the word.
3. **Prefix Check**: Use a trie to quickly determine if a path could potentially lead to a solution.
4. **Parallel Search**: For larger boards, consider parallelizing the search from different starting points.

These optimizations become particularly important when dealing with larger boards or longer words, as mentioned in the follow-up question. 