""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""


a = input('첫 번째 숫자를 입력하세요: ')
oper = input ('연산기호를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')
a = int(a)
b = int(b)
    
if oper == '+':
    print(a+b)
elif  oper == '-':
    print(a-b)
elif oper == '*':
    print(a*b)
elif oper == '/':
    print(a/b)
else:
    print('사칙 연산외 기호는 지원하지 않습니다.')

