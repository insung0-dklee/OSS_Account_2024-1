'''
 이 클래스는 가계부를 나타냅니다
 이 클래스에 대한 객체 생성시에 가계부의 이름을 넣어주어야 합니다.
 수입, 지출, 잔고확인의 기능을 가지고 있습니다.
'''


class account_book:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def income(self):
        print("수입을 입력하세요:", end = " ")
        money = int(input())
        self.balance += money
        
    def expendse(self):
        print("지출을 입력하세요:", end = " ")
        money = int(input())
        self.balance -= money
        
    def show_balance(self):
        print(self.name, "의 현재 잔고: ", self.balance)
    