import logging
logging.basicConfig(filename='mongo.txt',level=logging.INFO,filemode="w",format="%(asctime)s:%(message)s")
logging.info("Collection of data")
import pymongo
client = pymongo.MongoClient("mongodb+srv://pmahajan:usNdn4bWjQk5d9qU@cluster0.0gfbg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['Inventory']
collection=database['tablen01']
a=collection.find({"qty":75})
for i in a :
    logging.info(i)