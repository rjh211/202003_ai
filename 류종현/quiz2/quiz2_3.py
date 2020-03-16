'''
3.
Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
-영화관에서 카드를 사용하면 20% 할인율 적용
print 기능(print) # 잔액이 ( ) 원 입니다.
테스트코드
<입력>
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()
<출력>
잔액이 20000원 입니다.
마트에서 3000원 사용했습니다.
영화관에서 8000원 사용했습니다.
잔액이 부족합니다
잔액이 9000원 입니다.
'''

class Card:
    won = 0
    def __init__(self):
        self.won = 0

    def Charge(self, price):
        self.won = self.won + price
        print("잔액이 %d원 입니다." % int(self.won))

    def Consume(self, price, place):
        discountPrice = int(self.ApplySale(price,place))
        if self.won >= price - discountPrice:
            self.won = self.won - (price - discountPrice)
            print("%s에서 %d원 사용했습니다." %(place, price - discountPrice))
        else:
            print("잔액이 부족합니다.")


    def ApplySale(self, price, place):
        if place == '영화관':
            return price * 0.2
        else:
            return 0
    
    def Print(self):
        print("잔액이 %d원 입니다." % self.won)


card = Card()
card.Charge(20000)
card.Consume(3000,'마트')
card.Consume(10000,'영화관')
card.Consume(13000,'마트')
card.Print()