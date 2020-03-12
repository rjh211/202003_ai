"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""
a = input('점수를 입력하세요 : ')
a = int(a)

if 80 < a <=100:
    print('A')
elif 60 < a <=80:
    print('B')
elif 40 < a <=60:
    print('C')
elif 20 < a <=40:
    print('D')
else:
    print('F')