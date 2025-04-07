# window_sum.md
- 最长重复字符替换 / Longest Repeating Character Replacement [LeetCode 424]

## Problem Description

## Problem Description

### Longest Repeating Character Replacement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return _the length of the longest substring containing the same letter you can get after performing the above operations_.

#### Example 1:

**Input:** s = "ABAB", k = 2
**Output:** 4
**Explanation:** Replace the two 'A's with two 'B's or vice versa.

#### Example 2:

**Input:** s = "AABABBA", k = 1
**Output:** 4
**Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

#### Constraints:

*   `1 <= s.length <= 10^5`
*   `s` consists of only uppercase English letters.
*   `0 <= k <= s.length`

## Solution

**Problem Explanation**

The problem requires finding the length of the longest substring containing the same letter that can be obtained after performing at most `k` operations on a given string `s`. An operation involves changing any character in the string to any other uppercase English character.

### Key Insights

*   The problem can be solved using a sliding window approach.
*   We need to maintain a frequency count of characters within the current window.
*   The maximum frequency count of any character in the window represents the number of characters that don't need to be replaced.
*   The number of characters that need to be replaced is the window size minus the maximum frequency count.
*   If the number of characters to be replaced exceeds `k`, we need to shrink the window.

### Step-by-Step Approach

1.  Initialize a sliding window with two pointers, `left` and `right`, both at the start of the string.
2.  Create a frequency count dictionary `char_count` to store the frequency of characters within the current window.
3.  Iterate through the string using the `right` pointer, expanding the window to the right.
4.  For each character encountered, update its frequency count in `char_count`.
5.  Keep track of the maximum frequency count `max_count` seen so far within the window.
6.  Check if the number of characters to be replaced (`right - left + 1 - max_count`) exceeds `k`.
7.  If it does, shrink the window by moving the `left` pointer to the right and update the frequency count accordingly.
8.  Continue steps 3-7 until the `right` pointer reaches the end of the string.
9.  The maximum length of the window seen during the iteration represents the length of the longest substring containing the same letter after at most `k` operations.

### Python Solution

```python
def characterReplacement(s: str, k: int) -> int:
    """
    Returns the length of the longest substring containing the same letter 
    that can be obtained after performing at most k operations on the given string s.

    Args:
    s (str): The input string.
    k (int): The maximum number of operations allowed.

    Returns:
    int: The length of the longest substring containing the same letter.
    """
    char_count = {}  # Dictionary to store frequency count of characters
    max_count = 0    # Maximum frequency count seen so far
    left = 0         # Left pointer of the sliding window
    max_length = 0   # Maximum length of the window seen so far

    for right in range(len(s)):
        # Update frequency count of the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update maximum frequency count
        max_count = max(max_count, char_count[s[right]])
        
        # Check if the number of characters to be replaced exceeds k
        if right - left + 1 - max_count > k:
            # Shrink the window by moving the left pointer to the right
            char_count[s[left]] -= 1
            left += 1
        
        # Update maximum length of the window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(characterReplacement("ABAB", 2))     # Output: 4
print(characterReplacement("AABABBA", 1))  # Output: 4
print(characterReplacement("ABBB", 2))     # Output: 4
print(characterReplacement("ABC", 1))      # Output: 2
print(characterReplacement("AAAA", 0))     # Output: 4
```

### Time and Space Complexity Analysis

*   **Time Complexity:** O(n), where n is the length of the string `s`. This is because we are iterating through the string once using the `right` pointer.
*   **Space Complexity:** O(1), as the size of the `char_count` dictionary is bounded by the number of unique uppercase English letters (26). Hence, the space complexity is constant.

### Test Cases

The provided Python solution includes test cases to verify its correctness. Additional test cases can be added to cover more scenarios:

*   Edge cases: empty string, single-character string, `k` equals 0
*   Boundary cases: `k` equals the length of the string, string contains all identical characters
*   General cases: string contains a mix of characters, `k` is less than the length of the string

These test cases help ensure the solution is robust and handles different input scenarios correctly.