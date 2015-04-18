import webbrowser
import http.server
import socketserver


Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8000), Handler)
webbrowser.open_new_tab("http://127.0.0.1:8000")
httpd.serve_forever()
