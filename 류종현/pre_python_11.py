"""11. 최대공약수를 구하는 함수를 구현하시오"""
import math

num1 = input('첫 번째 숫자를 입력하세요.')
num2 = input('두 번째 숫자를 입력하세요.')

num1 = int(num1)
num2 = int(num2)

def gcdMethod(num1, num2):
    return math.gcd(num1,num2)

print(gcdMethod(num1,num2))