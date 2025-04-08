import string # Not strictly necessary as isalnum() is a string method

class Solution:
    """
    Solves the Valid Palindrome problem using the two-pointer approach.
    """
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome after converting to lowercase
        and removing non-alphanumeric characters.

        Args:
            s: The input string.

        Returns:
            True if the processed string is a palindrome, False otherwise.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1

            # Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters (case-insensitive)
            # This comparison only happens if both pointers landed on alphanumeric chars
            # OR if left >= right after skipping (in which case the outer loop terminates)
            if left < right: # Ensure pointers haven't crossed after skipping
                if s[left].lower() != s[right].lower():
                    return False # Mismatch found

                # Move pointers inward if characters matched
                left += 1
                right -= 1
            # No else needed: if left >= right, the outer loop condition handles termination

        # If the loop completes without returning False, it's a palindrome
        return True

# --- Test Cases ---
def run_tests():
    solution = Solution()

    # Example 1: Basic Palindrome
    s1 = "A man, a plan, a canal: Panama"
    expected1 = True
    result1 = solution.isPalindrome(s1)
    print(f"Test Case 1: Input='{s1}', Output={result1}, Expected={expected1}")
    assert result1 == expected1

    # Example 2: Not a Palindrome
    s2 = "race a car"
    expected2 = False
    result2 = solution.isPalindrome(s2)
    print(f"Test Case 2: Input='{s2}', Output={result2}, Expected={expected2}")
    assert result2 == expected2

    # Example 3: Empty string after filtering
    s3 = " "
    expected3 = True
    result3 = solution.isPalindrome(s3)
    print(f"Test Case 3: Input='{s3}', Output={result3}, Expected={expected3}")
    assert result3 == expected3

    # Test Case 4: Only non-alphanumeric
    s4 = ",.;':"
    expected4 = True
    result4 = solution.isPalindrome(s4)
    print(f"Test Case 4: Input='{s4}', Output={result4}, Expected={expected4}")
    assert result4 == expected4

    # Test Case 5: Single alphanumeric character
    s5 = "a"
    expected5 = True
    result5 = solution.isPalindrome(s5)
    print(f"Test Case 5: Input='{s5}', Output={result5}, Expected={expected5}")
    assert result5 == expected5

    # Test Case 6: Single non-alphanumeric character
    s6 = "."
    expected6 = True
    result6 = solution.isPalindrome(s6)
    print(f"Test Case 6: Input='{s6}', Output={result6}, Expected={expected6}")
    assert result6 == expected6

    # Test Case 7: Numbers involved
    s7 = "0P"
    expected7 = False
    result7 = solution.isPalindrome(s7)
    print(f"Test Case 7: Input='{s7}', Output={result7}, Expected={expected7}")
    assert result7 == expected7

    # Test Case 8: Palindrome with numbers
    s8 = "1b1"
    expected8 = True
    result8 = solution.isPalindrome(s8)
    print(f"Test Case 8: Input='{s8}', Output={result8}, Expected={expected8}")
    assert result8 == expected8

    # Test Case 9: Case difference
    s9 = "RaceCar"
    expected9 = True
    result9 = solution.isPalindrome(s9)
    print(f"Test Case 9: Input='{s9}', Output={result9}, Expected={expected9}")
    assert result9 == expected9

    # Test Case 10: Pointer crossing edge case
    s10 = ".," # Should result in empty string comparison -> True
    expected10 = True
    result10 = solution.isPalindrome(s10)
    print(f"Test Case 10: Input='{s10}', Output={result10}, Expected={expected10}")
    assert result10 == expected10

    # Test Case 11: Pointer crossing edge case 2
    s11 = "a." # Should result in "a" comparison -> True
    expected11 = True
    result11 = solution.isPalindrome(s11)
    print(f"Test Case 11: Input='{s11}', Output={result11}, Expected={expected11}")
    assert result11 == expected11

    print("\nAll test cases passed!")

if __name__ == "__main__":
    run_tests()

