# palindrome_ii.md)
- 实现 strStr() / Implement strStr() [LeetCode 28]

## Problem Description

Here is the full description of LeetCode problem #28, "Find the Index of the First Occurrence in a String":

---

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

### Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

### Constraints:
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

--- 

Let me know if you'd like any further clarification or assistance!

## Solution

### Problem Explanation
The problem requires us to find the first occurrence of the string `needle` in the string `haystack`. If `needle` is found in `haystack`, we return the starting index of the first occurrence; otherwise, we return -1. 

For example:
- If `haystack` is "sadbutsad" and `needle` is "sad", the first occurrence starts at index 0, so we return 0.
- If `haystack` is "leetcode" and `needle` is "leeto", there is no occurrence, so we return -1.

### Approach
1. **Edge Cases Handling**: 
   - If `needle` is an empty string, return 0 (though constraints say lengths are at least 1).
   - If the length of `needle` is greater than `haystack`, return -1 immediately since it's impossible for `needle` to be a substring.

2. **Sliding Window Check**:
   - Iterate through `haystack` from index 0 to `len(haystack) - len(needle)`.
   - For each index `i`, check if the substring `haystack[i:i+len(needle)]` matches `needle`.
   - If a match is found, return `i`.
   - If no match is found after all iterations, return -1.

### Solution Code
```python
def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    len_haystack = len(haystack)
    len_needle = len(needle)
    if len_needle > len_haystack:
        return -1
    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i+len_needle] == needle:
            return i
    return -1

# Test cases
print(strStr("sadbutsad", "sad"))      # Output: 0
print(strStr("leetcode", "leeto"))     # Output: -1
print(strStr("hello", "ll"))           # Output: 2
print(strStr("aaaaa", "bba"))          # Output: -1
print(strStr("a", "a"))                # Output: 0
print(strStr("abc", "c"))              # Output: 2
```

### Explanation
- **Edge Cases Handling**: The function first checks if `needle` is an empty string (though constraints prevent this). Then, it checks if `needle` is longer than `haystack`, in which case it's impossible to find the substring, so it returns -1.
- **Sliding Window Check**: The loop runs from index 0 to `len(haystack) - len(needle)`. For each index `i`, it checks if the substring starting at `i` of length `len(needle)` matches `needle`. If found, it returns `i` immediately. If the loop completes without finding a match, it returns -1.
- **Test Cases**: The provided test cases cover various scenarios including the first occurrence, no occurrence, exact match, and partial matches to ensure correctness.

### Time and Space Complexity
- **Time Complexity**: O((n - m) * m), where n is the length of `haystack` and m is the length of `needle`. In the worst case, for each of the (n - m + 1) starting positions, we compare m characters.
- **Space Complexity**: O(1), as no additional space is used apart from a few variables for indices and lengths.

This approach efficiently checks for the first occurrence of `needle` in `haystack` by leveraging a sliding window technique.