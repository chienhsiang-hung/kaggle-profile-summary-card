import pymongo
import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        myclient = pymongo.MongoClient( os.environ.get('MONGODB_URI') )
        mydb = myclient['sample_weatherdata']
        mycol = mydb['data']

        mydata = mycol.find_one()
        print(mydata)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        self.wfile.write('Succeseed.'.encode())

        from util import mongodb
        self.wfile.write(str(mongodb.mydata).encode())
        return