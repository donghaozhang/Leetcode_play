from typing import List
import heapq

def nth_ugly_number_dp(n: int) -> int:
    """
    使用动态规划找出第n个丑数
    :param n: int，要找的第n个丑数
    :return: int，第n个丑数
    """
    # dp[i]表示第i+1个丑数
    dp = [1] * n
    
    # 三个指针，分别指向乘以2、3、5后可能产生下一个丑数的位置
    p2 = p3 = p5 = 0
    
    for i in range(1, n):
        # 计算三个候选的下一个丑数
        next2 = dp[p2] * 2
        next3 = dp[p3] * 3
        next5 = dp[p5] * 5
        
        # 取最小的作为下一个丑数
        dp[i] = min(next2, next3, next5)
        
        # 更新对应的指针
        if dp[i] == next2:
            p2 += 1
        if dp[i] == next3:
            p3 += 1
        if dp[i] == next5:
            p5 += 1
    
    return dp[n-1]

def nth_ugly_number_heap(n: int) -> int:
    """
    使用最小堆找出第n个丑数
    :param n: int，要找的第n个丑数
    :return: int，第n个丑数
    """
    # 使用集合去重
    seen = {1}
    # 最小堆存储候选的丑数
    heap = [1]
    # 质因数列表
    factors = [2, 3, 5]
    
    # 找第n个丑数
    result = 1
    for _ in range(n):
        result = heapq.heappop(heap)
        # 生成下一组候选的丑数
        for factor in factors:
            new_ugly = result * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    return result

def test_nth_ugly_number():
    # 测试用例1：基本情况
    assert nth_ugly_number_dp(1) == 1, "First ugly number should be 1"
    assert nth_ugly_number_heap(1) == 1, "First ugly number should be 1"
    
    # 测试用例2：前10个丑数
    expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    for i, expected_value in enumerate(expected, 1):
        assert nth_ugly_number_dp(i) == expected_value, \
            f"DP: {i}th ugly number should be {expected_value}"
        assert nth_ugly_number_heap(i) == expected_value, \
            f"Heap: {i}th ugly number should be {expected_value}"
    
    # 测试用例3：较大的n
    n = 15
    dp_result = nth_ugly_number_dp(n)
    heap_result = nth_ugly_number_heap(n)
    assert dp_result == heap_result, \
        f"Both methods should give same result for n={n}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_nth_ugly_number() 