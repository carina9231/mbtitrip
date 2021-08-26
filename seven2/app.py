from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.mbti



@app.route('/mbti')
def qna():
   return render_template('mbmb.html')



@app.route('/mbti/review', methods=['GET'])
def mb():
    rev = list(db.us.find({}, {'_id': False}))
    return jsonify({'aaa': rev})


@app.route('/mbti/res', methods=['POST'])
def res():
    titi= request.form['target'];

    return



@app.route('/mbti/result', methods=['POST'])
def hom():
    return render_template('index.html')

'''
@app.route('/mbti/list', methods=['GET'])
def mbti():

    mb = list(db.mt.find({},{'_id': False}))
    ct = list(db.ct.find({},{'_id': False}))
    li=  list(db.like.find({},{'_id': False}))
    return render_template('index.html')
'''



@app.route('/mbti/like', methods=['POST'])
def like_region():
    region_receive = request.form['region_give']

    target_like = db.mbti.find_one({'region': region_receive})
    current_like = target_like['like']

    new_like = current_like + 1

    db.mbti.update_one({'region': region_receive}, {'$set':{'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})


@app.route('/likedata', methods=['POST'])
def make_like():
    sample_data = request.form['sample_data']

    db.like.update_one({'name': sample_data}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 클릭완료'})


@app.route('/mbti/likedata', methods=['GET'])
def show_like():
    like_data = list(db.like.find({}, {'_id': False}).sort('like',-1))

    return jsonify({'like_datas': like_data})