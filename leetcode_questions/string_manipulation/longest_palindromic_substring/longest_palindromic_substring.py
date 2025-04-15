class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in string s.
        
        Args:
            s: Input string
            
        Returns:
            The longest palindromic substring
        """
        # Initialize a 2D DP table where dp[i][j] indicates if substring s[i:j+1] is a palindrome
        dp = [[False for i in range(len(s))] for i in range(len(s))]
        
        # Single characters are palindromes
        for i in range(len(s)):
            dp[i][i] = True
            
        max_length = 1  # Minimum palindrome length is 1
        start = 0       # Starting index of the longest palindrome
        
        # Check for palindromes of different lengths
        for length in range(2, len(s)+1):
            # Check all possible starting positions
            for i in range(len(s)-length+1):
                end = i + length - 1  # Ending index
                
                # Special case for length 2
                if length == 2:
                    if s[i] == s[end]:
                        dp[i][end] = True
                        if length > max_length:
                            max_length = length
                            start = i
                else:
                    # A substring is a palindrome if:
                    # 1. First and last characters match
                    # 2. The substring between them is a palindrome
                    if s[i] == s[end] and dp[i+1][end-1]:
                        dp[i][end] = True
                        if length > max_length:
                            max_length = length
                            start = i
        
        return s[start:start+max_length]
    
    def longestPalindrome_expand(self, s: str) -> str:
        """
        Alternative approach: Expand around centers.
        This is more efficient than the DP approach.
        
        Args:
            s: Input string
            
        Returns:
            The longest palindromic substring
        """
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
        """
        Helper function to expand around center.
        
        Args:
            s: Input string
            left: Left index
            right: Right index
            
        Returns:
            Length of palindrome expanded from center
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1  # Length of palindrome


def test_longest_palindrome():
    """Test the longestPalindrome function with various examples"""
    solution = Solution()
    
    # Test case 1: Regular case with multiple palindromes
    s1 = "babad"
    result1 = solution.longestPalindrome(s1)
    assert result1 in ["bab", "aba"], f"Expected 'bab' or 'aba', got '{result1}'"
    
    # Test case 2: Single palindrome
    s2 = "cbbd"
    result2 = solution.longestPalindrome(s2)
    assert result2 == "bb", f"Expected 'bb', got '{result2}'"
    
    # Test case 3: Single character
    s3 = "a"
    result3 = solution.longestPalindrome(s3)
    assert result3 == "a", f"Expected 'a', got '{result3}'"
    
    # Test case 4: Entire string is a palindrome
    s4 = "racecar"
    result4 = solution.longestPalindrome(s4)
    assert result4 == "racecar", f"Expected 'racecar', got '{result4}'"
    
    # Test case 5: Multiple palindromes of same length
    s5 = "aacabdkacaa"
    result5 = solution.longestPalindrome(s5)
    assert result5 == "aca", f"Expected 'aca', got '{result5}'"
    
    # Test the expand around center approach
    result1_expand = solution.longestPalindrome_expand(s1)
    assert result1_expand in ["bab", "aba"], f"Expected 'bab' or 'aba', got '{result1_expand}'"
    
    result4_expand = solution.longestPalindrome_expand(s4)
    assert result4_expand == "racecar", f"Expected 'racecar', got '{result4_expand}'"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome() 