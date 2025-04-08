# palindrome.md)
- 验证回文串 II / Valid Palindrome II [LeetCode 680]

## Problem Description

**Problem Description:**

Given a string `s`, return `true` if the `s` can be palindrome after deleting **at most one** character from it.

**Example 1:**
```
Input: s = "aba"
Output: true
```

**Example 2:**
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3:**
```
Input: s = "abc"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Solution

### Explanation of the Problem

The problem asks us to determine if a given string can be converted into a palindrome by removing **at most one character**. A palindrome is a string that reads the same forwards and backwards. 

For example:
- "aba" is already a palindrome, so no deletion is needed (returns `true`).
- "abca" can be made into a palindrome by deleting 'c' (returns `true`).
- "abc" cannot be made into a palindrome by deleting just one character (returns `false`).

### Approach to Solve the Problem

1. **Two Pointers Technique**: Use two pointers, one at the start (`left`) and one at the end (`right`) of the string.
2. **Check for Mismatch**: Move the pointers towards the center while the characters at the pointers match.
3. **Handle Mismatch**: If a mismatch is found, check the two possibilities:
   - Skip the character at the `left` pointer and check if the substring from `left+1` to `right` is a palindrome.
   - Skip the character at the `right` pointer and check if the substring from `left` to `right-1` is a palindrome.
4. **Return Result**: If either of the above possibilities results in a palindrome, return `true`; otherwise, return `false`.

### Solution Code

```python
def validPalindrome(s: str) -> bool:
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check both possibilities: skip left or skip right
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -= 1
    return True

# Test cases
print(validPalindrome("aba"))     # Output: True
print(validPalindrome("abca"))    # Output: True
print(validPalindrome("abc"))     # Output: False
print(validPalindrome("deeee"))   # Output: True
print(validPalindrome("racecar")) # Output: True
print(validPalindrome("abcd"))    # Output: False
```

### Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the length of the string. In the worst case, we might check the entire string twice (once for each pointer when a mismatch occurs), but this still simplifies to O(N).
- **Space Complexity**: O(1). We are using constant extra space for the pointers and the helper function does not use additional space proportional to the input size.

### Test Cases

1. **Input**: "aba"  
   **Output**: `True`  
   **Explanation**: The string is already a palindrome.

2. **Input**: "abca"  
   **Output**: `True`  
   **Explanation**: Deleting 'c' makes it "aba", which is a palindrome.

3. **Input**: "abc"  
   **Output**: `False`  
   **Explanation**: No single deletion can make this a palindrome.

4. **Input**: "deeee"  
   **Output**: `True`  
   **Explanation**: Deleting 'd' makes it "eeee", which is a palindrome.

5. **Input**: "racecar"  
   **Output**: `True`  
   **Explanation**: The string is already a palindrome.

6. **Input**: "abcd"  
   **Output**: `False`  
   **Explanation**: No single deletion can make this a palindrome.

These test cases cover various scenarios including already palindromic strings, strings that can be made palindromic with one deletion, and strings that cannot be made palindromic with one deletion.