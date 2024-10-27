import datetime
import pymongo
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/MRI"
client = MongoClient(uri)
database=client["MRI"]
collection=database["MRI"]

def insert_mri(mri):
    now=datetime.datetime.now(tz=datetime.timezone.utc)
    mri_soup = BeautifulSoup(mri)
    title=mri_soup.find("h1").text
    print(title)
    h4s=mri_soup.find_all("h4")
    print(h4s)
    domaine = h4s[1].text
    retribution = h4s[3].text
    difficulty = h4s[5].text
    tds = mri_soup.find_all("td")
    print("Recherche de la description:")
    count=0
    description=""
    for td in tds:
        if (td.get("style")=="padding-top:0;padding-right:18px;padding-bottom:9px;padding-left:18px"):
            count+=1
            if count==2:
                description=td.text
                break
    
    collection.insert_one({
        "title":title,
        "description":description,
        "date":now,
        "domaine":domaine,
        "retribution":retribution,
        "difficulty":difficulty,
        "mri":mri
        })
           
def get_mris():
    now=datetime.datetime.now(tz=datetime.timezone.utc)
    month_ago=now-datetime.timedelta(days=30)
    dico_recherche={
        "date":{
            "$gt":month_ago
    }}
    return collection.find(dico_recherche,{"mri":0,"date":0})

def getMri(identifier):
    return collection.find_one({"_id":ObjectId(identifier)})
def cleanResult(result):
    result["_id"]=str(result["_id"])
    return result