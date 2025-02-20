def fibonacci(n):
    """
    计算斐波那契数列的第n个数，使用滚动数组优化空间
    :param n: int，要计算的位置（从0开始）
    :return: int，第n个斐波那契数
    """
    if n <= 1:
        return n
        
    # 只使用两个变量来滚动计算
    prev, curr = 0, 1
    
    # 从2开始计算到n
    for _ in range(2, n + 1):
        # 计算下一个数
        prev, curr = curr, prev + curr
            
    return curr

def test_fibonacci():
    # 测试用例1：基本情况
    assert fibonacci(0) == 0, f"Expected 0, but got {fibonacci(0)}"
    assert fibonacci(1) == 1, f"Expected 1, but got {fibonacci(1)}"
    
    # 测试用例2：第5个数
    assert fibonacci(5) == 5, f"Expected 5, but got {fibonacci(5)}"
    
    # 测试用例3：第10个数
    assert fibonacci(10) == 55, f"Expected 55, but got {fibonacci(10)}"
    
    # 测试用例4：验证序列的前几个数
    sequence = [fibonacci(i) for i in range(7)]
    expected = [0, 1, 1, 2, 3, 5, 8]
    assert sequence == expected, f"Expected {expected}, but got {sequence}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_fibonacci() 