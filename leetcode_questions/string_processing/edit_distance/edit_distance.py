class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # 构造 (m+1) x (n+1) 的 DP 表
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化：空字符串转为另一个字符串需要插入/删除所有字符
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # 填充 DP 表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],    # 删除
                        dp[i][j - 1],    # 插入
                        dp[i - 1][j - 1] # 替换
                    ) + 1
        
        return dp[m][n]


# 测试代码
def test_edit_distance():
    solution = Solution()
    # 测试用例1: "horse" -> "ros" 需要 3 次编辑操作
    assert solution.minDistance("horse", "ros") == 3, f"Expected 3, got {solution.minDistance('horse', 'ros')}"
    
    # 其他测试用例
    assert solution.minDistance("", "abc") == 3
    assert solution.minDistance("abc", "") == 3
    assert solution.minDistance("intention", "execution") == 5
    assert solution.minDistance("abcd", "abcd") == 0

    print("所有测试用例通过！")

if __name__ == "__main__":
    test_edit_distance() 