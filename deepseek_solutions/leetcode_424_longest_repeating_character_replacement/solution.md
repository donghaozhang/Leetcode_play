# window_sum.md)
- 最长重复字符替换 / Longest Repeating Character Replacement [LeetCode 424]

## Problem Description

Here is the full description of LeetCode problem #424, "Longest Repeating Character Replacement":

---

**Problem Statement:**

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

**Example 1:**

```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

**Example 2:**

```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

--- 

Let me know if you'd like any clarification or additional help with this problem!

## Solution

### Problem Explanation
The problem asks us to find the length of the longest substring in a given string `s` where we can replace at most `k` characters to make all characters in the substring the same. The key insight is that the longest valid substring will have a length equal to the count of the most frequent character in any window plus `k` (but not exceeding the total window size).

### Approach
1. **Sliding Window Technique**: We'll use a sliding window approach to maintain a window of characters where the number of replacements needed (window length - count of most frequent character) is at most `k`.
2. **Frequency Count**: We'll maintain a frequency dictionary to keep track of the count of each character within the current window.
3. **Window Expansion and Contraction**: 
   - Expand the window by moving the right pointer forward, updating the frequency count.
   - If the number of replacements needed (window length - max frequency) exceeds `k`, move the left pointer forward to shrink the window, updating the frequency count accordingly.
4. **Track Maximum Length**: Throughout the process, keep track of the maximum window length that satisfies the condition.

### Solution Code
```python
def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_length = 0
    left = 0
    max_count = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        
        # If the current window size minus the max count is greater than k,
        # we need to move the left pointer forward
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Explanation
1. **Initialization**: We start with an empty dictionary `count` to keep track of character frequencies, `max_length` to store the result, `left` pointer to mark the start of the window, and `max_count` to store the highest frequency of any character in the current window.
2. **Sliding Window**: As we iterate over the string with the `right` pointer:
   - **Update Frequency**: Increment the count of the current character.
   - **Update Max Count**: Check if the current character's frequency is the highest in the window.
   - **Window Adjustment**: If the number of replacements needed (window size - max frequency) exceeds `k`, move the `left` pointer forward, decrementing the count of the character at `left`.
   - **Update Result**: The window size (`right - left + 1`) is a candidate for `max_length`.
3. **Result**: After processing the entire string, `max_length` holds the length of the longest valid substring.

### Time and Space Complexity
- **Time Complexity**: O(n), where n is the length of the string. We process each character exactly once.
- **Space Complexity**: O(1), since the dictionary holds at most 26 keys (uppercase English letters).

### Test Cases
```python
# Test Case 1
assert characterReplacement("ABAB", 2) == 4

# Test Case 2
assert characterReplacement("AABABBA", 1) == 4

# Test Case 3: Edge case with k=0
assert characterReplacement("AAAAA", 0) == 5

# Test Case 4: Entire string needs replacement
assert characterReplacement("ABCDE", 5) == 5

# Test Case 5: No replacements needed
assert characterReplacement("AABBB", 0) == 3

print("All test cases passed!")
```

### Explanation of Test Cases
1. **Test Case 1**: The entire string can be converted to "BBBB" or "AAAA" with 2 replacements, so the result is 4.
2. **Test Case 2**: The substring "AABBBBA" (after replacing one 'A') has "BBBB" of length 4.
3. **Test Case 3**: With no replacements allowed, the longest substring of 'A's is 5.
4. **Test Case 4**: All characters can be replaced to form any single-character substring of length 5.
5. **Test Case 5**: Without replacements, the longest substring of the same character is "BBB" of length 3.

This approach efficiently finds the solution using a sliding window and frequency count, ensuring optimal performance.