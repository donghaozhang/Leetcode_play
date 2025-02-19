from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        方法一：DFS + 回溯（选或不选）
        """
        def dfs_backtrack(start: int, curr: List[int]) -> None:
            # 将当前子集加入结果
            result.append(curr[:])
            
            # 从 start 开始遍历，避免重复
            for i in range(start, len(nums)):
                # 选择当前元素
                curr.append(nums[i])
                # 递归处理后面的元素
                dfs_backtrack(i + 1, curr)
                # 回溯，撤销选择
                curr.pop()
        
        result = []
        dfs_backtrack(0, [])
        return result
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """
        方法二：DFS + 循环（按位置枚举）
        """
        def dfs_position(pos: int, k: int, curr: List[int]) -> None:
            # 如果已经选择了 k 个元素，收集结果
            if len(curr) == k:
                result.append(curr[:])
                return
            
            # 从 pos 开始选择元素
            for i in range(pos, len(nums)):
                curr.append(nums[i])
                dfs_position(i + 1, k, curr)
                curr.pop()
        
        result = []
        # 枚举子集大小 k
        for k in range(len(nums) + 1):
            dfs_position(0, k, [])
        return result


# 测试代码
def test_subsets():
    solution = Solution()
    
    # 测试用例 1
    nums1 = [1,2,3]
    result1 = solution.subsets(nums1)
    expected1 = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    assert sorted(map(str, result1)) == sorted(map(str, expected1)), "测试用例 1 失败"
    
    # 测试用例 2
    nums2 = [1]
    result2 = solution.subsets(nums2)
    expected2 = [[], [1]]
    assert sorted(map(str, result2)) == sorted(map(str, expected2)), "测试用例 2 失败"
    
    # 测试用例 3：空数组
    nums3 = []
    result3 = solution.subsets(nums3)
    expected3 = [[]]
    assert result3 == expected3, "测试用例 3 失败"
    
    # 测试方法二
    result4 = solution.subsets2(nums1)
    assert sorted(map(str, result4)) == sorted(map(str, expected1)), "方法二测试失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_subsets() 