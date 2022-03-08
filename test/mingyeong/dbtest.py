from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.Test

# myId_receive = db.users.find_one()['_id']
# print(myId_receive)

# doc = {'name':'노논ㄴㄴ','id':'dkdjf9111'}
# db.users.insert_one(doc)

doc = {'user_id':'mingyeongso','following_id':'snoopso'}
db.follows.insert_one(doc)