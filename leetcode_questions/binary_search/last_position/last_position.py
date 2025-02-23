def find_last_position(nums, target):
    """
    在有序数组中查找目标值的最后一个位置
    :param nums: List[int]，有序数组
    :param target: int，目标值
    :return: int，目标值的最后一个位置，如果不存在返回-1
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
            
    # 检查右边界
    if nums[right] == target:
        return right
    # 检查左边界
    if nums[left] == target:
        return left
        
    return -1

def test_find_last_position():
    """测试查找最后一个位置"""
    # 测试基本情况
    nums1 = [1, 2, 3, 3, 3, 4, 5]
    assert find_last_position(nums1, 3) == 4, "Should find last position"
    
    # 测试目标值在开头
    nums2 = [1, 1, 1, 2, 3]
    assert find_last_position(nums2, 1) == 2, "Should find last position at beginning"
    
    # 测试目标值在结尾
    nums3 = [1, 2, 3, 4, 4]
    assert find_last_position(nums3, 4) == 4, "Should find last position at end"
    
    # 测试目标值不存在
    nums4 = [1, 2, 4, 5]
    assert find_last_position(nums4, 3) == -1, "Should return -1 when target not found"
    
    # 测试空数组
    assert find_last_position([], 1) == -1, "Should handle empty array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_last_position() 