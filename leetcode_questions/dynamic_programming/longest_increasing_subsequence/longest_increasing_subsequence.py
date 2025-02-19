#!/usr/bin/env python

class Solution:
    def longestIncreasingSubsequence(self, nums: list) -> list:
        if not nums:
            return []
        
        n = len(nums)
        dp = [1] * n              # dp[i]：以 nums[i] 结尾的最长子序列的长度
        prev = [-1] * n           # prev[i]：记录前驱索引以便重构子序列
        
        max_len = 1
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        # 重构最长上升子序列
        lis = []
        index = max_index
        while index != -1:
            lis.append(nums[index])
            index = prev[index]
        lis.reverse()
        return lis

# 测试代码
def test_longest_increasing_subsequence():
    solution = Solution()
    nums = [4, 5, 6, 1, 2, 3, 5]
    expected = [1, 2, 3, 5]
    result = solution.longestIncreasingSubsequence(nums)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_longest_increasing_subsequence() 