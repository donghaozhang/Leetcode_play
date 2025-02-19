class Solution:
    def canWinBash(self, n: int) -> bool:
        """
        判断在 Bash 游戏中先手是否能赢
        
        参数:
            n: int, 石头的数量
        返回:
            bool, True 表示先手能赢，False 表示先手必输
        """
        # 方法一：记忆化搜索
        def can_win_memo(n: int, memo: dict) -> bool:
            # 已经计算过的状态，直接返回
            if n in memo:
                return memo[n]
            
            # 边界条件
            if n <= 0:
                return False
            if n <= 3:
                return True
            
            # 尝试拿走 1、2 或 3 颗石头
            # 只要存在一种使对手必输的拿法，当前玩家就能赢
            for i in range(1, 4):
                if not can_win_memo(n - i, memo):
                    memo[n] = True
                    return True
            
            # 所有拿法都使对手能赢，则当前玩家必输
            memo[n] = False
            return False

        # 方法二：数学归纳
        def can_win_math(n: int) -> bool:
            return n % 4 != 0

        # 这里使用记忆化搜索方法
        return can_win_memo(n, {})


# 测试代码
def test_bash_game():
    solution = Solution()
    
    # 测试用例 1：n = 4，期望输出 false
    assert not solution.canWinBash(4), "n=4 时应该返回 False"
    
    # 测试用例 2：n = 5，期望输出 true
    assert solution.canWinBash(5), "n=5 时应该返回 True"
    
    # 测试用例 3：n = 1，期望输出 true
    assert solution.canWinBash(1), "n=1 时应该返回 True"
    
    # 测试用例 4：n = 8，期望输出 false
    assert not solution.canWinBash(8), "n=8 时应该返回 False"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_bash_game() 