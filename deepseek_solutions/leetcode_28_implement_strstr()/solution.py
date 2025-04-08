def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    len_haystack = len(haystack)
    len_needle = len(needle)
    if len_needle > len_haystack:
        return -1
    for i in range(len_haystack - len_needle + 1):
        if haystack[i:i+len_needle] == needle:
            return i
    return -1

# Test cases
print(strStr("sadbutsad", "sad"))      # Output: 0
print(strStr("leetcode", "leeto"))     # Output: -1
print(strStr("hello", "ll"))           # Output: 2
print(strStr("aaaaa", "bba"))          # Output: -1
print(strStr("a", "a"))                # Output: 0
print(strStr("abc", "c"))              # Output: 2
