def find_peak_element(nums):
    """
    寻找数组中的峰值元素
    峰值元素是指大于左右相邻值的元素
    :param nums: List[int]，输入数组
    :return: int，任一峰值元素的索引
    """
    if not nums:
        return -1
        
    left, right = 0, len(nums) - 1
    
    while left + 1 < right:
        mid = (left + right) // 2
        
        # 如果中间元素小于其右邻居，峰值在右边
        if nums[mid] < nums[mid + 1]:
            left = mid
        # 否则，峰值在左边或就是中间元素
        else:
            right = mid
            
    # 返回较大的那个元素的索引
    return left if nums[left] > nums[right] else right

def test_find_peak_element():
    """测试寻找峰值元素"""
    # 测试基本情况
    nums1 = [1, 2, 1, 3, 5, 6, 4]
    result1 = find_peak_element(nums1)
    assert nums1[result1] > nums1[result1-1] and nums1[result1] > nums1[result1+1], "Should find a peak element"
    
    # 测试单调递增数组
    nums2 = [1, 2, 3, 4, 5]
    result2 = find_peak_element(nums2)
    assert result2 == 4, "Should handle monotonic increasing array"
    
    # 测试单调递减数组
    nums3 = [5, 4, 3, 2, 1]
    result3 = find_peak_element(nums3)
    assert result3 == 0, "Should handle monotonic decreasing array"
    
    # 测试只有两个元素的数组
    nums4 = [2, 1]
    result4 = find_peak_element(nums4)
    assert result4 == 0, "Should handle array with two elements"
    
    # 测试只有一个元素的数组
    nums5 = [1]
    result5 = find_peak_element(nums5)
    assert result5 == 0, "Should handle array with one element"
    
    # 测试空数组
    assert find_peak_element([]) == -1, "Should handle empty array"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_find_peak_element() 