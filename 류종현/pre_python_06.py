"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""

a = input('숫자를 입력하세요 : ')
a = int(a)
doubleA = a*2
for i in range(1,doubleA):
    if i <= 5:
        for j in range(1,1+a-i):
            print(" ",end="")
        for k in range(1,i+1):
            print("★",end="")
    else:
        for l in range(1,1+a-(doubleA - i)):
            print(" ",end="")
        for m in range(1,doubleA - (i-1)):
            print("★",end="") 
    print("\n")
