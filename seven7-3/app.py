from flask import Flask, render_template, jsonify, request
#client = MongoClient('mongodb://moud:0519@localhost', 27017)
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.mbti



@app.route('/mbti')
def main():

       return render_template('mbmb.html')



@app.route('/mbti/result/<mbti>/<int:order>')
def result(mbti,order):




    mbtis = list(db.mbti.find({}, {'_id': False}))
    city = list(db.city.find({}, {'_id': False}))
    img = list(db.img.find({}, {'_id': False}))

    area1 = mbtis[order]['area1']
    area2 = mbtis[order]['area2']

    city1 = city[area1]['city']
    city2 = city[area2]['city']

    tour1 = city[area1]['tour']
    tour2 = city[area2]['tour']

    restaurant1 = city[area1]['food']
    restaurant2 = city[area2]['food']

    cafe1 = city[area1]['cafe']
    cafe2 = city[area2]['cafe']

    like1 = city[area1]['like']
    like2 = city[area2]['like']

    img1= img[area1]['img']
    img2= img[area2]['img']
    return render_template('index.html',mbti=mbti,cafe1=cafe1,cafe2=cafe2,city1=city1,city2=city2,tour1=tour1,tour2=tour2,restaurant1=restaurant1,restaurant2=restaurant2,like1=like1,like2=like2,area1=area1,area2=area2,img1=img1,img2=img2)


@app.route('/mbti/like', methods=['POST'])
def like():
    receive = int(request.form['response'])
    like = list(db.city.find({}, {'_id': False}))
    citys = like[receive]['city']
    target = like[receive]['like']
    n_like = target + 1

    db.city.update_one({'city': citys}, {'$set': {'like': n_like}})

    return jsonify({'msg':'좋아요 완료!'})



@app.route('/mbti/all/mbti')
def mbti():
    return render_template('inin.html')


@app.route('/mbti/all/area')
def area():

   return render_template('like_local.html')


@app.route('/mbti/re', methods=['GET'])
def information():
    qna = list(db.qna.find({}, {'_id': False}))
    img = list(db.img.find({}, {'_id': False}))
    city = list(db.city.find({}, {'_id': False}))
    mbti = list(db.mbti.find({}, {'_id': False}))

    return jsonify({'qna':qna,'city':city,'mbti':mbti,'img':img})