class Solution:
    def maxCoins(self, nums: list) -> int:
        # 处理空数组情况
        if not nums:
            return 0
            
        # 在数组两端添加1，简化边界处理
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] 表示戳破开区间 (i, j) 内所有气球获得的最大分数
        dp = [[0] * n for _ in range(n)]
        
        # gap 表示区间长度，即 j - i
        # 从 gap=2 开始，表示至少有一个气球可以戳破（开区间，i 和 j 是边界，不戳破）
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                # 尝试在区间 (i,j) 中选择一个气球最后戳破
                for k in range(i + 1, j):
                    score = dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    dp[i][j] = max(dp[i][j], score)
        
        return dp[0][n-1]

# 测试代码
def test_burst_balloons():
    solution = Solution()
    
    # 测试用例1
    assert solution.maxCoins([3,1,5,8]) == 167
    
    # 测试用例2
    assert solution.maxCoins([1,5]) == 10
    
    # 测试用例3
    assert solution.maxCoins([7]) == 7
    
    # 测试用例4
    assert solution.maxCoins([]) == 0
    
    # 测试用例5: 对于 [3,1,5,8,2] 的最优戳破顺序，经动态规划计算得到最大分数为 192
    assert solution.maxCoins([3,1,5,8,2]) == 192
    
    print("所有测试用例通过!")

if __name__ == "__main__":
    test_burst_balloons() 