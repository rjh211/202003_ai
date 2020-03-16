'''
1.
문자열의 역순이 문자열과 동일하면 팰린드롬이라고 한다.
예를 들어, "토마토"는 팰린드롬이지만, "radio"는 팰린드롬이 아니다.
문자열이 주어지면 python 함수를 작성하여 팰린드롬인지 여부를 확인하시오.

테스트코드
<입력>
print(is_palindrome("radio"))
print(is_palindrome("토마토"))

<출력>
False
True
'''
import math
print('다음과 같은 형식으로 문자를 입력하시오. ex: print(is_palindrome("radio"))')
a = input('입력 : ')
isPalindrome = 0

word = a.split('"')[1]

for i in range(0, math.ceil(len(word)/2)):
    if word[i] == word[len(word)-1-i]:
        isPalindrome = isPalindrome + 1

if isPalindrome == math.ceil(len(word)/2):
    print('True')
else:
    print('False')