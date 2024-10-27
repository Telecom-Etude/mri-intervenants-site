import datetime
import pymongo
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
#from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/MRI"
client = MongoClient(uri)
database=client["MRI"]
collection=database["MRI"]

def insert_mri(mri):
    now=datetime.datetime.now(tz=datetime.timezone.utc)
    mri_soup = BeautifulSoup(mri)
    title=mri_soup.find("h1").text
    print(title)
    
