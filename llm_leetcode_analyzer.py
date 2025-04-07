import os
import subprocess
import re
from datetime import datetime
import webbrowser

def analyze_solution(folder_path):
    """分析单个解决方案的状态"""
    if not os.path.exists(folder_path):
        return None
    
    py_path = os.path.join(folder_path, "solution.py")
    if not os.path.exists(py_path):
        return None
    
    # 获取创建时间
    creation_time = datetime.fromtimestamp(os.path.getctime(py_path))
    
    # 尝试运行Python文件
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
            'error_msg': "运行超时（5秒）",
            'creation_time': creation_time
        }
    except Exception as e:
        return {
            'has_error': True,
            'has_output': False,
            'error_msg': str(e),
            'creation_time': creation_time
        }

def generate_html_report(problems):
    """生成HTML格式的进度报告"""
    # 计算统计数据
    total_problems = len(problems)
    solved_count = sum(1 for p in problems if p['status'] != 'Unsolved')
    passed_count = sum(1 for p in problems if p['status'] == 'Pass')
    error_count = sum(1 for p in problems if p['status'] == 'Fail')
    
    solved_percentage = (solved_count / total_problems * 100) if total_problems > 0 else 0
    passed_percentage = (passed_count / total_problems * 100) if total_problems > 0 else 0
    error_percentage = (error_count / total_problems * 100) if total_problems > 0 else 0
    
    # 生成表格行
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
                <a href="llama4_maverick_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.py" class="solution-link">Python</a>
                <a href="llama4_maverick_solutions/leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}/solution.md" class="solution-link">题解</a>
            </div>
        """ if problem['status'] != 'Unsolved' else '-'
        
        table_rows.append(f"""
            <tr>
                <td>{problem['number']}</td>
                <td>{problem['name']}</td>
                <td class="{status_class}">{problem['status']}</td>
                <td>{problem['creation_time'].strftime('%Y-%m-%d %H:%M:%S') if problem['creation_time'] else '-'}</td>
                <td>{solution_links}</td>
                <td>{error_details}</td>
            </tr>
        """)
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table_rows_str = '\n'.join(table_rows)
    
    # Use f-string for the entire HTML template
    html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetCode Progress Report</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif;
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
        </style>
        <script>
            // Intercept clicks on Python and Markdown file links and redirect to appropriate viewers
            document.addEventListener('DOMContentLoaded', function() {{
                document.addEventListener('click', function(event) {{
                    // Check if the clicked element is a link
                    if (event.target.tagName === 'A') {{
                        const href = event.target.getAttribute('href');
                        // Create an absolute URL if it's a relative path
                        const absolutePath = href.startsWith('http') ? href : new URL(href, window.location.href).href;
                        
                        // Handle Python files
                        if (href.endsWith('.py')) {{
                            event.preventDefault();
                            window.location.href = `code-viewer.html?file=${{encodeURIComponent(absolutePath)}}`;
                        }} 
                        // Handle Markdown files
                        else if (href.endsWith('.md')) {{
                            event.preventDefault();
                            window.location.href = `markdown-viewer.html?file=${{encodeURIComponent(absolutePath)}}`;
                        }}
                    }}
                }});
            }});
        </script>
    </head>
    <body>
        <h1>LeetCode Progress Report</h1>
        
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
                    <th>Created</th>
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

def main():
    # 读取README.md获取所有题目
    with open("README.md", 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 提取题目信息
    leetcode_pattern = r'([^/]+) / ([^[]+) \[LeetCode (\d+)\]'
    matches = re.findall(leetcode_pattern, content)
    
    problems = []
    for match in matches:
        chinese_name, english_name, leetcode_number = match
        folder_name = f"llama4_maverick_solutions/leetcode_{leetcode_number}_{english_name.strip().lower().replace(' ', '_')}"
        
        # Clean up problem names
        clean_english, clean_chinese = clean_problem_name(english_name, chinese_name)
        
        # 分析解决方案
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
    
    # 按题号排序
    problems.sort(key=lambda x: int(x['number']))
    
    # 生成HTML报告
    html = generate_html_report(problems)
    
    # 保存并打开报告
    report_path = "llm_solution_comparison_report.html"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Report generated: {os.path.abspath(report_path)}")
    webbrowser.open(f"file://{os.path.abspath(report_path)}")

if __name__ == "__main__":
    main() 