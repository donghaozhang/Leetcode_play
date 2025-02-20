def count_zero_substrings(s):
    """
    计算字符串中全零子串的个数
    :param s: str，输入字符串（只包含'0'和'1'）
    :return: int，全零子串的个数
    """
    if not s:
        return 0
        
    count = 0
    current_zeros = 0
    
    # 遍历字符串，统计连续的0
    for char in s:
        if char == '0':
            current_zeros += 1
            # 每增加一个0，就会产生current_zeros个新的全零子串
            count += current_zeros
        else:
            current_zeros = 0
            
    return count

def test_count_zero_substrings():
    # 测试用例1
    s1 = "001000"
    assert count_zero_substrings(s1) == 9, f"Expected 9, but got {count_zero_substrings(s1)}"
    
    # 测试用例2：空字符串
    assert count_zero_substrings("") == 0, "Expected 0 for empty string"
    
    # 测试用例3：没有0
    s3 = "111"
    assert count_zero_substrings(s3) == 0, f"Expected 0, but got {count_zero_substrings(s3)}"
    
    # 测试用例4：全是0
    s4 = "000"
    assert count_zero_substrings(s4) == 6, f"Expected 6, but got {count_zero_substrings(s4)}"
    
    # 测试用例5：交替出现
    s5 = "01010"
    assert count_zero_substrings(s5) == 3, f"Expected 3, but got {count_zero_substrings(s5)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_count_zero_substrings() 