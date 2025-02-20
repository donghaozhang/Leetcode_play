def backpack(m, A):
    """
    计算大小为m的背包最多能装多少
    :param m: int，背包大小
    :param A: List[int]，物品大小列表
    :return: int，最大能装的大小
    """
    if not A or m <= 0:
        return 0
        
    n = len(A)
    # dp[i][j] 表示前i个物品能否组成大小j
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True  # 空背包可以组成大小0
    
    # 对每个物品
    for i in range(1, n + 1):
        dp[i][0] = True  # 不选任何物品可以组成大小0
        # 对每个大小
        for j in range(m + 1):
            # 不选第i个物品
            dp[i][j] = dp[i-1][j]
            # 选第i个物品（如果大小允许）
            if j >= A[i-1]:
                dp[i][j] |= dp[i-1][j-A[i-1]]
    
    # 找到最大的可行大小
    for j in range(m, -1, -1):
        if dp[n][j]:
            return j
            
    return 0

def backpack_optimized(m, A):
    """
    使用滚动数组优化空间的解法
    :param m: int，背包大小
    :param A: List[int]，物品大小列表
    :return: int，最大能装的大小
    """
    if not A or m <= 0:
        return 0
        
    # 只使用一维数组
    dp = [False] * (m + 1)
    dp[0] = True
    
    # 对每个物品
    for item in A:
        # 从大到小遍历，避免重复使用同一个物品
        for j in range(m, item - 1, -1):
            dp[j] |= dp[j - item]
    
    # 找到最大的可行大小
    for j in range(m, -1, -1):
        if dp[j]:
            return j
            
    return 0

def test_backpack():
    # 测试用例1：基本情况
    m1, A1 = 10, [3, 4, 8, 5]
    assert backpack(m1, A1) == 9, f"Expected 9, but got {backpack(m1, A1)}"
    assert backpack_optimized(m1, A1) == 9, f"Expected 9, but got {backpack_optimized(m1, A1)}"
    
    # 测试用例2：空数组
    assert backpack(5, []) == 0, "Expected 0 for empty array"
    assert backpack_optimized(5, []) == 0, "Expected 0 for empty array"
    
    # 测试用例3：背包大小为0
    assert backpack(0, [1, 2, 3]) == 0, "Expected 0 for zero capacity"
    assert backpack_optimized(0, [1, 2, 3]) == 0, "Expected 0 for zero capacity"
    
    # 测试用例4：恰好装满
    m4, A4 = 5, [2, 3]
    assert backpack(m4, A4) == 5, f"Expected 5, but got {backpack(m4, A4)}"
    assert backpack_optimized(m4, A4) == 5, f"Expected 5, but got {backpack_optimized(m4, A4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_backpack() 