def backpack_iii(A, V, m):
    """
    计算在背包容量m下能获得的最大价值（物品可重复选择）
    :param A: List[int]，物品大小列表
    :param V: List[int]，物品价值列表
    :param m: int，背包容量
    :return: int，最大价值
    """
    if not A or not V or m <= 0:
        return 0
        
    n = len(A)
    # dp[i] 表示容量为i时能获得的最大价值
    dp = [0] * (m + 1)
    
    # 对每个物品
    for i in range(n):
        # 从小到大遍历容量（因为物品可以重复使用）
        for j in range(A[i], m + 1):
            # 选择当前物品，加上剩余容量的最大价值
            dp[j] = max(dp[j], dp[j - A[i]] + V[i])
    
    return dp[m]

def backpack_iii_2d(A, V, m):
    """
    使用二维数组的实现（更容易理解）
    :param A: List[int]，物品大小列表
    :param V: List[int]，物品价值列表
    :param m: int，背包容量
    :return: int，最大价值
    """
    if not A or not V or m <= 0:
        return 0
        
    n = len(A)
    # dp[i][j] 表示前i个物品，容量为j时能获得的最大价值
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 对每个物品
    for i in range(1, n + 1):
        for j in range(m + 1):
            # 不选第i个物品
            dp[i][j] = dp[i-1][j]
            # 选择第i个物品（可以重复选择）
            if j >= A[i-1]:
                dp[i][j] = max(dp[i][j], dp[i][j-A[i-1]] + V[i-1])
    
    return dp[n][m]

def test_backpack_iii():
    # 测试用例1：基本情况
    A1 = [2, 3, 5, 6]
    V1 = [1, 5, 2, 4]
    m1 = 10
    assert backpack_iii(A1, V1, m1) == 15, \
        f"Expected 15, but got {backpack_iii(A1, V1, m1)}"
    assert backpack_iii_2d(A1, V1, m1) == 15, \
        f"Expected 15, but got {backpack_iii_2d(A1, V1, m1)}"
    
    # 测试用例2：空数组
    assert backpack_iii([], [], 5) == 0, "Expected 0 for empty arrays"
    assert backpack_iii_2d([], [], 5) == 0, "Expected 0 for empty arrays"
    
    # 测试用例3：背包容量为0
    A3 = [1, 2, 3]
    V3 = [1, 2, 3]
    assert backpack_iii(A3, V3, 0) == 0, "Expected 0 for zero capacity"
    assert backpack_iii_2d(A3, V3, 0) == 0, "Expected 0 for zero capacity"
    
    # 测试用例4：只能选一种物品多次
    A4 = [2, 4, 6]
    V4 = [3, 4, 5]
    m4 = 8
    assert backpack_iii(A4, V4, m4) == 12, \
        f"Expected 12, but got {backpack_iii(A4, V4, m4)}"
    assert backpack_iii_2d(A4, V4, m4) == 12, \
        f"Expected 12, but got {backpack_iii_2d(A4, V4, m4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_backpack_iii() 