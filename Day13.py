class Calculator:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

while True:
    a = float(input("첫번째 숫자를 입력하세요.:"))
    b = float(input("두번째 숫자를 입력하세요.:"))
    cal = Calculator(a,b)

    c = input("연산자를 입력하세요.(+ , - , * , /):")

    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)