#아래 3줄만 있으면 DB 연결 문제 없음
from pymongo import MongoClient
client = MongoClient('mongodb+srv://wonboklee:cpftl415!!@cluster0.pktujdj.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

#
# doc = {
#     'name' : 'bob',
#     'age' : 29
# }
#------------------------------------------------------------------------------------
# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# all_users = list(db.users.find({},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})
#------------------------------------------------------------------------------------
# all_users = list(db.users.find({},{'_id':False}))
# 모든 유저 찾기
# for user in all_users:
#     print(user)


# user = db.users.find_one({'name':'bok'})
# 복 한명만 찾기
# print(user)

#db 업데이트
# db.users.update_one({'name':'bob'},{'$set':{'age':19}})

#db 삭제
# db.users.delete_one({'name':'bob'})



