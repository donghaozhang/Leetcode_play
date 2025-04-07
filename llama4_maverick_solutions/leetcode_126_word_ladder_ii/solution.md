# letter_combinations.md)

## 图论 (Graph)
- 单词接龙 II / Word Ladder II [LeetCode 126]

## Problem Description

## Word Ladder II
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:</p>

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every <code>s<sub>i</sub></code> for <code>1 <= i <= k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
	<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong> from </em><code>beginWord</code><em> to </em><code>endWord</code><em>, or an empty list if no such sequence exists</em>. Each sequence should be returned as a list of the words <code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> []
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= beginWord.length <= 5</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 <= wordList.length <= 5000</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord != endWord</code></li>
	<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
</ul>

## Solution

## Problem Explanation
The problem requires finding all the shortest transformation sequences from a given `beginWord` to an `endWord` using a dictionary `wordList`. A transformation sequence is a sequence of words where every adjacent pair of words differs by a single letter, and every word in the sequence (except the first one) is in the `wordList`.

## Step-by-Step Approach
1. **Create a set of words**: Convert the `wordList` to a set for efficient lookups.
2. **Check if `endWord` is in `wordList`**: If `endWord` is not in the set, return an empty list as there's no valid transformation sequence.
3. **Perform BFS**: Use Breadth-First Search (BFS) to find the shortest distance from `beginWord` to `endWord`. During BFS, maintain a dictionary to store the neighbors of each word.
4. **Perform DFS**: Use Depth-First Search (DFS) to construct all the shortest transformation sequences from `beginWord` to `endWord` using the neighbors dictionary.
5. **Return the result**: Return all the shortest transformation sequences found by DFS.

## Python Solution
```python
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
```

## Time Complexity Analysis
The time complexity of the solution is O(N \* M^2), where N is the number of words in `wordList` and M is the length of each word.

*   The BFS traversal takes O(N \* M^2) time because for each word, we generate all possible next words by replacing one character at a time, which takes O(M^2) time.
*   The DFS traversal takes O(N \* M) time in the worst case because we visit each word once and construct the transformation sequences.

## Space Complexity Analysis
The space complexity of the solution is O(N \* M), where N is the number of words in `wordList` and M is the length of each word.

*   We use a set to store the words in `wordList`, which takes O(N \* M) space.
*   We use a dictionary to store the neighbors of each word, which takes O(N \* M) space in the worst case.
*   We use a list to store the result, which takes O(N \* M) space in the worst case.