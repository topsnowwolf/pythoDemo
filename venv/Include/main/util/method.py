user1 ={'name':'wolf','age':24,'sex':1}
user2={'name':'snowwolf','age':25,'sex':1}
user3={'name':'topswowwolf','age':26,'sex':1,'hobby':['看书','钓鱼','练字','下棋']}
users =[user1,user2,user3]

def getUserInfo(userName):
    for user in users:
        if user['name'] == userName:
            return user

u = getUserInfo(userName='snowwolf')
print(u)


def makePazzi(*toppings):
    print(toppings)

makePazzi("test")
makePazzi("test1","test2",2)