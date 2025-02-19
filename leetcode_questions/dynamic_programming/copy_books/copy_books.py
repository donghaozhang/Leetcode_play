class Solution:
    def copyBooks(self, pages: list, k: int) -> int:
        n = len(pages)
        if n == 0:
            return 0
        
        # 预处理前缀和，cum[i] 表示 pages[0...i-1] 的和，cum[0] = 0
        cum = [0] * (n + 1)
        for i in range(1, n + 1):
            cum[i] = cum[i - 1] + pages[i - 1]
        
        # 初始化 dp 表
        # dp[i][j] 表示将前 i 本书分给 j 个人所能达到的最小最大负担
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for j in range(k + 1):
            dp[0][j] = 0  # 0 本书负担为 0
        for i in range(1, n + 1):
            dp[i][1] = cum[i]  # 只有一个人，负担为前 i 本书的总和
        
        # 动态规划求解
        for j in range(2, k + 1):  # 抄书人数量从 2 到 k
            for i in range(j, n + 1):  # 至少 i>=j，每个人至少分一册
                # 尝试所有分割点 p，使得前 p 本书分给 j-1 个人，
                # 剩余 [p, i-1] 分给最后一个人
                for p in range(j - 1, i):
                    # 该分割方式下，最大的负担为：
                    # max(dp[p][j-1], cum[i]-cum[p])
                    cost = max(dp[p][j - 1], cum[i] - cum[p])
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[n][k]


# 测试代码
def test_copy_books():
    solution = Solution()
    # 测试用例: pages = [3,2,1,1,1,1], k = 3, 预期结果为 4
    pages = [3,2,1,1,1,1]
    k = 3
    result = solution.copyBooks(pages, k)
    assert result == 4, f"Expected 4, got {result}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_copy_books() 