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
