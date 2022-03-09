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

@app.route('/myFollowing')
def myfollowing():
    return render_template('following.html')

# 나의 ID를 불러오기
@app.route('/myID', methods=['GET'])
def myID():
    myID = list(db.users.find({}, {'_id': False}))
    print(myID)
    return jsonify({'myID': myID})

# 팔로우를 추천하는 (내가 팔로우하지 않는) 유저 목록 카드로 붙여넣기
@app.route('/followCheck', methods=['GET'])
def followCheck():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 내가 팔로우한 유저 목록 카드로 붙여넣기
@app.route('/followCheck2', methods=['GET'])
def followCheck2():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 내가 팔로우한 유저 숫자 가져오기
@app.route('/followingNum', methods=['GET'])
def followingNum():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 나를 팔로우한 유저 숫자 가져오기
@app.route('/followerNum', methods=['GET'])
def followerNum():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 팔로우 기능 실행
@app.route('/follow', methods=['POST'])
def follow():
   myID = request.form['myID']
   followingID = request.form['followingID']
   follow = {'user_id': myID, 'following_id': followingID}
   db.follows.insert_one(follow)
   return jsonify({'result':'success', 'msg': followingID + '를 언팔로우했습니다.'})

# 언팔로우 기능 실행
@app.route('/unfollow', methods=['POST'])
def unfollow():
   myID = request.form['myID']
   followingID = request.form['followingID']
   unfollow = {'user_id': myID, 'following_id': followingID}
   db.follows.delete_one(unfollow)
   return jsonify({'result':'success', 'msg': followingID + '를 언팔로우했습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)