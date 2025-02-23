def is_palindrome(s):
    """
    判断字符串是否是回文串（只考虑字母和数字字符，忽略大小写）
    :param s: str，输入字符串
    :return: bool，是否是回文串
    """
    if not s:
        return True
        
    # 将字符串转换为小写，并只保留字母和数字
    filtered = ''.join(c.lower() for c in s if c.isalnum())
    
    # 使用双指针判断是否回文
    left, right = 0, len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1
        
    return True

def test_is_palindrome():
    """测试回文串判断"""
    # 测试基本情况
    assert is_palindrome("A man, a plan, a canal: Panama"), "Should be palindrome"
    
    # 测试非回文串
    assert not is_palindrome("race a car"), "Should not be palindrome"
    
    # 测试空字符串
    assert is_palindrome(""), "Empty string should be palindrome"
    
    # 测试只有空格和标点
    assert is_palindrome(" ,"), "String with only spaces and punctuation should be palindrome"
    
    # 测试数字
    assert is_palindrome("12321"), "Should handle numbers"
    assert not is_palindrome("12345"), "Should handle non-palindrome numbers"
    
    # 测试混合字符
    assert is_palindrome("A1b2,2b1a"), "Should handle mixed characters"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_is_palindrome() 