def min_cost_for_coupon(prices, target):
    """
    计算使用满减券所需的最小花费
    :param prices: List[int]，菜品价格列表
    :param target: int，满减券的满减金额
    :return: int，最小花费，如果无法使用满减券返回-1
    """
    if not prices:
        return -1
        
    # dp[i] 表示是否能组成金额i
    dp = [False] * (target + 1)
    dp[0] = True  # 不选任何菜品，金额为0
    
    # 记录可以达到的最小金额（大于等于target）
    min_valid_sum = float('inf')
    
    # 当前可以组成的所有金额
    current_sums = {0}
    
    # 对每个菜品
    for price in prices:
        # 记录这轮新增的金额
        new_sums = set()
        # 对当前已有的每个金额
        for curr_sum in current_sums:
            new_sum = curr_sum + price
            # 如果新金额大于等于target，更新最小有效金额
            if new_sum >= target:
                min_valid_sum = min(min_valid_sum, new_sum)
            # 否则记录新金额（避免金额过大）
            elif new_sum < target:
                new_sums.add(new_sum)
        # 更新当前可组成的金额集合
        current_sums.update(new_sums)
    
    return min_valid_sum if min_valid_sum != float('inf') else -1

def test_min_cost_for_coupon():
    # 测试用例1：基本情况
    prices1 = [12, 5, 8, 4]
    target1 = 15
    assert min_cost_for_coupon(prices1, target1) == 16, \
        f"Expected 16, but got {min_cost_for_coupon(prices1, target1)}"
    
    # 测试用例2：空数组
    assert min_cost_for_coupon([], 10) == -1, \
        "Expected -1 for empty array"
    
    # 测试用例3：恰好满足
    prices3 = [5, 10, 15]
    target3 = 15
    assert min_cost_for_coupon(prices3, target3) == 15, \
        f"Expected 15, but got {min_cost_for_coupon(prices3, target3)}"
    
    # 测试用例4：无法满足条件
    prices4 = [1, 2, 3]
    target4 = 20
    assert min_cost_for_coupon(prices4, target4) == -1, \
        f"Expected -1, but got {min_cost_for_coupon(prices4, target4)}"
    
    # 测试用例5：多种组合
    prices5 = [8, 7, 6, 5, 4]
    target5 = 16
    assert min_cost_for_coupon(prices5, target5) == 16, \
        f"Expected 16, but got {min_cost_for_coupon(prices5, target5)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_min_cost_for_coupon() 