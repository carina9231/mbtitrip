from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.bin



@app.route('/')
def home():
   return render_template('main.html')


@app.route('/work')
def work():
   return render_template('photo.html')


@app.route('/work/street')
def street():
   return render_template('as.html')


@app.route('/work/flower')
def flower():
   return render_template('as.html')


@app.route('/work/moon')
def moon():
   return render_template('as.html')


@app.route('/work/ch')
def ch():
   return render_template('as.html')


@app.route('/work/beauty')
def beauty():
   return render_template('as.html')


@app.route('/work/castle')
def castle():
   return render_template('as.html')



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





#연습용 창고


## HTML을 주는 부분
@app.route('/book')
def book():
    return render_template('mongo.html')

## API 역할을 하는 부분
@app.route('/book/review', methods=['POST'])
def write_review():
    title_receive = request.form['tg']
    author_receive = request.form['ag']
    review_receive = request.form['rg']
    doc = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    db.bookreview.insert_one(doc)
    return jsonify({'msg': '저장!'})


@app.route('/book/review', methods=['GET'])
def read_reviews():
    rev = list(db.bookreview.find({}, {'_id': False}))
    return jsonify({'alr': rev})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)











