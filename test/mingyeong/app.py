from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.Test
app = Flask(__name__)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/myID', methods=['GET'])
def myID():
    myID = list(db.users.find({}, {'_id': False}))
    print(myID)
    return jsonify({'myID': myID})

@app.route('/followCheck', methods=['GET'])
def recommendList():
    recommendList = list(db.follows.find({}, {'_id': False}))
    print(recommendList)
    return jsonify({'recommendList': recommendList})

<<<<<<< HEAD
=======
# @app.route('/recommendList', methods=['GET'])
# def recommendList():
#     listID = list(db.users.find({}, {'_id': False}))
#     print(listID)
#     return jsonify({'listID': listID})
>>>>>>> parent of f7d03ba (feat: follow 기능 구현 완료, follow 하지 않은 사람들 추천 기능 구현 완료)

@app.route('/follow', methods=['POST'])
def follow():
   myID = request.form['myID']
   followingID = request.form['followingID']
   follow = {'user_id': myID, 'following_id': followingID}
   db.follows.insert_one(follow)
   return jsonify({'result':'success', 'msg': '팔로우했습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)