from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(f'hi {user}'.encode())
    self.wfile.write("<h1>this is h1 tag</h1>".encode('utf-8'))
    return {
      "statusCode": 200, 
      "headers": {'content-type': 'text/html'},
      "body": 'hello word'
    }