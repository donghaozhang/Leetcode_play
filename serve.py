import http.server
import socketserver
import os
import sys
import webbrowser
import threading
import time
import socket

PORT = 8000

# Custom request handler that adds CORS headers
class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()
    
    def guess_type(self, path):
        """Guess the type of a file based on its extension."""
        base, ext = os.path.splitext(path)
        if ext == '.md':
            return 'text/markdown'
        return super().guess_type(path)

def open_browser():
    """Open the models comparison report in a web browser."""
    # Wait for the server to start
    time.sleep(1)
    
    # Path to the models comparison report
    report_path = "llm_analysis_result/models_comparison_report.html"
    
    # Check if the report exists
    if os.path.exists(report_path):
        url = f"http://localhost:8000/{report_path}"
        print(f"\nOpening models comparison report at: {url}")
        webbrowser.open(url)
    else:
        # If report doesn't exist, open the server root
        url = "http://localhost:8000"
        print(f"\nModels comparison report not found. Opening server root at: {url}")
        webbrowser.open(url)

def run_server():
    PORT = 8000
    Handler = CORSHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            
            # Start a thread to open the browser
            threading.Thread(target=open_browser, daemon=True).start()
            
            # Start the server
            httpd.serve_forever()
    except socket.error as e:
        if e.errno == 10048:  # Port already in use
            print(f"Port {PORT} is already in use. The server might already be running.")
            print(f"Try accessing: http://localhost:{PORT}/llm_analysis_result/models_comparison_report.html")
        else:
            print(f"Socket error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    print(f"Starting HTTP server in directory {os.getcwd()}")
    print("This will allow your browser to properly load all Python and Markdown files.")
    print("Preparing to open the model comparison report...")
    run_server() 