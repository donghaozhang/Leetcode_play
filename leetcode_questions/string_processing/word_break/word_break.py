class Solution:
    def wordBreak(self, s: str, wordDict: set) -> bool:
        n = len(s)
        # dp[i] 表示 s[0:i] 是否可以被拆分成字典中的单词
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串可以拆分
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]

# 测试代码
def test_word_break():
    solution = Solution()
    
    # 测试用例1
    s1 = "lintcode"
    wordDict1 = {"lint", "code", "li"}
    assert solution.wordBreak(s1, wordDict1) is True, f"Expected True for s={s1} and wordDict={wordDict1}"
    
    # 测试用例2
    s2 = "lintcode"
    wordDict2 = {"lin", "code", "li"}
    assert solution.wordBreak(s2, wordDict2) is False, f"Expected False for s={s2} and wordDict={wordDict2}"
    
    # 其他测试用例
    s3 = "applepenapple"
    wordDict3 = {"apple", "pen"}
    assert solution.wordBreak(s3, wordDict3) is True, "Expected True for applepenapple"
    
    s4 = "catsandog"
    wordDict4 = {"cats", "dog", "sand", "and", "cat"}
    assert solution.wordBreak(s4, wordDict4) is False, "Expected False for catsandog"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_word_break() 