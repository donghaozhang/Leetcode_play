import os
import requests
import re
import random
import json
import subprocess
from dotenv import load_dotenv
import webbrowser
from datetime import datetime

# Load environment variables from .env file
load_dotenv("c:/Users/zdhpe/Desktop/Job_Search/bike_repair_repo/bike_repair_agent/.env")


# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OpenRouter API key not found. Please check your .env file.")

# Function to read README.md and extract LeetCode questions
def extract_leetcode_questions(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all LeetCode questions with their numbers
    leetcode_pattern = r'([^/]+) / ([^[]+) \[LeetCode (\d+)\]'
    matches = re.findall(leetcode_pattern, content)
    
    leetcode_questions = []
    for match in matches:
        chinese_name, english_name, leetcode_number = match
        folder_name = f"deepseek_solutions/leetcode_{leetcode_number}_{english_name.strip().lower().replace(' ', '_')}"
        is_solved = os.path.exists(folder_name)
        
        leetcode_questions.append({
            'chinese_name': chinese_name.strip(),
            'english_name': english_name.strip(),
            'leetcode_number': leetcode_number,
            'full_name': f"{chinese_name.strip()} / {english_name.strip()} [LeetCode {leetcode_number}]",
            'is_solved': is_solved,
            'folder_name': folder_name
        })
    
    return leetcode_questions

# Function to get problem description from LeetCode using DeepSeek
def get_leetcode_problem_description(problem_number):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-deepseek-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode DeepSeek Solver"
    }
    
    prompt = f"Please provide the full description of LeetCode problem #{problem_number}, including examples and constraints. Return only the problem description as it appears on LeetCode."
    
    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that provides information about LeetCode problems."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return f"Unable to retrieve problem description for LeetCode #{problem_number}"

