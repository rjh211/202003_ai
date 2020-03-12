"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

first = input('첫 번째 사람 : enter key를 누르시오')
firstValue = random.randrange(1,7)

second = input('두 번째 사람 : enter key를 누르시오')
secondValue = random.randrange(1,7)

if firstValue > secondValue:
    print(firstValue, ':', secondValue, '첫 번째 사람 승리')
elif firstValue == secondValue:
    print(firstValue, ':', secondValue, '무승부')
else:
    print(firstValue, ':', secondValue, '두 번째 사람 승리')
