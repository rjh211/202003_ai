"""1. 아래와 같이 숫자를 두번 물어보게 하고 ★을 출력해서 사각형을 만드시오
가로의 숫자를 입력하시오 : 
세로의 숫자를 입력하시오 : """

a = input('첫 번째 숫자를 입력하세요: ')
b = input('두 번째 숫자를 입력하세요: ')

a = int(a)
b = int(b)

for i in range(1,a+1):        # ①번 for문
    for j in range(1, b+1):   # ②번 for문
        print("★", end = " ") 
    print('') 