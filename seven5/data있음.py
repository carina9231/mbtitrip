from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.mbti                           # 'bin'라는 이름의 db를 만듭니다.


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client.mbti

my_client = MongoClient("mongodb://localhost:27017/")


# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.

db.us.insert_one({'q':'1.특별한 약속이 없는 주말에 나는','a1':'단톡에 연락해서 친구들과 약속을 잡는다',
                  'a2':'침대랑 하루 종일 물아일체가 된다','r1':'e','r2':'i'})
db.us.insert_one({'q':'2.친구들과 놀 때 나는','a1':'왁자지껄한 신나는 분위기를 좋아한다',
                  'a2':'소수의 친구들과 소소하게 대화하는 것을 좋아한다','r1':'e','r2':'i'})
db.us.insert_one({'q':'3.숙소를 구할 때','a1':'저녁에 바비큐 파티를 여는 곳',
                  'a2':'조용하고 아늑한 곳','r1':'e','r2':'i'})

db.us.insert_one({'q':'4.연인에게 줄 선물을 고르게 된 나는','a1':'실용성은 없어도 예쁘고 기억에 남을 선물',
                  'a2':'연인에게 요즘 가장 필요할 것 같은 선물 ','r1':'n','r2':'s'})
db.us.insert_one({'q':'5.여행지에서 식사할 때','a1':'처음 본 순간 사랑에 빠진 길거리 가게',
                  'a2':'유~명한 맛집을 작정하고 노리는 헌터','r1':'n','r2':'s'})
db.us.insert_one({'q':'6.화려한 건축물을 보며 드는 생각은','a1':'"와 멋있다..." 감탄한다',
                  'a2':'"어떤 방법으로 지었을까?" 고민한다','r1':'n','r2':'s'})

db.us.insert_one({'q':'7.화났을 때 나는','a1':'할 말이 많지만 너무 분해서 눈물부터 난다',
                  'a2':'논리적으로 잘 말하면서 따진다 ','r1':'f','r2':'t'})
db.us.insert_one({'q':'8.고민을 얘기하는 친구, 듣다 보니 친구의 잘못인 것 같다. 그럴 때 나','a1':'직접적으로 말하면 친구가 싫어할까 봐 돌려 말한다',
                  'a2':'친구의 잘못된 점을 지적한다','r1':'f','r2':'t'})
db.us.insert_one({'q':'9.친구에게 차 사고가 났다고 전화 왔을 때 나의 대답은','a1':'"괜찮아? ㅠㅠ 다친 데는 없어?"',
                  'a2':'"보험 들었어?"','r1':'f','r2':'t'})

db.us.insert_one({'q':'10.해외여행 계획을 짜게 된 나는','a1':'할 거면 제대로! 일별로 세부 일정을 정리한다',
                  'a2':'비행기 표만 끊어 두고 계획의 80% 끝난다고 생각한다','r1':'j','r2':'p'})
db.us.insert_one({'q':'11.끝나고 집에 가서 공부하려 했는데 친구들이 놀자고 붙잡는다. 나는?','a1':'계획에 없던 일인데… 매우 당황스럽다',
                  'a2':'오케이!! 역시 계획대로 안 되는 것이 인생! 놀자!!!','r1':'j','r2':'p'})
db.us.insert_one({'q':'12.여행을 다녀온 후','a1':'캐리어를 열고 물건을 정리한다',
                  'a2':'홈스윗홈.. 침대로 점프!','r1':'j','r2':'p'})


db.mt.insert_one({"mbti":'ISTP','ar1':1,'ar2':2})
db.mt.insert_one({"mbti":'ISFP','ar1':3,'ar2':4},)
db.mt.insert_one({"mbti":'INFP','ar1':5,'ar2':2},)
db.mt.insert_one({"mbti":'INTP','ar1':5,'ar2':6},)
db.mt.insert_one({"mbti":'ISTJ','ar1':7,'ar2':8},)
db.mt.insert_one({"mbti":'ISFJ','ar1':7,'ar2':9},)
db.mt.insert_one({"mbti":'INFJ','ar1':10,'ar2':6},)
db.mt.insert_one({"mbti":'INTJ','ar1':7,'ar2':11},)
db.mt.insert_one({"mbti":'ESTJ','ar1':5,'ar2':12},)
db.mt.insert_one({"mbti":'ESFJ','ar1':13,'ar2':8},)
db.mt.insert_one({"mbti":'ENFJ','ar1':3,'ar2':8},)
db.mt.insert_one({"mbti":'ENTJ','ar1':5,'ar2':6},)
db.mt.insert_one({"mbti":'ESTP','ar1':3,'ar2':8},)
db.mt.insert_one({"mbti":'ESFP','ar1':10,'ar2':14},)
db.mt.insert_one({"mbti":'ENTP','ar1':4,'ar2':12},)
db.mt.insert_one({"mbti":'ENFP','ar1':13,'ar2':14},)

db.mt.insert_one({"_id":'mbti','1':'ISTP','2':'ISFP','3':'INFP','4':'INTP','5':'ISTJ','6':'ISFJ','7':'INFJ','8':'INTJ',
                '9':'ESTJ','10':'ESFJ','11':'ENFJ','12':'ENTJ','13':'ESTP','14':'ESFP','15':'ENTP','16':'ENFP'})




