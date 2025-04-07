def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_length = 0
    left = 0
    max_count = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        
        # If the current window size minus the max count is greater than k,
        # we need to move the left pointer forward
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
