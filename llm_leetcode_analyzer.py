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

def setup_viewers(results_dir):
    """Copy and setup the code and markdown viewers"""
    # Copy the existing style.css file to the results directory
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        source_css_path = os.path.join(current_dir, "style.css")
        
        if os.path.exists(source_css_path):
            # Copy the existing CSS file
            with open(source_css_path, 'r', encoding='utf-8') as source:
                css_content = source.read()
                with open(os.path.join(results_dir, "style.css"), 'w', encoding='utf-8') as target:
                    target.write(css_content)
            print(f"Copied style.css to {results_dir}")
        else:
            # Create basic CSS if original not found
            print(f"style.css not found in {current_dir}. Creating a basic style.")
            basic_css = """
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2 {
                margin-bottom: 20px;
            }
            pre {
                background-color: #f5f5f5;
                padding: 15px;
                border-radius: 8px;
                overflow: auto;
            }
            .solution-links {
                display: flex;
                gap: 10px;
            }
            .solution-link {
                color: #007bff;
                text-decoration: none;
                padding: 5px 10px;
                border-radius: 4px;
                background-color: #f8f9fa;
            }
            .solution-link:hover {
                background-color: #e9ecef;
                text-decoration: underline;
            }
            """
            with open(os.path.join(results_dir, "style.css"), 'w', encoding='utf-8') as f:
                f.write(basic_css)
    except Exception as e:
        print(f"Warning: Could not copy or create style.css: {e}")
    
    # Create the code and markdown viewers
    code_viewer = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Viewer</title>
    <link rel="stylesheet" href="style.css">
    <!-- Add Prism.js for syntax highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-okaidia.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css">
    <style>
        .code-container {
            position: relative;
            background-color: #272822;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        
        .code-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 15px;
            background-color: #1e1f1c;
            border-radius: 8px 8px 0 0;
            border-bottom: 1px solid #3a3a3a;
        }
        
        .file-path {
            color: #f8f8f2;
            font-family: monospace;
            font-size: 0.9rem;
        }
        
        .actions {
            display: flex;
            gap: 10px;
        }
        
        .action-button {
            background: none;
            border: none;
            color: #f8f8f2;
            cursor: pointer;
            font-size: 0.9rem;
            padding: 2px 8px;
            border-radius: 4px;
        }
        
        .action-button:hover {
            background-color: #3a3a3a;
        }
        
        pre {
            margin: 0;
            border-radius: 0 0 8px 8px;
            max-height: 700px;
            overflow: auto;
        }
        
        code {
            font-family: 'Fira Code', 'Consolas', 'Monaco', monospace;
            font-size: 14px;
            tab-size: 4;
        }
        
        .line-numbers .line-numbers-rows {
            border-right: 1px solid #3a3a3a;
        }
        
        .back-to-list {
            display: inline-block;
            margin-bottom: 20px;
            color: #007bff;
            text-decoration: none;
        }
        
        .back-to-list:hover {
            text-decoration: underline;
        }
        
        #loading {
            text-align: center;
            padding: 20px;
            font-style: italic;
            color: #666;
        }
        
        .file-error {
            background-color: #fff3f3;
            border-left: 4px solid #ff6b6b;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }
        
        .file-error h3 {
            margin-top: 0;
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>LeetCode Solution Code Viewer</h1>
        
        <a href="models_comparison_report.html" class="back-to-list">← Back to Comparison</a>
        
        <div id="loading">Loading...</div>
        
        <div id="error-container" style="display: none;">
            <div class="file-error">
                <h3>File Load Error</h3>
                <p id="error-message">Unable to load file. This might be due to browser security restrictions.</p>
                <p>Due to browser security restrictions, some files might not be directly accessible. Try these options:</p>
                <ol>
                    <li>Make sure you're using the web server to view files (not opening directly from filesystem)</li>
                    <li>Enter code manually in the box below</li>
                    <li>View the original file: <a id="error-file-link" href="#" target="_blank">View Original File</a></li>
                </ol>
            </div>
            
            <div class="manual-input">
                <h3>Manual Code Input</h3>
                <p>You can copy code from the original file and paste it below, then click "Display Code":</p>
                <textarea id="manual-code" style="width:100%;min-height:300px;" placeholder="Paste Python code here..."></textarea>
                <br><br>
                <button id="display-manual-code" style="background:#007bff;color:white;border:none;padding:10px 16px;border-radius:4px;cursor:pointer;">Display Code</button>
            </div>
        </div>
        
        <div id="code-viewer" style="display: none;">
            <h2 id="file-title">File Name</h2>
            
            <div class="code-container">
                <div class="code-header">
                    <div class="file-path" id="file-path">Path/to/file</div>
                    <div class="actions">
                        <button class="action-button" id="copy-btn">Copy Code</button>
                        <button class="action-button" id="raw-btn">View Raw File</button>
                    </div>
                </div>
                <pre class="line-numbers"><code id="code-content" class="language-python"></code></pre>
            </div>
        </div>
    </div>

    <!-- Add Prism.js for syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>
    
    <script>
        function displayCode(code, filePath) {
            // Display the code with syntax highlighting
            const codeElement = document.getElementById('code-content');
            codeElement.textContent = code;
            
            // Detect language from file extension
            const fileExt = filePath.split('.').pop().toLowerCase();
            let language = 'python'; // Default
            
            // Map file extensions to Prism language classes
            const langMap = {
                'py': 'python',
                'js': 'javascript',
                'ts': 'typescript',
                'html': 'html',
                'css': 'css',
                'json': 'json',
                'md': 'markdown'
            };
            
            if (langMap[fileExt]) {
                language = langMap[fileExt];
                codeElement.className = `language-${language}`;
            }
            
            // Force Prism to highlight the code
            Prism.highlightElement(codeElement);
            
            // Show the code viewer
            document.getElementById('loading').style.display = 'none';
            document.getElementById('code-viewer').style.display = 'block';
            
            // Update file title and path
            const fileName = filePath.split('/').pop();
            document.getElementById('file-title').textContent = fileName;
            document.getElementById('file-path').textContent = filePath;
            document.title = `${fileName} - Code Viewer`;
            
            // Add event listeners for buttons
            document.getElementById('copy-btn').addEventListener('click', function() {
                navigator.clipboard.writeText(code)
                    .then(() => alert('Code copied to clipboard'))
                    .catch(err => console.error('Copy failed:', err));
            });
            
            document.getElementById('raw-btn').addEventListener('click', function() {
                window.location.href = filePath;
            });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            // Get file path from URL parameter
            const urlParams = new URLSearchParams(window.location.search);
            const filePath = urlParams.get('file');
            
            if (!filePath) {
                document.getElementById('loading').textContent = 'No file path specified';
                return;
            }
            
            // Setup error handling UI
            document.getElementById('error-file-link').href = filePath;
            
            // Try different methods to load the file
            let loadedSuccessfully = false;
            
            // First try XMLHttpRequest (works better with local files)
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200 && !loadedSuccessfully) {
                        loadedSuccessfully = true;
                        displayCode(xhr.responseText, filePath);
                    } else if (xhr.status !== 200 && !loadedSuccessfully) {
                        // If XHR fails, try fetch API as backup
                        fetch(filePath)
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error(`HTTP error! Status: ${response.status}`);
                                }
                                return response.text();
                            })
                            .then(code => {
                                loadedSuccessfully = true;
                                displayCode(code, filePath);
                            })
                            .catch(error => {
                                if (!loadedSuccessfully) {
                                    document.getElementById('loading').style.display = 'none';
                                    document.getElementById('error-message').textContent = `Load error: ${error.message}`;
                                    document.getElementById('error-container').style.display = 'block';
                                }
                            });
                    }
                }
            };
            xhr.open('GET', filePath, true);
            xhr.send();
            
            // Setup manual code input button
            document.getElementById('display-manual-code').addEventListener('click', function() {
                const manualCode = document.getElementById('manual-code').value;
                if (manualCode.trim()) {
                    displayCode(manualCode, filePath);
                    document.getElementById('error-container').style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>"""

    markdown_viewer = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Viewer</title>
    <link rel="stylesheet" href="style.css">
    <!-- GitHub Markdown CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
    <!-- Prism for code highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-okaidia.min.css">
    <style>
        .markdown-container {
            position: relative;
            background-color: #fff;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            padding: 20px 30px;
        }
        
        .markdown-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 15px;
            background-color: #f6f8fa;
            border-radius: 8px 8px 0 0;
            border-bottom: 1px solid #e1e4e8;
            margin: -20px -30px 20px;
        }
        
        .file-path {
            font-family: monospace;
            font-size: 0.9rem;
            color: #586069;
        }
        
        .actions {
            display: flex;
            gap: 10px;
        }
        
        .action-button {
            background: none;
            border: 1px solid #ddd;
            color: #24292e;
            cursor: pointer;
            font-size: 0.9rem;
            padding: 2px 8px;
            border-radius: 4px;
        }
        
        .action-button:hover {
            background-color: #f1f1f1;
        }
        
        .back-to-list {
            display: inline-block;
            margin-bottom: 20px;
            color: #007bff;
            text-decoration: none;
        }
        
        .back-to-list:hover {
            text-decoration: underline;
        }
        
        #loading {
            text-align: center;
            padding: 20px;
            font-style: italic;
            color: #666;
        }
        
        .file-error {
            background-color: #fff3f3;
            border-left: 4px solid #ff6b6b;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }
        
        .file-error h3 {
            margin-top: 0;
            color: #e74c3c;
        }
        
        /* GitHub Markdown customization */
        .markdown-body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            word-wrap: break-word;
            padding: 15px 0;
        }
        
        .markdown-body pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.5;
            background-color: #282c34;
            border-radius: 6px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        }
        
        .markdown-body code {
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>LeetCode Solution Markdown Viewer</h1>
        
        <a href="models_comparison_report.html" class="back-to-list">← Back to Comparison</a>
        
        <div id="loading">Loading...</div>
        
        <div id="error-container" style="display: none;">
            <div class="file-error">
                <h3>File Load Error</h3>
                <p id="error-message">Unable to load file. This might be due to browser security restrictions.</p>
                <p>Due to browser security restrictions, some files might not be directly accessible. Try these options:</p>
                <ol>
                    <li>Make sure you're using the web server to view files (not opening directly from filesystem)</li>
                    <li>Enter markdown manually in the box below</li>
                    <li>View the original file: <a id="error-file-link" href="#" target="_blank">View Original File</a></li>
                </ol>
            </div>
            
            <div class="manual-input">
                <h3>Manual Markdown Input</h3>
                <p>You can copy markdown from the original file and paste it below, then click "Render Markdown":</p>
                <textarea id="manual-markdown" style="width:100%;min-height:300px;" placeholder="Paste markdown content here..."></textarea>
                <br><br>
                <button id="display-manual-markdown" style="background:#007bff;color:white;border:none;padding:10px 16px;border-radius:4px;cursor:pointer;">Render Markdown</button>
            </div>
        </div>
        
        <div id="markdown-viewer" style="display: none;">
            <h2 id="file-title">File Name</h2>
            
            <div class="markdown-container">
                <div class="markdown-header">
                    <div class="file-path" id="file-path">Path/to/file</div>
                    <div class="actions">
                        <button class="action-button" id="copy-btn">Copy Source</button>
                        <button class="action-button" id="raw-btn">View Raw File</button>
                    </div>
                </div>
                <div id="markdown-content" class="markdown-body"></div>
            </div>
        </div>
    </div>

    <!-- Add Marked.js for Markdown rendering -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    
    <!-- Add Prism.js for syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    
    <script>
        // Configure Marked to use Prism for syntax highlighting
        marked.setOptions({
            highlight: function(code, lang) {
                if (Prism.languages[lang]) {
                    return Prism.highlight(code, Prism.languages[lang], lang);
                } else {
                    return code;
                }
            },
            breaks: true,
            gfm: true
        });
        
        function renderMarkdown(markdown, filePath) {
            // Render the markdown content
            const markdownHTML = marked.parse(markdown);
            document.getElementById('markdown-content').innerHTML = markdownHTML;
            
            // Show the markdown viewer
            document.getElementById('loading').style.display = 'none';
            document.getElementById('markdown-viewer').style.display = 'block';
            
            // Update file title and path
            const fileName = filePath.split('/').pop();
            document.getElementById('file-title').textContent = fileName;
            document.getElementById('file-path').textContent = filePath;
            document.title = `${fileName} - Markdown Viewer`;
            
            // Add event listeners for buttons
            document.getElementById('copy-btn').addEventListener('click', function() {
                navigator.clipboard.writeText(markdown)
                    .then(() => alert('Markdown source copied to clipboard'))
                    .catch(err => console.error('Copy failed:', err));
            });
            
            document.getElementById('raw-btn').addEventListener('click', function() {
                window.location.href = filePath;
            });
            
            // Highlight all code blocks after rendering
            const codeBlocks = document.querySelectorAll('pre code');
            codeBlocks.forEach(block => {
                Prism.highlightElement(block);
            });
        }
        
        document.addEventListener('DOMContentLoaded', function() {
            // Get file path from URL parameter
            const urlParams = new URLSearchParams(window.location.search);
            const filePath = urlParams.get('file');
            
            if (!filePath) {
                document.getElementById('loading').textContent = 'No file path specified';
                return;
            }
            
            // Setup error handling UI
            document.getElementById('error-file-link').href = filePath;
            
            // Try different methods to load the file
            let loadedSuccessfully = false;
            
            // First try XMLHttpRequest (works better with local files)
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200 && !loadedSuccessfully) {
                        loadedSuccessfully = true;
                        renderMarkdown(xhr.responseText, filePath);
                    } else if (xhr.status !== 200 && !loadedSuccessfully) {
                        // If XHR fails, try fetch API as backup
                        fetch(filePath)
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error(`HTTP error! Status: ${response.status}`);
                                }
                                return response.text();
                            })
                            .then(markdown => {
                                loadedSuccessfully = true;
                                renderMarkdown(markdown, filePath);
                            })
                            .catch(error => {
                                if (!loadedSuccessfully) {
                                    document.getElementById('loading').style.display = 'none';
                                    document.getElementById('error-message').textContent = `Load error: ${error.message}`;
                                    document.getElementById('error-container').style.display = 'block';
                                }
                            });
                    }
                }
            };
            xhr.open('GET', filePath, true);
            xhr.send();
            
            // Setup manual markdown input button
            document.getElementById('display-manual-markdown').addEventListener('click', function() {
                const manualMarkdown = document.getElementById('manual-markdown').value;
                if (manualMarkdown.trim()) {
                    renderMarkdown(manualMarkdown, filePath);
                    document.getElementById('error-container').style.display = 'none';
                }
            });
        });
    </script>
</body>
</html>"""

    # Write the viewers to files
    with open(os.path.join(results_dir, "code-viewer.html"), 'w', encoding='utf-8') as f:
        f.write(code_viewer)
    
    with open(os.path.join(results_dir, "markdown-viewer.html"), 'w', encoding='utf-8') as f:
        f.write(markdown_viewer)

def generate_solution_links(model_name, problem, base_path=""):
    """Generate HTML for solution links with viewers"""
    if problem['status'] == 'Unsolved':
        return '-'
    
    # Create clean problem path
    problem_base = f"leetcode_{problem['number']}_{problem['name'].split(' (')[0].lower().replace(' ', '_')}"
    
    # For direct links use relative paths
    direct_path = f"{base_path}/{model_name}_solutions/{problem_base}"
    
    # For viewers, ensure proper path to the solution files
    # Use ../ as files are in the parent directory relative to the viewer in llm_analysis_result
    viewer_path = f"../{model_name}_solutions/{problem_base}"
    
    return f"""
        <div class="solution-links">
            <a href="{direct_path}/solution.py" class="solution-link" target="_blank">Python</a>
            <a href="{direct_path}/solution.md" class="solution-link" target="_blank">Solution</a>
            <a href="code-viewer.html?file={viewer_path}/solution.py" class="solution-link" target="_blank">View Python</a>
            <a href="markdown-viewer.html?file={viewer_path}/solution.md" class="solution-link" target="_blank">View Solution</a>
        </div>
    """

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
        
        # Generate solution links with relative path
        solution_links = generate_solution_links(model_name, problem, base_path="..")
        
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
            
            # Store the actual problem object for this model
            problem_details[number]['models'][model_name] = {
                'status': problem['status'],
                'status_class': status_class,
                'error_msg': problem.get('error_msg', None),
                'number': number,
                'name': problem['name']
            }
    
    # Generate comparison rows
    comparison_rows = []
    for number in sorted(problem_details.keys(), key=int):
        problem_info = problem_details[number]
        model_columns = []
        for model_name in model_results.keys():
            if model_name in problem_info['models']:
                model_data = problem_info['models'][model_name]
                
                # Generate proper solution links
                solution_links = generate_solution_links(
                    model_name, 
                    model_data,  # Pass the actual model data which has structure needed
                    base_path=".."
                )
                
                error_details = ''
                if model_data['status'] == 'Fail' and model_data.get('error_msg'):
                    error_id = f"error-{model_name}-{number}"
                    error_details = f"""
                        <span class="toggle-error" onclick="toggleErrorDetails('{error_id}')">View Error</span>
                        <div id="{error_id}" class="error-details">{model_data['error_msg']}</div>
                    """
            else:
                # Default values if this model doesn't have data for this problem
                model_data = {
                    'status': 'Unsolved',
                    'status_class': 'status-unknown'
                }
                solution_links = '-'
                error_details = ''
            
            model_columns.append(f"""
                <td class="{model_data['status_class']}">{model_data['status']}</td>
                <td>{solution_links}</td>
                <td>{error_details}</td>
            """)
        
        comparison_rows.append(f"""
            <tr>
                <td>{number}</td>
                <td>{problem_info['name']}</td>
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
    
    # Setup viewers
    setup_viewers(results_dir)
    
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