# palindrome_ii.md)
- 实现 strStr() / Implement strStr() [LeetCode 28]

## Problem Description

```markdown
## 28. Find the Index of the First Occurrence in a String

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

**Example 2:**

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.

**Constraints:**

*   `1 <= haystack.length, needle.length <= 10^4`
*   `haystack` and `needle` consist of only lowercase English letters.
```

## Solution

Okay, let's tackle the "Implement strStr()" problem (LeetCode 28).

## 1. Explanation of the Problem

The goal is to find the starting index of the *first* occurrence of a given string (`needle`) within another string (`haystack`). If the `needle` string is found as a contiguous substring within the `haystack`, we return the index in `haystack` where this match begins. If the `needle` is not found anywhere within the `haystack`, we should return -1.

For example:
*   If `haystack = "hello"` and `needle = "ll"`, the `needle` "ll" starts at index 2 in `haystack`. So, we return 2.
*   If `haystack = "aaaaa"` and `needle = "bba"`, the `needle` "bba" does not appear anywhere in `haystack`. So, we return -1.
*   If `haystack = "sadbutsad"` and `needle = "sad"`, the `needle` "sad" appears twice, starting at index 0 and index 6. We need the *first* occurrence, so we return 0.

The constraints mention that both strings consist of lowercase English letters and have lengths between 1 and 10^4.

## 2. Step-by-Step Approach (Naive Sliding Window)

The most straightforward approach is to "slide" the `needle` across the `haystack` and check for a match at each possible starting position.

1.  **Get Lengths:** Determine the lengths of the `haystack` (let's call it `n`) and the `needle` (let's call it `m`).
2.  **Handle Edge Cases:**
    *   If `m` (length of `needle`) is 0, the problem statement constraints say `needle.length >= 1`, so we don't need to handle the empty needle case based *strictly* on the constraints. (Standard `strStr` often returns 0 for an empty needle).
    *   If `m > n`, it's impossible for the `needle` to be a substring of the `haystack`, so we can immediately return -1.
3.  **Iterate Through Possible Starting Positions:** We need to check every possible starting index `i` in the `haystack` where the `needle` could potentially begin. The `needle` has length `m`. If we start checking at index `i`, the substring we compare against `needle` will be `haystack[i : i + m]`. The last possible valid starting index `i` is when `i + m` equals `n` (the length of `haystack`). Therefore, `i` can range from 0 up to `n - m`.
4.  **Check for Match:** For each starting index `i` from 0 to `n - m`:
    *   Extract the substring of `haystack` starting at `i` with length `m`. In Python, this is `haystack[i : i + m]`.
    *   Compare this substring with the `needle`.
    *   If they are identical, we have found the first occurrence (since we are iterating from the beginning). Return the current index `i`.
5.  **No Match Found:** If the loop completes without finding any match, it means the `needle` is not present in the `haystack`. Return -1.

**Example Walkthrough:** `haystack = "sadbutsad"`, `needle = "sad"`
*   `n = 9`, `m = 3`
*   Possible starting indices `i`: 0, 1, 2, 3, 4, 5, 6 (`n - m = 9 - 3 = 6`)
*   `i = 0`: `haystack[0:3]` is "sad". Does "sad" == "sad"? Yes. Return `i = 0`.

**Example Walkthrough:** `haystack = "leetcode"`, `needle = "leeto"`
*   `n = 8`, `m = 5`
*   Possible starting indices `i`: 0, 1, 2, 3 (`n - m = 8 - 5 = 3`)
*   `i = 0`: `haystack[0:5]` is "leetc". Does "leetc" == "leeto"? No.
*   `i = 1`: `haystack[1:6]` is "eetco". Does "eetco" == "leeto"? No.
*   `i = 2`: `haystack[2:7]` is "etcod". Does "etcod" == "leeto"? No.
*   `i = 3`: `haystack[3:8]` is "tcode". Does "tcode" == "leeto"? No.
*   Loop finishes. Return -1.

## 3. Python Solution

