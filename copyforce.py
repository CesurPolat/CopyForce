from genericpath import exists
from http.server import BaseHTTPRequestHandler, HTTPServer

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        f = open("Website/404.html","r")
        if self.path == "/":
            self.path="/index.html"
        if exists("Website"+self.path):
            f = open("Website"+self.path, "r")
        
        self.wfile.write(bytes(f.read(),"utf-8"))

server = HTTPServer(("",80),NeuralHTTP)
print("Server Running...")
server.serve_forever()