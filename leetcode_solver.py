import os
import requests
import re
import random
import subprocess
from dotenv import load_dotenv
import markdown
from bs4 import BeautifulSoup

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
    
    print(f"Solving problem: {problem_name}...")
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

# Main function
def main():
    readme_path = "README.md"
    
    # Extract LeetCode questions from README
    leetcode_questions = extract_leetcode_questions(readme_path)
    
    if not leetcode_questions:
        print("No LeetCode questions found in the README.md file.")
        return
    
    # Display available LeetCode questions
    print(f"Found {len(leetcode_questions)} LeetCode questions in README.md:")
    for i, question in enumerate(leetcode_questions):
        print(f"{i+1}. {question['full_name']}")
    
    # Choose a random question or let user select
    try:
        choice = input("\nEnter the number of the question to solve (or press Enter for a random question): ")
        if choice.strip():
            index = int(choice) - 1
            if 0 <= index < len(leetcode_questions):
                selected_question = leetcode_questions[index]
            else:
                print("Invalid choice. Selecting a random question.")
                selected_question = random.choice(leetcode_questions)
        else:
            selected_question = random.choice(leetcode_questions)
    except:
        print("Invalid input. Selecting a random question.")
        selected_question = random.choice(leetcode_questions)
    
    problem_number = selected_question['leetcode_number']
    print(f"\nSelected problem: {selected_question['full_name']}")
    
    # Create folder structure
    folder_name = f"llama4_maverick_solutions/leetcode_{problem_number}_{selected_question['english_name'].strip().lower().replace(' ', '_')}"
    os.makedirs(folder_name, exist_ok=True)
    
    # Get problem description
    problem_description = get_leetcode_problem_description(problem_number)
    print("\n--- PROBLEM DESCRIPTION ---")
    print(problem_description)
    print("---------------------------\n")
    
    # Solve the problem
    solution = solve_leetcode_problem(problem_description, selected_question['full_name'])
    
    print("\n--- SOLUTION ---")
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
        
        # Run the Python file
        try:
            print("\nRunning the solution...")
            result = subprocess.run(["python", solution_py_path], capture_output=True, text=True)
            print("\n--- EXECUTION RESULT ---")
            if result.stdout:
                print("Output:")
                print(result.stdout)
            if result.stderr:
                print("Errors:")
                print(result.stderr)
            print("------------------------")
        except Exception as e:
            print(f"Error running the solution: {e}")
    else:
        print("No Python code found in the solution.")

if __name__ == "__main__":
    main() 