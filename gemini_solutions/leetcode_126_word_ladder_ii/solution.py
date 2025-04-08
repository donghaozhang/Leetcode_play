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