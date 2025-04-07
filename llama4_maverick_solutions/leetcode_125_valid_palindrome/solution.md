# reverse_string.md)
- 判断回文串 / Valid Palindrome [LeetCode 125]

## Problem Description

## Valid Palindrome

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a palindrome*, or `false` otherwise.

### Example 1:

**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.

### Example 2:

**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.

### Example 3:

**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

### Constraints:

*   `1 <= s.length <= 2 * 10^5`
*   `s` consists only of printable ASCII characters.

## Solution

## Problem Explanation

The problem requires determining whether a given string is a palindrome or not. A palindrome is a phrase that reads the same forward and backward after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters.

The input is a string `s`, and the output is a boolean value indicating whether the string is a palindrome or not.

Key constraints and edge cases:

*   The input string `s` consists only of printable ASCII characters.
*   The length of the input string `s` is between 1 and 2 \* 10^5.
*   The input string `s` may contain non-alphanumeric characters, which should be ignored when checking for palindrome.
*   The input string `s` may be empty after removing non-alphanumeric characters, in which case it is considered a palindrome.

## Step-by-Step Approach

1.  **Preprocess the input string**: Convert the input string to lowercase and remove non-alphanumeric characters.
2.  **Compare characters from both ends**: Initialize two pointers, one at the start and one at the end of the preprocessed string.
3.  **Check for mismatch**: Compare the characters at the current positions of the two pointers. If they are different, the string is not a palindrome.
4.  **Move pointers towards the center**: If the characters match, move the pointers towards the center of the string.
5.  **Repeat steps 3-4 until pointers meet or cross**: Continue comparing characters and moving pointers until they meet or cross each other.
6.  **Return the result**: If the loop completes without finding a mismatch, the string is a palindrome.

## Python Solution

```python
def isPalindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome after removing non-alphanumeric characters and converting to lowercase.

    Args:
    s (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    
    # Continue the loop until the pointers meet or cross each other
    while left < right:
        # If the character at the left pointer is not alphanumeric, move the left pointer to the right
        if not s[left].isalnum():
            left += 1
            continue
        
        # If the character at the right pointer is not alphanumeric, move the right pointer to the left
        if not s[right].isalnum():
            right -= 1
            continue
        
        # Compare the characters at the current positions of the two pointers (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    # If the loop completes without finding a mismatch, the string is a palindrome
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
    ]
    
    for s, expected in test_cases:
        result = isPalindrome(s)
        print(f"Input: {s}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test case failed for input: {s}"
    
    print("All test cases passed.")
```

## Time and Space Complexity Analysis

*   **Time complexity**: O(n), where n is the length of the input string `s`. This is because we are potentially scanning the entire string once.
*   **Space complexity**: O(1), as we are not using any additional space that scales with the input size. We are only using a constant amount of space to store the pointers and variables.

The provided Python solution is complete, runnable, and includes test cases to verify its correctness. It adheres to the given constraints and efficiently solves the problem by avoiding unnecessary preprocessing steps and directly comparing characters from both ends of the string.