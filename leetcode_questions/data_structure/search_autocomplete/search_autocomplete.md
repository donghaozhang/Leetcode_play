# Search Autocomplete System

## Problem

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). The system should:

1. Return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed
2. Sort results by frequency (highest first) and then by ASCII order
3. Store new sentences when the user finishes typing (indicated by '#')

## Examples

**Example 1:**
```
Input:
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]

Output:
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation:
- Input "i": Returns ["i love you", "island", "i love leetcode"]
  - "i love you" (5 times)
  - "island" (3 times)
  - "i love leetcode" (2 times)
  - "iroman" (2 times) is excluded as it's the 4th result

- Input " ": Returns ["i love you", "i love leetcode"]
  - Only two sentences match "i "

- Input "a": Returns []
  - No sentences match "i a"

- Input "#": Returns []
  - Stores "i a" as a new sentence
```

## Constraints

- 1 <= n <= 100 (number of sentences)
- 1 <= sentences[i].length <= 100
- 1 <= times[i] <= 50
- Input character c is lowercase English letter, '#', or space
- Each sentence ends with '#'
- At most 5000 calls to input()

## Approach: Trie with Sentence Tracking

The solution uses a trie data structure with additional tracking of sentences at each node. Here's how it works:

1. **Trie Structure**:
   - Each node contains:
     - Children nodes for each possible character
     - A dictionary mapping sentences to their frequencies

2. **Key Components**:
   - `TrieNode`: Basic trie node with children and sentence frequencies
   - `AutocompleteSystem`: Main class implementing the autocomplete logic
   - `add_to_trie`: Helper method to add sentences with their frequencies
   - `input`: Processes each character and returns matching sentences

3. **Implementation Details**:
   - Store sentences at each node along the path
   - Track current input and node position
   - Sort results by frequency and ASCII order
   - Handle special character '#' for sentence completion

### Python Implementation:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.curr_sentence)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        sorted_sentences = sorted(sentences.items(), key=lambda x: (-x[1], x[0]))
        
        return [s[0] for s in sorted_sentences[:3]]
```

## Complexity Analysis

- **Time Complexity**:
  - Initialization: O(N * L), where N is number of sentences and L is average length
  - Input: O(1) for character processing, O(M log M) for sorting, where M is number of matching sentences
  - Overall: O(N * L) initialization, O(M log M) per input call

- **Space Complexity**:
  - O(N * L) for storing the trie
  - O(L) for current sentence tracking
  - Overall: O(N * L)

## Why This Approach Works

1. **Efficiency**:
   - Trie provides O(1) lookup per character
   - Storing sentences at each node enables quick prefix matching
   - Sorting is only done on matching sentences, not all sentences

2. **Correctness**:
   - Maintains all possible completions at each node
   - Properly handles frequency and ASCII ordering
   - Correctly processes new sentences

3. **Memory Optimization**:
   - Shares common prefixes among sentences
   - Only stores necessary information at each node
   - Efficient handling of large input sets

## Example Walkthrough

For the example input "i":
1. Start at root node
2. Move to 'i' node
3. Get all sentences at this node: ["i love you", "island", "iroman", "i love leetcode"]
4. Sort by frequency and ASCII order
5. Return top 3: ["i love you", "island", "i love leetcode"] 