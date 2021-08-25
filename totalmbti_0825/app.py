from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbmbtitrip

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/likedata', methods=['POST'])
def make_like():
    sample_data = request.form['sample_data']

    db.users.update_one({'name': sample_data}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 클릭완료'})


@app.route('/likedata', methods=['GET'])
def show_like():
    like_data = list(db.users.find({}, {'_id': False}))

    return jsonify({'like_datas': like_data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)