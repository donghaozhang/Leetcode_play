from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    """
    Design a search autocomplete system for a search engine.
    """
    def __init__(self, sentences: List[str], times: List[int]):
        """
        Initialize the system with historical sentences and their frequencies.
        
        Args:
            sentences: List of historical sentences
            times: List of corresponding frequencies
        """
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
            
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()
        
    def input(self, c: str) -> List[str]:
        """
        Process input character and return top 3 matching sentences.
        
        Args:
            c: Input character
            
        Returns:
            List of top 3 matching sentences
        """
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
        
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        
        return ans

    def add_to_trie(self, sentence: str, count: int) -> None:
        """
        Add a sentence to the trie with its frequency.
        
        Args:
            sentence: Sentence to add
            count: Frequency of the sentence
        """
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] += count

# Test cases
if __name__ == "__main__":
    # Example 1
    sentences = ["i love you", "island", "iroman", "i love leetcode"]
    times = [5, 3, 2, 2]
    obj = AutocompleteSystem(sentences, times)
    
    print("Example 1:")
    print(obj.input("i"))  # ["i love you", "island", "i love leetcode"]
    print(obj.input(" "))  # ["i love you", "i love leetcode"]
    print(obj.input("a"))  # []
    print(obj.input("#"))  # []
    
    # Example 2: Empty input
    obj = AutocompleteSystem([], [])
    print("\nExample 2:")
    print(obj.input("h"))  # []
    print(obj.input("#"))  # []
    
    # Example 3: Single character input
    obj = AutocompleteSystem(["hello"], [1])
    print("\nExample 3:")
    print(obj.input("h"))  # ["hello"]
    print(obj.input("e"))  # ["hello"]
    print(obj.input("#"))  # [] 