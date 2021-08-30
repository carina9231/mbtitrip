from pymongo import MongoClient
#client = MongoClient('mongodb://moud:0519@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.mbti




db.qna.insert_one({'q':'1.특별한 약속이 없는 주말에 나는?','a1':'단톡에 연락해서 친구들과 약속을 잡는다.',
                  'a2':'침대랑 하루 종일 물아일체가 된다.'})
db.qna.insert_one({'q':'2.친구들과 놀 때 나는?','a1':'왁자지껄한 신나는 분위기를 좋아한다.',
                  'a2':'소수의 친구들과 소소하게 대화하는 것을 좋아한다.'})
db.qna.insert_one({'q':'3.숙소를 구할 때?','a1':'저녁에 바비큐 파티를 여는 곳',
                  'a2':'조용하고 아늑한 곳'})
db.qna.insert_one({'q':'4.연인에게 줄 선물을 고르게 된 나는?','a1':'실용성은 없어도 예쁘고 기억에 남을 선물',
                  'a2':'연인에게 요즘 가장 필요할 것 같은 선물 '})
db.qna.insert_one({'q':'5.여행지에서 식사할 때 나는?','a1':'처음 본 순간 사랑에 빠진 길거리 가게',
                  'a2':'유~명한 맛집을 작정하고 노리는 헌터'})
db.qna.insert_one({'q':'6.화려한 건축물을 보며 드는 생각은?','a1':'"와 멋있다..." 감탄한다.',
                  'a2':'"어떤 방법으로 지었을까?" 고민한다.',})
db.qna.insert_one({'q':'7.화났을 때 나는?','a1':'할 말이 많지만 너무 분해서 눈물부터 난다.',
                  'a2':'논리적으로 잘 말하면서 따진다.'})
db.qna.insert_one({'q':'8.고민을 얘기하는 친구, 듣다 보니 친구의 잘못인 것 같다. 그럴 때 나는?','a1':'직접적으로 말하면 친구가 싫어할까 봐 돌려 말한다.',
                  'a2':'친구의 잘못된 점을 지적한다.'})
db.qna.insert_one({'q':'9.친구에게 차 사고가 났다고 전화 왔을 때 나의 대답은?','a1':'"괜찮아? ㅠㅠ 다친 데는 없어?"',
                  'a2':'"보험 들었어?"'})
db.qna.insert_one({'q':'10.해외여행 계획을 짜게 된 나는?','a1':'할 거면 제대로! 일별로 세부 일정을 정리한다.',
                  'a2':'비행기 표만 끊어 두고 계획의 80% 끝난다고 생각한다.'})
db.qna.insert_one({'q':'11.끝나고 집에 가서 공부하려 했는데 친구들이 놀자고 붙잡는다. 나는?','a1':'계획에 없던 일인데… 매우 당황스럽다.',
                  'a2':'오케이!! 역시 계획대로 안 되는 것이 인생! 놀자!!!'})
db.qna.insert_one({'q':'12.여행을 다녀온 후 나는?','a1':'캐리어를 열고 물건을 정리한다.',
                  'a2':'홈스윗홈.. 침대로 점프!'})


db.mbti.insert_one({'area1':0,'area2':1,'mbti':'ISTP','order':'0'})
db.mbti.insert_one({'area1':2,'area2':3,'mbti':'ISFP','order':'1'})
db.mbti.insert_one({'area1':4,'area2':1,'mbti':'INFP','order':'2'})
db.mbti.insert_one({'area1':4,'area2':5,'mbti':'INTP','order':'3'})
db.mbti.insert_one({'area1':6,'area2':7,'mbti':'ISTJ','order':'4'})
db.mbti.insert_one({'area1':6,'area2':8,'mbti':'ISFJ','order':'5'})
db.mbti.insert_one({'area1':9,'area2':5,'mbti':'INFJ','order':'6'})
db.mbti.insert_one({'area1':6,'area2':10,'mbti':'INTJ','order':'7'})
db.mbti.insert_one({'area1':4,'area2':11,'mbti':'ESTJ','order':'8'})
db.mbti.insert_one({'area1':12,'area2':7,'mbti':'ESFJ','order':'9'})
db.mbti.insert_one({'area1':2,'area2':7,'mbti':'ENFJ','order':'10'})
db.mbti.insert_one({'area1':4,'area2':5,'mbti':'ENTJ','order':'11'})
db.mbti.insert_one({'area1':2,'area2':7,'mbti':'ESTP','order':'12'})
db.mbti.insert_one({'area1':9,'area2':13,'mbti':'ESFP','order':'13'})
db.mbti.insert_one({'area1':3,'area2':11,'mbti':'ENTP','order':'14'})
db.mbti.insert_one({'area1':13,'area2':13,'mbti':'ENFP','order':'15'})


