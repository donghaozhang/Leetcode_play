# letter_combinations.md)

## 图论 (Graph)
- 单词接龙 II / Word Ladder II [LeetCode 126]

## Problem Description

```markdown
## 126. Word Ladder II

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

*   Every adjacent pair of words differs by a single letter.
*   Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
*   `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`, *or an empty list if no such sequence exists. Each sequence should be returned as a list of the words* `[beginWord, s1, s2, ..., sk]`.

**Example 1:**

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

**Example 2:**

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

**Constraints:**

*   `1 <= beginWord.length <= 5`
*   `endWord.length == beginWord.length`
*   `1 <= wordList.length <= 1000`
*   `wordList[i].length == beginWord.length`
*   `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
*   `beginWord != endWord`
*   All the words in `wordList` are **unique**.
*   The sum of all `wordList[i].length` will be sum of `beginWord.length` * `wordList.length`.
```

## Solution

Okay, let's break down the Word Ladder II problem (LeetCode 126).

**1. Problem Explanation**

The goal is to find *all* the sequences of words that transform a given `beginWord` into a given `endWord` with the minimum possible number of steps (shortest sequences). The rules for transformation are:

1.  **One Letter Difference:** Each adjacent pair of words in the sequence must differ by exactly one letter.
2.  **Valid Words:** All words in the sequence (except possibly `beginWord`) must exist in the provided `wordList`.
3.  **Target:** The sequence must end with `endWord`.

If no such transformation sequence exists, we should return an empty list. If multiple shortest sequences exist, we need to return all of them.

**Example:**
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`

Shortest sequences have length 5:
*   `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`
*   `"hit" -> "hot" -> "lot" -> "log" -> "cog"`

**2. Step-by-Step Approach**

This problem asks for *all shortest paths* in an implicit graph where words are nodes and an edge exists if two words differ by one letter. This suggests a two-phase approach:

**Phase 1: Find Shortest Path Length and Build Parent Pointers using BFS**

*   **Why BFS?** Breadth-First Search (BFS) is ideal for finding the shortest path in an unweighted graph.
*   **Level-by-Level Exploration:** We need to explore the graph level by level to ensure we find the shortest paths first.
*   **Tracking Distances:** We'll maintain a dictionary `distances` mapping each reachable word to its shortest distance (number of transformations) from `beginWord`.
*   **Tracking Parents:** Since we need to reconstruct *all* shortest paths, a single parent pointer isn't enough. A word might be reachable via multiple shortest paths. We'll use a dictionary `parents` where `parents[word]` stores a list of all words from which `word` can be reached in a shortest path step (i.e., `parent` such that `distance[word] = distance[parent] + 1`).
*   **Efficient Neighbor Finding:** Generating neighbors by changing one letter at a time (`O(L*26)`) and checking against the `wordList` (using a set for `O(1)` lookup) is more efficient than comparing against every word in the list (`O(N*L)`).
*   **Avoiding Cycles and Longer Paths:**
    *   Use the `distances` map to avoid revisiting words already assigned a shortest distance.
    *   Crucially, process the BFS level by level. Only consider adding a neighbor `next_word` if:
        1.  It hasn't been visited (`next_word` not in `distances`). In this case, record its distance, add its parent, and enqueue it.
        2.  It *has* been visited, but we found another path *of the same shortest length* (`distances[next_word] == current_distance + 1`). In this case, just add the current word as another parent to `next_word`. Don't re-enqueue.
    *   To optimize further and prevent exploring longer paths unnecessarily, remove words from the `wordSet` once *all* paths reaching them *at their shortest distance* have been processed (i.e., after processing a full level of the BFS).

**Phase 2: Reconstruct All Shortest Paths using DFS (Backtracking)**

