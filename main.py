

b_is_exit = 0
"""
Class : Account

변수 : money, detail;
함수
__init__
    @params : money
    입금,출금 장부를 초기화하고 초기 자금을 정해준다.
deposit
    @params : day,money,detail
    해당 날짜의 입금 장부에 금액, 내역을 넣어주고 잔액을 증가시킨다.
withdraw
    @params : day,money,detail
    해당 날짜의 출금 장부에 금액, 내역을 넣어주고 잔액을 감소시킨다.
get_balance
    @params : None
    @return : int
    현재 잔액을 반환해준다.
get_detail
    @params : day
    해당 날짜의 입금, 출금 내역을 출력한다.
"""
class AccountData:
    def __init__(self, money, detail):
        self.money = money
        self.detail = detail

class Account:
    def __init__(self, money):
        self.Deposit = {i: [] for i in range(1, 32)}
        self.WithDraw = {i: [] for i in range(1, 32)}
        self.money = money

    def deposit(self, day, money, detail):
        if day not in self.Deposit:
            self.Deposit[day] = []
        self.Deposit[day].append(AccountData(money, detail))
        self.money += money
        print(f"입금 완료\n{day}일 : {money}원({detail})")

    def withdraw(self, day, money, detail):
        if day not in self.WithDraw:
            self.WithDraw[day] = []
        self.WithDraw[day].append(AccountData(money, detail))
        self.money -= money
        print(f"출금 완료\n{day}일 : {money}원({detail})")
    def get_detail(self,day):
        print(day,"일")
        print("============================================================")
        print("입금 내역 : ")
        for data in self.Deposit[day]:
            print(data.detail,data.money)
        print("출금 내역 : ")
        for data in self.WithDraw[day]:
            print(data.detail,data.money)
        print("============================================================")

    def get_balance(self):
        return self.money
    
def print_helpMessage():
    print("============================================================")
    print("1. 입력(수입)")
    print("날짜, 금액, 수입내역을 입력하면 내 가계부의 수입에 반영됩니다.")
    print("2. 입력(지출)")
    print("날짜, 금액, 지출내역을 입력하면 내 가계부의 지출에 반영됩니다.")
    print("3. 조회(수입/지출 내역)")
    print("날짜를 입력하면 해당 날짜의 수입/지출 내역을 출력합니다.")
    print("4. 조회(잔액)")
    print("잔액을 반환합니다.")
    print("============================================================")
while not b_is_exit:
    myAccount = Account(0)
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        day,money,detail = input("날짜, 금액, 내역 입력 : ").split()
        day = int(day)
        money = int(money)
        myAccount.deposit(day,money,detail)

    elif func == "2":
        day,money,detail = input("날짜, 금액, 내역 입력 : ").split()
        day = int(day)
        money = int(money)
        myAccount.withdraw(day,money,detail)
    elif func == "3":
        day = int(input("날짜 입력 : "))
        myAccount.get_detail(day)
    elif func == "4":
        print(f"현재 잔액은 {myAccount.get_balance()}")
    elif func == "?":
        print_helpMessage()
    else:
        b_is_exit = not b_is_exit

