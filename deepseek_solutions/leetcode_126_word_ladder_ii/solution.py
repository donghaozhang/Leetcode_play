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