# Function to solve LeetCode problem using DeepSeek via OpenRouter API
def solve_leetcode_problem(problem_description, problem_name):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-deepseek-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode DeepSeek Solver"
    }
    
    prompt = f"""
Problem: {problem_name}

Description:
{problem_description}

Please provide:
1. An explanation of the problem
2. A step-by-step approach to solve it
3. A Python solution with time and space complexity analysis. Make sure the Python solution is complete, runnable, and includes test cases.
4. Test cases to verify the solution
"""
    
    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are an expert at solving LeetCode problems. Provide clear, optimized solutions with detailed explanations."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }
    
    print(f"DeepSeek解题中: {problem_name}...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return f"Unable to solve the problem due to an API error."

# Function to extract Python code from markdown solution
def extract_python_code(markdown_content):
    # Find all Python code blocks
    python_blocks = re.findall(r'```python\n(.*?)```', markdown_content, re.DOTALL)
    
    if not python_blocks:
        return None
    
    # Return the largest Python code block (usually the solution)
    return max(python_blocks, key=len)

# Function to create a runnable Python file with extracted code
def create_python_file(python_code, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(python_code)

# Function to check if a solution already exists
def check_existing_solution(folder_path):
    if not os.path.exists(folder_path):
        return False, None, None, None
    
    # Check for solution.md and solution.py
    md_path = os.path.join(folder_path, "solution.md")
    py_path = os.path.join(folder_path, "solution.py")
    
    if os.path.exists(md_path) and os.path.exists(py_path):
        # Get creation time
        creation_time = datetime.fromtimestamp(os.path.getctime(md_path))
        
        # Read files to return content
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        with open(py_path, 'r', encoding='utf-8') as f:
            py_content = f.read()
        
        return True, md_content, py_content, creation_time
    
    return False, None, None, None

# Function to compare solutions from different models
def compare_with_llama_solution(problem_number, english_name):
    llama_folder = f"llama4_maverick_solutions/leetcode_{problem_number}_{english_name.strip().lower().replace(' ', '_')}"
    if not os.path.exists(llama_folder):
        return "No Llama-4 solution found for comparison."
    
    llama_md_path = os.path.join(llama_folder, "solution.md")
    if not os.path.exists(llama_md_path):
        return "No Llama-4 solution markdown found for comparison."
    
    with open(llama_md_path, 'r', encoding='utf-8') as f:
        llama_md_content = f.read()
    
    # Ask DeepSeek to compare solutions
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-deepseek-solver.example.com",
        "X-Title": "LeetCode Model Comparison"
    }
    
    # Get DeepSeek solution
    deepseek_folder = f"deepseek_solutions/leetcode_{problem_number}_{english_name.strip().lower().replace(' ', '_')}"
    deepseek_md_path = os.path.join(deepseek_folder, "solution.md")
    
    if not os.path.exists(deepseek_md_path):
        return "DeepSeek solution not found for comparison."
    
    with open(deepseek_md_path, 'r', encoding='utf-8') as f:
        deepseek_md_content = f.read()
    
    prompt = f"""
Please compare the following two solutions for the same LeetCode problem:

SOLUTION 1 (Llama-4):
{llama_md_content}

SOLUTION 2 (DeepSeek):
{deepseek_md_content}

Provide a detailed comparison focusing on:
1. Algorithm approach differences
2. Code quality and readability
3. Time and space complexity differences
4. Strengths and weaknesses of each solution
5. Overall assessment of which solution is better and why
"""
    
    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "You are an expert at comparing coding solutions and providing insightful analysis."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    print("Comparing solutions from Llama-4 and DeepSeek...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        comparison = response.json()["choices"][0]["message"]["content"]
        
        # Save comparison to file
        comparison_folder = "model_comparisons"
        os.makedirs(comparison_folder, exist_ok=True)
        comparison_path = os.path.join(comparison_folder, f"comparison_leetcode_{problem_number}.md")
        
        with open(comparison_path, 'w', encoding='utf-8') as f:
            f.write(f"# Solution Comparison for LeetCode {problem_number}\n\n")
            f.write(comparison)
        
        print(f"Comparison saved to {comparison_path}")
        return comparison
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return "Failed to generate comparison due to API error."

# Function to process a single problem iteratively
def process_problem(selected_question, run_tests=True, compare_with_llama=True):
    problem_number = selected_question['leetcode_number']
    print(f"\n处理题目: {selected_question['full_name']}")
    
    # Create folder structure
    folder_name = selected_question['folder_name']
    os.makedirs(folder_name, exist_ok=True)
    
    # Check if solution already exists
    exists, md_content, py_content, creation_time = check_existing_solution(folder_name)
    
    solution_md_path = os.path.join(folder_name, "solution.md")
    solution_py_path = os.path.join(folder_name, "solution.py")
    
    if exists:
        print(f"  已有DeepSeek解决方案(创建于: {creation_time.strftime('%Y-%m-%d %H:%M:%S')})")
        print(f"  跳过此题并继续...")
        return {
            "problem_number": problem_number,
            "status": "existing",
            "solution_path": solution_md_path,
            "execution_result": None,
            "comparison_result": None
        }
    
    # Get problem description
    problem_description = get_leetcode_problem_description(problem_number)
    print(f"  已获取题目描述")
    
    # Solve the problem
    solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
    print(f"  已生成解决方案")
    
    # Save solution to markdown file
    with open(solution_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {selected_question['full_name']}\n\n")
        f.write("## Problem Description\n\n")
        f.write(problem_description)
        f.write("\n\n## Solution\n\n")
        f.write(solution)
    
    print(f"  已保存解决方案到 {solution_md_path}")
    
    # Extract Python code and save to Python file
    python_code = extract_python_code(solution)
    execution_result = None
    
    if python_code:
        create_python_file(python_code, solution_py_path)
        print(f"  已提取Python代码并保存到 {solution_py_path}")
        
        # Run the solution if requested
        if run_tests:
            try:
                print(f"  运行解决方案...")
                result = subprocess.run(["python", solution_py_path], capture_output=True, text=True, timeout=30)
                execution_result = {
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "success": result.returncode == 0
                }
                
                print(f"  运行结果: {'成功' if result.returncode == 0 else '失败'}")
                if result.stderr:
                    print(f"  错误信息: {result.stderr[:100]}...")
            except Exception as e:
                print(f"  运行解决方案时出错: {e}")
                execution_result = {
                    "stdout": "",
                    "stderr": str(e),
                    "success": False
                }
    else:
        print(f"  在解决方案中未找到Python代码")
    
    # Compare with Llama solution if requested
    comparison_result = None
    if compare_with_llama:
        llama_folder = f"llama4_maverick_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
        if os.path.exists(llama_folder):
            print(f"  检测到已有Llama-4解决方案，进行比较...")
            comparison = compare_with_llama_solution(problem_number, selected_question['english_name'])
            comparison_result = comparison
            print(f"  已完成解决方案比较")
    
    return {
        "problem_number": problem_number,
        "status": "new",
        "solution_path": solution_md_path,
        "execution_result": execution_result,
        "comparison_result": comparison_result is not None
    }

# Function to generate solutions iteratively for multiple problems
def iterative_solution_generation(leetcode_questions, num_problems=5, run_tests=True, compare_with_llama=True):
    # Filter unsolved questions
    unsolved_questions = [q for q in leetcode_questions if not q['is_solved']]
    
    if not unsolved_questions:
        print("没有未解决的题目，无法迭代生成解决方案。")
        return
    
    # Limit to the specified number or available unsolved problems
    num_to_solve = min(num_problems, len(unsolved_questions))
    questions_to_solve = unsolved_questions[:num_to_solve]
    
    print(f"\n===== DeepSeek LeetCode 迭代解题 =====")
    print(f"将依次解决 {num_to_solve} 道题目")
    
    results = []
    start_time = datetime.now()
    
    # Process each problem one by one
    for i, question in enumerate(questions_to_solve, 1):
        print(f"\n[{i}/{num_to_solve}] 开始处理题目 {question['leetcode_number']}: {question['english_name']}")
        result = process_problem(question, run_tests, compare_with_llama)
        results.append(result)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() / 60
    
    # Generate summary report
    successful_count = sum(1 for r in results if r["status"] == "new" and (r["execution_result"] is None or r["execution_result"]["success"]))
    failed_count = sum(1 for r in results if r["status"] == "new" and r["execution_result"] is not None and not r["execution_result"]["success"])
    skipped_count = sum(1 for r in results if r["status"] == "existing")
    
    print("\n===== 迭代解题完成 =====")
    print(f"总用时: {duration:.2f} 分钟")
    print(f"总处理题目: {len(results)}")
    print(f"新生成解决方案: {len(results) - skipped_count}")
    print(f"  - 运行成功: {successful_count}")
    print(f"  - 运行失败: {failed_count}")
    print(f"跳过已有解决方案: {skipped_count}")
    
    # Generate detailed report file
    report_folder = "deepseek_reports"
    os.makedirs(report_folder, exist_ok=True)
    report_file = os.path.join(report_folder, f"iterative_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# DeepSeek LeetCode 迭代解题报告\n\n")
        f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"总用时: {duration:.2f} 分钟\n\n")
        f.write(f"## 概要\n\n")
        f.write(f"- 总处理题目: {len(results)}\n")
        f.write(f"- 新生成解决方案: {len(results) - skipped_count}\n")
        f.write(f"  - 运行成功: {successful_count}\n")
        f.write(f"  - 运行失败: {failed_count}\n")
        f.write(f"- 跳过已有解决方案: {skipped_count}\n\n")
        
        f.write("## 详细结果\n\n")
        for result in results:
            status_str = "已有解决方案，已跳过" if result["status"] == "existing" else "新生成解决方案"
            execution_str = ""
            if result["status"] == "new" and result["execution_result"] is not None:
                execution_str = "- 运行结果: " + ("成功" if result["execution_result"]["success"] else "失败")
                if not result["execution_result"]["success"] and result["execution_result"]["stderr"]:
                    execution_str += f"\n- 错误信息: ```\n{result['execution_result']['stderr'][:500]}...\n```"
            
            comparison_str = ""
            if result["status"] == "new" and result["comparison_result"]:
                comparison_str = "- 已与Llama-4解决方案进行比较"
            
            f.write(f"### LeetCode {result['problem_number']}\n\n")
            f.write(f"- 状态: {status_str}\n")
            f.write(f"- 解决方案路径: {result['solution_path']}\n")
            if execution_str:
                f.write(f"{execution_str}\n")
            if comparison_str:
                f.write(f"{comparison_str}\n")
            f.write("\n")
    
    print(f"\n详细报告已保存到: {report_file}")
    
    return report_file

# Main function
def main():
    readme_path = "README.md"
    
    # Extract LeetCode questions from README
    leetcode_questions = extract_leetcode_questions(readme_path)
    
    if not leetcode_questions:
        print("没有在README.md文件中找到LeetCode题目。")
        return
    
    # Count solved and unsolved questions
    solved_count = sum(1 for q in leetcode_questions if q['is_solved'])
    total_count = len(leetcode_questions)
    
    print("\n===== DeepSeek LeetCode Solver =====")
    print(f"当前DeepSeek进度: 已解决 {solved_count}/{total_count} 题 ({(solved_count/total_count*100):.1f}%)")
    print(f"未解决: {total_count - solved_count} 题")
    
    # Ask for operation mode
    print("\n请选择操作模式:")
    print("1. 交互式解题 (单题处理，有交互提示)")
    print("2. 迭代式解题 (批量处理多道题目)")
    
    mode_choice = input("\n输入选项 (1 或 2，默认为 1): ").strip()
    
    if mode_choice == "2":
        # Iterative mode
        num_problems_str = input("\n要迭代解决的题目数量 (默认 5): ").strip()
        try:
            num_problems = int(num_problems_str) if num_problems_str else 5
        except:
            num_problems = 5
        
        run_tests_choice = input("是否运行生成的代码以验证解决方案? (y/n, 默认 y): ").lower().strip()
        run_tests = run_tests_choice != 'n'
        
        compare_choice = input("是否与已有的Llama-4解决方案进行比较? (y/n, 默认 y): ").lower().strip()
        compare_with_llama = compare_choice != 'n'
        
        report_file = iterative_solution_generation(
            leetcode_questions, 
            num_problems, 
            run_tests, 
            compare_with_llama
        )
        
        # Ask if user wants to view the report
        view_report = input("\n是否在浏览器中查看生成报告? (y/n, 默认 y): ").lower().strip()
        if view_report != 'n' and report_file:
            try:
                webbrowser.open(f"file://{os.path.abspath(report_file)}")
                print(f"已在浏览器中打开报告")
            except:
                print(f"无法在浏览器中打开。报告位置: {os.path.abspath(report_file)}")
    else:
        # Interactive mode - original functionality
        # Ask if user wants to see solved problems
        show_solved = input("\n是否显示已解决的题目？(y/n, 默认n): ").lower().strip() == 'y'
        
        # Display available LeetCode questions
        print(f"\n找到 {len(leetcode_questions)} 个 LeetCode 题目在 README.md 中:")
        available_questions = []
        for i, question in enumerate(leetcode_questions, 1):
            if not question['is_solved'] or show_solved:
                status = "[已解决]" if question['is_solved'] else "[未解决]"
                print(f"{i}. {status} {question['full_name']}")
                available_questions.append(question)
        
        if not available_questions:
            print("\n恭喜！所有题目都已解决！")
            return
        
        # Choose a random question or let user select
        try:
            choice = input("\n输入题目编号来解题 (或直接按回车随机选择一题): ")
            if choice.strip():
                index = int(choice) - 1
                if 0 <= index < len(available_questions):
                    selected_question = available_questions[index]
                else:
                    print("无效的选择。随机选择一题。")
                    # Only select from unsolved questions if not showing solved ones
                    candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
                    selected_question = random.choice(candidates)
            else:
                # Only select from unsolved questions if not showing solved ones
                candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
                selected_question = random.choice(candidates)
        except:
            print("无效的输入。随机选择一题。")
            # Only select from unsolved questions if not showing solved ones
            candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
            selected_question = random.choice(candidates)
        
        problem_number = selected_question['leetcode_number']
        print(f"\n已选择题目: {selected_question['full_name']}")
        
        # Create folder structure
        folder_name = selected_question['folder_name']
        os.makedirs(folder_name, exist_ok=True)
        
        # Check if solution already exists
        exists, md_content, py_content, creation_time = check_existing_solution(folder_name)
        
        if exists:
            print(f"\n发现已有DeepSeek解决方案！创建于: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
            solution_md_path = os.path.join(folder_name, "solution.md")
            solution_py_path = os.path.join(folder_name, "solution.py")
            
            print(f"\n解决方案存储位置:")
            print(f"- Markdown 文件: {solution_md_path}")
            print(f"- Python 文件: {solution_py_path}")
            
            # Extract problem description from existing markdown
            md_parts = md_content.split("## Problem Description\n\n", 1)
            if len(md_parts) > 1:
                solution_parts = md_parts[1].split("\n\n## Solution\n\n", 1)
                if len(solution_parts) > 1:
                    problem_description = solution_parts[0]
                else:
                    problem_description = "Problem description not found."
            else:
                problem_description = "Problem description not found."
            
            # Ask if want to generate a new solution
            choice = input("\n已有解决方案，是否要生成新的DeepSeek解决方案？(y/n, 默认n): ").lower().strip()
            if choice == 'y':
                print("\n将生成新的DeepSeek解决方案...")
                # Backup old solution
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_folder = os.path.join(folder_name, f"previous_{timestamp}")
                os.makedirs(backup_folder, exist_ok=True)
                
                with open(os.path.join(backup_folder, "solution.md"), 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                with open(os.path.join(backup_folder, "solution.py"), 'w', encoding='utf-8') as f:
                    f.write(py_content)
                
                print(f"已备份现有解决方案到 {backup_folder}")
                
                # Get problem description and solve
                problem_description = get_leetcode_problem_description(problem_number)
                solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
                
                # Save solution to markdown file
                with open(solution_md_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {selected_question['full_name']}\n\n")
                    f.write("## Problem Description\n\n")
                    f.write(problem_description)
                    f.write("\n\n## Solution\n\n")
                    f.write(solution)
                
                print(f"\n解决方案已保存到 {solution_md_path}")
                
                # Extract Python code and save to Python file
                python_code = extract_python_code(solution)
                if python_code:
                    create_python_file(python_code, solution_py_path)
                    print(f"Python代码已提取并保存到 {solution_py_path}")
            
            # Ask if user wants to run the solution
            run_choice = input("\n是否运行解决方案？(y/n, 默认y): ").lower().strip()
            if run_choice != 'n':
                try:
                    print("\n运行解决方案...")
                    result = subprocess.run(["python", solution_py_path], capture_output=True, text=True)
                    print("\n--- 执行结果 ---")
                    if result.stdout:
                        print("输出:")
                        print(result.stdout)
                    if result.stderr:
                        print("错误:")
                        print(result.stderr)
                    print("---------------")
                except Exception as e:
                    print(f"运行解决方案时出错: {e}")
            else:
                print("\n跳过运行解决方案。")
                
            # Ask if user wants to view the solution
            view_choice = input("\n是否在浏览器中查看解决方案？(y/n, 默认n): ").lower().strip()
            if view_choice == 'y':
                try:
                    webbrowser.open(f"file://{os.path.abspath(solution_md_path)}")
                    print(f"已在浏览器中打开 solution.md")
                except:
                    print(f"无法在浏览器中打开。文件位置: {os.path.abspath(solution_md_path)}")
            
            # Ask if user wants to compare with Llama solution
            compare_choice = input("\n是否与Llama-4解决方案进行比较？(y/n, 默认n): ").lower().strip()
            if compare_choice == 'y':
                comparison = compare_with_llama_solution(problem_number, selected_question['english_name'])
                print("\n--- 解决方案比较 ---")
                print(comparison)
                print("------------------")
        else:
            # Get problem description
            problem_description = get_leetcode_problem_description(problem_number)
            print("\n--- 题目描述 ---")
            print(problem_description)
            print("---------------------------\n")
            
            # Solve the problem
            solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
            
            print("\n--- DeepSeek解决方案 ---")
            print(solution)
            print("---------------------------")
            
            # Save solution to markdown file
            solution_md_path = os.path.join(folder_name, f"solution.md")
            with open(solution_md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {selected_question['full_name']}\n\n")
                f.write("## Problem Description\n\n")
                f.write(problem_description)
                f.write("\n\n## Solution\n\n")
                f.write(solution)
            
            print(f"\n解决方案已保存到 {solution_md_path}")
            
            # Extract Python code and save to Python file
            python_code = extract_python_code(solution)
            if python_code:
                solution_py_path = os.path.join(folder_name, f"solution.py")
                create_python_file(python_code, solution_py_path)
                print(f"Python代码已提取并保存到 {solution_py_path}")
                
                # Ask user if they want to run the solution
                run_choice = input("\n是否运行解决方案? (y/n, 默认y): ").strip().lower()
                if run_choice != 'n':
                    try:
                        print("\n运行解决方案...")
                        result = subprocess.run(["python", solution_py_path], capture_output=True, text=True)
                        print("\n--- 执行结果 ---")
                        if result.stdout:
                            print("输出:")
                            print(result.stdout)
                        if result.stderr:
                            print("错误:")
                            print(result.stderr)
                        print("---------------")
                    except Exception as e:
                        print(f"运行解决方案时出错: {e}")
                else:
                    print("\n跳过运行解决方案。")
            else:
                print("在解决方案中未找到Python代码。")
            
            # Check if Llama solution exists for comparison
            llama_folder = f"llama4_maverick_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
            if os.path.exists(llama_folder):
                compare_choice = input("\n检测到已有Llama-4解决方案，是否进行比较？(y/n, 默认y): ").lower().strip()
                if compare_choice != 'n':
                    comparison = compare_with_llama_solution(problem_number, selected_question['english_name'])
                    print("\n--- 解决方案比较 ---")
                    print(comparison)
                    print("------------------")
                    
                    # Ask if user wants to view the comparison in browser
                    view_compare = input("\n是否在浏览器中查看比较结果？(y/n, 默认n): ").lower().strip()
                    if view_compare == 'y':
                        comparison_path = os.path.join("model_comparisons", f"comparison_leetcode_{problem_number}.md")
                        if os.path.exists(comparison_path):
                            try:
                                webbrowser.open(f"file://{os.path.abspath(comparison_path)}")
                                print(f"已在浏览器中打开比较结果")
                            except:
                                print(f"无法在浏览器中打开。文件位置: {os.path.abspath(comparison_path)}")

if __name__ == "__main__":
    main() 