import http.server
import socketserver
import webbrowser
import os

PORT = 8000

if __name__ == "__main__":
    # Change working directory to where the HTML file is
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    # Launch browser
    webbrowser.open(f"http://localhost:{PORT}")

    # Start server
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
