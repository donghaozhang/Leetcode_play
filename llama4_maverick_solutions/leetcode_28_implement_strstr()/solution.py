def strStr(haystack: str, needle: str) -> int:
    """
    Returns the index of the first occurrence of `needle` in `haystack`, 
    or `-1` if `needle` is not part of `haystack`.
    
    Args:
    haystack (str): The string to search in.
    needle (str): The string to search for.
    
    Returns:
    int: The index of the first occurrence of `needle` in `haystack`, or `-1`.
    """
    if not needle:  # If needle is empty, return 0
        return 0
    
    needle_len = len(needle)
    haystack_len = len(haystack)
    
    for i in range(haystack_len - needle_len + 1):
        # Check if the substring of haystack starting at i is equal to needle
        if haystack[i:i + needle_len] == needle:
            return i
    
    # If no match is found, return -1
    return -1

# Test cases
print(strStr("sadbutsad", "sad"))  # Expected output: 0
print(strStr("leetcode", "leeto"))  # Expected output: -1
print(strStr("hello", ""))  # Expected output: 0
print(strStr("", "a"))  # Expected output: -1
print(strStr("a", "a"))  # Expected output: 0
print(strStr("abc", "c"))  # Expected output: 2
