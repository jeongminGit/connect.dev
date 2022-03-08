from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.connect_dev

@app.route('/')
def home():
    return render_template('profile.html')

# mkprofile.html용
@app.route("/connect_dev", methods=["POST"])
def profile_post():
    url1_receive = request.form['url1_give']
    url2_receive = request.form['url2_give']
    url3_receive = request.form['url3_give']
    name_receive = request.form['name_give']
    job_receive = request.form['job_give']
    comment_receive = request.form['comment_give']
    num_receive = request.form['num_give']

    doc = {
        'name':name_receive,
        'job':job_receive,
        'comment':comment_receive,
        'num': num_receive,
        'url1': url1_receive,
        'url2': url2_receive,
        'url3': url3_receive,
    }
    db.user.insert_one(doc)

    return jsonify({'msg':'저장완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)