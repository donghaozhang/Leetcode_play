# Design Tic-Tac-Toe

## Problem

Design a Tic-Tac-Toe game that is played between two players on an n x n grid. The following rules apply:

1. A move is guaranteed to be valid and is placed on an empty block
2. Once a winning condition is reached, no more moves are allowed
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game

Implement the `TicTacToe` class with the following methods:
- `TicTacToe(n)`: Initializes the object with the size of the board n
- `move(row, col, player)`: Places a move at (row, col) for the given player and returns:
  - 0 if there is no winner
  - 1 if player 1 wins
  - 2 if player 2 wins

## Examples

**Example 1:**
```
Input:
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]

Output: [null, 0, 0, 0, 0, 0, 0, 1]

Explanation:
TicTacToe ticTacToe = new TicTacToe(3);
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |
|X|X|X|
```

## Constraints

- 2 <= n <= 100
- player is 1 or 2
- 0 <= row, col < n
- (row, col) are unique for each different call to move
- At most n² calls will be made to move

## Approach: O(1) per Move

The solution uses a clever counting approach to achieve O(1) time complexity per move. Here's how it works:

1. **Tracking Counts**:
   - Maintain counts for each row, column, and diagonal
   - Player 1 adds 1 to the count
   - Player 2 subtracts 1 from the count

2. **Winning Condition**:
   - If any row, column, or diagonal reaches n (for player 1) or -n (for player 2), that player wins
   - This works because we need exactly n moves of the same player in a line to win

### Key Components:

1. **Data Structures**:
   ```python
   self.rows = [0] * n      # Track row sums
   self.cols = [0] * n      # Track column sums
   self.diagonals = [0] * 2 # Track diagonal sums
   ```

2. **Move Implementation**:
   ```python
   def move(self, row: int, col: int, player: int) -> int:
       value = 1 if player == 1 else -1
       
       # Update counts
       self.rows[row] += value
       self.cols[col] += value
       if row == col:
           self.diagonals[0] += value
       if row + col == self.n - 1:
           self.diagonals[1] += value
           
       # Check winning condition
       target = self.n if player == 1 else -self.n
       if (abs(self.rows[row]) == self.n or 
           abs(self.cols[col]) == self.n or 
           abs(self.diagonals[0]) == self.n or 
           abs(self.diagonals[1]) == self.n):
           return player
           
       return 0
   ```

### Python Implementation:

```python
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonals = [0] * 2
        
    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if player == 1 else -1
        
        self.rows[row] += value
        self.cols[col] += value
        
        if row == col:
            self.diagonals[0] += value
        if row + col == self.n - 1:
            self.diagonals[1] += value
            
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diagonals[0]) == self.n or 
            abs(self.diagonals[1]) == self.n):
            return player
            
        return 0
```

## Complexity Analysis

- **Time Complexity**: O(1) per move
  - Each move operation involves a constant number of operations
  - No loops or iterations are needed

- **Space Complexity**: O(n)
  - We need O(n) space for rows and columns
  - O(1) space for diagonals
  - Total space is O(n)

## Why This Approach Works

1. **Efficiency**:
   - The solution achieves O(1) time per move
   - No need to check the entire board after each move
   - Counts are maintained incrementally

2. **Correctness**:
   - The counting approach correctly identifies winning conditions
   - Handles all possible winning patterns (rows, columns, diagonals)
   - Works for any board size n

3. **Memory Optimization**:
   - Only stores necessary information (counts)
   - No need to store the actual board state
   - Space usage is linear in n

## Example Walkthrough

For the example game:
1. Initial state: All counts are 0
2. Move (0,0,1): 
   - row[0] = 1, col[0] = 1, diag[0] = 1
3. Move (0,2,2):
   - row[0] = 0, col[2] = -1
4. Move (2,2,1):
   - row[2] = 1, col[2] = 0, diag[0] = 2
5. Move (1,1,2):
   - row[1] = -1, col[1] = -1, diag[0] = 1, diag[1] = -1
6. Move (2,0,1):
   - row[2] = 2, col[0] = 2
7. Move (1,0,2):
   - row[1] = -2, col[0] = 1
8. Move (2,1,1):
   - row[2] = 3 (wins) 