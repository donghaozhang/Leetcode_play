def characterReplacement(s: str, k: int) -> int:
    """
    Returns the length of the longest substring containing the same letter 
    that can be obtained after performing at most k operations on the given string s.

    Args:
    s (str): The input string.
    k (int): The maximum number of operations allowed.

    Returns:
    int: The length of the longest substring containing the same letter.
    """
    char_count = {}  # Dictionary to store frequency count of characters
    max_count = 0    # Maximum frequency count seen so far
    left = 0         # Left pointer of the sliding window
    max_length = 0   # Maximum length of the window seen so far

    for right in range(len(s)):
        # Update frequency count of the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update maximum frequency count
        max_count = max(max_count, char_count[s[right]])
        
        # Check if the number of characters to be replaced exceeds k
        if right - left + 1 - max_count > k:
            # Shrink the window by moving the left pointer to the right
            char_count[s[left]] -= 1
            left += 1
        
        # Update maximum length of the window
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(characterReplacement("ABAB", 2))     # Output: 4
print(characterReplacement("AABABBA", 1))  # Output: 4
print(characterReplacement("ABBB", 2))     # Output: 4
print(characterReplacement("ABC", 1))      # Output: 2
print(characterReplacement("AAAA", 0))     # Output: 4
