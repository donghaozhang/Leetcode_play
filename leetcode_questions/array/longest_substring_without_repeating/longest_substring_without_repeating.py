def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without duplicate characters
    """
    # Dictionary to store the last index of each character
    char_index = {}
    
    # Result to store the max length
    max_length = 0
    
    # Starting index of current non-repeating substring
    start = 0
    
    # Iterate through the string
    for i, char in enumerate(s):
        # If character is already in the current window
        if char in char_index:
            # Update start to be after the last occurrence of the current character
            # We use max to handle cases where the previous occurrence is before the current window
            start = max(start, char_index[char] + 1)
        
        # Update the last seen index of the character
        char_index[char] = i
        
        # Update the maximum length
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Example 1
    s1 = "abcabcbb"
    print(length_of_longest_substring(s1))  # Expected output: 3
    
    # Example 2
    s2 = "bbbbb"
    print(length_of_longest_substring(s2))  # Expected output: 1
    
    # Example 3
    s3 = "pwwkew"
    print(length_of_longest_substring(s3))  # Expected output: 3
    
    # Additional test cases
    s4 = ""
    print(length_of_longest_substring(s4))  # Expected output: 0
    
    s5 = "au"
    print(length_of_longest_substring(s5))  # Expected output: 2 