def longest_repeating_character(s, k):
    """
    找到替换k个字符后可以得到的最长重复字符子串
    :param s: str，输入字符串
    :param k: int，允许替换的字符数量
    :return: int，最长重复字符子串的长度
    """
    if not s:
        return 0
        
    # 使用数组记录窗口内每个字符的出现次数
    char_count = {}
    max_count = 0  # 窗口内出现最多的字符的次数
    max_length = 0  # 最长重复字符子串的长度
    left = 0  # 窗口左边界
    
    for right in range(len(s)):
        # 更新右边界字符的计数
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        # 更新窗口内出现最多的字符的次数
        max_count = max(max_count, char_count[s[right]])
        
        # 当前窗口长度减去最多字符出现次数，就是需要替换的字符数量
        # 如果超过k，需要缩小窗口
        window_size = right - left + 1
        if window_size - max_count > k:
            # 移除左边界字符的计数
            char_count[s[left]] -= 1
            left += 1
        
        # 更新最大长度
        max_length = max(max_length, right - left + 1)
    
    return max_length

def test_longest_repeating_character():
    # 测试用例1
    s1 = "ABABA"
    k1 = 2
    assert longest_repeating_character(s1, k1) == 5, f"Expected 5, but got {longest_repeating_character(s1, k1)}"
    
    # 测试用例2：空字符串
    assert longest_repeating_character("", 2) == 0, "Expected 0 for empty string"
    
    # 测试用例3：k = 0
    s3 = "AABAB"
    k3 = 0
    assert longest_repeating_character(s3, k3) == 2, f"Expected 2, but got {longest_repeating_character(s3, k3)}"
    
    # 测试用例4：全相同字符
    s4 = "AAAA"
    k4 = 2
    assert longest_repeating_character(s4, k4) == 4, f"Expected 4, but got {longest_repeating_character(s4, k4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_longest_repeating_character() 