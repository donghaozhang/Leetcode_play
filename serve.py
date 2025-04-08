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
            print(f"Server started. Access at http://localhost:{PORT}")
            print("Enter the URL above in your browser to view the LeetCode solution website.")
            print("Press Ctrl+C to stop the server.")
            
            # Start browser in a separate thread
            threading.Thread(target=open_browser, daemon=True).start()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"\nError: Port {PORT} is already in use. Another instance may be running.")
            print(f"You can try accessing http://localhost:{PORT}/llm_analysis_result/models_comparison_report.html")
        else:
            print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print(f"Starting HTTP server in directory {os.getcwd()}")
    print("This will allow your browser to properly load all Python and Markdown files.")
    print("Preparing to open the model comparison report...")
    run_server() 