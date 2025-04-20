# Group Anagrams

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```

## Approach

The key insight for this problem is that anagrams will have the same characters, just in a different order. We can use this property to group them efficiently.

1. Create a hash map where:
   - The keys are the sorted versions of each string (since anagrams will have the same sorted string)
   - The values are lists of original strings that, when sorted, match the key

2. Iterate through each string in the input array:
   - Sort the characters of the current string
   - Use the sorted string as a key to add the original string to the appropriate group in the hash map

3. Return the values of the hash map as the result

## Solution

```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
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
```

## Time Complexity

- O(n * k log k) where:
  - n is the number of strings in the input array
  - k is the maximum length of a string in the input array
  - For each string, we sort its characters which takes O(k log k) time

## Space Complexity

- O(n * k) for storing all strings in the hash map

## Optimizations

For strings with only lowercase English letters (as specified in the constraints), we could optimize further by using character counts instead of sorting. This would change the time complexity to O(n * k):

```python
def group_anagrams(strs: List[str]) -> List[List[str]]:
    result = {}
    
    for s in strs:
        # Create a count array for all 26 lowercase letters
        count = [0] * 26
        
        # Count the frequency of each character
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Use the count array as a key
        # Since lists can't be used as dictionary keys, convert to tuple
        key = tuple(count)
        
        if key not in result:
            result[key] = [s]
        else:
            result[key].append(s)
    
    return list(result.values())
```

This optimization works well when the input strings contain only a limited set of characters (like lowercase English letters) and would be more efficient for large strings where sorting would be more expensive. 