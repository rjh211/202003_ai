"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """

string = input('주민등록번호를 입력하세요("-"  포함)')

splitstr = string.split('-')
sex = int(splitstr[1][0])
if (sex == 1 or sex == 3) and len(string) == 14:
    print('남자')
elif sex == 2 or sex == 4 and len(string) == 14:
    print('여자')
else:
    print('올바른 주민등록번호를 입력해주세요.')