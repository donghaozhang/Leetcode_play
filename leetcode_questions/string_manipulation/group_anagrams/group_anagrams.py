from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.
    
    Args:
        strs: List of strings to be grouped
        
    Returns:
        List of groups, where each group contains strings that are anagrams of each other
    """
    result = []
    anagram_map = {}
    
    for s in strs:
        # Sort each string to create a key for the hash map
        sorted_str = ''.join(sorted(s))
        
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = [s]
        else:
            anagram_map[sorted_str].append(s)
    
    # Convert the hash map values to the result list
    for group in anagram_map.values():
        result.append(group)
    
    return result

# Test cases
if __name__ == "__main__":
    # Example 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs1))  # Expected: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] (order may vary)
    
    # Example 2
    strs2 = [""]
    print(group_anagrams(strs2))  # Expected: [[""]]
    
    # Example 3
    strs3 = ["a"]
    print(group_anagrams(strs3))  # Expected: [["a"]] 