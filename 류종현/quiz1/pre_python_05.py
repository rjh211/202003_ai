"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
s = input('Please input S : ')
n = input('Please input N : ')

s = int(s)
n = int(n)

for i in range(1,s+1):
    for j in range(1,n+1):
        mulResult = i*j
        print('%i' % mulResult, end=" ")
    print("\n")