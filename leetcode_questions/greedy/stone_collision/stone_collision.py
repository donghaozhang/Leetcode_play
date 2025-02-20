import heapq

def min_stone_after_collision(stones):
    """
    计算石头碰撞后剩余的最小石头大小
    :param stones: List[int]，石头大小列表
    :return: int，最后剩下的石头的最小可能大小
    """
    if not stones:
        return 0
    if len(stones) == 1:
        return stones[0]
        
    # 将石头大小转换为负数并建堆，这样可以用最小堆实现最大堆
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    
    # 当还有至少两块石头时继续碰撞
    while len(stones) > 1:
        # 取出最大的两块石头
        stone1 = -heapq.heappop(stones)
        stone2 = -heapq.heappop(stones)
        
        # 计算碰撞后的大小
        diff = abs(stone1 - stone2)
        if diff > 0:  # 如果还有剩余，放回堆中
            heapq.heappush(stones, -diff)
    
    # 如果还有石头，返回其大小；否则返回0
    return -stones[0] if stones else 0

def min_stone_after_collision_pq(stones):
    """
    使用优先队列的另一种实现
    :param stones: List[int]，石头大小列表
    :return: int，最后剩下的石头的最小可能大小
    """
    if not stones:
        return 0
    if len(stones) == 1:
        return stones[0]
        
    # 创建优先队列（最大堆）
    pq = []
    for stone in stones:
        heapq.heappush(pq, -stone)  # 负数实现最大堆
    
    # 当队列中至少有两块石头时
    while len(pq) > 1:
        # 取出最大的两块石头
        x = -heapq.heappop(pq)
        y = -heapq.heappop(pq)
        
        # 如果碰撞后还有剩余
        if x != y:
            heapq.heappush(pq, -(abs(x - y)))
    
    # 返回最后剩下的石头大小，如果没有则返回0
    return -pq[0] if pq else 0

def test_min_stone_after_collision():
    # 测试用例1：基本情况
    stones1 = [2, 7, 4, 1, 8, 1]
    assert min_stone_after_collision(stones1) == 1, \
        f"Expected 1, but got {min_stone_after_collision(stones1)}"
    assert min_stone_after_collision_pq(stones1) == 1, \
        f"Expected 1, but got {min_stone_after_collision_pq(stones1)}"
    
    # 测试用例2：空数组
    assert min_stone_after_collision([]) == 0, "Expected 0 for empty array"
    assert min_stone_after_collision_pq([]) == 0, "Expected 0 for empty array"
    
    # 测试用例3：只有一块石头
    stones3 = [5]
    assert min_stone_after_collision(stones3) == 5, \
        f"Expected 5, but got {min_stone_after_collision(stones3)}"
    assert min_stone_after_collision_pq(stones3) == 5, \
        f"Expected 5, but got {min_stone_after_collision_pq(stones3)}"
    
    # 测试用例4：所有石头相同大小
    stones4 = [2, 2, 2, 2]
    assert min_stone_after_collision(stones4) == 0, \
        f"Expected 0, but got {min_stone_after_collision(stones4)}"
    assert min_stone_after_collision_pq(stones4) == 0, \
        f"Expected 0, but got {min_stone_after_collision_pq(stones4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_min_stone_after_collision() 