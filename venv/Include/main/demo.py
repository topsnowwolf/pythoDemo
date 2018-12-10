users = ['admin','test','rose']
#del users[3]
print(users)
users = ['admin','test','jock','rose']
user = users.pop();#栈未
user = users.pop(1);#顺算第二位
print(users)
user = users.pop(0);#栈顶
print(users)
users = ['admin','test','jock','rose','admin']
print(users)
users.remove("admin");
print(users)
users = ['admin','test','jock','rose','admin']
users.reverse()
print(users)
for user in users:
    print(user)