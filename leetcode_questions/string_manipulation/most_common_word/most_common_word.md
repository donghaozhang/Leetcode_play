# Most Common Word

## Problem

Given a string `paragraph` and a string array of banned words `banned`, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

## Examples

**Example 1:**
```
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive, punctuation is ignored, and "hit" isn't the answer even though it occurs more because it is banned.
```

**Example 2:**
```
Input: paragraph = "a.", banned = []
Output: "a"
```

## Approach

1. Remove all punctuation by replacing them with spaces.
2. Split the paragraph into individual words.
3. Convert all words to lowercase for case-insensitive counting.
4. Count the frequency of each word using a dictionary (hash map).
5. Find the most frequent word that is not in the banned list.

## Solution

```python
def most_common_word(paragraph: str, banned: List[str]) -> str:
    # Replace all punctuation with spaces
    paragraph = paragraph.replace('!', ' ').replace('?', ' ').replace(';', ' ') \
                        .replace('.', ' ').replace(',', ' ').replace('\'', ' ')
    
    # Count word frequencies
    word_counts = {}
    for word in paragraph.split():
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Find the most frequent non-banned word
    max_count = 0
    result = ''
    for word, count in word_counts.items():
        if word not in banned and count > max_count:
            result = word
            max_count = count
    
    return result
```

## Time Complexity

- O(n + m), where n is the length of the paragraph and m is the number of banned words.
  - Replacing punctuation and splitting the paragraph: O(n)
  - Counting word frequencies: O(n)
  - Checking against banned words list: O(m) assuming efficient lookup (banned list is implemented as a set)

## Space Complexity

- O(n + m):
  - Dictionary to store word counts: O(n) in the worst case where all words are unique
  - Storage for banned words: O(m) for the hash set lookup

## Optimization Notes

1. We could use regular expressions to clean the input more efficiently.
2. Convert the banned list to a set for O(1) lookups.
3. We could combine the splitting and counting in a single pass to improve efficiency.

## Alternative Solution (with regex)

```python
import re
from collections import Counter

def most_common_word(paragraph: str, banned: List[str]) -> str:
    # Convert banned list to set for O(1) lookup
    banned_set = set(banned)
    
    # Use regex to replace all non-alphanumeric characters with spaces and split into words
    words = re.findall(r'\w+', paragraph.lower())
    
    # Count word frequencies and find most common non-banned word
    for word, count in Counter(words).most_common():
        if word not in banned_set:
            return word
            
    return ""  # This should not happen given the problem constraints
``` 