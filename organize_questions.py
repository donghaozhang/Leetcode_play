import os
import shutil
import glob
import subprocess

# 按照题目类型归类文件
question_types = {
    'backtracking': {
        'subsets': ['subsets.md', 'subsets.py']
    },
    'graph_search': {
        'word_ladder': ['word_ladder.md', 'word_ladder.py']
    },
    'math': {
        'fast_power': ['fast_power.py', 'fast_power.md']
    }
}

def update_readme():
    # 题目中英文对照
    question_translations = {
        'subsets': ('全子集', 'Subsets [LintCode 17]'),
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
            
            # 查找 Python 文件
            python_file = next((f for f in files if f.endswith('.py')), None)
            python_link = f"[Python](leetcode_questions/{type_name}/{question}/{python_file})" if python_file else "Python"
            
            # 查找 Markdown 文件（说明文件）
            md_file = next((f for f in files if f.endswith('.md') and not f.startswith('README')), None)
            solution_link = f"[题解](leetcode_questions/{type_name}/{question}/{md_file})" if md_file else ""
            
            # 生成题目行，添加题目链接
            readme_content += f"- {chinese_name} / {english_name}"
            if problem_link:
                readme_content += f" - [题目链接]({problem_link})"
            readme_content += f" - {python_link}"
            if solution_link:
                readme_content += f" - {solution_link}"
            readme_content += "\n"
            
            # 如果有题目描述，添加描述
            if question in problem_descriptions:
                readme_content += f"```\n{problem_descriptions[question].strip()}\n```\n\n"
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

def git_commit_and_push():
    try:
        # 检查是否有更改需要提交
        status = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, 
                              text=True)
        
        if status.stdout.strip():
            # 添加所有更改
            subprocess.run(['git', 'add', '.'], check=True)
            
            # 提交更改
            commit_message = "整理 LeetCode 题解文件结构"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            
            # 推送到远程仓库
            subprocess.run(['git', 'push'], check=True)
            print("成功提交并推送更改到远程仓库")
        else:
            print("没有需要提交的更改")
            
    except subprocess.CalledProcessError as e:
        print(f"Git 操作失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

def organize_files():
    # 获取当前目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    
    # 列出当前目录下的所有文件
    all_files = glob.glob('*.*')
    print(f"找到的文件: {all_files}")
    
    # 创建基础目录
    base_dir = 'leetcode_questions'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # 如果存在旧的 questions 目录，移动其内容
    old_questions_dir = 'questions'
    if os.path.exists(old_questions_dir):
        for item in os.listdir(old_questions_dir):
            src_path = os.path.join(old_questions_dir, item)
            dst_path = os.path.join(base_dir, item)
            if os.path.isdir(src_path):
                if not os.path.exists(dst_path):
                    shutil.copytree(src_path, dst_path)
                else:
                    for file in os.listdir(src_path):
                        shutil.move(
                            os.path.join(src_path, file),
                            os.path.join(dst_path, file)
                        )
        # 删除旧的 questions 目录
        shutil.rmtree(old_questions_dir)
    
    # 为每种类型创建文件夹并移动文件
    for type_name, questions in question_types.items():
        # 创建类型目录
        type_dir = os.path.join(base_dir, type_name)
        if not os.path.exists(type_dir):
            os.makedirs(type_dir)
        
        # 为每个问题创建子目录
        for question, files in questions.items():
            question_dir = os.path.join(type_dir, question)
            if not os.path.exists(question_dir):
                os.makedirs(question_dir)
            
            # 移动相关文件
            for file in files:
                file_path = os.path.join(current_dir, file)
                if os.path.exists(file_path):
                    print(f"移动文件: {file} 到 {question_dir}")
                    shutil.move(file_path, os.path.join(question_dir, file))
                else:
                    print(f"警告: 未找到文件 {file}")
    
    # 更新 README.md
    update_readme()
    
    # 提交并推送更改
    git_commit_and_push()

if __name__ == "__main__":
    organize_files() 