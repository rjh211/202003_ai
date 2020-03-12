"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""

string = input('알파벳을 입력해주세요 : ')

if string.isalpha() and string.isupper():
    string = string.lower()
elif string.isalpha() and string.islower():
    string = string.upper()
else:
    string = '입력 형식이 잘못되었습니다.'
print(string)