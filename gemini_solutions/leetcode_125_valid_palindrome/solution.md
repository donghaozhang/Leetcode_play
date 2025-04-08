# reverse_string.md)
- 判断回文串 / Valid Palindrome [LeetCode 125]

## Problem Description

```markdown
## 125. Valid Palindrome

A phrase is a **palindrome** if after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

**Example 3:**

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

**Constraints:**

*   `1 <= s.length <= 2 * 10^5`
*   `s` consists only of printable ASCII characters.
```

## Solution

Okay, let's break down the "Valid Palindrome" problem.

**1. Explanation of the Problem**

The goal is to determine if a given string `s` is a palindrome, but with specific preprocessing steps:
1.  **Case Insensitivity:** Treat uppercase and lowercase letters as the same (e.g., 'A' is equivalent to 'a').
2.  **Alphanumeric Only:** Ignore any characters that are not letters (a-z, A-Z) or numbers (0-9). Punctuation, spaces, etc., should be removed.

After applying these two steps, we check if the resulting string reads the same forwards and backward. An empty string resulting from the filtering process is considered a valid palindrome.

**2. Step-by-Step Approach (Two-Pointer Method)**

This is generally the most efficient approach in terms of space complexity.

1.  **Initialization:** Set up two pointers: `left` starting at the beginning of the string (index 0) and `right` starting at the end of the string (index `len(s) - 1`).
2.  **Iteration:** Use a `while` loop that continues as long as `left` is less than `right`.
3.  **Skip Non-Alphanumeric (Left):** Inside the loop, move the `left` pointer forward (`left += 1`) as long as `left < right` *and* the character `s[left]` is *not* alphanumeric. The `left < right` condition prevents the left pointer from crossing the right pointer unnecessarily.
4.  **Skip Non-Alphanumeric (Right):** Similarly, move the `right` pointer backward (`right -= 1`) as long as `left < right` *and* the character `s[right]` is *not* alphanumeric.
5.  **Compare Characters:** Once both `left` and `right` point to alphanumeric characters (or the loop condition `left < right` becomes false):
    *   Compare `s[left].lower()` and `s[right].lower()`. We convert both to lowercase to handle case insensitivity.
    *   If they are *not* equal, the string is not a palindrome, so return `False`.
6.  **Move Pointers:** If the characters match, move the pointers towards the center: `left += 1` and `right -= 1`.
7.  **Palindrome Confirmation:** If the `while` loop completes without finding any mismatches (meaning `left` eventually becomes equal to or greater than `right`), it means all relevant character pairs matched. Return `True`.

**Alternative Approach (Filter and Compare):**

1.  Create a new string or list.
2.  Iterate through the original string `s`.
3.  For each character, check if it's alphanumeric.
4.  If it is, convert it to lowercase and append it to the new string/list.
5.  After iterating through the whole string, check if the new filtered string is equal to its reverse.

*Self-Correction:* While the filter-and-compare approach is conceptually simpler, it uses extra space (O(N)) to store the filtered string. The two-pointer approach is generally preferred for its O(1) space complexity. We will implement the two-pointer approach.

**3. Python Solution**

```python
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

```

**Complexity Analysis:**

*   **Time Complexity:** O(N), where N is the length of the input string `s`. In the worst-case scenario, each pointer (`left` and `right`) traverses approximately half of the string. The `isalnum()` and `lower()` operations take constant time per character. Therefore, the total time is proportional to the length of the string.
*   **Space Complexity:** O(1). We are only using a fixed amount of extra space for the `left` and `right` pointers and temporary variables for comparison. We are not creating any new data structures whose size depends on the input string length.

**4. Test Cases (Included in the Python code above)**

1.  `s = "A man, a plan, a canal: Panama"` -> `True` (Standard example)
2.  `s = "race a car"` -> `False` (Standard non-palindrome)
3.  `s = " "` -> `True` (Empty string after filtering)
4.  `s = ",.;':"` -> `True` (Only non-alphanumeric, results in empty string)
5.  `s = "a"` -> `True` (Single alphanumeric character)
6.  `s = "."` -> `True` (Single non-alphanumeric character)
7.  `s = "0P"` -> `False` (Simple non-palindrome with number)
8.  `s = "1b1"` -> `True` (Palindrome with numbers)
9.  `s = "RaceCar"` -> `True` (Case difference)
10. `s = ",."` -> `True` (Edge case where pointers skip everything)
11. `s = "a."` -> `True` (Edge case where one pointer skips)