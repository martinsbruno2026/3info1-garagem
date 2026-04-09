from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/veiculos/":
            data = [{"id":1,"modelo":"Onix","ano":2020,"preco":50000}]
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

server = HTTPServer(('0.0.0.0',8000), Handler)
print("Running on 8000")
server.serve_forever()
