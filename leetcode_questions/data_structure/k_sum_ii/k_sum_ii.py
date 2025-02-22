from typing import List

def k_sum_ii(numbers: List[int], k: int, target: int) -> List[List[int]]:
    """
    找出所有k个数之和等于target的组合
    :param numbers: List[int]，输入数组
    :param k: int，要选择的数字个数
    :param target: int，目标和
    :return: List[List[int]]，所有可能的组合
    """
    def backtrack(start: int, curr_k: int, curr_sum: int, path: List[int]) -> None:
        """
        回溯生成组合
        :param start: 当前可选择的起始位置
        :param curr_k: 当前已选择的数字个数
        :param curr_sum: 当前已选数字之和
        :param path: 当前组合
        """
        # 剪枝条件
        if curr_k > k:  # 使用数字过多
            return
        if curr_sum > target:  # 和超过目标
            return
        if len(numbers) - start < k - curr_k:  # 剩余数字不足
            return
            
        # 找到一个有效组合
        if curr_k == k and curr_sum == target:
            result.append(path[:])
            return
            
        # 尝试选择每个数字
        for i in range(start, len(numbers)):
            path.append(numbers[i])
            backtrack(i + 1, curr_k + 1, curr_sum + numbers[i], path)
            path.pop()
    
    result = []
    numbers.sort()  # 排序以便更好地剪枝
    backtrack(0, 0, 0, [])
    return result

def test_k_sum_ii():
    """测试k数之和II的实现"""
    # 测试用例1：基本情况
    numbers1 = [1, 2, 3, 4]
    k1 = 2
    target1 = 5
    expected1 = [[1, 4], [2, 3]]
    assert sorted(k_sum_ii(numbers1, k1, target1)) == sorted(expected1), \
        f"Expected {expected1}, but got {k_sum_ii(numbers1, k1, target1)}"
    
    # 测试用例2：没有解
    numbers2 = [1, 2, 3, 4]
    k2 = 3
    target2 = 15
    assert k_sum_ii(numbers2, k2, target2) == [], \
        "Should return empty list when no solution exists"
    
    # 测试用例3：k等于数组长度
    numbers3 = [1, 2, 3]
    k3 = 3
    target3 = 6
    expected3 = [[1, 2, 3]]
    assert k_sum_ii(numbers3, k3, target3) == expected3, \
        f"Expected {expected3}, but got {k_sum_ii(numbers3, k3, target3)}"
    
    # 测试用例4：多个解
    numbers4 = [1, 2, 3, 4, 5]
    k4 = 3
    target4 = 9
    result4 = k_sum_ii(numbers4, k4, target4)
    assert len(result4) > 1, "Should find multiple solutions"
    for combo in result4:
        assert len(combo) == k4, "Each combination should have k numbers"
        assert sum(combo) == target4, "Sum should equal target"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_k_sum_ii() 