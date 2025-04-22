from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Find all words from the given list that exist in the board.
        
        Args:
            board: 2D grid of characters
            words: List of words to search for
            
        Returns:
            List of words found in the board
        """
        WORD_KEY = '$'
        
        # Build the trie
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = []

        def backtracking(row: int, col: int, parent: dict) -> None:
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                # as well as avoiding using set() for results
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    print(f"Example 1: {solution.findWords(board1, words1)}")  # Expected: ["eat","oath"]
    
    # Example 2
    board2 = [
        ["a","b"],
        ["c","d"]
    ]
    words2 = ["abcb"]
    print(f"Example 2: {solution.findWords(board2, words2)}")  # Expected: [] 