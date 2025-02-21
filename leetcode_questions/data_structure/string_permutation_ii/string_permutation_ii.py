from typing import List
from collections import Counter

def string_permutation_ii(s: str) -> List[str]:
    """
    生成字符串的所有不重复排列
    :param s: str，输入字符串
    :return: List[str]，所有不重复的排列
    """
    def backtrack(counter: Counter, curr: List[str], length: int) -> None:
        """
        回溯生成排列
        :param counter: Counter，当前可用字符计数
        :param curr: List[str]，当前排列
        :param length: int，目标长度
        """
        if len(curr) == length:
            result.append(''.join(curr))
            return
        
        # 遍历所有可用字符
        for char in sorted(counter.keys()):  # 排序确保字典序
            if counter[char] > 0:
                # 选择当前字符
                curr.append(char)
                counter[char] -= 1
                
                # 递归生成剩余排列
                backtrack(counter, curr, length)
                
                # 回溯，撤销选择
                curr.pop()
                counter[char] += 1
    
    result = []
    if not s:
        return result
    
    # 统计字符频率
    counter = Counter(s)
    backtrack(counter, [], len(s))
    return result

def string_permutation_ii_iterative(s: str) -> List[str]:
    """
    使用迭代方法生成字符串的所有不重复排列
    :param s: str，输入字符串
    :return: List[str]，所有不重复的排列
    """
    if not s:
        return []
    
    # 初始化结果集
    result = ['']
    counter = Counter(s)
    
    # 对每个位置，尝试所有可能的字符
    for _ in range(len(s)):
        new_result = []
        for perm in result:
            # 计算当前排列后剩余可用字符
            curr_counter = Counter(s) - Counter(perm)
            # 尝试添加每个可用字符
            for char in sorted(curr_counter.keys()):
                if curr_counter[char] > 0:
                    new_result.append(perm + char)
        result = new_result
    
    return result

def test_string_permutation_ii():
    # 测试用例1：基本情况
    s1 = "abb"
    expected1 = ["abb", "bab", "bba"]
    assert sorted(string_permutation_ii(s1)) == expected1
    assert sorted(string_permutation_ii_iterative(s1)) == expected1
    
    # 测试用例2：所有字符相同
    s2 = "aaa"
    expected2 = ["aaa"]
    assert string_permutation_ii(s2) == expected2
    assert string_permutation_ii_iterative(s2) == expected2
    
    # 测试用例3：空字符串
    s3 = ""
    expected3 = []
    assert string_permutation_ii(s3) == expected3
    assert string_permutation_ii_iterative(s3) == expected3
    
    # 测试用例4：无重复字符
    s4 = "abc"
    expected4 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert sorted(string_permutation_ii(s4)) == expected4
    assert sorted(string_permutation_ii_iterative(s4)) == expected4
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_string_permutation_ii() 