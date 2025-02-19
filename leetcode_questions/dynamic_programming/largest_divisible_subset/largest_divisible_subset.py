class Solution:
    def largestDivisibleSubset(self, nums: list) -> list:
        if not nums:
            return []
        
        # 排序，保证较小数字在前，有助于判断整除关系
        nums.sort()
        n = len(nums)
        
        # dp[i] 表示以 nums[i] 结尾的最大整除子集的长度
        dp = [1] * n
        # prev[i] 用于记录构造最大子集时 nums[i] 的前驱下标
        prev = [-1] * n
        
        max_dp = 1
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_dp:
                max_dp = dp[i]
                max_index = i
                
        # 重构结果子集
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        result.reverse()
        return result

# 测试代码
def test_largest_divisible_subset():
    solution = Solution()
    
    # 测试用例：输入 [1,2,3,4,5,6,7,8]，预期输出 {1,2,4,8}
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    result = solution.largestDivisibleSubset(nums)
    
    # 由于可能有多个答案，我们仅验证结果是一个合法的整除子集，并且长度与预期一致。
    # 这里预期最长子集长度为 4。
    assert len(result) == 4, f"Expected subset of length 4, but got {len(result)}"
    for i in range(1, len(result)):
        assert result[i] % result[i - 1] == 0, "Subset is not divisible"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_largest_divisible_subset() 