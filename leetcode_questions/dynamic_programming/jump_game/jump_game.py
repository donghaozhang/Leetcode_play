def can_jump(nums):
    """
    判断是否能跳到最后一个位置
    :param nums: List[int]，每个位置可以跳跃的最大距离
    :return: bool，是否能到达最后一个位置
    """
    if not nums:
        return False
        
    n = len(nums)
    # 记录当前能到达的最远位置
    max_reach = 0
    
    # 遍历每个位置（只需要遍历到倒数第二个位置）
    for i in range(n - 1):
        # 如果当前位置无法到达，直接返回False
        if i > max_reach:
            return False
            
        # 更新能到达的最远位置
        max_reach = max(max_reach, i + nums[i])
        
        # 如果已经能到达最后一个位置，提前返回True
        if max_reach >= n - 1:
            return True
    
    # 判断最终是否能到达最后一个位置
    return max_reach >= n - 1

def test_can_jump():
    # 测试用例1：基本情况
    nums1 = [2, 3, 1, 1, 4]
    assert can_jump(nums1) == True, f"Expected True, but got {can_jump(nums1)}"
    
    # 测试用例2：无法到达
    nums2 = [3, 2, 1, 0, 4]
    assert can_jump(nums2) == False, f"Expected False, but got {can_jump(nums2)}"
    
    # 测试用例3：空数组
    assert can_jump([]) == False, "Expected False for empty array"
    
    # 测试用例4：单个元素
    nums4 = [0]
    assert can_jump(nums4) == True, f"Expected True, but got {can_jump(nums4)}"
    
    # 测试用例5：全零数组
    nums5 = [0, 0, 0]
    assert can_jump(nums5) == False, f"Expected False, but got {can_jump(nums5)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_can_jump() 