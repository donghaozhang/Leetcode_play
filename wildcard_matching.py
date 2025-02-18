class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] 表示 s[0:i] 与 p[0:j] 是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 当 s 为空时，只有 p 中所有字符为 '*' 才匹配
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # 填充 dp 数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' 匹配空序列或者匹配一个字符
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        
        return dp[m][n]


# 测试代码
def test_wildcard_matching():
    solution = Solution()
    
    # 测试用例：isMatch("aab", "c*a*b") -> False
    assert solution.isMatch("aab", "c*a*b") == False, "Test case: (aab, c*a*b) should return False"
    
    # 测试用例：isMatch("abc", "*?c") -> True
    assert solution.isMatch("abc", "*?c") == True, "Test case: (abc, *?c) should return True"
    
    # 其他测试用例
    assert solution.isMatch("aa", "a") == False
    assert solution.isMatch("aa", "*") == True
    assert solution.isMatch("cb", "?a") == False
    assert solution.isMatch("adceb", "*a*b") == True

    print("所有测试用例通过！")

if __name__ == "__main__":
    test_wildcard_matching() 