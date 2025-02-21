from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    找出所有和为target的组合，每个数字可以重复使用
    :param candidates: List[int]，候选数字列表
    :param target: int，目标和
    :return: List[List[int]]，所有可能的组合
    """
    def backtrack(start: int, remain: int, curr: List[int]) -> None:
        """
        回溯生成组合
        :param start: int，当前可选数字的起始索引
        :param remain: int，剩余需要的和
        :param curr: List[int]，当前组合
        """
        if remain == 0:
            # 找到一个有效组合
            result.append(curr[:])
            return
        
        for i in range(start, len(candidates)):
            # 剪枝：如果当前数字已经大于剩余和，后面的更大数字都不需要尝试
            if candidates[i] > remain:
                break
                
            # 选择当前数字
            curr.append(candidates[i])
            # 因为可以重复使用，所以下一轮从i开始
            backtrack(i, remain - candidates[i], curr)
            # 回溯，撤销选择
            curr.pop()
    
    # 排序以便剪枝
    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result

def combination_sum_iterative(candidates: List[int], target: int) -> List[List[int]]:
    """
    使用迭代方法找出所有和为target的组合
    :param candidates: List[int]，候选数字列表
    :param target: int，目标和
    :return: List[List[int]]，所有可能的组合
    """
    candidates.sort()
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # 和为0的组合是空列表
    
    # 对每个可能的和，尝试添加每个候选数字
    for i in range(1, target + 1):
        for num in candidates:
            # 如果当前数字已经大于目标和，后面的更大数字都不需要尝试
            if num > i:
                break
            
            # 将num添加到所有和为(i-num)的组合中
            for prev_comb in dp[i - num]:
                # 确保组合是非递减的（避免重复）
                if not prev_comb or num >= prev_comb[-1]:
                    dp[i].append(prev_comb + [num])
    
    return dp[target]

def test_combination_sum():
    # 测试用例1：基本情况
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    assert sorted(map(sorted, combination_sum(candidates1.copy(), target1))) == \
           sorted(map(sorted, expected1))
    assert sorted(map(sorted, combination_sum_iterative(candidates1.copy(), target1))) == \
           sorted(map(sorted, expected1))
    
    # 测试用例2：没有解
    candidates2 = [2, 4]
    target2 = 1
    expected2 = []
    assert combination_sum(candidates2.copy(), target2) == expected2
    assert combination_sum_iterative(candidates2.copy(), target2) == expected2
    
    # 测试用例3：多个解
    candidates3 = [2, 3, 5]
    target3 = 8
    expected3 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted(map(sorted, combination_sum(candidates3.copy(), target3))) == \
           sorted(map(sorted, expected3))
    assert sorted(map(sorted, combination_sum_iterative(candidates3.copy(), target3))) == \
           sorted(map(sorted, expected3))
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_combination_sum() 