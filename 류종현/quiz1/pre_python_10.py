"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

a = input('숫자를 입력하세요 : ')
a = int(a)

def factorial(value):
  result = 1
  for i in range(1,value+1):
    result *= i
  return result
  

print(factorial(a))