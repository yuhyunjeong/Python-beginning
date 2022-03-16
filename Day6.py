a=input("첫 번째 과목의 점수를 입력하세요.:")
b=input("두 번째 과목의 점수를 입력하세요.:")
c=input("세 번째 과목의 점수를 입력하세요.:")

avg= (int(a)+int(b)+int(c))/3

if avg>=50:
    print("평균 점수는 ",avg,"점으로 합격입니다.")
else:
    print("평균 점수는 ",avg,"으로 불합격입니다.")

a=input("단어를 입력해주세요.:")
b=input("문장을 입력해주세요.:")

if a in b:
    print("단어가 있습니다.")
else:
    print("단어가 없습니다.")