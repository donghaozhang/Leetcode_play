def str_str(haystack, needle):
    """
    在字符串中查找子串第一次出现的位置
    :param haystack: str，主字符串
    :param needle: str，要查找的子串
    :return: int，子串第一次出现的位置，如果不存在返回-1
    """
    if not needle:
        return 0
        
    if not haystack:
        return -1
        
    # 遍历所有可能的起始位置
    for i in range(len(haystack) - len(needle) + 1):
        # 检查从i开始的子串是否匹配
        j = 0
        while j < len(needle) and haystack[i + j] == needle[j]:
            j += 1
        if j == len(needle):
            return i
            
    return -1

def str_str_pythonic(haystack, needle):
    """
    使用Python内置的字符串查找功能
    :param haystack: str，主字符串
    :param needle: str，要查找的子串
    :return: int，子串第一次出现的位置，如果不存在返回-1
    """
    if not needle:
        return 0
        
    try:
        return haystack.index(needle)
    except ValueError:
        return -1

def test_str_str():
    """测试字符串查找"""
    # 测试基本情况
    assert str_str("hello", "ll") == 2, "Should find substring"
    assert str_str_pythonic("hello", "ll") == 2, "Should find substring"
    
    # 测试空字符串
    assert str_str("", "") == 0, "Should handle empty strings"
    assert str_str_pythonic("", "") == 0, "Should handle empty strings"
    assert str_str("", "a") == -1, "Should handle empty haystack"
    assert str_str_pythonic("", "a") == -1, "Should handle empty haystack"
    
    # 测试不存在的子串
    assert str_str("aaaaa", "bba") == -1, "Should handle non-existent substring"
    assert str_str_pythonic("aaaaa", "bba") == -1, "Should handle non-existent substring"
    
    # 测试子串在开头
    assert str_str("hello", "he") == 0, "Should find substring at start"
    assert str_str_pythonic("hello", "he") == 0, "Should find substring at start"
    
    # 测试子串在结尾
    assert str_str("hello", "lo") == 3, "Should find substring at end"
    assert str_str_pythonic("hello", "lo") == 3, "Should find substring at end"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_str_str() 