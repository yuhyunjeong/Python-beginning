a=0
count=0
while a<=100:
    a+=1
    if a%2==0 and a%7!=0:
        count+=1
print("1부터 100까지의 수 중에서 짝수이면서 7의 배수가 아닌 수:",count,"개")

i=0
sum=0
while True:
    i=int(input("숫자를 입력하세요:"))
    if i==0:
        break
    else:
        sum+=i
print(sum)