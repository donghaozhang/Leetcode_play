from typing import List

def letter_combinations(digits: str) -> List[str]:
    """
    生成电话号码的所有可能的字母组合
    :param digits: str，输入的数字字符串
    :return: List[str]，所有可能的字母组合
    """
    if not digits:
        return []
        
    # 数字到字母的映射
    DIGIT_TO_LETTERS = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: List[str]) -> None:
        """
        回溯生成组合
        :param index: 当前处理的数字索引
        :param path: 当前路径
        """
        if len(path) == len(digits):
            result.append(''.join(path))
            return
            
        for letter in DIGIT_TO_LETTERS[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    result = []
    backtrack(0, [])
    return result

def test_letter_combinations():
    """测试电话号码的字母组合"""
    # 测试用例1：基本情况
    digits1 = "23"
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(letter_combinations(digits1)) == sorted(expected1), \
        f"Expected {expected1}, but got {letter_combinations(digits1)}"
    
    # 测试用例2：空字符串
    assert letter_combinations("") == [], \
        "Should return empty list for empty input"
    
    # 测试用例3：单个数字
    digits3 = "2"
    expected3 = ["a", "b", "c"]
    assert sorted(letter_combinations(digits3)) == sorted(expected3), \
        f"Expected {expected3}, but got {letter_combinations(digits3)}"
    
    # 测试用例4：包含4个数字
    digits4 = "2345"
    result4 = letter_combinations(digits4)
    assert len(result4) == 3 * 3 * 3 * 3, \
        "Should generate correct number of combinations"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_letter_combinations() 