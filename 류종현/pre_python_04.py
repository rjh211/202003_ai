"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""

a = input('가로를 입력하세요: ')
b = input('세로를 입력하세요: ')

a = int(a)
b = int(b)

def area(width , height):
    return (width * height)/2

print(area(a,b))