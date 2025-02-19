class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1  # 已保证 s[0] != "0"
        
        for i in range(2, n + 1):
            one_digit = int(s[i-1:i])
            two_digits = int(s[i-2:i])
            
            if one_digit != 0:
                dp[i] += dp[i-1]
            
            # 检查两位数是否构成有效的字符（10~26）
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]


# 测试代码
def test_decode_ways():
    solution = Solution()
    
    # 测试用例1
    assert solution.numDecodings("12") == 2, f"Expected 2, got {solution.numDecodings('12')}"
    
    # 测试用例2
    assert solution.numDecodings("226") == 3, f"Expected 3, got {solution.numDecodings('226')}"
    
    # 测试用例3：空字符串无解
    assert solution.numDecodings("") == 0, "Expected 0 for empty string"
    
    # 测试用例4：字符串以0开头无效
    assert solution.numDecodings("0") == 0, "Expected 0 for '0'"
    
    # 测试用例5
    assert solution.numDecodings("10") == 1, f"Expected 1, got {solution.numDecodings('10')}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_decode_ways() 