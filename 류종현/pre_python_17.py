"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""

for i in range(1988, 2061):
    if i % 4 == 2:
        print(i)
