tu = ("Hello","This is Python","Bye")

dic = {}
for i in range(0,3):
    dic.update({tu[i]:len(tu[i])})

print(dic)


