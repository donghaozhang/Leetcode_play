def minimum_partition(nums):
    """
    将数组划分为两组，使得两组和的差最小
    :param nums: List[int]，输入数组
    :return: int，两组和的最小差值
    """
    if not nums:
        return 0
        
    total = sum(nums)
    target = total // 2  # 尽量接近总和的一半
    
    # dp[i][j] 表示前i个数能否组成和j
    n = len(nums)
    dp = [False] * (target + 1)
    dp[0] = True  # 空集的和为0
    
    # 记录可以达到的最大和
    max_sum = 0
    
    # 对每个数字
    for num in nums:
        # 从大到小遍历，避免重复使用同一个数字
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                max_sum = max(max_sum, j)
    
    # 一组的和为max_sum，另一组的和为total-max_sum
    return total - 2 * max_sum

def test_minimum_partition():
    # 测试用例1：基本情况
    nums1 = [1, 6, 11, 5]
    assert minimum_partition(nums1) == 1, f"Expected 1, but got {minimum_partition(nums1)}"
    
    # 测试用例2：空数组
    assert minimum_partition([]) == 0, "Expected 0 for empty array"
    
    # 测试用例3：只有一个数
    nums3 = [5]
    assert minimum_partition(nums3) == 5, f"Expected 5, but got {minimum_partition(nums3)}"
    
    # 测试用例4：可以平分
    nums4 = [1, 2, 3, 4]
    assert minimum_partition(nums4) == 0, f"Expected 0, but got {minimum_partition(nums4)}"
    
    # 测试用例5：较大的差值
    nums5 = [1, 2, 3, 10]
    assert minimum_partition(nums5) == 4, f"Expected 4, but got {minimum_partition(nums5)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_minimum_partition() 