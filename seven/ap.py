from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.bin



@app.route('/mbti')
def qna():
   return render_template('mbmb.html')


@app.route('/mbti/result')
def re():
   return render_template('mbtiend.html')


@app.route('/mbti/review', methods=['GET'])
def mb():
    rev = list(db.us.find({}, {'_id': False}))
    return jsonify({'aaa': rev})


@app.route('/mbti/res', methods=['POST'])
def res():
    titi= request.form['target'];
    doc = {'mbti': titi}
    return jsonify({'alr': doc})