*   **Starting Point:** If the BFS completes without finding `endWord` (i.e., `endWord` is not in `parents` or `distances`), return `[]`.
*   **Backward Traversal:** Start a Depth-First Search (DFS) or backtracking function from `endWord`.
*   **Path Building:** The DFS function will take the current `word` and the `current_path` built so far (from `endWord` backward).
*   **Recursive Step:** For the current `word`, iterate through all its `parents` (obtained from the `parents` map built during BFS). Recursively call the DFS for each `parent`, passing the updated path.
*   **Base Case:** When the DFS reaches `beginWord`, a complete shortest path has been found. Add the *reverse* of the `current_path` (since we built it backward) to the final results list.
*   **Backtracking:** After exploring all paths from a parent, remove the current word from the path to allow exploration of other branches.

**Algorithm Summary:**

1.  Initialize `wordSet = set(wordList)`. Check if `endWord` is in `wordSet`. If not, return `[]`.
2.  Initialize `distances = {beginWord: 0}`, `parents = defaultdict(list)`, `queue = deque([beginWord])`.
3.  Perform level-by-level BFS:
    *   While `queue` is not empty and `endWord` has not been reached at the *minimum* distance found so far:
        *   Process all nodes currently in the `queue` (one level). Keep track of `visited_this_level`.
        *   For each `current_word`:
            *   Generate all possible `next_word` neighbors (differ by one letter).
            *   If `next_word == endWord`: Mark `found = True`. Add `current_word` to `parents[endWord]`.
            *   If `next_word` in `wordSet`:
                *   If `next_word` not in `distances`: Add it (`distances`, `parents`, `queue`, `visited_this_level`).
                *   Else if `distances[next_word] == distances[current_word] + 1`: Add `current_word` to `parents[next_word]`.
        *   Remove `visited_this_level` words from `wordSet`.
        *   If `found` is true after processing the level, break the BFS (we've processed all nodes at the shortest path level).
4.  Initialize `results = []`.
5.  If `endWord` was found (e.g., `endWord` in `parents`):
    *   Define a recursive `backtrack(word, current_path)` function.
    *   Base case: `word == beginWord`. Add `reversed(current_path + [beginWord])` to `results`.
    *   Recursive step: For `p` in `parents[word]`, call `backtrack(p, current_path + [word])`. (Or modify `current_path` in place with append/pop for efficiency).
    *   Start the backtracking: `backtrack(endWord, [])` (adjust path building based on implementation).
6.  Return `results`.

**3. Python Solution**

```python
from collections import deque, defaultdict
import string # More concise way to get alphabet

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        """
        Finds all shortest transformation sequences from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: A list of valid words for transformation.

        Returns:
            A list of all shortest transformation sequences, or an empty list
            if no such sequence exists.
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # --- Phase 1: BFS to find shortest distance and build parent graph ---
        distances = {beginWord: 0}  # Stores shortest distance from beginWord
        parents = defaultdict(list) # Stores parent nodes in shortest paths
        queue = deque([beginWord])
        found = False # Flag to indicate if endWord has been reached
        word_len = len(beginWord)
        # alphabet = string.ascii_lowercase # Use string.ascii_lowercase

        # Level-by-level BFS
        while queue and not found:
            level_size = len(queue)
            # Words visited at the current distance level.
            # We remove them from wordSet *after* processing the level
            # to allow multiple paths of the same shortest length.
            visited_this_level = set()

            for _ in range(level_size):
                current_word = queue.popleft()
                current_dist = distances[current_word]

                # Generate neighbors
                for i in range(word_len):
                    original_char = current_word[i]
                    for char_code in range(ord('a'), ord('z') + 1):
                        char = chr(char_code)
                        if char == original_char:
                            continue

                        next_word = current_word[:i] + char + current_word[i+1:]

                        # Check if the neighbor is the endWord
                        if next_word == endWord:
                            # If endWord is reached, record parent and set found flag.
                            # We continue processing the rest of this level
                            # to find all paths reaching endWord at this shortest distance.
                            parents[endWord].append(current_word)
                            found = True
                            # No need to check distance for endWord here, BFS guarantees shortest

                        # Check if the neighbor is a valid word in the set
                        # and potentially part of a shortest path
                        if next_word in wordSet:
                            # If not visited yet (no distance recorded)
                            if next_word not in distances:
                                distances[next_word] = current_dist + 1
                                parents[next_word].append(current_word)
                                # Add to queue only if not already added in this level
                                if next_word not in visited_this_level:
                                     queue.append(next_word)
                                     visited_this_level.add(next_word)
                            # If visited, but reachable via another path of the SAME shortest length
                            elif distances[next_word] == current_dist + 1:
                                parents[next_word].append(current_word)
                                # Do not add to queue again, already processed or will be processed

            # Remove words visited at this level from the main wordSet
            # This prevents using them in longer paths later
            wordSet -= visited_this_level

        # --- Phase 2: DFS (Backtracking) to reconstruct paths ---
        results = []
        # If endWord was never reached by BFS
        if not found: # Equivalent to checking if endWord in parents
            return []

        # Backtracking function to build paths from endWord to beginWord
        def backtrack(word: str, current_path: list[str]):
            # Prepend word to the current path being built
            current_path.append(word)

            if word == beginWord:
                # Base case: reached the beginning, add the reversed path
                results.append(current_path[::-1])
            else:
                # Continue backtracking through parents
                # Check if word exists in parents (it should if found=True)
                if word in parents:
                    for parent_word in parents[word]:
                        backtrack(parent_word, current_path)

            # Backtrack: remove the current word before returning
            current_path.pop()

        # Start backtracking from the endWord
        backtrack(endWord, [])

        return results

# --- Test Cases ---
solver = Solution()

# Example 1
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot","dot","dog","lot","log","cog"]
expected1 = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
output1 = solver.findLadders(beginWord1, endWord1, wordList1)
# Sort lists within lists and the outer list for comparison
output1_sorted = sorted([sorted(path) for path in output1])
expected1_sorted = sorted([sorted(path) for path in expected1])
print(f"Test Case 1:")
print(f"Input: beginWord='{beginWord1}', endWord='{endWord1}', wordList={wordList1}")
print(f"Output: {output1}")
print(f"Expected: {expected1}")
print(f"Correct: {output1_sorted == expected1_sorted}")
print("-" * 20)


# Example 2
beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot","dot","dog","lot","log"]
expected2 = []
output2 = solver.findLadders(beginWord2, endWord2, wordList2)
print(f"Test Case 2:")
print(f"Input: beginWord='{beginWord2}', endWord='{endWord2}', wordList={wordList2}")
print(f"Output: {output2}")
print(f"Expected: {expected2}")
print(f"Correct: {output2 == expected2}")
print("-" * 20)

# Test Case 3: No path exists
beginWord3 = "a"
endWord3 = "c"
wordList3 = ["a","b","c"]
expected3 = [["a","c"]] # Correction: Should be [["a", "c"]] if b is not needed, but problem implies transformation through list? Let's assume direct is allowed if dist=1. If not, need 'b'. Let's re-read. "Every si for 1 <= i <= k is in wordList". This means intermediate steps must be in wordList. endWord must also be in wordList. beginWord doesn't need to be.
# Rerun with correct understanding:
beginWord3 = "a"
endWord3 = "c"
wordList3 = ["b", "c"] # 'a' -> 'c' is not possible via wordList
expected3 = []
output3 = solver.findLadders(beginWord3, endWord3, wordList3)
print(f"Test Case 3 (No Path):")
print(f"Input: beginWord='{beginWord3}', endWord='{endWord3}', wordList={wordList3}")
print(f"Output: {output3}")
print(f"Expected: {expected3}")
print(f"Correct: {output3 == expected3}")
print("-" * 20)

# Test Case 4: Direct path
beginWord4 = "hot"
endWord4 = "dot"
wordList4 = ["hot", "dot", "dog"]
expected4 = [["hot", "dot"]]
output4 = solver.findLadders(beginWord4, endWord4, wordList4)
output4_sorted = sorted([sorted(path) for path in output4])
expected4_sorted = sorted([sorted(path) for path in expected4])
print(f"Test Case 4 (Direct Path):")
print(f"Input: beginWord='{beginWord4}', endWord='{endWord4}', wordList={wordList4}")
print(f"Output: {output4}")
print(f"Expected: {expected4}")
print(f"Correct: {output4_sorted == expected4_sorted}")
print("-" * 20)


# Test Case 5: More complex paths
beginWord5 = "red"
endWord5 = "tax"
wordList5 = ["ted","tex","red","tax","tad","den","rex","pee"]
# red -> ted -> tex -> tax (length 4)
# red -> rex -> tex -> tax (length 4)
expected5 = [["red","ted","tex","tax"], ["red","rex","tex","tax"]]
output5 = solver.findLadders(beginWord5, endWord5, wordList5)
output5_sorted = sorted([sorted(path) for path in output5])
expected5_sorted = sorted([sorted(path) for path in expected5])
print(f"Test Case 5 (Multiple Shortest):")
print(f"Input: beginWord='{beginWord5}', endWord='{endWord5}', wordList={wordList5}")
print(f"Output: {output5}")
print(f"Expected: {expected5}")
print(f"Correct: {output5_sorted == expected5_sorted}")
print("-" * 20)

# Test Case 6: beginWord in wordList
beginWord6 = "hot"
endWord6 = "dog"
wordList6 = ["hot", "dot", "dog"]
expected6 = [["hot", "dot", "dog"]]
output6 = solver.findLadders(beginWord6, endWord6, wordList6)
output6_sorted = sorted([sorted(path) for path in output6])
expected6_sorted = sorted([sorted(path) for path in expected6])
print(f"Test Case 6 (beginWord in wordList):")
print(f"Input: beginWord='{beginWord6}', endWord='{endWord6}', wordList={wordList6}")
print(f"Output: {output6}")
print(f"Expected: {expected6}")
print(f"Correct: {output6_sorted == expected6_sorted}")
print("-" * 20)


**Time and Space Complexity Analysis**

*   **N:** Number of words in `wordList`.
*   **L:** Length of each word.
*   **A:** Size of the alphabet (26).

*   **Time Complexity:**
    *   Preprocessing (`set(wordList)`): O(N * L)
    *   BFS:
        *   Neighbor generation for a word: O(L * A) = O(L) since A=26 is constant.
        *   In the worst case, we might visit each word and generate its neighbors. The number of edges in the implicit graph can be up to O(N^2), but we explore efficiently. The dominant factor is visiting nodes and generating neighbors. Total BFS time is roughly O(N * L^2) (N nodes, each taking O(L*L) for neighbor generation O(L*A) and string slicing O(L), plus set lookups O(L)). A tighter bound considering neighbor generation and set lookups is O(N * L * A) = **O(N * L)**.
        *   Building the `parents` map happens within BFS.
    *   DFS (Backtracking):
        *   The number of shortest paths (K) can be exponential in the worst case relative to N.
        *   The DFS traverses the graph defined by the `parents` map. The time complexity is proportional to the total number of nodes and edges in all the shortest paths found. This can be roughly estimated as O(K * path\_length * L) where path\_length is the shortest path length (at most N). So, potentially **O(K * N * L)** in the worst case for path reconstruction.
    *   Overall: **O(N * L + K * N * L)**. The BFS part O(N*L) is often dominated by the DFS part if K is large.

*   **Space Complexity:**
    *   `wordSet`: O(N * L)
    *   `distances`: O(N * L)
    *   `parents`: O(N * L) in the worst case (stores parent pointers for potentially many nodes)
    *   `queue`: O(N * L)
    *   DFS recursion stack: O(path\_length * L) = O(N * L) in the worst case.
    *   `results` list: O(K * path\_length * L) = O(K * N * L) to store the output paths.
    *   Overall (excluding result storage): **O(N * L)**.
    *   Overall (including result storage): **O(N * L + K * N * L)**.

**4. Test Cases**

See the test cases included within the Python code block above. They cover:
*   The examples provided in the problem description.
*   Cases where no path exists (`endWord` not in `wordList`, or no valid transformation sequence).
*   Cases with a direct transformation (length 2 path).
*   Cases with multiple shortest paths.
*   Cases where `beginWord` is also present in `wordList`.