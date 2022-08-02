import pymongo
import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        client = pymongo.MongoClient( os.environ.get('MONGODB_URI') )
        db = client.test

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # self.wfile.write(os.environ.get('MONGODB_URI').encode())
        return