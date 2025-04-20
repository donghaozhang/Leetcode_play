# Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Approach: Sliding Window

We can solve this problem using the sliding window technique:

1. Maintain a window of characters that contains no duplicates.
2. Use a hash map to track the last index where each character appeared.
3. As we iterate through the string, we expand the window to the right.
4. If we encounter a character that's already in our window, we shrink the window from the left to exclude the previous occurrence of this character.
5. Keep track of the maximum window size seen so far.

## Solution

```python
def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last index of each character
    char_index = {}
    
    # Result to store the max length
    max_length = 0
    
    # Starting index of current non-repeating substring
    start = 0
    
    # Iterate through the string
    for i, char in enumerate(s):
        # If character is already in the current window
        if char in char_index:
            # Update start to be after the last occurrence of the current character
            # We use max to handle cases where the previous occurrence is before the current window
            start = max(start, char_index[char] + 1)
        
        # Update the last seen index of the character
        char_index[char] = i
        
        # Update the maximum length
        max_length = max(max_length, i - start + 1)
    
    return max_length
```

## Time Complexity

- O(n): We only need to iterate through the string once, where n is the length of the string.

## Space Complexity

- O(min(m, n)): We need a hash map to store the characters, where m is the size of the character set and n is the length of the string. In the worst case, all characters in the string are unique, so the space complexity is bounded by the minimum of m and n.

## Walkthrough with Example

Let's trace through the algorithm with the input `s = "abcabcbb"`:

1. Initialize `char_index = {}`, `max_length = 0`, `start = 0`
2. Iterate through the string:
   - i=0, char='a':
     - 'a' is not in char_index
     - char_index = {'a': 0}, max_length = 1, start = 0
   - i=1, char='b':
     - 'b' is not in char_index
     - char_index = {'a': 0, 'b': 1}, max_length = 2, start = 0
   - i=2, char='c':
     - 'c' is not in char_index
     - char_index = {'a': 0, 'b': 1, 'c': 2}, max_length = 3, start = 0
   - i=3, char='a':
     - 'a' is in char_index at index 0
     - start = max(0, 0+1) = 1
     - char_index = {'a': 3, 'b': 1, 'c': 2}, max_length = 3, start = 1
   - i=4, char='b':
     - 'b' is in char_index at index 1
     - start = max(1, 1+1) = 2
     - char_index = {'a': 3, 'b': 4, 'c': 2}, max_length = 3, start = 2
   - i=5, char='c':
     - 'c' is in char_index at index 2
     - start = max(2, 2+1) = 3
     - char_index = {'a': 3, 'b': 4, 'c': 5}, max_length = 3, start = 3
   - i=6, char='b':
     - 'b' is in char_index at index 4
     - start = max(3, 4+1) = 5
     - char_index = {'a': 3, 'b': 6, 'c': 5}, max_length = 3, start = 5
   - i=7, char='b':
     - 'b' is in char_index at index 6
     - start = max(5, 6+1) = 7
     - char_index = {'a': 3, 'b': 7, 'c': 5}, max_length = 3, start = 7

3. Return max_length = 3

## Special Case: Empty String

For an empty string (`s = ""`), the algorithm will not enter the loop, and the max_length will remain 0, which is the correct answer.

## Why We Use max() for the Start Index

When we find a repeating character, we update the start position to be after the last occurrence of this character. However, we need to ensure that we don't move the start position backward (which would be incorrect). 

For example, with `s = "abba"`:
- When we encounter the second 'b', we update start to be after the first 'b'
- When we encounter the second 'a', we need to make sure we don't move start back to after the first 'a', because that would include a repeated 'b'

The `max(start, char_index[char] + 1)` ensures that we only move the start position forward. 