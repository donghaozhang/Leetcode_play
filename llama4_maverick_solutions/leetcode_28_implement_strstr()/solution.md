# palindrome_ii.md)
- 实现 strStr() / Implement strStr() [LeetCode 28]

## Problem Description

# 28. Find the Index of the First Occurrence in a String
## Description
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

## Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Constraints:
* `1 <= haystack.length, needle.length <= 10^4`
* `haystack` and `needle` consist of only lowercase English characters.

## Solution

## Problem Explanation
The problem requires finding the index of the first occurrence of a given string `needle` in another string `haystack`. If `needle` is not found in `haystack`, the function should return `-1`.

## Step-by-Step Approach
1. **Check if `needle` is empty**: If `needle` is an empty string, it is considered to be a substring of any string, so the function should return `0`.
2. **Iterate over `haystack`**: Iterate over the characters in `haystack`, considering each character as a potential starting point for `needle`.
3. **Compare substrings**: For each starting point in `haystack`, compare the substring of `haystack` starting at that point with `needle`.
4. **Return the index or `-1`**: If a match is found, return the index of the starting point. If no match is found after checking all possible starting points, return `-1`.

## Python Solution
```python
def strStr(haystack: str, needle: str) -> int:
    """
    Returns the index of the first occurrence of `needle` in `haystack`, 
    or `-1` if `needle` is not part of `haystack`.
    
    Args:
    haystack (str): The string to search in.
    needle (str): The string to search for.
    
    Returns:
    int: The index of the first occurrence of `needle` in `haystack`, or `-1`.
    """
    if not needle:  # If needle is empty, return 0
        return 0
    
    needle_len = len(needle)
    haystack_len = len(haystack)
    
    for i in range(haystack_len - needle_len + 1):
        # Check if the substring of haystack starting at i is equal to needle
        if haystack[i:i + needle_len] == needle:
            return i
    
    # If no match is found, return -1
    return -1

# Test cases
print(strStr("sadbutsad", "sad"))  # Expected output: 0
print(strStr("leetcode", "leeto"))  # Expected output: -1
print(strStr("hello", ""))  # Expected output: 0
print(strStr("", "a"))  # Expected output: -1
print(strStr("a", "a"))  # Expected output: 0
print(strStr("abc", "c"))  # Expected output: 2
```

## Time and Space Complexity Analysis
* **Time complexity**: The time complexity of this solution is O(n*m), where n is the length of `haystack` and m is the length of `needle`. This is because in the worst-case scenario, we are comparing every substring of `haystack` of length m with `needle`.
* **Space complexity**: The space complexity is O(1), as we are not using any additional space that scales with the input size. The space used does not grow with the size of the input strings, so it is constant.

## Alternative Solution using Python's built-in `str.find()` method
Python's `str` type has a built-in method `find()` that does exactly what this problem requires. Here's how you can use it:
```python
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Test cases
print(strStr("sadbutsad", "sad"))  # Expected output: 0
print(strStr("leetcode", "leeto"))  # Expected output: -1
print(strStr("hello", ""))  # Expected output: 0
print(strStr("", "a"))  # Expected output: -1
print(strStr("a", "a"))  # Expected output: 0
print(strStr("abc", "c"))  # Expected output: 2
```
This solution is more concise and efficient, as it leverages the optimized implementation of `str.find()` in Python. The time complexity remains O(n*m) in the worst case, but the actual performance is likely to be better due to the optimized C implementation underlying `str.find()`.