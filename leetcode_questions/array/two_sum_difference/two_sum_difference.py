def two_sum_difference(nums, target):
    """
    找到数组中两个数的差等于目标值
    :param nums: List[int]，输入数组
    :param target: int，目标差值
    :return: List[int]，两个数的下标，较小数在前
    """
    if not nums or len(nums) < 2:
        return []
        
    # 创建带索引的数组并排序
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort()  # 按数值排序
    
    # 双指针搜索
    left, right = 0, 1
    target = abs(target)  # 处理负数目标值
    
    while right < len(nums):
        diff = nums_with_index[right][0] - nums_with_index[left][0]
        
        if diff == target:
            # 返回原始索引，较小数在前
            left_index = nums_with_index[left][1]
            right_index = nums_with_index[right][1]
            return [min(left_index, right_index), max(left_index, right_index)]
        
        if diff < target:
            right += 1
        else:  # diff > target
            left += 1
            # 确保 left < right
            if left == right:
                right += 1
                
    return []

def test_two_sum_difference():
    # 测试用例1
    nums1 = [2, 7, 15, 24]
    target1 = 5
    assert two_sum_difference(nums1, target1) == [0, 1], f"Expected [0, 1], but got {two_sum_difference(nums1, target1)}"
    
    # 测试用例2：空数组
    assert two_sum_difference([], 1) == [], "Expected empty array for empty input"
    
    # 测试用例3：负数目标值
    nums3 = [1, 5, 8, 13]
    target3 = -4
    assert two_sum_difference(nums3, target3) == [0, 1], f"Expected [0, 1], but got {two_sum_difference(nums3, target3)}"
    
    # 测试用例4：没有解
    nums4 = [1, 2, 3]
    target4 = 5
    assert two_sum_difference(nums4, target4) == [], "Expected empty array when no solution exists"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_two_sum_difference() 