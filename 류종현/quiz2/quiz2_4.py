'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''
class Movie_card:
    def __init__(self):
        pass
    def consume_Theater(self, price):
        return price * 0.8
        
class Mart_card:
    def __init__(self):
        pass
    def consume_Mart(self, price):
        return price * 0.9
class Traffic_card:
    def __init__(self):
        pass
    def consume_Traffic(self, price):
        return price * 0.9

class Multi_card(Movie_card, Mart_card, Traffic_card):
    won = 0
    def __init__(self):
        self.won = 0

    def Charge(self, charge):
        self.won = self.won + charge
        print("%d이 충전되었습니다." % charge)

    def Consume(self, price, place):
        discounted = price
        if self.won >= discounted:
            if place == '마트':
                discounted = self.consume_Mart(price)
            elif place == '영화관':
                discounted = self.consume_Theater(price)
            elif place == '교통':
                discounted = self.consume_Traffic(price)

            self.won = self.won - discounted

            print("%s에서 %d원을 사용했습니다." %(place, discounted))
        else:
            print("잔액이 부족합니다.")

    def print(self):
        print("잔액이 %d입니다." % self.won)


multi_card=Multi_card()
multi_card.Charge(20000)
multi_card.Consume(5000,'마트')
multi_card.Consume(10000,'영화관')
multi_card.Consume(2000,'교통')
multi_card.print()