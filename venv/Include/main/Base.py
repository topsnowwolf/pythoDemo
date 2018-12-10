# car = 'bm'
# print(car == 'bm')
# user1 = {'name':'wolf','age':23}
# name = user1['name']
# #user1['name']='topsnowwolf'
# print(user1)
# user1 = {'name':'wolf'}
# print(user1)
# print(name)
# user = {}
# user['name']='wolf'
# user['age']=23
# user['name']='snowwol'
# print(user)
# del user['name']
# print(user)
#items对key和value的遍历
user ={'name':'wolf','age':23,'sex':1}
for key,value in user.items():
    print(key+":"+str(value))
#keys对key遍历
user ={'name':'wolf','age':23,'sex':1}
for key in user.keys():
    print(key)

user ={'name':'wolf','age':23,'sex':1}
for value in user.values():
    print(value)
#嵌套到列表
user1 ={'name':'wolf','age':24,'sex':1}
user2={'name':'snowwolf','age':25,'sex':1}
user3={'name':'topswowwolf','age':26,'sex':1,'hobby':['看书','钓鱼','练字','下棋']}
users =[user1,user2,user3]
for u in users:
    print(u)
for user in users[:5]:
    print(user)

for hobby in user3['hobby']:
    print(hobby)