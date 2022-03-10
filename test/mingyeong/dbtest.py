from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.snoopso

# myId_receive = db.users.find_one()['_id']
# print(myId_receive)

doc = {
'id': "etest",
'name': "암아알",
'job':"프론트엔드 개발자",
'comment':"졸려요",
'num': "Node.js",
'url1': "https://www.youtube.com/",
'url2': "https://www.youtube.com/",
'url3': "https://www.youtube.com/"}
db.users.insert_one(doc)

# doc = {'user_id':'mingyeongso','following_id':'snoopso'}
# db.follows.insert_one(doc)