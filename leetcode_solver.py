import os
import requests
import re
import random
import subprocess
from dotenv import load_dotenv
import markdown
from bs4 import BeautifulSoup
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
        leetcode_questions.append({
            'chinese_name': chinese_name.strip(),
            'english_name': english_name.strip(),
            'leetcode_number': leetcode_number,
            'full_name': f"{chinese_name.strip()} / {english_name.strip()} [LeetCode {leetcode_number}]"
        })
    
    return leetcode_questions

# Function to get problem description from LeetCode (simulated)
def get_leetcode_problem_description(problem_number):
    # In a real application, you might want to scrape the actual problem description
    # For now, we'll use OpenRouter to get the problem description
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode Problem Solver"
    }
    
    prompt = f"Please provide the full description of LeetCode problem #{problem_number}, including examples and constraints. Return only the problem description as it appears on LeetCode."
    
    payload = {
        "model": "meta-llama/llama-4-maverick:free",
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

# Function to solve LeetCode problem using OpenRouter API
def solve_leetcode_problem(problem_description, problem_name):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode Problem Solver"
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
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {"role": "system", "content": "You are an expert at solving LeetCode problems. Provide clear, optimized solutions with detailed explanations."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }
    
    print(f"解题中: {problem_name}...")
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

# Main function
def main():
    readme_path = "README.md"
    
    # Extract LeetCode questions from README
    leetcode_questions = extract_leetcode_questions(readme_path)
    
    if not leetcode_questions:
        print("没有在README.md文件中找到LeetCode题目。")
        return
    
    # Display available LeetCode questions
    print(f"找到 {len(leetcode_questions)} 个 LeetCode 题目在 README.md 中:")
    for i, question in enumerate(leetcode_questions):
        print(f"{i+1}. {question['full_name']}")
    
    # Choose a random question or let user select
    try:
        choice = input("\n输入题目编号来解题 (或直接按回车随机选择一题): ")
        if choice.strip():
            index = int(choice) - 1
            if 0 <= index < len(leetcode_questions):
                selected_question = leetcode_questions[index]
            else:
                print("无效的选择。随机选择一题。")
                selected_question = random.choice(leetcode_questions)
        else:
            selected_question = random.choice(leetcode_questions)
    except:
        print("无效的输入。随机选择一题。")
        selected_question = random.choice(leetcode_questions)
    
    problem_number = selected_question['leetcode_number']
    print(f"\n已选择题目: {selected_question['full_name']}")
    
    # Create folder structure
    folder_name = f"llama4_maverick_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
    os.makedirs(folder_name, exist_ok=True)
    
    # Check if solution already exists
    exists, md_content, py_content, creation_time = check_existing_solution(folder_name)
    
    if exists:
        print(f"\n发现已有的解决方案！创建于: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
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
        choice = input("\n已有解决方案，是否要生成新的解决方案？(y/n, 默认n): ").lower().strip()
        if choice == 'y':
            print("\n将生成新的解决方案...")
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
    else:
        # Get problem description
        problem_description = get_leetcode_problem_description(problem_number)
        print("\n--- 题目描述 ---")
        print(problem_description)
        print("---------------------------\n")
        
        # Solve the problem
        solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
        
        print("\n--- 解决方案 ---")
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

if __name__ == "__main__":
    main() 