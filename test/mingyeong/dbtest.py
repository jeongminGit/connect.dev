from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.Test

# myId_receive = db.users.find_one()['_id']
# print(myId_receive)

<<<<<<< HEAD
<<<<<<< HEAD
doc = {'name':'졸리다','id':'sleepy'}
=======
doc = {'name':'야호야호','id':'hoya'}
>>>>>>> parent of f7d03ba (feat: follow 기능 구현 완료, follow 하지 않은 사람들 추천 기능 구현 완료)
=======
doc = {'name':'야호야호','id':'hoya'}
>>>>>>> parent of f7d03ba (feat: follow 기능 구현 완료, follow 하지 않은 사람들 추천 기능 구현 완료)
db.users.insert_one(doc)

# doc = {'user_id':'snoopso','following_id':'mingyeongso'}
# db.follows.insert_one(doc)