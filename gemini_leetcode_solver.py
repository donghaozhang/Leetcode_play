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
load_dotenv()

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
        folder_name = f"gemini_solutions/leetcode_{leetcode_number}_{english_name.strip().lower().replace(' ', '_')}"
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

# Function to get problem description from LeetCode using Gemini
def get_leetcode_problem_description(problem_number):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-gemini-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode Gemini Solver"
    }
    
    prompt = f"Please provide the full description of LeetCode problem #{problem_number}, including examples and constraints. Return only the problem description as it appears on LeetCode."
    
    payload = {
        "model": "google/gemini-2.5-pro-exp-03-25:free",
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

# Function to solve LeetCode problem using Gemini via OpenRouter API
def solve_leetcode_problem(problem_description, problem_name):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-gemini-solver.example.com",  # Replace with your actual site
        "X-Title": "LeetCode Gemini Solver"
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
        "model": "google/gemini-2.5-pro-exp-03-25:free",
        "messages": [
            {"role": "system", "content": "You are an expert at solving LeetCode problems. Provide clear, optimized solutions with detailed explanations."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }
    
    print(f"Gemini is solving: {problem_name}...")
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
def compare_with_other_solution(problem_number, english_name, other_model="deepseek"):
    other_folder = f"{other_model}_solutions/leetcode_{problem_number}_{english_name.strip().lower().replace(' ', '_')}"
    if not os.path.exists(other_folder):
        return f"No {other_model} solution found for comparison."
    
    other_md_path = os.path.join(other_folder, "solution.md")
    if not os.path.exists(other_md_path):
        return f"No {other_model} solution markdown found for comparison."
    
    with open(other_md_path, 'r', encoding='utf-8') as f:
        other_md_content = f.read()
    
    # Ask Gemini to compare solutions
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://leetcode-gemini-solver.example.com",
        "X-Title": "LeetCode Model Comparison"
    }
    
    # Get Gemini solution
    gemini_folder = f"gemini_solutions/leetcode_{problem_number}_{english_name.strip().lower().replace(' ', '_')}"
    gemini_md_path = os.path.join(gemini_folder, "solution.md")
    
    if not os.path.exists(gemini_md_path):
        return "Gemini solution not found for comparison."
    
    with open(gemini_md_path, 'r', encoding='utf-8') as f:
        gemini_md_content = f.read()
    
    prompt = f"""
Please compare the following two solutions for the same LeetCode problem:

SOLUTION 1 ({other_model.capitalize()}):
{other_md_content}

SOLUTION 2 (Gemini):
{gemini_md_content}

Provide a detailed comparison focusing on:
1. Algorithm approach differences
2. Code quality and readability
3. Time and space complexity differences
4. Strengths and weaknesses of each solution
5. Overall assessment of which solution is better and why
"""
    
    payload = {
        "model": "google/gemini-2.5-pro-exp-03-25:free", 
        "messages": [
            {"role": "system", "content": "You are an expert at comparing coding solutions and providing insightful analysis."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    print(f"Comparing solutions from {other_model.capitalize()} and Gemini...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        comparison = response.json()["choices"][0]["message"]["content"]
        
        # Save comparison to file
        comparison_folder = "model_comparisons"
        os.makedirs(comparison_folder, exist_ok=True)
        comparison_path = os.path.join(comparison_folder, f"comparison_leetcode_{problem_number}_{other_model}_vs_gemini.md")
        
        with open(comparison_path, 'w', encoding='utf-8') as f:
            f.write(f"# Solution Comparison for LeetCode {problem_number}\n\n")
            f.write(comparison)
        
        print(f"Comparison saved to {comparison_path}")
        return comparison
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return "Failed to generate comparison due to API error."

# Function to process a single problem
def process_problem(selected_question, run_tests=True, compare_with_other=True, other_model="deepseek"):
    problem_number = selected_question['leetcode_number']
    print(f"\nProcessing problem: {selected_question['full_name']}")
    
    # Create folder structure
    folder_name = selected_question['folder_name']
    os.makedirs(folder_name, exist_ok=True)
    
    # Check if solution already exists
    exists, md_content, py_content, creation_time = check_existing_solution(folder_name)
    
    solution_md_path = os.path.join(folder_name, "solution.md")
    solution_py_path = os.path.join(folder_name, "solution.py")
    
    if exists:
        print(f"  Existing Gemini solution found (created on: {creation_time.strftime('%Y-%m-%d %H:%M:%S')})")
        print(f"  Skipping this problem and continuing...")
        return {
            "problem_number": problem_number,
            "status": "existing",
            "solution_path": solution_md_path,
            "execution_result": None,
            "comparison_result": None
        }
    
    # Get problem description
    problem_description = get_leetcode_problem_description(problem_number)
    print(f"  Problem description retrieved")
    
    # Solve the problem
    solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
    print(f"  Solution generated")
    
    # Save solution to markdown file
    with open(solution_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {selected_question['full_name']}\n\n")
        f.write("## Problem Description\n\n")
        f.write(problem_description)
        f.write("\n\n## Solution\n\n")
        f.write(solution)
    
    print(f"  Solution saved to {solution_md_path}")
    
    # Extract Python code and save to Python file
    python_code = extract_python_code(solution)
    execution_result = None
    
    if python_code:
        create_python_file(python_code, solution_py_path)
        print(f"  Python code extracted and saved to {solution_py_path}")
        
        # Run the solution if requested
        if run_tests:
            try:
                print(f"  Running solution...")
                result = subprocess.run(["python", solution_py_path], capture_output=True, text=True, timeout=30)
                execution_result = {
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "success": result.returncode == 0
                }
                
                print(f"  Execution result: {'success' if result.returncode == 0 else 'failure'}")
                if result.stderr:
                    print(f"  Error message: {result.stderr[:100]}...")
            except Exception as e:
                print(f"  Error running solution: {e}")
                execution_result = {
                    "stdout": "",
                    "stderr": str(e),
                    "success": False
                }
    else:
        print(f"  No Python code found in solution")
    
    # Compare with other solution if requested
    comparison_result = None
    if compare_with_other:
        other_folder = f"{other_model}_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
        if os.path.exists(other_folder):
            print(f"  Found existing {other_model} solution, comparing...")
            comparison = compare_with_other_solution(problem_number, selected_question['english_name'], other_model)
            comparison_result = comparison
            print(f"  Solution comparison completed")
    
    return {
        "problem_number": problem_number,
        "status": "new",
        "solution_path": solution_md_path,
        "execution_result": execution_result,
        "comparison_result": comparison_result is not None
    }

# Function to generate solutions iteratively for multiple problems
def iterative_solution_generation(leetcode_questions, num_problems=5, run_tests=True, compare_with_other=True, other_model="deepseek"):
    # Filter unsolved questions
    unsolved_questions = [q for q in leetcode_questions if not q['is_solved']]
    
    if not unsolved_questions:
        print("No unsolved problems found. Cannot generate iterative solutions.")
        return
    
    # Limit to the specified number or available unsolved problems
    num_to_solve = min(num_problems, len(unsolved_questions))
    questions_to_solve = unsolved_questions[:num_to_solve]
    
    print(f"\n===== Gemini LeetCode Iterative Solver =====")
    print(f"Will solve {num_to_solve} problems sequentially")
    
    results = []
    start_time = datetime.now()
    
    # Process each problem one by one
    for i, question in enumerate(questions_to_solve, 1):
        print(f"\n[{i}/{num_to_solve}] Starting problem {question['leetcode_number']}: {question['english_name']}")
        result = process_problem(question, run_tests, compare_with_other, other_model)
        results.append(result)
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() / 60
    
    # Generate summary report
    successful_count = sum(1 for r in results if r["status"] == "new" and (r["execution_result"] is None or r["execution_result"]["success"]))
    failed_count = sum(1 for r in results if r["status"] == "new" and r["execution_result"] is not None and not r["execution_result"]["success"])
    skipped_count = sum(1 for r in results if r["status"] == "existing")
    
    print("\n===== Iterative Solving Completed =====")
    print(f"Total time: {duration:.2f} minutes")
    print(f"Total problems processed: {len(results)}")
    print(f"New solutions generated: {len(results) - skipped_count}")
    print(f"  - Successfully executed: {successful_count}")
    print(f"  - Failed execution: {failed_count}")
    print(f"Skipped existing solutions: {skipped_count}")
    
    # Generate detailed report file
    report_folder = "gemini_reports"
    os.makedirs(report_folder, exist_ok=True)
    report_file = os.path.join(report_folder, f"iterative_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Gemini LeetCode Iterative Solving Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total time: {duration:.2f} minutes\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- Total problems processed: {len(results)}\n")
        f.write(f"- New solutions generated: {len(results) - skipped_count}\n")
        f.write(f"  - Successfully executed: {successful_count}\n")
        f.write(f"  - Failed execution: {failed_count}\n")
        f.write(f"- Skipped existing solutions: {skipped_count}\n\n")
        
        f.write("## Detailed Results\n\n")
        for result in results:
            status_str = "Existing solution, skipped" if result["status"] == "existing" else "New solution generated"
            execution_str = ""
            if result["status"] == "new" and result["execution_result"] is not None:
                execution_str = "- Execution result: " + ("success" if result["execution_result"]["success"] else "failure")
                if not result["execution_result"]["success"] and result["execution_result"]["stderr"]:
                    execution_str += f"\n- Error message: ```\n{result['execution_result']['stderr'][:500]}...\n```"
            
            comparison_str = ""
            if result["status"] == "new" and result["comparison_result"]:
                comparison_str = f"- Compared with {other_model} solution"
            
            f.write(f"### LeetCode {result['problem_number']}\n\n")
            f.write(f"- Status: {status_str}\n")
            f.write(f"- Solution path: {result['solution_path']}\n")
            if execution_str:
                f.write(f"{execution_str}\n")
            if comparison_str:
                f.write(f"{comparison_str}\n")
            f.write("\n")
    
    print(f"\nDetailed report saved to: {report_file}")
    
    return report_file

# Main function
def main():
    readme_path = "README.md"
    
    # Extract LeetCode questions from README
    leetcode_questions = extract_leetcode_questions(readme_path)
    
    if not leetcode_questions:
        print("No LeetCode problems found in README.md file.")
        return
    
    # Count solved and unsolved questions
    solved_count = sum(1 for q in leetcode_questions if q['is_solved'])
    total_count = len(leetcode_questions)
    
    print("\n===== Gemini LeetCode Solver =====")
    print(f"Current Gemini progress: Solved {solved_count}/{total_count} problems ({(solved_count/total_count*100):.1f}%)")
    print(f"Unsolved: {total_count - solved_count} problems")
    
    # Ask for operation mode
    print("\nSelect operation mode:")
    print("1. Interactive solving (process one problem with prompts)")
    print("2. Iterative solving (batch process multiple problems)")
    
    mode_choice = input("\nEnter option (1 or 2, default is 1): ").strip()
    
    if mode_choice == "2":
        # Iterative mode
        num_problems_str = input("\nNumber of problems to solve iteratively (default 5): ").strip()
        try:
            num_problems = int(num_problems_str) if num_problems_str else 5
        except:
            num_problems = 5
        
        run_tests_choice = input("Run generated code to verify solutions? (y/n, default y): ").lower().strip()
        run_tests = run_tests_choice != 'n'
        
        compare_choice = input("Compare with existing DeepSeek solutions? (y/n, default y): ").lower().strip()
        compare_with_other = compare_choice != 'n'
        
        report_file = iterative_solution_generation(
            leetcode_questions, 
            num_problems, 
            run_tests, 
            compare_with_other
        )
        
        # Ask if user wants to view the report
        view_report = input("\nView generated report in browser? (y/n, default y): ").lower().strip()
        if view_report != 'n' and report_file:
            try:
                webbrowser.open(f"file://{os.path.abspath(report_file)}")
                print(f"Report opened in browser")
            except:
                print(f"Could not open in browser. Report location: {os.path.abspath(report_file)}")
    else:
        # Interactive mode
        # Ask if user wants to see solved problems
        show_solved = input("\nShow solved problems? (y/n, default n): ").lower().strip() == 'y'
        
        # Display available LeetCode questions
        print(f"\nFound {len(leetcode_questions)} LeetCode problems in README.md:")
        available_questions = []
        for i, question in enumerate(leetcode_questions, 1):
            if not question['is_solved'] or show_solved:
                status = "[Solved]" if question['is_solved'] else "[Unsolved]"
                print(f"{i}. {status} {question['full_name']}")
                available_questions.append(question)
        
        if not available_questions:
            print("\nCongratulations! All problems have been solved!")
            return
        
        # Choose a random question or let user select
        try:
            choice = input("\nEnter problem number to solve (or press Enter for random selection): ")
            if choice.strip():
                index = int(choice) - 1
                if 0 <= index < len(available_questions):
                    selected_question = available_questions[index]
                else:
                    print("Invalid selection. Randomly selecting a problem.")
                    # Only select from unsolved questions if not showing solved ones
                    candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
                    selected_question = random.choice(candidates)
            else:
                # Only select from unsolved questions if not showing solved ones
                candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
                selected_question = random.choice(candidates)
        except:
            print("Invalid input. Randomly selecting a problem.")
            # Only select from unsolved questions if not showing solved ones
            candidates = [q for q in available_questions if not q['is_solved']] if not show_solved else available_questions
            selected_question = random.choice(candidates)
        
        problem_number = selected_question['leetcode_number']
        print(f"\nSelected problem: {selected_question['full_name']}")
        
        # Create folder structure
        folder_name = selected_question['folder_name']
        os.makedirs(folder_name, exist_ok=True)
        
        # Check if solution already exists
        exists, md_content, py_content, creation_time = check_existing_solution(folder_name)
        
        if exists:
            print(f"\nFound existing Gemini solution! Created on: {creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
            solution_md_path = os.path.join(folder_name, "solution.md")
            solution_py_path = os.path.join(folder_name, "solution.py")
            
            print(f"\nSolution storage location:")
            print(f"- Markdown file: {solution_md_path}")
            print(f"- Python file: {solution_py_path}")
            
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
            choice = input("\nSolution already exists. Generate a new Gemini solution? (y/n, default n): ").lower().strip()
            if choice == 'y':
                print("\nGenerating new Gemini solution...")
                # Backup old solution
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_folder = os.path.join(folder_name, f"previous_{timestamp}")
                os.makedirs(backup_folder, exist_ok=True)
                
                with open(os.path.join(backup_folder, "solution.md"), 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                with open(os.path.join(backup_folder, "solution.py"), 'w', encoding='utf-8') as f:
                    f.write(py_content)
                
                print(f"Backed up existing solution to {backup_folder}")
                
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
                
                print(f"\nSolution saved to {solution_md_path}")
                
                # Extract Python code and save to Python file
                python_code = extract_python_code(solution)
                if python_code:
                    create_python_file(python_code, solution_py_path)
                    print(f"Python code extracted and saved to {solution_py_path}")
            
            # Ask if user wants to run the solution
            run_choice = input("\nRun the solution? (y/n, default y): ").lower().strip()
            if run_choice != 'n':
                try:
                    print("\nRunning solution...")
                    result = subprocess.run(["python", solution_py_path], capture_output=True, text=True)
                    print("\n--- Execution Results ---")
                    if result.stdout:
                        print("Output:")
                        print(result.stdout)
                    if result.stderr:
                        print("Errors:")
                        print(result.stderr)
                    print("---------------------")
                except Exception as e:
                    print(f"Error running solution: {e}")
            else:
                print("\nSkipping solution execution.")
                
            # Ask if user wants to view the solution
            view_choice = input("\nView solution in browser? (y/n, default n): ").lower().strip()
            if view_choice == 'y':
                try:
                    webbrowser.open(f"file://{os.path.abspath(solution_md_path)}")
                    print(f"Opened solution.md in browser")
                except:
                    print(f"Could not open in browser. File location: {os.path.abspath(solution_md_path)}")
            
            # Ask if user wants to compare with DeepSeek solution
            compare_choice = input("\nCompare with DeepSeek solution? (y/n, default n): ").lower().strip()
            if compare_choice == 'y':
                comparison = compare_with_other_solution(problem_number, selected_question['english_name'], "deepseek")
                print("\n--- Solution Comparison ---")
                print(comparison)
                print("--------------------------")
        else:
            # Get problem description
            problem_description = get_leetcode_problem_description(problem_number)
            print("\n--- Problem Description ---")
            print(problem_description)
            print("---------------------------\n")
            
            # Solve the problem
            solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
            
            print("\n--- Gemini Solution ---")
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
            
            print(f"\nSolution saved to {solution_md_path}")
            
            # Extract Python code and save to Python file
            python_code = extract_python_code(solution)
            if python_code:
                solution_py_path = os.path.join(folder_name, f"solution.py")
                create_python_file(python_code, solution_py_path)
                print(f"Python code extracted and saved to {solution_py_path}")
                
                # Ask user if they want to run the solution
                run_choice = input("\nRun the solution? (y/n, default y): ").strip().lower()
                if run_choice != 'n':
                    try:
                        print("\nRunning solution...")
                        result = subprocess.run(["python", solution_py_path], capture_output=True, text=True)
                        print("\n--- Execution Results ---")
                        if result.stdout:
                            print("Output:")
                            print(result.stdout)
                        if result.stderr:
                            print("Errors:")
                            print(result.stderr)
                        print("---------------------")
                    except Exception as e:
                        print(f"Error running solution: {e}")
                else:
                    print("\nSkipping solution execution.")
            else:
                print("No Python code found in solution.")
            
            # Check if DeepSeek solution exists for comparison
            deepseek_folder = f"deepseek_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
            if os.path.exists(deepseek_folder):
                compare_choice = input("\nFound existing DeepSeek solution. Compare solutions? (y/n, default y): ").lower().strip()
                if compare_choice != 'n':
                    comparison = compare_with_other_solution(problem_number, selected_question['english_name'], "deepseek")
                    print("\n--- Solution Comparison ---")
                    print(comparison)
                    print("--------------------------")
                    
                    # Ask if user wants to view the comparison in browser
                    view_compare = input("\nView comparison in browser? (y/n, default n): ").lower().strip()
                    if view_compare == 'y':
                        comparison_path = os.path.join("model_comparisons", f"comparison_leetcode_{problem_number}_deepseek_vs_gemini.md")
                        if os.path.exists(comparison_path):
                            try:
                                webbrowser.open(f"file://{os.path.abspath(comparison_path)}")
                                print(f"Opened comparison in browser")
                            except:
                                print(f"Could not open in browser. File location: {os.path.abspath(comparison_path)}")

if __name__ == "__main__":
    main() 