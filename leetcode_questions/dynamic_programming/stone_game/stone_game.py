class Solution:
    def stoneGame(self, stones: list) -> int:
        if not stones:
            return 0
            
        n = len(stones)
        if n <= 1:
            return 0
            
        # 预处理区间和
        sum_interval = [[0] * n for _ in range(n)]
        for i in range(n):
            sum_interval[i][i] = stones[i]
            for j in range(i + 1, n):
                sum_interval[i][j] = sum_interval[i][j-1] + stones[j]
        
        # dp[i][j] 表示合并区间[i,j]的最小代价
        dp = [[float('inf')] * n for _ in range(n)]
        
        # 初始化：单个石子堆不需要代价
        for i in range(n):
            dp[i][i] = 0
        
        # 按区间长度计算
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 尝试不同的分割点
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + sum_interval[i][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]

# 测试代码
def test_stone_game():
    solution = Solution()
    
    # 测试用例1
    assert solution.stoneGame([3, 4, 3]) == 17
    
    # 测试用例2
    assert solution.stoneGame([4, 1, 1, 4]) == 18
    
    # 测试用例3
    assert solution.stoneGame([1]) == 0
    
    # 测试用例4
    assert solution.stoneGame([]) == 0
    
    # 测试用例5: 修正预期值
    # [2,4,1,1] 的最优合并过程：
    # 1. 合并后两堆：[2,4,2]，代价为 2
    # 2. 合并4和2：[2,6]，代价为 6
    # 3. 合并2和6：[8]，代价为 8
    # 总代价 = 2 + 6 + 8 = 16
    assert solution.stoneGame([2, 4, 1, 1]) == 16
    
    print("所有测试用例通过!")

if __name__ == "__main__":
    test_stone_game() 