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
    html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>力扣刷题进度报告</title>
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
        </style>
    </head>
    <body>
        <h1>力扣刷题进度报告</h1>
        
        <div class="summary">
            <h2>统计信息</h2>
            <p>总题目数: {total_problems}</p>
            <p>已解决: {solved_count} ({solved_percentage:.1f}%)</p>
            <p>通过测试: {passed_count} ({passed_percentage:.1f}%)</p>
            <p>有语法错误: {error_count} ({error_percentage:.1f}%)</p>
        </div>
        
        <table>
            <thead>
                <tr>
                    <th>题号</th>
                    <th>题目名称</th>
                    <th>状态</th>
                    <th>创建时间</th>
                    <th>详细信息</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        
        <div class="last-updated">
            最后更新时间: {current_time}
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
    
    # 计算统计数据
    total_problems = len(problems)
    solved_count = sum(1 for p in problems if p['status'] != '未解决')
    passed_count = sum(1 for p in problems if p['status'] == '通过')
    error_count = sum(1 for p in problems if p['status'] == '语法错误')
    
    solved_percentage = (solved_count / total_problems * 100) if total_problems > 0 else 0
    passed_percentage = (passed_count / total_problems * 100) if total_problems > 0 else 0
    error_percentage = (error_count / total_problems * 100) if total_problems > 0 else 0
    
    # 生成表格行
    table_rows = []
    for i, problem in enumerate(problems):
        status_class = {
            '通过': 'status-pass',
            '语法错误': 'status-fail',
            '未解决': 'status-unknown'
        }[problem['status']]
        
        error_details = ''
        if problem['status'] == '语法错误' and problem['error_msg']:
            error_id = f"error-{i}"
            error_details = f"""
                <span class="toggle-error" onclick="toggleErrorDetails('{error_id}')">查看错误</span>
                <div id="{error_id}" class="error-details">{problem['error_msg']}</div>
            """
        
        table_rows.append(f"""
            <tr>
                <td>{problem['number']}</td>
                <td>{problem['chinese_name']}</td>
                <td class="{status_class}">{problem['status']}</td>
                <td>{problem['creation_time'].strftime('%Y-%m-%d %H:%M:%S') if problem['creation_time'] else '-'}</td>
                <td>{error_details}</td>
            </tr>
        """)
    
    # 填充HTML模板
    html = html.format(
        total_problems=total_problems,
        solved_count=solved_count,
        solved_percentage=solved_percentage,
        passed_count=passed_count,
        passed_percentage=passed_percentage,
        error_count=error_count,
        error_percentage=error_percentage,
        table_rows='\n'.join(table_rows),
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    return html

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
        
        # 分析解决方案
        analysis = analyze_solution(folder_name)
        
        if analysis:
            status = '通过' if not analysis['has_error'] else '语法错误'
            problems.append({
                'number': leetcode_number,
                'chinese_name': chinese_name.strip(),
                'status': status,
                'creation_time': analysis['creation_time'],
                'error_msg': analysis['error_msg']
            })
        else:
            problems.append({
                'number': leetcode_number,
                'chinese_name': chinese_name.strip(),
                'status': '未解决',
                'creation_time': None,
                'error_msg': None
            })
    
    # 按题号排序
    problems.sort(key=lambda x: int(x['number']))
    
    # 生成HTML报告
    html = generate_html_report(problems)
    
    # 保存并打开报告
    report_path = "leetcode_progress_report.html"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"报告已生成: {os.path.abspath(report_path)}")
    webbrowser.open(f"file://{os.path.abspath(report_path)}")

if __name__ == "__main__":
    main() 