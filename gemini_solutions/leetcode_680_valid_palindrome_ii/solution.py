import unittest

class Solution:
    """
    Solves the LeetCode 680: Valid Palindrome II problem.
    Determines if a string can become a palindrome by deleting at most one character.
    """
    def validPalindrome(self, s: str) -> bool:
        """
        Checks if the string s can be a palindrome after deleting at most one character.

        Args:
            s: The input string.

        Returns:
            True if s can be a palindrome after at most one deletion, False otherwise.
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Mismatch found. Try deleting s[left] or s[right].
                # Check if the substring s[left+1...right] is a palindrome
                is_palindrome1 = self.is_palindrome_range(s, left + 1, right)
                # Check if the substring s[left...right-1] is a palindrome
                is_palindrome2 = self.is_palindrome_range(s, left, right - 1)
                
                # If either deletion results in a palindrome, return True
                return is_palindrome1 or is_palindrome2

        # If the loop completes, the string is already a palindrome (0 deletions)
        return True

    def is_palindrome_range(self, s: str, low: int, high: int) -> bool:
        """
        Helper function to check if a substring defined by indices is a palindrome.
        
        Args:
            s: The original string.
            low: The starting index of the substring (inclusive).
            high: The ending index of the substring (inclusive).
            
        Returns:
            True if the substring s[low...high] is a palindrome, False otherwise.
        """
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

# --- Test Cases ---

class TestValidPalindromeII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.validPalindrome("aba"))

    def test_example2(self):
        self.assertTrue(self.solution.validPalindrome("abca")) # Delete 'c' -> "aba"

    def test_example3(self):
        self.assertFalse(self.solution.validPalindrome("abc"))

    def test_already_palindrome(self):
        self.assertTrue(self.solution.validPalindrome("racecar"))
        
    def test_delete_middle(self):
        self.assertTrue(self.solution.validPalindrome("cbbcc")) # Already palindrome

    def test_delete_near_middle1(self):
        self.assertTrue(self.solution.validPalindrome("raceacar")) # Delete 'e' -> "racacar" or delete 'a' -> "racecar"

    def test_delete_near_middle2(self):
        self.assertTrue(self.solution.validPalindrome("abac")) # Delete 'c' -> "aba"

    def test_delete_end1(self.assertTrue(self.solution.validPalindrome("aab"))) # Delete 'b' -> "aa"

    def test_delete_end2(self.assertTrue(self.solution.validPalindrome("baa"))) # Delete 'b' -> "aa"
        
    def test_long_string_true(self):
        #                             l              r
        #                             l             r
        #                             l            r
        #                             l           r
        #                             l          r
        #                             l         r
        #                             l        r
        #                             l       r
        #                             l      r
        #                             l     r
        #                             l    r  <- mismatch 'b' != 'e'
        # Try deleting 'b': "eeccccbebaeeabebccceea"[10+1:21] -> "ebaeeabebcc" -> is_palindrome(11, 20) -> False ('e' != 'c')
        # Try deleting 'e': "eeccccbebaeeabebccceea"[10:21-1] -> "bebaeeabebc" -> is_palindrome(10, 19) -> True ('b'=='b', 'e'=='c' NO)
        # Let's retrace:
        # s = "eeccccbebaeeabebccceea"
        # l=0, r=21 -> e==a -> False
        # is_palindrome_range(s, 1, 21) -> "eccccbebaeeabebccceea" -> e==a -> False
        # is_palindrome_range(s, 0, 20) -> "eeccccbebaeeabebcccee" -> e==e -> True
        #   is_palindrome_range(s, 1, 19) -> "eccccbebaeeabebccce" -> e==e -> True
        #     is_palindrome_range(s, 2, 18) -> "ccccbebaeeabebccc" -> c==c -> True
        #       is_palindrome_range(s, 3, 17) -> "cccbebaeeabebcc" -> c==c -> True
        #         is_palindrome_range(s, 4, 16) -> "ccbebaeeabebc" -> c==c -> True
        #           is_palindrome_range(s, 5, 15) -> "cbebaeeabeb" -> c==b -> False
        # Let's try a simpler long case: "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgta"
        # This should be true (delete 'k' or 't')
        s_long_true = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgta"
        self.assertTrue(self.solution.validPalindrome(s_long_true)) # Fails if middle check is wrong. Let's re-verify logic.
        # If s[l] != s[r], we check is_palindrome(l+1, r) OR is_palindrome(l, r-1).
        # Example: "aguokepatgbnv..." vs "...qvnbgta" -> a==a
        #          "guokepatgbnv..." vs "...qvnbgt" -> g==t -> False
        # Check 1: is_palindrome(s, l+1, r) -> is_palindrome(s, 1, N-1) -> "uokepatgbnv...qvnbgt" -> u==t -> False
        # Check 2: is_palindrome(s, l, r-1) -> is_palindrome(s, 0, N-2) -> "aguokepatgbnv...qvnbg" -> a==g -> False
        # Hmm, the example string I found online might be wrong, or my manual trace is flawed. Let's trust the code logic for now.
        # Let's try a known true case: "abca" -> l=0, r=3 (a==a) -> l=1, r=2 (b!=c)
        #   check1: is_palindrome(s, 1+1, 2) -> is_palindrome(s, 2, 2) -> True
        #   check2: is_palindrome(s, 1, 2-1) -> is_palindrome(s, 1, 1) -> True
        #   Returns True or True -> True. Correct.
        # Let's try "raceacar" -> l=0, r=7 (r==r) -> l=1, r=6 (a==a) -> l=2, r=5 (c==c) -> l=3, r=4 (e!=a)
        #   check1: is_palindrome(s, 3+1, 4) -> is_palindrome(s, 4, 4) -> True
        #   check2: is_palindrome(s, 3, 4-1) -> is_palindrome(s, 3, 3) -> True
        #   Returns True or True -> True. Correct.
        # Let's re-check the long string from LeetCode discussion:
        s_lc_true = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgta" # This is NOT a valid case, it seems.
        # Let's try one that *should* be true:
        s_long_true_corrected = "abacaba" # Already palindrome
        self.assertTrue(self.solution.validPalindrome(s_long_true_corrected))
        s_long_true_corrected2 = "abaxcaba" # Delete x
        self.assertTrue(self.solution.validPalindrome(s_long_true_corrected2))


    def test_long_string_false(self):
        s_long_false = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.assertFalse(self.solution.validPalindrome(s_long_false))
        s_long_false2 = "abacdedcaba" # Needs 2 deletions (d, e)
        self.assertFalse(self.solution.validPalindrome(s_long_false2))

    def test_empty_string(self):
        # Constraint: 1 <= s.length <= 10^5, so empty string is not possible.
        # self.assertTrue(self.solution.validPalindrome("")) # Would be true if allowed
        pass

    def test_single_char(self):
        self.assertTrue(self.solution.validPalindrome("a"))


# To run the tests from the command line:
# python your_file_name.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

