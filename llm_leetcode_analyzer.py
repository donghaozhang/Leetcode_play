import os
import subprocess
import re
from datetime import datetime
import webbrowser

def analyze_solution(folder_path):
    """Analyze the status of a single solution"""
    if not os.path.exists(folder_path):
        return None
    
    py_path = os.path.join(folder_path, "solution.py")
    if not os.path.exists(py_path):
        return None
    
    # Get creation time
    creation_time = datetime.fromtimestamp(os.path.getctime(py_path))
    
    # Try to run the Python file
    try:
        result = subprocess.run(["python", py_path], capture_output=True, text=True, timeout=5)
        has_error = bool(result.stderr)
        has_output = bool(result.stdout)
        return {
            'has_error': has_error,
            'has_output': has_output,
            'error_msg': result.stderr if has_error else None,
            'output': result.stdout if has_output else None,
            'creation_time': creation_time
        }
    except subprocess.TimeoutExpired:
        return {
            'has_error': True,
            'has_output': False,
            'error_msg': "Execution timeout (5 seconds)",
            'creation_time': creation_time
        }
    except Exception as e:
        return {
            'has_error': True,
            'has_output': False,
            'error_msg': str(e),
            'creation_time': creation_time
        }

def generate_html_report(problems, model_name):
    """Generate HTML progress report"""
    # Calculate statistics
    total_problems = len(problems)
    solved_count = sum(1 for p in problems if p['status'] != 'Unsolved')
    passed_count = sum(1 for p in problems if p['status'] == 'Pass')
    error_count = sum(1 for p in problems if p['status'] == 'Fail')
    
    solved_percentage = (solved_count / total_problems * 100) if total_problems > 0 else 0
    passed_percentage = (passed_count / total_problems * 100) if total_problems > 0 else 0
    error_percentage = (error_count / total_problems * 100) if total_problems > 0 else 0
    
    # Generate table rows
    table_rows = []
    for i, problem in enumerate(problems):
        status_class = {
            'Pass': 'status-pass',
            'Fail': 'status-fail',
            'Unsolved': 'status-unknown'
        }[problem['status']]
        
        error_details = ''
        if problem['status'] == 'Fail' and problem['error_msg']:
            error_id = f"error-{i}"
            error_details = f"""
                <span class="toggle-error" onclick="toggleErrorDetails('{error_id}')">View Error</span>
                <div id="{error_id}" class="error-details">{problem['error_msg']}</div>
            """
        
        # Add solution links
        solution_links = f"""
            <div class="solution-links">
                <a href="../{model_name}_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.py" class="solution-link">Python</a>
                <a href="../{model_name}_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.md" class="solution-link">Solution</a>
            </div>
        """ if problem['status'] != 'Unsolved' else '-'
        
        table_rows.append(f"""
            <tr>
                <td>{problem['number']}</td>
                <td>{problem['name']}</td>
                <td class="{status_class}">{problem['status']}</td>
                <td>{solution_links}</td>
                <td>{error_details}</td>
            </tr>
        """)
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table_rows_str = '\n'.join(table_rows)
    
    # HTML template
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetCode Progress Report - {model_name}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }}
            .summary {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 30px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f8f9fa;
                position: sticky;
                top: 0;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
            .status-pass {{
                color: #28a745;
                font-weight: bold;
            }}
            .status-fail {{
                color: #dc3545;
                font-weight: bold;
            }}
            .status-unknown {{
                color: #6c757d;
                font-weight: bold;
            }}
            .error-details {{
                display: none;
                background-color: #f8d7da;
                padding: 10px;
                margin-top: 5px;
                border-radius: 4px;
                font-family: monospace;
                white-space: pre-wrap;
            }}
            .toggle-error {{
                color: #dc3545;
                cursor: pointer;
                text-decoration: underline;
            }}
            .last-updated {{
                text-align: right;
                color: #6c757d;
                font-size: 0.9em;
            }}
            .solution-links {{
                display: flex;
                gap: 10px;
            }}
            .solution-link {{
                color: #007bff;
                text-decoration: none;
            }}
            .solution-link:hover {{
                text-decoration: underline;
            }}
            .model-tabs {{
                display: flex;
                gap: 10px;
                margin-bottom: 20px;
            }}
            .model-tab {{
                padding: 10px 20px;
                background-color: #f8f9fa;
                border-radius: 4px;
                cursor: pointer;
            }}
            .model-tab.active {{
                background-color: #007bff;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>LeetCode Progress Report - {model_name}</h1>
        
        <div class="model-tabs">
            <a href="llama4_maverick_solution_report.html" class="model-tab {' active' if model_name == 'llama4_maverick' else ''}">Llama-4 Maverick Solutions</a>
            <a href="deepseek_solution_report.html" class="model-tab {' active' if model_name == 'deepseek' else ''}">DeepSeek Solutions</a>
            <a href="gemini_solution_report.html" class="model-tab {' active' if model_name == 'gemini' else ''}">Gemini 2.5 Pro Solutions</a>
        </div>
        
        <div class="summary">
            <h2>Statistics</h2>
            <p>Total Problems: {total_problems}</p>
            <p>Solved: {solved_count} ({solved_percentage:.1f}%)</p>
            <p>Passed: {passed_count} ({passed_percentage:.1f}%)</p>
            <p>Failed: {error_count} ({error_percentage:.1f}%)</p>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Problem Name</th>
                    <th>Status</th>
                    <th>Solutions</th>
                    <th>Details</th>
                </tr>
            </thead>
            <tbody>
                {table_rows_str}
            </tbody>
        </table>
        
        <div class="last-updated">
            Last Updated: {current_time}
        </div>
        
        <script>
            function toggleErrorDetails(id) {{
                const details = document.getElementById(id);
                if (details.style.display === 'none') {{
                    details.style.display = 'block';
                }} else {{
                    details.style.display = 'none';
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    return html

def clean_problem_name(english_name, chinese_name):
    """Clean up problem names by removing markdown references and file extensions"""
    # Remove markdown/file references in parentheses
    english_name = re.sub(r'\([^)]*\.md\)', '', english_name)
    english_name = re.sub(r'\([^)]*\.py\)', '', english_name)
    
    # Remove file extensions
    english_name = re.sub(r'\.md$', '', english_name)
    english_name = re.sub(r'\.py$', '', english_name)
    
    # Remove any remaining markdown headers or sections
    english_name = re.sub(r'#.*?$', '', english_name)
    english_name = re.sub(r'^[-\s]*', '', english_name)
    
    # Clean up Chinese name
    chinese_name = chinese_name.strip()
    
    # Remove any trailing/leading whitespace
    english_name = english_name.strip()
    
    return english_name, chinese_name

def analyze_solutions(model_name):
    """Analyze solutions for a specific model"""
    # Read README.md to get all problems
    with open("README.md", 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract problem information
    leetcode_pattern = r'([^/]+) / ([^[]+) \[LeetCode (\d+)\]'
    matches = re.findall(leetcode_pattern, content)
    
    problems = []
    for match in matches:
        chinese_name, english_name, leetcode_number = match
        folder_name = f"{model_name}_solutions/leetcode_{leetcode_number}_{english_name.strip().lower().replace(' ', '_')}"
        
        # Clean up problem names
        clean_english, clean_chinese = clean_problem_name(english_name, chinese_name)
        
        # Analyze solution
        analysis = analyze_solution(folder_name)
        
        if analysis:
            status = 'Pass' if not analysis['has_error'] else 'Fail'
            problems.append({
                'number': leetcode_number,
                'name': f"{clean_english} ({clean_chinese})",
                'status': status,
                'creation_time': analysis['creation_time'],
                'error_msg': analysis['error_msg']
            })
        else:
            problems.append({
                'number': leetcode_number,
                'name': f"{clean_english} ({clean_chinese})",
                'status': 'Unsolved',
                'creation_time': None,
                'error_msg': None
            })
    
    # Sort by problem number
    problems.sort(key=lambda x: int(x['number']))
    
    return problems

def generate_summary_report(model_results):
    """Generate a summary HTML report comparing all models"""
    # Calculate summary statistics for each model
    summary_rows = []
    for model_name, problems in model_results.items():
        total_problems = len(problems)
        solved_count = sum(1 for p in problems if p['status'] != 'Unsolved')
        passed_count = sum(1 for p in problems if p['status'] == 'Pass')
        error_count = sum(1 for p in problems if p['status'] == 'Fail')
        
        solved_percentage = (solved_count / total_problems * 100) if total_problems > 0 else 0
        passed_percentage = (passed_count / total_problems * 100) if total_problems > 0 else 0
        error_percentage = (error_count / total_problems * 100) if total_problems > 0 else 0
        
        summary_rows.append(f"""
            <tr>
                <td>{model_name.capitalize()}</td>
                <td>{total_problems}</td>
                <td>{solved_count} ({solved_percentage:.1f}%)</td>
                <td>{passed_count} ({passed_percentage:.1f}%)</td>
                <td>{error_count} ({error_percentage:.1f}%)</td>
            </tr>
        """)
    
    # Generate detailed comparison table
    problem_details = {}
    for model_name, problems in model_results.items():
        for problem in problems:
            number = problem['number']
            if number not in problem_details:
                problem_details[number] = {'name': problem['name'], 'models': {}}
            
            status_class = {
                'Pass': 'status-pass',
                'Fail': 'status-fail',
                'Unsolved': 'status-unknown'
            }[problem['status']]
            
            solution_links = f"""
                <div class="solution-links">
                    <a href="../{model_name}_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.py" class="solution-link">Python</a>
                    <a href="../{model_name}_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.md" class="solution-link">Solution</a>
                </div>
            """ if problem['status'] != 'Unsolved' else '-'
            
            error_details = ''
            if problem['status'] == 'Fail' and problem['error_msg']:
                error_id = f"error-{model_name}-{number}"
                error_details = f"""
                    <span class="toggle-error" onclick="toggleErrorDetails('{error_id}')">View Error</span>
                    <div id="{error_id}" class="error-details">{problem['error_msg']}</div>
                """
            
            problem_details[number]['models'][model_name] = {
                'status': problem['status'],
                'status_class': status_class,
                'solution_links': solution_links,
                'error_details': error_details
            }
    
    # Generate comparison rows
    comparison_rows = []
    for number in sorted(problem_details.keys(), key=int):
        problem = problem_details[number]
        model_columns = []
        for model_name in model_results.keys():
            model_data = problem['models'].get(model_name, {
                'status': 'Unsolved',
                'status_class': 'status-unknown',
                'solution_links': '-',
                'error_details': ''
            })
            
            model_columns.append(f"""
                <td class="{model_data['status_class']}">{model_data['status']}</td>
                <td>{model_data['solution_links']}</td>
                <td>{model_data['error_details']}</td>
            """)
        
        comparison_rows.append(f"""
            <tr>
                <td>{number}</td>
                <td>{problem['name']}</td>
                {''.join(model_columns)}
            </tr>
        """)
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # HTML template for summary page
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetCode Models Comparison Report</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1, h2 {{
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }}
            .summary {{
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 30px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f8f9fa;
                position: sticky;
                top: 0;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
            .status-pass {{
                color: #28a745;
                font-weight: bold;
            }}
            .status-fail {{
                color: #dc3545;
                font-weight: bold;
            }}
            .status-unknown {{
                color: #6c757d;
                font-weight: bold;
            }}
            .error-details {{
                display: none;
                background-color: #f8d7da;
                padding: 10px;
                margin-top: 5px;
                border-radius: 4px;
                font-family: monospace;
                white-space: pre-wrap;
            }}
            .toggle-error {{
                color: #dc3545;
                cursor: pointer;
                text-decoration: underline;
            }}
            .last-updated {{
                text-align: right;
                color: #6c757d;
                font-size: 0.9em;
            }}
            .solution-links {{
                display: flex;
                gap: 10px;
            }}
            .solution-link {{
                color: #007bff;
                text-decoration: none;
            }}
            .solution-link:hover {{
                text-decoration: underline;
            }}
            .model-links {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .model-link {{
                display: inline-block;
                padding: 10px 20px;
                margin: 0 10px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 4px;
            }}
            .model-link:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>LeetCode Models Comparison Report</h1>
        
        <div class="model-links">
            <a href="llama4_maverick_solution_report.html" class="model-link">Llama-4 Maverick Report</a>
            <a href="deepseek_solution_report.html" class="model-link">DeepSeek Report</a>
            <a href="gemini_solution_report.html" class="model-link">Gemini 2.5 Pro Report</a>
        </div>
        
        <h2>Summary Statistics</h2>
        <table>
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Total Problems</th>
                    <th>Solved</th>
                    <th>Passed</th>
                    <th>Failed</th>
                </tr>
            </thead>
            <tbody>
                {''.join(summary_rows)}
            </tbody>
        </table>
        
        <h2>Detailed Comparison</h2>
        <table>
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Problem Name</th>
                    {''.join([f'''
                        <th colspan="3" style="text-align: center;">{model.capitalize()}</th>
                    ''' for model in model_results.keys()])}
                </tr>
                <tr>
                    <th></th>
                    <th></th>
                    {''.join(['''
                        <th>Status</th>
                        <th>Solutions</th>
                        <th>Details</th>
                    ''' for _ in model_results.keys()])}
                </tr>
            </thead>
            <tbody>
                {''.join(comparison_rows)}
            </tbody>
        </table>
        
        <div class="last-updated">
            Last Updated: {current_time}
        </div>
        
        <script>
            function toggleErrorDetails(id) {{
                const details = document.getElementById(id);
                if (details.style.display === 'none') {{
                    details.style.display = 'block';
                }} else {{
                    details.style.display = 'none';
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    return html

def main():
    # Create results directory
    results_dir = "llm_analysis_result"
    os.makedirs(results_dir, exist_ok=True)
    
    # Analyze all models
    models = ['llama4_maverick', 'deepseek', 'gemini']
    model_results = {}
    
    for model in models:
        # Analyze solutions
        problems = analyze_solutions(model)
        model_results[model] = problems
        
        # Generate individual HTML report
        html = generate_html_report(problems, model)
        
        # Save report in the results directory
        report_path = os.path.join(results_dir, f"{model}_solution_report.html")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Report generated for {model}: {os.path.abspath(report_path)}")
    
    # Generate and save summary report
    summary_html = generate_summary_report(model_results)
    summary_path = os.path.join(results_dir, "models_comparison_report.html")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_html)
    
    print(f"Summary report generated: {os.path.abspath(summary_path)}")
    
    # Open the summary report by default
    webbrowser.open(f"file://{os.path.abspath(summary_path)}")

if __name__ == "__main__":
    main() 