from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.mbti

mbti_result=''

@app.route('/mbti')
def main():
       intp='intp'
       return render_template('mbmb.html',res=intp)



@app.route('/mbti/result/<mbti>/<int:order>')
def result(mbti,order):

    mbtis = mbti
    orders = order

    mbti = list(db.mt.find({}, {'_id': False}))
    like = list(db.like.find({}, {'_id': False}))

    city1 = mbti[order]['city1']
    city2 = mbti[order]['city2']
    tour1 = mbti[order]['tour1']
    tour2 = mbti[order]['tour2']
    restaurant1 = mbti[order]['food1']
    restaurant2 = mbti[order]['food2']
    cafe1 = mbti[order]['cafe1']
    cafe2 = mbti[order]['cafe2']

    return render_template('index.html',mbti=mbtis,cafe1=cafe1,cafe2=cafe2,city1=city1,city2=city2,tour1=tour1,tour2=tour2,restaurant1=restaurant1,restaurant2=restaurant2)






@app.route('/mbti/all/mbti')
def mbti():
   return render_template('inin.html')


@app.route('/mbti/all/area')
def area():

   return render_template('like_local.html')


@app.route('/mbti/re', methods=['GET'])
def information():
    respons = list(db.us.find({}, {'_id': False}))


    return jsonify({'qna':respons})





