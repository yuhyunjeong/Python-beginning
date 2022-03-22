i=0
lst=[]
while i < 7:
    a = int(input("정수를 입력해주세요."))
    lst.append(a)
    i+=1
    
sum=0
for i in lst:
    sum += i

avg = sum/7
print("평균:",avg)