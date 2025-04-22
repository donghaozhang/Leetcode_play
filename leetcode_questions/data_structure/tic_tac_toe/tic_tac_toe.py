class TicTacToe:
    """
    Design a Tic-Tac-Toe game that supports n x n board.
    """
    def __init__(self, n: int):
        """
        Initialize the game board with size n x n.
        
        Args:
            n: Size of the board
        """
        self.n = n
        # Track the sum of moves for each row
        self.rows = [0] * n
        # Track the sum of moves for each column
        self.cols = [0] * n
        # Track the sum of moves for the two diagonals
        self.diagonals = [0] * 2  # [main diagonal, anti-diagonal]
        
    def move(self, row: int, col: int, player: int) -> int:
        """
        Place a move on the board and check if there's a winner.
        
        Args:
            row: Row index (0-based)
            col: Column index (0-based)
            player: Player ID (1 or 2)
            
        Returns:
            0: No winner
            1: Player 1 wins
            2: Player 2 wins
        """
        # Player 1 adds 1, Player 2 subtracts 1
        value = 1 if player == 1 else -1
        
        # Update row and column counts
        self.rows[row] += value
        self.cols[col] += value
        
        # Update diagonal counts if move is on a diagonal
        if row == col:
            self.diagonals[0] += value  # Main diagonal
        if row + col == self.n - 1:
            self.diagonals[1] += value  # Anti-diagonal
            
        # Check if any row, column, or diagonal has n moves of the same player
        target = self.n if player == 1 else -self.n
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diagonals[0]) == self.n or 
            abs(self.diagonals[1]) == self.n):
            return player
            
        return 0

# Test cases
if __name__ == "__main__":
    # Example 1
    tic_tac_toe = TicTacToe(3)
    moves = [
        (0, 0, 1),  # Player 1
        (0, 2, 2),  # Player 2
        (2, 2, 1),  # Player 1
        (1, 1, 2),  # Player 2
        (2, 0, 1),  # Player 1
        (1, 0, 2),  # Player 2
        (2, 1, 1),  # Player 1 wins
    ]
    
    print("Example 1:")
    for move in moves:
        result = tic_tac_toe.move(*move)
        print(f"Move: {move}, Result: {result}")
    
    # Example 2: No winner
    tic_tac_toe = TicTacToe(2)
    moves = [
        (0, 0, 1),
        (0, 1, 2),
        (1, 0, 1),
        (1, 1, 2),
    ]
    
    print("\nExample 2:")
    for move in moves:
        result = tic_tac_toe.move(*move)
        print(f"Move: {move}, Result: {result}") 