# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

## Examples

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints
- 1 <= s.length <= 1000
- s consists of only digits and English letters.

## Solution Approaches

### 1. Dynamic Programming Approach

The dynamic programming approach uses a 2D array `dp` where `dp[i][j]` indicates whether the substring from index `i` to index `j` is a palindrome.

#### Key Observation
A substring is a palindrome if:
1. The first and last characters are the same
2. The substring without these two characters is also a palindrome

Mathematically: `P(i,j) = (s[i] == s[j]) && P(i+1, j-1)`

#### Algorithm:
1. Initialize a 2D DP table `dp[i][j]` to `False`
2. All substrings of length 1 are palindromes: `dp[i][i] = True`
3. Check all substrings of length 2: `dp[i][i+1] = (s[i] == s[i+1])`
4. For substrings of length 3 or more, use the recurrence relation: `dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`
5. Keep track of the longest palindrome found

#### Time and Space Complexity:
- **Time Complexity**: O(n²) - We need to fill a 2D table of size n×n
- **Space Complexity**: O(n²) - For the DP table

#### Python Implementation:
```python
def longestPalindrome(self, s: str) -> str:
    # Initialize DP table
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    
    # Single characters are palindromes
    for i in range(len(s)):
        dp[i][i] = True
        
    max_length = 1
    start = 0
    
    # Check for palindromes of different lengths
    for length in range(2, len(s)+1):
        for i in range(len(s)-length+1):
            end = i + length - 1
            
            # Special case for length 2
            if length == 2:
                if s[i] == s[end]:
                    dp[i][end] = True
                    if length > max_length:
                        max_length = length
                        start = i
            else:
                # For length 3 or more
                if s[i] == s[end] and dp[i+1][end-1]:
                    dp[i][end] = True
                    if length > max_length:
                        max_length = length
                        start = i
    
    return s[start:start+max_length]
```

### 2. Expand Around Center Approach

This approach is more efficient than the DP approach and works by expanding around each potential center of a palindrome.

#### Key Observation
A palindrome mirrors around its center. There are 2n-1 potential centers for a palindrome (n single-character centers and n-1 between-character centers).

#### Algorithm:
1. For each character or space between characters:
   - Expand around the center while the left and right characters match
   - Keep track of the longest palindrome found
2. Return the longest palindrome

#### Time and Space Complexity:
- **Time Complexity**: O(n²) - In the worst case, we expand around each center for up to n steps
- **Space Complexity**: O(1) - Only a few variables are needed

#### Python Implementation:
```python
def longestPalindrome(self, s: str) -> str:
    if not s or len(s) < 1:
        return ""
        
    start = 0
    end = 0
    
    for i in range(len(s)):
        # Expand around center for odd length palindromes
        len1 = self._expand_around_center(s, i, i)
        # Expand around center for even length palindromes
        len2 = self._expand_around_center(s, i, i + 1)
        # Get the maximum length
        length = max(len1, len2)
        
        # Update if current palindrome is longer
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
            
    return s[start:end+1]

def _expand_around_center(self, s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        
    return right - left - 1  # Length of palindrome
```

### Comparing the Approaches

1. **Dynamic Programming**:
   - Intuitive approach that builds on smaller subproblems
   - Uses more memory (O(n²))
   - Good for educational purposes to understand the structure of the problem

2. **Expand Around Center**:
   - More efficient in practice (still O(n²) time complexity but with less overhead)
   - Uses minimal space (O(1))
   - Often the preferred approach for this problem

## Other Approaches (Not Implemented)

### Manacher's Algorithm
This algorithm can solve the problem in O(n) time, but it's more complex to implement. It cleverly uses the symmetry property of palindromes to avoid redundant comparisons.

## Related Problems
- [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) - Count all palindromic substrings
- [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) - Find the longest subsequence that is a palindrome 