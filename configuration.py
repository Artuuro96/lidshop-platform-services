from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

url = config("MONGODB_URL")
client = MongoClient(url, server_api=ServerApi('1'))
db = client.lidshop
