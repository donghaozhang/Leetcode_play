class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        实现快速幂算法
        @param x: 底数
        @param n: 指数
        @return: x^n
        """
        # 处理负数指数的情况
        if n < 0:
            x = 1 / x
            n = -n
        
        def fast_power(base: float, power: int) -> float:
            if power == 0:
                return 1.0
            
            # 递归计算一半的结果
            half = fast_power(base, power // 2)
            
            # 如果是奇数次幂，需要多乘一次底数
            if power % 2 == 1:
                return half * half * base
            else:
                return half * half
        
        return fast_power(x, n)
    
    def myPow_iterative(self, x: float, n: int) -> float:
        """
        快速幂算法的迭代实现
        @param x: 底数
        @param n: 指数
        @return: x^n
        """
        # 处理负数指数的情况
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_product = x
        
        # 根据n的二进制表示计算结果
        while n > 0:
            if n & 1:  # 如果当前位是1
                result *= current_product
            current_product *= current_product
            n >>= 1  # n右移一位
        
        return result


# 测试代码
def test_fast_power():
    solution = Solution()
    
    # 测试用例1：正数幂
    assert abs(solution.myPow(2.0, 10) - 1024.0) < 1e-10, "测试用例1失败"
    assert abs(solution.myPow_iterative(2.0, 10) - 1024.0) < 1e-10, "迭代方法测试用例1失败"
    
    # 测试用例2：负数幂
    assert abs(solution.myPow(2.0, -2) - 0.25) < 1e-10, "测试用例2失败"
    assert abs(solution.myPow_iterative(2.0, -2) - 0.25) < 1e-10, "迭代方法测试用例2失败"
    
    # 测试用例3：零次幂
    assert abs(solution.myPow(2.0, 0) - 1.0) < 1e-10, "测试用例3失败"
    assert abs(solution.myPow_iterative(2.0, 0) - 1.0) < 1e-10, "迭代方法测试用例3失败"
    
    # 测试用例4：奇数次幂
    assert abs(solution.myPow(2.0, 3) - 8.0) < 1e-10, "测试用例4失败"
    assert abs(solution.myPow_iterative(2.0, 3) - 8.0) < 1e-10, "迭代方法测试用例4失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_fast_power() 