

from flask import Flask, render_template, request, jsonify
import certifi
from pymongo import MongoClient
app = Flask(__name__)

ca = certifi.where()
client = MongoClient("mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.dbsparta


# doc = {
#         'name': 'B',
#         'job': '프론트엔드 개발자',
#         'comment': '소개글을 써볼까....',
#         'num': 'React'
# }
# db.moons.insert_one(doc)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
   user_list = list(db.moons.find({},{'_id':False}))
   return jsonify({'moons': user_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)