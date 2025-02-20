def window_sum(nums, k):
    """
    计算数组中所有连续k个数的和
    :param nums: List[int]，输入数组
    :param k: int，窗口大小
    :return: List[int]，所有窗口的和
    """
    if not nums or k <= 0 or k > len(nums):
        return []
        
    n = len(nums)
    result = []
    
    # 计算第一个窗口的和
    window_sum = sum(nums[:k])
    result.append(window_sum)
    
    # 滑动窗口，每次减去左边的数，加上右边的数
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        result.append(window_sum)
        
    return result

def test_window_sum():
    # 测试用例1
    nums1 = [1, 2, 7, 8, 5]
    k1 = 3
    assert window_sum(nums1, k1) == [10, 17, 20], f"Expected [10, 17, 20], but got {window_sum(nums1, k1)}"
    
    # 测试用例2：空数组
    assert window_sum([], 2) == [], "Expected empty array for empty input"
    
    # 测试用例3：k大于数组长度
    nums3 = [1, 2, 3]
    k3 = 4
    assert window_sum(nums3, k3) == [], "Expected empty array when k > len(nums)"
    
    # 测试用例4：k = 1
    nums4 = [1, 2, 3]
    k4 = 1
    assert window_sum(nums4, k4) == [1, 2, 3], "Expected original array when k = 1"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_window_sum() 