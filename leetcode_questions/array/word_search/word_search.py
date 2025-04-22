from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if a word exists in the grid by moving to adjacent cells.
        
        Args:
            board: 2D grid of characters
            word: String to search for
            
        Returns:
            True if word exists in the grid, False otherwise
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        # Try starting from each cell in the grid
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # No match found after exploring all starting positions
        return False

    def backtrack(self, row: int, col: int, suffix: str) -> bool:
        """
        Backtracking helper function to explore possible paths.
        
        Args:
            row: Current row index
            col: Current column index
            suffix: Remaining part of the word to match
            
        Returns:
            True if the remaining suffix can be matched, False otherwise
        """
        # Base case: entire word has been matched
        if len(suffix) == 0:
            return True

        # Check if current position is valid and matches the first character
        if (row < 0 or row == self.ROWS or 
            col < 0 or col == self.COLS or 
            self.board[row][col] != suffix[0]):
            return False

        # Mark the current cell as visited
        self.board[row][col] = '#'
        
        # Explore all four possible directions
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + row_offset, col + col_offset, suffix[1:]):
                return True

        # Revert the cell back to its original value
        self.board[row][col] = suffix[0]
        
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word1 = "ABCCED"
    print(f"Example 1: {solution.exist(board1, word1)}")  # Expected: True
    
    # Example 2
    board2 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word2 = "SEE"
    print(f"Example 2: {solution.exist(board2, word2)}")  # Expected: True
    
    # Example 3
    board3 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word3 = "ABCB"
    print(f"Example 3: {solution.exist(board3, word3)}")  # Expected: False 