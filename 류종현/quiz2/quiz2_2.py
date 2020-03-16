'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.


테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))

<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.

'''

import datetime
year = int(input("연도를 입력하시오 : "))
month = int(input("월을 입력하시오 : "))
day = int(input("일을 입력하시오 : "))

def printDayOfTheWeek(year, month, day):
    date = ""
    numOfWeekday = datetime.date(year,month,day).weekday()
    if numOfWeekday == 0:
        date = "월요일"
    elif numOfWeekday == 1:
        date = "화요일"
    elif numOfWeekday == 2:
        date = "수요일"
    elif numOfWeekday == 3:
        date = "목요일"
    elif numOfWeekday == 4:
        date = "금요일"
    elif numOfWeekday == 5:
        date = "토요일"
    elif numOfWeekday == 6:
        date = "일요일"
        
    return date

print("%d년 %d월 %d일은 %s 입니다." % (year, month, day, printDayOfTheWeek(year,month,day)))