```python
import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the index of the first occurrence of needle in haystack.

        Args:
            haystack: The string to search within.
            needle: The string to search for.

        Returns:
            The index of the first occurrence, or -1 if not found.
        """
        n = len(haystack)
        m = len(needle)

        # Per constraints, m >= 1.
        # If needle is longer than haystack, it cannot be found.
        if m > n:
            return -1

        # Iterate through possible starting indices in haystack.
        # The last possible starting index is n - m.
        # range(stop) goes up to stop - 1, so we need range(n - m + 1).
        for i in range(n - m + 1):
            # Check if the substring of haystack starting at i matches needle
            # Using string slicing is concise and often optimized in Python.
            if haystack[i : i + m] == needle:
                return i

            # Alternative: Manual character-by-character comparison
            # match = True
            # for j in range(m):
            #     if haystack[i + j] != needle[j]:
            #         match = False
            #         break
            # if match:
            #     return i

        # If the loop completes without finding a match
        return -1

# --- Test Cases ---

class TestStrStr(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.strStr("sadbutsad", "sad"), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.strStr("leetcode", "leeto"), -1)

    def test_needle_at_end(self):
        self.assertEqual(self.solution.strStr("hello", "ll"), 2)

    def test_needle_not_found(self):
        self.assertEqual(self.solution.strStr("aaaaa", "bba"), -1)

    def test_needle_longer_than_haystack(self):
        self.assertEqual(self.solution.strStr("a", "aa"), -1)

    def test_haystack_equals_needle(self):
        self.assertEqual(self.solution.strStr("abc", "abc"), 0)

    def test_single_char_needle(self):
        self.assertEqual(self.solution.strStr("mississippi", "p"), 8)

    def test_long_strings_match(self):
        haystack = "a" * 10000 + "b"
        needle = "a" * 5000 + "b"
        self.assertEqual(self.solution.strStr(haystack, needle), 5000)

    def test_long_strings_no_match(self):
        haystack = "a" * 10000
        needle = "a" * 5000 + "b"
        self.assertEqual(self.solution.strStr(haystack, needle), -1)

    def test_partial_match_then_mismatch(self):
        self.assertEqual(self.solution.strStr("mississippi", "issip"), 4)

    def test_partial_match_at_end(self):
         self.assertEqual(self.solution.strStr("abcabdabcabd", "abcabd"), 0) # Found at start
         self.assertEqual(self.solution.strStr("abcabcabd", "abcabd"), 3) # Found later


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

```

**Explanation of the Code:**

1.  `n` and `m` store the lengths of `haystack` and `needle`.
2.  The `if m > n:` check handles the case where the `needle` cannot possibly fit in the `haystack`.
3.  The `for i in range(n - m + 1):` loop iterates through all valid starting positions `i` for the `needle` within the `haystack`.
4.  `haystack[i : i + m]` creates a substring of `haystack` starting at index `i` and having the same length as `needle`.
5.  `if haystack[i : i + m] == needle:` compares this substring with the `needle`. If they match, `i` is the starting index of the first occurrence, so we return `i`.
6.  If the loop finishes without returning, it means no match was found, so we return -1.
7.  The `unittest` framework is used to provide comprehensive test cases covering various scenarios.

**Complexity Analysis:**

*   **Time Complexity:** O(N * M)
    *   The outer loop runs `n - m + 1` times, which is O(N) in the worst case (when `m` is small or constant).
    *   Inside the loop, slicing `haystack[i : i + m]` takes O(M) time.
    *   Comparing the slice with `needle` also takes O(M) time in the worst case.
    *   Therefore, the total time complexity is O((N - M) * M) ≈ O(N * M).
*   **Space Complexity:** O(M) or O(1)
    *   If we consider the space used by the string slice `haystack[i : i + m]`, the space complexity is O(M).
    *   However, Python's string slicing might be optimized internally, and if the comparison is done character by character without explicitly creating a new string object for the slice every time (or if garbage collection is efficient), the auxiliary space complexity could be considered closer to O(1). For typical interview analysis, stating O(M) due to the slice is safer, or O(1) if you explicitly implement character-by-character comparison within the loop (like the commented-out alternative).

**Optimization Note (KMP Algorithm):**

While the O(N*M) solution is simple and often sufficient for typical constraints like these, a more advanced algorithm called the Knuth-Morris-Pratt (KMP) algorithm can solve this problem in O(N + M) time complexity by preprocessing the `needle` to avoid redundant comparisons after a mismatch. The space complexity for KMP is O(M) to store the preprocessing information (the LPS array). Implementing KMP is more complex but significantly faster for very large strings.

## 4. Test Cases

The provided Python solution includes a `unittest` suite with the following test cases:

1.  `test_example_1`: `haystack = "sadbutsad", needle = "sad"` -> Expected: 0
2.  `test_example_2`: `haystack = "leetcode", needle = "leeto"` -> Expected: -1
3.  `test_needle_at_end`: `haystack = "hello", needle = "ll"` -> Expected: 2
4.  `test_needle_not_found`: `haystack = "aaaaa", needle = "bba"` -> Expected: -1
5.  `test_needle_longer_than_haystack`: `haystack = "a", needle = "aa"` -> Expected: -1
6.  `test_haystack_equals_needle`: `haystack = "abc", needle = "abc"` -> Expected: 0
7.  `test_single_char_needle`: `haystack = "mississippi", needle = "p"` -> Expected: 8
8.  `test_long_strings_match`: Tests with longer strings where a match exists.
9.  `test_long_strings_no_match`: Tests with longer strings where no match exists.
10. `test_partial_match_then_mismatch`: `haystack = "mississippi", needle = "issip"` -> Expected: 4 (ensures it handles partial matches correctly).
11. `test_partial_match_at_end`: `haystack = "abcabdabcabd", needle = "abcabd"` -> Expected: 0. `haystack = "abcabcabd", needle = "abcabd"` -> Expected: 3. (Handles overlapping potential matches).