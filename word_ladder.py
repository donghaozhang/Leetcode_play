from collections import deque
from typing import List, Set

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        计算从 beginWord 转换到 endWord 的最短转换序列的长度
        
        参数:
            beginWord: 起始单词
            endWord: 目标单词
            wordList: 单词字典
        返回:
            最短转换序列的长度，如果无法转换则返回 0
        """
        # 将 wordList 转换为集合，提高查找效率
        word_set = set(wordList)
        
        # 如果 endWord 不在字典中，无法完成转换
        if endWord not in word_set:
            return 0
            
        # 如果 beginWord 在字典中，将其移除（避免重复访问）
        if beginWord in word_set:
            word_set.remove(beginWord)
            
        # 使用双向 BFS
        begin_set = {beginWord}
        end_set = {endWord}
        word_set.remove(endWord)
        
        length = 1
        
        # 字母表
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # 当两个方向的搜索都未结束时继续
        while begin_set and end_set:
            # 总是从较小的集合开始搜索
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                
            # 存储下一层的单词
            next_level_set = set()
            
            # 遍历当前层的所有单词
            for word in begin_set:
                word_chars = list(word)
                
                # 尝试改变每个位置的字母
                for i in range(len(word)):
                    old_char = word_chars[i]
                    
                    # 尝试替换为 a-z 中的每个字母
                    for letter in letters:
                        word_chars[i] = letter
                        new_word = ''.join(word_chars)
                        
                        # 如果在另一方向的搜索中找到这个单词，说明找到了最短路径
                        if new_word in end_set:
                            return length + 1
                            
                        # 如果新单词在字典中，将其加入下一层
                        if new_word in word_set:
                            next_level_set.add(new_word)
                            word_set.remove(new_word)
                            
                    # 恢复原始字母
                    word_chars[i] = old_char
                    
            # 更新当前层为下一层
            begin_set = next_level_set
            length += 1
            
        # 无法完成转换
        return 0


# 测试代码
def test_word_ladder():
    solution = Solution()
    
    # 测试用例 1
    begin1 = "hit"
    end1 = "cog"
    dict1 = ["hot","dot","dog","lot","log","cog"]
    assert solution.ladderLength(begin1, end1, dict1) == 5, "测试用例 1 失败"
    
    # 测试用例 2：无法转换
    begin2 = "hit"
    end2 = "cog"
    dict2 = ["hot","dot","dog","lot","log"]
    assert solution.ladderLength(begin2, end2, dict2) == 0, "测试用例 2 失败"
    
    # 测试用例 3：起点等于终点
    begin3 = "hit"
    end3 = "hit"
    dict3 = ["hit"]
    assert solution.ladderLength(begin3, end3, dict3) == 1, "测试用例 3 失败"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_word_ladder() 