# Word Search II

## Problem

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Examples

**Example 1:**
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2:**
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

## Approach: Trie + Backtracking

The solution uses a combination of Trie data structure and backtracking to efficiently find all words in the board. Here's how it works:

1. **Build a Trie**: First, we build a trie from all the words in the input list. This helps us efficiently search for prefixes and words.

2. **Backtracking Search**: For each cell in the board, we perform a backtracking search:
   - If the current cell's character exists in the trie, we start exploring
   - We mark visited cells to prevent reuse
   - We explore all four directions (up, down, left, right)
   - When we find a complete word, we add it to our results
   - We restore the board after each exploration

3. **Optimizations**:
   - We remove matched words from the trie to avoid duplicates
   - We prune empty branches from the trie to reduce search space
   - We use in-place board modification to track visited cells

### Key Components:

1. **Trie Construction**:
   - Each node represents a character
   - A special key ('$') marks the end of a word
   - The trie helps us quickly determine if a path could lead to a valid word

2. **Backtracking Function**:
   - Explores all possible paths from a given cell
   - Maintains the current state in the trie
   - Handles visited cells and path restoration
   - Collects matched words

### Python Implementation:

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        # Build the trie
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row: int, col: int, parent: dict) -> None:
            letter = board[row][col]
            currNode = parent[letter]
            
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)
            
            board[row][col] = '#'
            
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            board[row][col] = letter
        
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords
```

## Complexity Analysis

- **Time Complexity**: O(M * N * 4^L)
  - M and N are the dimensions of the board
  - L is the maximum length of words
  - 4^L represents the maximum number of paths to explore
  - The trie helps reduce the actual search space significantly

- **Space Complexity**: O(N)
  - N is the total number of letters in the dictionary
  - Space is used for the trie data structure
  - Additional O(L) space for the recursion stack

## Why This Approach Works

1. **Efficient Prefix Search**: The trie allows us to quickly determine if a path could lead to a valid word, pruning invalid paths early.

2. **Avoiding Duplicates**: By removing matched words from the trie, we ensure each word is found only once.

3. **Memory Efficiency**: We use the board itself to track visited cells, avoiding additional space for a visited matrix.

4. **Pruning**: Empty branches are removed from the trie, reducing the search space for subsequent searches.

This approach is particularly effective for large boards and word lists, as it efficiently prunes the search space and avoids redundant searches. 