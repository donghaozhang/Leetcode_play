from collections import deque, defaultdict

def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    """
    Finds all the shortest transformation sequences from beginWord to endWord using wordList.

    Args:
    beginWord (str): The starting word.
    endWord (str): The target word.
    wordList (list[str]): A list of words that can be used in the transformation sequence.

    Returns:
    list[list[str]]: A list of lists, where each sublist is a transformation sequence from beginWord to endWord.
    """

    # Create a set of words for efficient lookups
    word_set = set(wordList)
    
    # Check if endWord is in wordList
    if endWord not in word_set:
        return []

    # Initialize the neighbors dictionary
    neighbors = defaultdict(list)

    # Perform BFS to find the shortest distance and neighbors
    queue = deque([beginWord])
    visited = {beginWord}
    found = False
    while queue:
        level_size = len(queue)
        level_visited = set()
        for _ in range(level_size):
            word = queue.popleft()
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i+1:]
                    if next_word == endWord:
                        found = True
                    if next_word in word_set and next_word not in visited:
                        if next_word not in level_visited:
                            queue.append(next_word)
                            level_visited.add(next_word)
                        neighbors[word].append(next_word)
        visited.update(level_visited)
        if found:
            break

    # If endWord is not reachable, return an empty list
    if not found:
        return []

    # Perform DFS to construct the transformation sequences
    result = []
    def dfs(word, path):
        if word == endWord:
            result.append(path[:])
            return
        for neighbor in neighbors[word]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

    dfs(beginWord, [beginWord])
    return result

# Test cases
print(findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

print(findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
# Output: []

print(findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
# Output: [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
