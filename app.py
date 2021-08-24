from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mbti


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def show_mbti():
    mbti_name = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'mbti_names': mbti_name})


@app.route('/api/list', methods=['GET'])
def show_region():
    region_name = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'region_names': region_name})

@app.route('/api/list', methods=['GET'])
def show_cafe():
    cafe_name = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'cafe_names': cafe_name})

@app.route('/api/list', methods=['GET'])
def show_site():
    site_name = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'site_names': site_name})

@app.route('/api/list', methods=['GET'])
def show_restaurant():
    restaurant_name = list(db.mbti.find({}, {'_id': False}))
    return jsonify({'restaurant_names': restaurant_name})

@app.route('/api/like', methods=['POST'])
def like_region():
    region_receive = request.form['region_give']

    target_like = db.mbti.find_one({'region': region_receive})
    current_like = target_like['like']

    new_like = current_like + 1

    db.mbti.update_one({'region': region_receive}, {'$set':{'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)