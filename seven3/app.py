from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.mbti



@app.route('/mbti')
def mbti():
   return render_template('mbmb.html')






@app.route('/mbti/re', methods=['GET'])
def information():
    respons = list(db.us.find({}, {'_id': False}))
    mbti = list(db.mt.find({}, {'_id': False}))
    city = list(db.ct.find({}, {'_id': False}))

    return jsonify({'qna':respons,'mbti':mbti,'city':city})


@app.route('/mbti/result')
def result():
   return render_template('index.html')

