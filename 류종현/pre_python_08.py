"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오"""
a = input('정수를 입력하세요 : ')
a = int(a)
result = a%2
if result == 0:
    print('짝수')
else:
    print('홀수')