db.ct.insert_one({"ct":'단양','ca':'카페단(충북 단양군 단양읍 삼봉로 107-1)','tl':'고수동굴(충북 단양군 단양읍 고수동굴길 8','fd':'가연(충북 단양군 단양읍 삼봉로 87)'})
db.ct.insert_one({"ct":'파주','ca':'레드파이프(경기 파주시 지목록 17-7)','tl':'헤이리 예술마을(경기 파주시 탄현면 헤이리마을길 70-21)','fd':'오알비스트로(경기 파주시 소리천로 25 유은타워7가 308호)'},)
db.ct.insert_one({"ct":'속초','ca':'보사노바 커피로스터스(강원 속초시 해오름로 161)','tl':'속초중앙시장(강원도 속초시 중앙동 중앙로147번길 16), 영금정(강원 속초시 여금정로 43)','fd':'만석닭강정본점(강원 속초시 조양동 속초해수욕장)'},)
db.ct.insert_one({"ct":'전주','ca':'구프오프(전북 전주시 완산구 천경로 27-1)','tl':'전주동물원(전북 전주시 덕진구 소리로 68 전주동물원)','fd':'온단(전북 전주시 완산구 전주천동로 210 1층)'},)
db.ct.insert_one({"ct":'부산','ca':'모모스커피(부산 금정구 오시게로 18-1)','tl':'감천문화마을(부산 사하구 감내2로 203)','fd':'50년전통할매국밥(부산 동구 중앙대로533번길 4)'},)
db.ct.insert_one({"ct":'담양','ca':'감성공판장(전남 담양군 월산면 담장로 143)','tl':'메타세쿼이아 가로수길(전남 담양군 담양읍 메타세쿼이아로 12)','fd':'전통식당(전남 담양군 고서면 고읍현길 38-4)'},)
db.ct.insert_one({"ct":'경주','ca':'훌림목(경북 경주시 포석로 1061-9)','tl':'반월성(경상북도 경주시 인왕동 387-1)','fd':'도솔마을(경북 경주시 손효자길  8-13)'},)
db.ct.insert_one({"ct":'제주도','ca':'봄날카페(제주시 애월읍 애월리 2540번지)','tl':'카멜리아 힐(제주특별자치도 서귀포시 안덕면 병악로 166)','fd':'올래국수(제주 제주시 귀아랑길 24)'},)
db.ct.insert_one({"ct":'순천','ca':'브루웍스(전남 순천시 역전길 61)','tl':'낙안민속자연휴양림(전라남도 순천시 낙안면 민속마을길 1600)','fd':'대숲골농원(전남 순천시 학동길 36)'},)
db.ct.insert_one({"ct":'강릉','ca':'곳;(강릉시 사천면 사천진리 262-7)','tl':'정동진레일바이크(강원도 강릉시 강동면 정동역길 17)','fd':'강릉 불고기(강원도 강릉시 강동면 하시동리 718)'},)
db.ct.insert_one({"ct":'울릉도','ca':'카페 울라(경북 울릉군 북면 추산길 88-13)','tl':'대풍감 스카이워크(경상북도 울릉군 서면 태하리)','fd':'보배식당(경북 울릉군 울릉읍 도동2길 50-4)'},)
db.ct.insert_one({"ct":'통영','ca':'카페녘(경남 통영시 용남면 남해안대로 21 더벨르타워 카페녘)','tl':'동피랑 벽화마을(경남 통영시 동피랑1길 6-18)','fd':'동피랑쭈굴(경남 통영시 통영해안로 363-1)'},)
db.ct.insert_one({"ct":'여수','ca':'여수딸기모찌(전남 여수시 중앙로 70 여수딸기모찌)','tl':'오동도(전남 여수시 수정동 산1-11)','fd':'명동게장(전남 여수시 봉산남4길 23-26)'},)
db.ct.insert_one({"ct":'양양','ca':'서퍼스 파라다이스(강원도 양양군 현남면 인구길 60-7)','tl':'서피비치(강원도 양양군 현북면 하조대해안길 119 KR)','fd':'송이버섯마을(강원도 양양군 양양읍 월리 339)'},)


'''
db.like.insert_one({"ct":'단양','like':2});
db.like.insert_one({"ct":'파주','like':3});
db.like.insert_one({"ct":'속초','like':4});
db.like.insert_one({"ct":'전주','like':1});
db.like.insert_one({"ct":'부산','like':8});
db.like.insert_one({"ct":'담양','like':7});
db.like.insert_one({"ct":'경주','like':9});
db.like.insert_one({"ct":'제주도','like':3});
db.like.insert_one({"ct":'순천','like':6});
db.like.insert_one({"ct":'강릉','like':12});
db.like.insert_one({"ct":'울릉도','like':22});
db.like.insert_one({"ct":'통영','like':31});
db.like.insert_one({"ct":'여수','like':13});
db.like.insert_one({"ct":'양양','like':65});

'''

