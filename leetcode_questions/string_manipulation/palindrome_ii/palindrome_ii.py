def valid_palindrome_ii(s):
    """
    判断字符串是否可以通过删除一个字符成为回文串
    :param s: str，输入字符串
    :return: bool，是否可以通过删除一个字符成为回文串
    """
    def is_palindrome(left, right):
        """检查子串是否是回文串"""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    # 使用双指针从两端向中间移动
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 尝试删除左边或右边的字符
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1
    
    return True

def test_valid_palindrome_ii():
    """测试验证回文串 II"""
    # 测试基本情况
    assert valid_palindrome_ii("abca"), "Should handle one deletion"
    
    # 测试无法通过删除一个字符成为回文串的情况
    assert not valid_palindrome_ii("abc"), "Should return false when impossible"
    
    # 测试已经是回文串的情况
    assert valid_palindrome_ii("aba"), "Should handle palindrome"
    assert valid_palindrome_ii("aa"), "Should handle palindrome"
    
    # 测试需要删除中间字符的情况
    assert valid_palindrome_ii("abcba"), "Should handle middle deletion"
    
    # 测试需要删除开头或结尾字符的情况
    assert valid_palindrome_ii("abba"), "Should handle edge deletion"
    
    # 测试空字符串和单个字符
    assert valid_palindrome_ii(""), "Should handle empty string"
    assert valid_palindrome_ii("a"), "Should handle single character"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_valid_palindrome_ii() 