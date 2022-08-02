import pymongo
import os


myclient = pymongo.MongoClient( os.environ.get('MONGODB_URI') )
mydb = myclient['sample_weatherdata']
mycol = mydb['data']
mydata = mycol.find_one()