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

