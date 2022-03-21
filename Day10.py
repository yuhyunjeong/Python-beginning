a = int(input("정수를 입력하세요.:"))

def getSum(num):
    result=0
    for i in range(1, num+1):
        result += i       
    return result

print(getSum(a))