
# 지출 기록, 잔액 확인 기능
def minus_money(origin, money):
    return origin - money

def expense_record(balance):
    try:
        expense = int(input("지출할 금액을 입력하세요: "))
        if expense > balance:
            print("잔액이 부족합니다!")
        else:
            balance = minus_money(balance, expense)
            print(f"지출 완료! 잔고: {balance}원")
    except ValueError:
        print("유효한 금액을 입력하세요.")
    return balance

balance = 1000  # 초기 잔액

while True:
    func = input("기능 입력 (1: 지출 기록, q: 종료): ")

    if func == "1":
        balance = expense_record(balance)
    
    elif func.lower() == "q":
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("알 수 없는 기능입니다. 다시 시도하세요.")
