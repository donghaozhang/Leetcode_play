class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        # dp[i][j] 表示s[i:j+1]是否是回文串
        dp = [[False] * n for _ in range(n)]
        
        # 初始化：单个字符都是回文串
        for i in range(n):
            dp[i][i] = True
        
        start = 0  # 最长回文子串的起始位置
        max_len = 1  # 最长回文子串的长度
        
        # 按照子串长度从小到大计算
        for length in range(2, n + 1):
            # 遍历所有可能的起始位置
            for i in range(n - length + 1):
                j = i + length - 1  # 子串的结束位置
                
                if length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                
                # 更新最长回文子串的信息
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length
        
        return s[start:start + max_len]

# 测试代码
def test_longest_palindrome():
    solution = Solution()
    
    # 测试用例1
    assert solution.longestPalindrome("babad") in ["bab", "aba"]
    
    # 测试用例2
    assert solution.longestPalindrome("cbbd") == "bb"
    
    # 测试用例3
    assert solution.longestPalindrome("a") == "a"
    
    # 测试用例4
    assert solution.longestPalindrome("") == ""
    
    # 测试用例5
    assert solution.longestPalindrome("abcba") == "abcba"
    
    print("所有测试用例通过!")

if __name__ == "__main__":
    test_longest_palindrome() 