from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://connect_dev:ukdzr1Y72Jilh3N0@cluster0.tgb50.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.connect_dev

# 문영안
@app.route('/')
def profile_main():
    return render_template('profile_main.html')

@app.route("/profile_main", methods=["GET"])
def profile_upload():
    profile = list(db.users.find({}, {'_id': False}))
    return jsonify({'profiling': profile})

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

@app.route('/profile_mk')
def profile_mk():
    return render_template('profile_mk.html')

@app.route('/profile_revise')
def profile_revise():
    return render_template('profile_revise.html')

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

@app.route('/profile_revise_delete', methods=["POST"])
def profile_delete():
    name_receive = request.form['name_give']
    db.users.delete_one({'name':name_receive})

    return jsonify({'msg':'저장완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)