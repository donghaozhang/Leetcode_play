def binary_search(nums, target):
    """
    在有序数组中查找目标值的任意位置
    :param nums: List[int]，有序数组
    :param target: int，目标值
    :return: int，目标值的位置，如果不存在返回-1
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def test_binary_search():
    """测试二分查找"""
    # 测试基本情况
    nums1 = [1, 2, 3, 3, 4, 5, 10]
    assert binary_search(nums1, 3) in [2, 3], "Should find target"
    
    # 测试目标值在开头
    nums2 = [1, 1, 1, 2, 3]
    assert binary_search(nums2, 1) in [0, 1, 2], "Should find target at beginning"
    
    # 测试目标值在结尾
    nums3 = [1, 2, 3, 4, 4]
    assert binary_search(nums3, 4) in [3, 4], "Should find target at end"
    
    # 测试目标值不存在
    nums4 = [1, 2, 4, 5]
    assert binary_search(nums4, 3) == -1, "Should return -1 when target not found"
    
    # 测试空数组
    assert binary_search([], 1) == -1, "Should handle empty array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_binary_search() 