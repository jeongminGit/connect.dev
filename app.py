

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

# 배정민

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'connect'

# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib


#################################
##  HTML을 주는 부분             ##
#################################
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload['id']})
        return render_template('login.html', nickname=user_info["id"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="환영합니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


#################################
##  로그인을 위한 API            ##
#################################

# [회원가입 API]
# id, pw, nickname을 받아서, mongoDB에 저장합니다.
# 저장하기 전에, pw를 sha256 방법(=단방향 암호화. 풀어볼 수 없음)으로 암호화해서 저장합니다.
@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.users.insert_one({'id': id_receive, 'pw': pw_hash})

    return jsonify({'result': 'success'})


# [로그인 API]
# id, pw를 받아서 맞춰보고, 토큰을 만들어 발급합니다.
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.users.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload(로그인한 정보:id, 유효시간)와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
        #    'name': name_receive
        #    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # 왜 decode('utf-8')을 지워야 하는가???
        # token = jwt.encode(payload, SECRET_KEY(서버만의 비밀키), algorithm='HS256').decode('utf-8')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

# [아이디 중복확인 API]
@app.route('/api/register/check_dup', methods=['POST'])
def check_dup():
    id_receive = request.form['id_give']
    exists = bool(db.users.find_one({"id": id_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# [유저 정보 확인 API]
# 로그인된 유저만 call 할 수 있는 API입니다.
# 유효한 토큰을 줘야 올바른 결과를 얻어갈 수 있습니다.
# (그렇지 않으면 남의 장바구니라든가, 정보를 누구나 볼 수 있겠죠?)

@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    # try / catch 문?
    # try 아래를 실행했다가, 에러가 있으면 except 구분으로 가란 얘기입니다.

    try:
        # token을 시크릿키로 디코딩합니다.
        # 보실 수 있도록 payload를 print 해두었습니다. 우리가 로그인 시 넣은 그 payload와 같은 것이 나옵니다.
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        # payload 안에 id가 들어있습니다. 이 id로 유저정보를 찾습니다.
        # 여기에선 그 예로 닉네임을 보내주겠습니다.
        userinfo = db.users.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:
        # 위를 실행했는데 만료시간이 지났으면 에러가 납니다.
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})



if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug=True)