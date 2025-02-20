import subprocess
import os

# 按照题目类型归类文件
question_types = {
    'dynamic_programming': {
        'longest_increasing_subsequence': [
            'longest_increasing_subsequence.py',
            'longest_increasing_subsequence.md',
            'Longest_Increasing_Subsequence_Explanation.md'
        ],
        'palindrome': ['palindrome_substring.md', 'longest_palindrome.md'],
        'stone_game': ['stone_game.md', 'stone_game.py'],
        'burst_balloons': ['burst_balloons.md', 'burst_balloons.py'],
        'triangle': ['triangle.md', 'triangle.py'],
        'decode_ways': ['decode_ways.md', 'decode_ways.py'],
        'copy_books': ['copy_books.md', 'copy_books.py'],
        'largest_divisible_subset': ['largest_divisible_subset.md', 'largest_divisible_subset.py']
    },
    'string_processing': {
        'wildcard_matching': ['wildcard_matching.md', 'wildcard_matching.py'],
        'edit_distance': ['edit_distance.md', 'edit_distance.py'],
        'word_break': ['word_break.md', 'word_break.py']
    },
    'data_structure': {
        'max_stack': ['max_stack.md', 'max_stack.py'],
        'stack_by_two_queues': ['stack_by_two_queues.md', 'stack_by_two_queues.py'],
        'queue_by_two_stacks': ['queue_by_two_stacks.md', 'queue_by_two_stacks.py']
    },
    'backtracking': {
        'n_queens': ['n_queens_ii.py'],
        'subsets': ['subsets.md', 'subsets.py']
    },
    'game_theory': {
        'bash_game': ['bash_game.md', 'bash_game.py']
    },
    'graph_search': {
        'knight_shortest_path': [
            'knight_shortest_path.md', 
            'knight_shortest_path.py',
            'knight_shortest_path_ii.md',
            'knight_shortest_path_ii.py'
        ],
        'word_ladder': ['word_ladder.md', 'word_ladder.py']
    },
    'math': {
        'fast_power': ['fast_power.py', 'fast_power.md']
    }
}

def update_readme():
    # 题目中英文对照
    question_translations = {
        'longest_increasing_subsequence': ('最长上升子序列', 'Longest Increasing Subsequence'),
        'palindrome': ('回文子串', 'Palindrome Substring'),
        'stone_game': ('石子游戏', 'Stone Game'),
        'burst_balloons': ('戳气球', 'Burst Balloons'),
        'triangle': ('三角形最小路径和', 'Triangle'),
        'decode_ways': ('解码方法', 'Decode Ways'),
        'copy_books': ('复制书籍', 'Copy Books'),
        'largest_divisible_subset': ('最大整除子集', 'Largest Divisible Subset'),
        'wildcard_matching': ('通配符匹配', 'Wildcard Matching'),
        'edit_distance': ('编辑距离', 'Edit Distance'),
        'word_break': ('单词拆分', 'Word Break'),
        'max_stack': ('最大栈', 'Max Stack'),
        'stack_by_two_queues': ('用两个队列实现栈', 'Stack Using Two Queues'),
        'queue_by_two_stacks': ('用两个栈实现队列', 'Queue Using Two Stacks'),
        'n_queens': ('N皇后 II', 'N-Queens II'),
        'subsets': ('全子集', 'Subsets [LintCode 17]'),
        'bash_game': ('Bash游戏', 'Bash Game'),
        'knight_shortest_path': ('骑士最短路径', 'Knight Shortest Path'),
        'word_ladder': ('单词接龙', 'Word Ladder [LintCode 120]'),
        'fast_power': ('快速幂', 'Fast Power [LintCode 140]')
    }

    # 添加题目描述字典
    problem_descriptions = {
        'word_ladder': """
给出两个单词（start和end）和一个字典，找出从start到end的最短转换序列。
规则：
1. 每次只能改变一个字母
2. 变换过程中的每个单词都必须在字典中出现
3. start可以不在字典中
4. 返回最短转换序列的长度

例如：
- start = "hit"
- end = "cog"
- dict = ["hot","dot","dog","lot","log"]
返回 5
最短转换序列是: "hit" -> "hot" -> "dot" -> "dog" -> "cog"
""",
        'subsets': """
给定一个整数数组，返回其所有可能的子集。

注意：
1. 子集中的元素必须是非降序的
2. 解集不能包含重复的子集
3. 空集是所有集合的子集

例如：
输入：[1,2,3]
输出：
[
  [],
  [1],
  [1,2],
  [1,2,3],
  [1,3],
  [2],
  [2,3],
  [3]
]

解题思路：
可以用两种方式构建搜索树：
1. 组合式搜索树：每个节点代表是否选择当前数字
2. 排列式搜索树：每层代表枚举下一个可以选择的数字
""",
        'fast_power': """
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

要求时间复杂度为 O(log n)。

示例：
输入: x = 2.00000, n = 10
输出: 1024.00000

解题思路：
1. 递归方法：将指数二分，递归计算
2. 迭代方法：利用二进制思想，按位计算
"""
    }

    readme_content = """# LeetCode 题解

这个仓库包含了我的 LeetCode 题解，按照不同的算法类型进行分类。每个题目都包含了详细的解题思路和 Python 实现。
部分题目正在完善中...

"""
    
    for type_name, questions in question_types.items():
        readme_content += f"\n## {type_name.replace('_', ' ').title()}\n\n"
        for question, files in questions.items():
            chinese_name, english_name = question_translations.get(
                question, 
                (question.replace('_', ' ').title(), question.replace('_', ' ').title())
            )
            
            # 添加题目链接
            problem_link = ""
            if question == 'word_ladder':
                problem_link = "https://www.lintcode.com/problem/word-ladder/"
            elif question == 'subsets':
                problem_link = "http://www.lintcode.com/problem/subsets"
            
            # 生成文件链接（如果文件存在）
            python_file = next((f for f in files if f.endswith('.py')), None)
            python_path = f"leetcode_questions/{type_name}/{question}/{python_file}" if python_file else None
            python_link = f"[Python]({python_path})" if python_path and os.path.exists(python_path) else "🚧 Python"
            
            md_file = next((f for f in files if f.endswith('.md') and not f.startswith('README')), None)
            md_path = f"leetcode_questions/{type_name}/{question}/{md_file}" if md_file else None
            solution_link = f"[题解]({md_path})" if md_path and os.path.exists(md_path) else "🚧 题解"
            
            # 生成题目行
            readme_content += f"- {chinese_name} / {english_name}"
            if problem_link:
                readme_content += f" - [题目链接]({problem_link})"
            readme_content += f" - {python_link} - {solution_link}\n"
            
            # 只为已实现的题目添加描述
            if question in problem_descriptions and os.path.exists(python_path):
                readme_content += f"```\n{problem_descriptions[question].strip()}\n```\n\n"
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

def git_commit_and_push():
    try:
        status = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, 
                              text=True)
        
        if status.stdout.strip():
            subprocess.run(['git', 'add', '.'], check=True)
            commit_message = "更新 README.md"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            subprocess.run(['git', 'push'], check=True)
            print("成功提交并推送更改到远程仓库")
        else:
            print("没有需要提交的更改")
            
    except subprocess.CalledProcessError as e:
        print(f"Git 操作失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    update_readme()
    git_commit_and_push() 