

from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient
app = Flask(__name__)

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.connect_dev


# 문영안

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   user_list = list(db.users.find({},{'_id':False}))
   return jsonify({'moons': user_list})

# 신상렬

# 메인 프로필화면 출력
@app.route('/profile')
def profile_main():
    return render_template('profile_main.html')

# 메인 프로필 화면에 DB정보 출력
@app.route("/profile_main", methods=["GET"])
def profile_upload():
    profile = list(db.users.find({}, {'_id': False}))
    return jsonify({'profiling': profile})

# 프로필 만들기 창에서 프로필 정보를 DB에 저장
@app.route('/profile_mk_post', methods=["POST"])
def profile_post():
    url1_receive = request.form['url1_give']
    url2_receive = request.form['url2_give']
    url3_receive = request.form['url3_give']
    name_receive = request.form['name_give']
    job_receive = request.form['job_give']
    comment_receive = request.form['comment_give']
    num_receive = request.form['num_give']

    doc = {
        'name': name_receive,
        'job': job_receive,
        'comment': comment_receive,
        'num': num_receive,
        'url1': url1_receive,
        'url2': url2_receive,
        'url3': url3_receive,
    }
    db.users.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

# 프로필 만들기 창 출력
@app.route('/profile_mk')
def profile_mk():
    return render_template('profile_mk.html')

# 수정하기 창 출력
@app.route('/profile_revise')
def profile_revise():
    return render_template('profile_revise.html')

# 수정하기 창에서 새로운 정보를 DB에 저장
@app.route('/profile_revise_upload', methods=["POST"])
def profile_revise_upload():
    url1_receive = request.form['url1_give']
    url2_receive = request.form['url2_give']
    url3_receive = request.form['url3_give']
    name_receive = request.form['name_give']
    job_receive = request.form['job_give']
    comment_receive = request.form['comment_give']
    num_receive = request.form['num_give']

    doc = {
        'name': name_receive,
        'job': job_receive,
        'comment': comment_receive,
        'num': num_receive,
        'url1': url1_receive,
        'url2': url2_receive,
        'url3': url3_receive,
    }
    db.users.insert_one(doc)

    return jsonify()

# DB에서 기존 정보 삭제
@app.route('/profile_revise_delete', methods=["POST"])
def profile_delete():
    name_receive = request.form['name_give']
    db.users.delete_one({'name':name_receive})

    return jsonify({'msg':'저장완료!'})


# 소민경

@app.route('/myFollowing')
def myfollowing():
    return render_template('following.html')

# 1 나의 ID를 불러오기
@app.route('/myID', methods=['GET'])
def myID():
    myID = list(db.users.find({}, {'_id': False}))
    print(myID)
    return jsonify({'myID': myID})

# 2 팔로우를 추천하는 (내가 팔로우하지 않는) 유저 목록 카드로 붙여넣기
@app.route('/followCheck', methods=['GET'])
def followCheck():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 3 내가 팔로우한 유저 목록 카드로 붙여넣기
@app.route('/followCheck2', methods=['GET'])
def followCheck2():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 4 내가 팔로우한 유저 숫자 가져오기
@app.route('/followingNum', methods=['GET'])
def followingNum():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 5 나를 팔로우한 유저 숫자 가져오기
@app.route('/followerNum', methods=['GET'])
def followerNum():
    recommendList = list(db.follows.find({}, {'_id': False}))
    userList = list(db.users.find({}, {'_id': False}))
    return jsonify({'recommendList': recommendList, 'userList': userList})

# 6 팔로우 기능 실행
@app.route('/follow', methods=['POST'])
def follow():
   myID = request.form['myID']
   followingID = request.form['followingID']
   follow = {'user_id': myID, 'following_id': followingID}
   db.follows.insert_one(follow)
   return jsonify({'result':'success', 'msg': followingID + '를 팔로우했습니다.'})

# 7 언팔로우 기능 실행
@app.route('/unfollow', methods=['POST'])
def unfollow():
   myID = request.form['myID']
   followingID = request.form['followingID']
   unfollow = {'user_id': myID, 'following_id': followingID}
   db.follows.delete_one(unfollow)
   return jsonify({'result':'success', 'msg': '언팔로우했습니다.'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug=True)