db.city.insert_one({"city":'단양','like':1,'img':"/static/image/Danyang.jpg",'cafe':'카페단(충북 단양군 단양읍 삼봉로 107-1)','tour':'고수동굴(충북 단양군 단양읍 고수동굴길 8','food':'가연(충북 단양군 단양읍 삼봉로 87)'})
db.city.insert_one({"city":'파주','like':2,'img':"/static/image/Paju.jpg",'cafe':'레드파이프(경기 파주시 지목록 17-7)','tour':'헤이리 예술마을(경기 파주시 탄현면 헤이리마을길 70-21)','food':'오알비스트로(경기 파주시 소리천로 25 유은타워7가 308호)'},)
db.city.insert_one({"city":'속초','like':3,'img':"/static/image/Sokcho.jpg",'cafe':'보사노바 커피로스터스(강원 속초시 해오름로 161)','tour':'속초중앙시장(강원도 속초시 중앙동 중앙로147번길 16), 영금정(강원 속초시 여금정로 43)','food':'만석닭강정본점(강원 속초시 조양동 속초해수욕장)'},)
db.city.insert_one({"city":'전주','like':4,'img':"/static/image/Jeonju.jpg",'cafe':'구프오프(전북 전주시 완산구 천경로 27-1)','tour':'전주동물원(전북 전주시 덕진구 소리로 68 전주동물원)','food':'온단(전북 전주시 완산구 전주천동로 210 1층)'},)
db.city.insert_one({"city":'부산','like':5,'img':"/static/image/Busan.jpg",'cafe':'모모스커피(부산 금정구 오시게로 18-1)','tour':'감천문화마을(부산 사하구 감내2로 203)','food':'50년전통할매국밥(부산 동구 중앙대로533번길 4)'},)
db.city.insert_one({"city":'담양','like':6,'img':"/static/image/Damyang.jpg",'cafe':'감성공판장(전남 담양군 월산면 담장로 143)','tour':'메타세쿼이아 가로수길(전남 담양군 담양읍 메타세쿼이아로 12)','food':'전통식당(전남 담양군 고서면 고읍현길 38-4)'},)
db.city.insert_one({"city":'경주','like':7,'img':"/static/image/Gyeongju.jpg",'cafe':'훌림목(경북 경주시 포석로 1061-9)','tour':'반월성(경상북도 경주시 인왕동 387-1)','food':'도솔마을(경북 경주시 손효자길  8-13)'},)
db.city.insert_one({"city":'제주도','like':8,'img':"/static/image/JejuIsland.jpg",'cafe':'봄날카페(제주시 애월읍 애월리 2540번지)','tour':'카멜리아 힐(제주특별자치도 서귀포시 안덕면 병악로 166)','food':'올래국수(제주 제주시 귀아랑길 24)'},)
db.city.insert_one({"city":'순천','like':9,'img':"/static/image/Suncheon.jpg",'cafe':'브루웍스(전남 순천시 역전길 61)','tour':'낙안민속자연휴양림(전라남도 순천시 낙안면 민속마을길 1600)','food':'대숲골농원(전남 순천시 학동길 36)'},)
db.city.insert_one({"city":'강릉','like':10,'img':"/static/image/Gangneung.jpg",'cafe':'곳;(강릉시 사천면 사천진리 262-7)','tour':'정동진레일바이크(강원도 강릉시 강동면 정동역길 17)','food':'강릉 불고기(강원도 강릉시 강동면 하시동리 718)'},)
db.city.insert_one({"city":'울릉도','like':11,'img':"/static/image/Ulleungdo.jpg",'cafe':'카페 울라(경북 울릉군 북면 추산길 88-13)','tour':'대풍감 스카이워크(경상북도 울릉군 서면 태하리)','food':'보배식당(경북 울릉군 울릉읍 도동2길 50-4)'},)
db.city.insert_one({"city":'통영','like':12,'img':"/static/image/Tongyeong.jpg",'cafe':'카페녘(경남 통영시 용남면 남해안대로 21 더벨르타워 카페녘)','tour':'동피랑 벽화마을(경남 통영시 동피랑1길 6-18)','food':'동피랑쭈굴(경남 통영시 통영해안로 363-1)'},)
db.city.insert_one({"city":'여수','like':13,'img':"/static/image/Yeosu.jpg",'cafe':'여수딸기모찌(전남 여수시 중앙로 70 여수딸기모찌)','tour':'오동도(전남 여수시 수정동 산1-11)','food':'명동게장(전남 여수시 봉산남4길 23-26)'},)
db.city.insert_one({"city":'양양','like':14,'img':"/static/image/Yangyang.jpg",'cafe':'서퍼스 파라다이스(강원도 양양군 현남면 인구길 60-7)','tour':'서피비치(강원도 양양군 현북면 하조대해안길 119 KR)','food':'송이버섯마을(강원도 양양군 양양읍 월리 339)'},)


