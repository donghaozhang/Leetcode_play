import http.server
import socketserver
import os
import sys
import webbrowser
import threading
import time

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    # Add CORS headers to allow loading resources
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()
    
    # Ensure proper content type for different file types
    def guess_type(self, path):
        if path.endswith('.py'):
            return 'text/plain'
        elif path.endswith('.md'):
            return 'text/markdown'
        return super().guess_type(path)

def open_browser():
    """Open the models comparison report in the default browser"""
    # Wait a moment for the server to start
    time.sleep(1)
    
    # Path to the comparison report
    report_path = "llm_analysis_result/models_comparison_report.html"
    
    # Check if the report exists
    if os.path.exists(report_path):
        url = f"http://localhost:{PORT}/{report_path}"
        print(f"Opening models comparison report: {url}")
        webbrowser.open(url)
    else:
        # Fallback to opening the server root
        print(f"Models comparison report not found at {report_path}")
        print(f"Opening server root instead")
        webbrowser.open(f"http://localhost:{PORT}")

def run_server():
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print(f"服务器已启动，请访问 http://localhost:{PORT}")
            print("在浏览器中输入上面的URL来查看LeetCode题解网站。")
            print("按Ctrl+C可停止服务器。")
            
            # Start browser in a separate thread
            threading.Thread(target=open_browser, daemon=True).start()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止。")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\n错误: 端口 {PORT} 已被占用。可能已有另一个实例正在运行。")
            print(f"你可以尝试访问 http://localhost:{PORT}/llm_analysis_result/models_comparison_report.html")
        else:
            print(f"\n错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print(f"正在目录 {os.getcwd()} 中启动HTTP服务器")
    print("这将允许您的浏览器正确加载所有Python和Markdown文件。")
    print("正在准备打开模型比较报告...")
    run_server() 