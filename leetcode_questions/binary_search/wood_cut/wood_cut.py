def wood_cut(woods, k):
    """
    将木材切割成k段等长的小段，求能得到的最大长度
    :param woods: List[int]，木材长度列表
    :param k: int，需要切割的段数
    :return: int，能得到的最大长度，如果无法切割返回0
    """
    if not woods or k <= 0:
        return 0
        
    # 二分查找的范围：1到最长木材的长度
    left, right = 1, max(woods)
    
    # 如果无法切割出k段，返回0
    if sum(wood // right for wood in woods) < k:
        return 0
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        # 计算当前长度能切出多少段
        total = sum(wood // mid for wood in woods)
        
        if total >= k:
            # 如果能切出k段或更多，尝试更大的长度
            left = mid
        else:
            # 如果切不出k段，需要减小长度
            right = mid
            
    # 检查右边界是否可行
    if sum(wood // right for wood in woods) >= k:
        return right
    # 返回左边界
    return left

def test_wood_cut():
    """测试木材切割"""
    # 测试基本情况
    woods1 = [232, 124, 456]
    k1 = 7
    assert wood_cut(woods1, k1) == 114, "Should find correct length"
    
    # 测试无法切割的情况
    woods2 = [1, 2, 3]
    k2 = 7
    assert wood_cut(woods2, k2) == 0, "Should return 0 when impossible"
    
    # 测试刚好能切割的情况
    woods3 = [5, 5, 5, 5]
    k3 = 4
    assert wood_cut(woods3, k3) == 5, "Should handle exact division"
    
    # 测试只有一根木材的情况
    woods4 = [10]
    k4 = 2
    assert wood_cut(woods4, k4) == 5, "Should handle single wood"
    
    # 测试空数组
    assert wood_cut([], 1) == 0, "Should handle empty array"
    
    # 测试k为0或负数
    woods5 = [1, 2, 3]
    assert wood_cut(woods5, 0) == 0, "Should handle k = 0"
    assert wood_cut(woods5, -1) == 0, "Should handle negative k"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_wood_cut() 