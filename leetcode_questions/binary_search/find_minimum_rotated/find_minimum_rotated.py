def find_minimum(nums):
    """
    在旋转排序数组中找到最小值
    :param nums: List[int]，旋转后的排序数组
    :return: int，数组中的最小值
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    # 如果数组没有旋转或只有一个元素
    if nums[left] < nums[right]:
        return nums[left]
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        # 与数组第一个元素比较
        if nums[mid] > nums[0]:
            left = mid
        else:
            right = mid
            
    # 返回左右指针中较小的值
    return min(nums[left], nums[right])

def find_minimum_with_duplicates(nums):
    """
    在可能包含重复元素的旋转排序数组中找到最小值
    :param nums: List[int]，旋转后的排序数组（可能包含重复元素）
    :return: int，数组中的最小值
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    # 如果数组没有旋转或只有一个元素
    if nums[left] < nums[right]:
        return nums[left]
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        # 与数组最后一个元素比较
        if nums[mid] > nums[right]:
            left = mid
        elif nums[mid] < nums[right]:
            right = mid
        else:
            # 当中间值等于右边界值时，无法确定最小值在哪一边
            # 可以排除右边界，因为即使它是最小值，在mid处也有一个相同的值
            right -= 1
            
    # 返回左右指针中较小的值
    return min(nums[left], nums[right])

def test_find_minimum():
    """测试查找最小值"""
    # 测试基本情况
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    assert find_minimum(nums1) == 0, "Should find minimum in rotated array"
    
    # 测试未旋转的数组
    nums2 = [1, 2, 3, 4, 5]
    assert find_minimum(nums2) == 1, "Should handle non-rotated array"
    
    # 测试只有一个元素的数组
    nums3 = [1]
    assert find_minimum(nums3) == 1, "Should handle single element array"
    
    # 测试空数组
    assert find_minimum([]) == -1, "Should handle empty array"
    
    # 测试包含重复元素的数组
    nums4 = [3, 3, 1, 3]
    assert find_minimum_with_duplicates(nums4) == 1, "Should handle duplicates"
    
    nums5 = [2, 2, 2, 0, 1]
    assert find_minimum_with_duplicates(nums5) == 0, "Should handle duplicates"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_minimum() 