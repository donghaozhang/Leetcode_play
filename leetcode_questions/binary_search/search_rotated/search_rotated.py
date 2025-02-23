def search_rotated(nums, target):
    """
    在旋转排序数组中查找目标值
    :param nums: List[int]，旋转后的排序数组
    :param target: int，目标值
    :return: int，目标值的位置，如果不存在返回-1
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        if nums[left] < nums[mid]:
            # 左半部分有序
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid
        else:
            # 右半部分有序
            if nums[mid] < target <= nums[right]:
                left = mid
            else:
                right = mid
                
    # 检查左右边界
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
        
    return -1

def test_search_rotated():
    """测试旋转数组搜索"""
    # 测试基本情况
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated(nums1, 0) == 4, "Should find target in rotated array"
    
    # 测试目标值在左半部分
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated(nums2, 5) == 1, "Should find target in left part"
    
    # 测试目标值在右半部分
    nums3 = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated(nums3, 2) == 6, "Should find target in right part"
    
    # 测试目标值不存在
    nums4 = [4, 5, 6, 7, 0, 1, 2]
    assert search_rotated(nums4, 3) == -1, "Should return -1 when target not found"
    
    # 测试未旋转的数组
    nums5 = [1, 2, 3, 4, 5]
    assert search_rotated(nums5, 3) == 2, "Should handle non-rotated array"
    
    # 测试只有一个元素的数组
    nums6 = [1]
    assert search_rotated(nums6, 1) == 0, "Should handle single element array"
    
    # 测试空数组
    assert search_rotated([], 1) == -1, "Should handle empty array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_search_rotated() 