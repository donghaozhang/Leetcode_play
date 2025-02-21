from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    """
    生成数组的所有排列
    :param nums: List[int]，输入数组
    :return: List[List[int]]，所有可能的排列
    """
    def backtrack(used: set, curr: List[int]) -> None:
        """
        回溯生成排列
        :param used: set，已使用的数字集合
        :param curr: List[int]，当前排列
        """
        if len(curr) == len(nums):
            result.append(curr[:])
            return
        
        for num in nums:
            if num not in used:
                # 选择当前数字
                used.add(num)
                curr.append(num)
                
                # 递归生成剩余排列
                backtrack(used, curr)
                
                # 回溯，撤销选择
                curr.pop()
                used.remove(num)
    
    result = []
    if not nums:
        return result
    
    backtrack(set(), [])
    return result

def permutations_iterative(nums: List[int]) -> List[List[int]]:
    """
    使用迭代方法生成数组的所有排列
    :param nums: List[int]，输入数组
    :return: List[List[int]]，所有可能的排列
    """
    if not nums:
        return []
    
    # 从单个元素的排列开始
    result = [[nums[0]]]
    
    # 逐个添加剩余的数字
    for i in range(1, len(nums)):
        new_result = []
        # 对于每个现有的排列
        for perm in result:
            # 在每个可能的位置插入新数字
            for j in range(len(perm) + 1):
                new_perm = perm[:]
                new_perm.insert(j, nums[i])
                new_result.append(new_perm)
        result = new_result
    
    return result

def test_permutations():
    # 测试用例1：基本情况
    nums1 = [1, 2, 3]
    expected1 = [
        [1, 2, 3], [1, 3, 2],
        [2, 1, 3], [2, 3, 1],
        [3, 1, 2], [3, 2, 1]
    ]
    assert sorted(permutations(nums1)) == sorted(expected1)
    assert sorted(permutations_iterative(nums1)) == sorted(expected1)
    
    # 测试用例2：空数组
    nums2 = []
    expected2 = []
    assert permutations(nums2) == expected2
    assert permutations_iterative(nums2) == expected2
    
    # 测试用例3：单个元素
    nums3 = [1]
    expected3 = [[1]]
    assert permutations(nums3) == expected3
    assert permutations_iterative(nums3) == expected3
    
    # 测试用例4：两个元素
    nums4 = [1, 2]
    expected4 = [[1, 2], [2, 1]]
    assert sorted(permutations(nums4)) == sorted(expected4)
    assert sorted(permutations_iterative(nums4)) == sorted(expected4)
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_permutations() 