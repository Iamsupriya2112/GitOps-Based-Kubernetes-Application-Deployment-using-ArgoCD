from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"GitOps Python App Running Successfully!...")

PORT = 5000
server = HTTPServer(('', PORT), handler)
server.serve_forever()