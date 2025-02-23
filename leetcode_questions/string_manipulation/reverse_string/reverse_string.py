def reverse_string(s):
    """
    翻转字符串
    :param s: str，输入字符串
    :return: str，翻转后的字符串
    """
    if not s:
        return ""
        
    # 转换为列表进行翻转
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return ''.join(chars)

def reverse_string_pythonic(s):
    """
    使用Python切片的方式翻转字符串
    :param s: str，输入字符串
    :return: str，翻转后的字符串
    """
    return s[::-1]

def test_reverse_string():
    """测试字符串翻转"""
    # 测试基本情况
    assert reverse_string("hello") == "olleh", "Should reverse normal string"
    assert reverse_string_pythonic("hello") == "olleh", "Should reverse normal string"
    
    # 测试空字符串
    assert reverse_string("") == "", "Should handle empty string"
    assert reverse_string_pythonic("") == "", "Should handle empty string"
    
    # 测试单个字符
    assert reverse_string("a") == "a", "Should handle single character"
    assert reverse_string_pythonic("a") == "a", "Should handle single character"
    
    # 测试包含空格的字符串
    assert reverse_string("hello world") == "dlrow olleh", "Should handle string with spaces"
    assert reverse_string_pythonic("hello world") == "dlrow olleh", "Should handle string with spaces"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_reverse_string() 