import http.server
import socketserver
import os
import sys

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

def run_server():
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print(f"服务器已启动，请访问 http://localhost:{PORT}")
            print("在浏览器中输入上面的URL来查看LeetCode题解网站。")
            print("按Ctrl+C可停止服务器。")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止。")
        sys.exit(0)

if __name__ == "__main__":
    print(f"正在目录 {os.getcwd()} 中启动HTTP服务器")
    print("这将允许您的浏览器正确加载所有Python和Markdown文件。")
    run_server() 