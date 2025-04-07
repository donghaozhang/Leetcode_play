# palindrome.md
- 验证回文串 II / Valid Palindrome II [LeetCode 680]

## Problem Description

## Valid Palindrome II

Given a non-empty string `s`, you may delete at most one character. Judge whether you can make it a palindrome.

### Example 1:
**Input:** "aba"
**Output:** True

### Example 2:
**Input:** "abca"
**Output:** True
**Explanation:** You could delete the character 'c'.

### Note:
1. The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

## Solution

## Problem Explanation
The problem requires determining whether a given non-empty string can be made into a palindrome by deleting at most one character. A palindrome is a string that reads the same backward as forward.

## Step-by-Step Approach
1. **Initialize two pointers**: Start by initializing two pointers, one at the beginning of the string (`left`) and one at the end (`right`).
2. **Compare characters**: Compare the characters at the `left` and `right` pointers. If they are equal, move both pointers towards the center of the string.
3. **Handle mismatch**: If the characters at `left` and `right` are not equal, we have two possibilities to consider:
   - **Delete the character at `left`**: Check if the remaining substring (after deleting the character at `left`) is a palindrome.
   - **Delete the character at `right`**: Check if the remaining substring (after deleting the character at `right`) is a palindrome.
4. **Return result**: If either of the above possibilities results in a palindrome, return `True`. If neither results in a palindrome, return `False`.

## Python Solution
```python
def validPalindrome(s: str) -> bool:
    """
    Determines whether a given string can be made into a palindrome by deleting at most one character.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string can be made into a palindrome, False otherwise.
    """

    def is_palindrome(left, right):
        """
        Helper function to check if a substring is a palindrome.

        Args:
        left (int): The left index of the substring.
        right (int): The right index of the substring.

        Returns:
        bool: True if the substring is a palindrome, False otherwise.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check if deleting either character makes the string a palindrome
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("a", True),
        ("ab", True),
        ("aa", True),
        ("", False),  # Empty string is not considered valid input according to the problem statement
    ]

    for s, expected in test_cases:
        if s == "":  # Skip empty string as per problem constraints
            continue
        result = validPalindrome(s)
        print(f"Input: {s}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test case failed for input: {s}"
    print("All test cases passed.")
```

## Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the string. In the worst-case scenario, we might end up scanning the entire string once or twice (when checking for palindrome after deleting a character).
- **Space Complexity**: O(1), as we are using a constant amount of space to store the pointers and variables, regardless of the input size.

## Test Cases
The provided Python solution includes test cases to verify its correctness. These test cases cover various scenarios, including:
- Palindromes ("aba")
- Strings that can be made into palindromes by deleting one character ("abca")
- Strings that cannot be made into palindromes by deleting one character ("abc")
- Edge cases like single-character strings ("a") and two-character strings ("ab", "aa")