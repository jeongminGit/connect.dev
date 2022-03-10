
from flask import Flask, render_template, request, jsonify, redirect, url_for
import certifi
from pymongo import MongoClient
app = Flask(__name__)

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.connect_dev

# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})


doc = {"id": "shinshin",
'pw': "6885312a00c4e6ba444ae8a777f14bcf95682314e5bdb5225a87980d780b44b9",
'name': "신상렬",
'job': "백엔드개발자",
'comment': "야호아호안녕",
'num': "node.js",
'url1':"http://ji.so",
'url2':"",
'url3':""}
db.users.insert_one(doc)


# 6885312a00c4e6ba444ae8a777f14bcf95682314e5bdb5225a87980d780b44b9
# ad8f03413a50100f56c0b44d3da8d22e60d949497adbf2a80d4d87cc0fd074ed