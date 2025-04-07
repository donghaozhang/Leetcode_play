# letter_combinations.md)

## 图论 (Graph)
- 单词接龙 II / Word Ladder II [LeetCode 126]

## Problem Description

Here is the full description of LeetCode problem #126, "Word Ladder II," as it appears on LeetCode:

---

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s₁ -> s₂ -> ... -> sₖ` such that:

- Every adjacent pair of words differs by a single letter.
- Every `sᵢ` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sₖ == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`, *or an empty list if no such sequence exists*. Each sequence should be returned as a list of the words `[beginWord, s₁, s₂, ..., sₖ]`.

### Example 1:
**Input:**  
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`  
**Output:**  
`[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]`  
**Explanation:**  
There are 2 shortest transformation sequences:  
"hit" -> "hot" -> "dot" -> "dog" -> "cog"  
"hit" -> "hot" -> "lot" -> "log" -> "cog"  

### Example 2:
**Input:**  
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log"]`  
**Output:**  
`[]`  
**Explanation:**  
The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.  

### Constraints:
- `1 <= beginWord.length <= 5`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 500`
- `wordList[i].length == beginWord.length`
- `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
- `beginWord != endWord`
- All the words in `wordList` are **unique**.

---

## Solution

### Problem Explanation
The problem requires finding all the shortest transformation sequences from `beginWord` to `endWord` using words from a given `wordList`. Each adjacent word in the sequence must differ by exactly one letter, and all intermediate words must be in `wordList`. The solution must return all such shortest sequences or an empty list if no sequences exist.

### Approach
1. **Check for Edge Cases**: Verify if `endWord` is in `wordList`. If not, return an empty list.
2. **BFS for Shortest Paths**: Use Breadth-First Search (BFS) to explore the shortest paths from `beginWord` to `endWord`. BFS is suitable here because it naturally explores all nodes level by level, ensuring that the first time we reach `endWord`, it is via the shortest path.
3. **Track Paths**: During BFS, maintain a dictionary to record the predecessors of each word, i.e., the words that can lead to the current word with a single letter change. This helps in reconstructing the paths later.
4. **Reconstruct Paths**: Once BFS completes, use the predecessors dictionary to backtrack from `endWord` to `beginWord` to construct all possible shortest paths.
5. **Optimization with Level-wise Processing**: Process each level of BFS completely before moving to the next level to ensure that we only consider the shortest paths. This involves tracking visited words per level to avoid revisiting them in the same or subsequent levels, which could lead to longer paths.

### Solution Code
```python
from collections import deque, defaultdict

def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    
    # To help in BFS
    queue = deque()
    queue.append(beginWord)
    
    # To keep track of visited words and their level
    visited = defaultdict(int)
    visited[beginWord] = 0
    
    # To build the adjacency list for the graph
    adjacency = defaultdict(list)
    
    # To know when to stop BFS
    found = False
    level = 0
    
    while queue and not found:
        level_size = len(queue)
        for _ in range(level_size):
            current_word = queue.popleft()
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word == current_word:
                        continue
                    if next_word in wordSet:
                        if next_word not in visited:
                            visited[next_word] = level + 1
                            queue.append(next_word)
                            adjacency[current_word].append(next_word)
                        elif visited[next_word] == level + 1:
                            adjacency[current_word].append(next_word)
                        if next_word == endWord:
                            found = True
        level += 1
    
    # Now, perform DFS to reconstruct all paths from beginWord to endWord
    result = []
    
    def backtrack(node, path):
        if node == endWord:
            result.append(path.copy())
            return
        for neighbor in adjacency[node]:
            if visited[neighbor] == visited[node] + 1:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
    
    backtrack(beginWord, [beginWord])
    return result
```

### Explanation
1. **Initial Checks**: The code first checks if `endWord` is in `wordList`. If not, it returns an empty list immediately.
2. **BFS Setup**: A queue is initialized with `beginWord`, and a dictionary `visited` keeps track of the words encountered and their respective levels (distances from `beginWord`).
3. **BFS Execution**: For each word in the queue, the algorithm generates all possible one-letter transformations. Valid transformations (those in `wordList`) are checked. If a transformation hasn't been visited, it's added to the queue and marked with the current level + 1. The adjacency list is updated to reflect the connection between the current word and its valid transformations.
4. **Path Reconstruction**: After BFS completes, a backtracking function (DFS) is used to reconstruct all paths from `beginWord` to `endWord` using the adjacency list. The `visited` dictionary ensures only shortest paths are considered.
5. **Result Compilation**: The valid paths are collected in the result list and returned.

### Test Cases
```python
# Test Case 1
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))
# Expected Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

# Test Case 2
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(findLadders(beginWord, endWord, wordList))
# Expected Output: []

# Test Case 3
beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]
print(findLadders(beginWord, endWord, wordList))
# Expected Output: [["a", "c"]]
```

### Time and Space Complexity
- **Time Complexity**: 
  - BFS: O(N * L^2), where N is the number of words in `wordList` and L is the length of each word. For each word, we generate L variations, each requiring O(L) time to process.
  - DFS (Backtracking): In the worst case, the number of paths can be exponential, but in practice, it's limited by the shortest path constraint.
- **Space Complexity**: 
  - O(N * L) for storing the adjacency list and visited levels. The result storage can also be O(N * P), where P is the number of paths, but this is output-dependent.