import datetime
import pymongo
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/MRI"
with open('dbLogin.json', 'r') as file:
    data = json.load(file)
client = MongoClient(uri,username=data["user"],password=data["pass"],authSource="admin")
database=client["MRI"]
collection=database["MRI"]

def insert_mri(mri):
    now=datetime.datetime.now(tz=datetime.timezone.utc)
    mri_soup = BeautifulSoup(mri)
    mri_soup = BeautifulSoup(str(mri_soup.center.extract()),"html.parser")
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
        print(td.get("style"))
        if (td.get("style")=='padding: 0px 18px 9px; font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;'):
            count+=1
            if count==3:
                description=td.text[12:]
                break
    #centers = mri_soup.find_all("center")
    #print("Centers :",centers)
    #print("Len centers", len(centers))
    #centers[1].decompose()
    scripts=mri_soup.find_all("script")
    for script in scripts:
        script.decompose()
    mri=str(mri_soup)
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