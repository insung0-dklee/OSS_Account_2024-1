b_is_exit = 0
balance = 0
transactions = []

def print_help():
    print("가계부 프로그램 도움말:")
    print("1: 수입 입력")
    print("2: 지출 입력")
    print("3: 잔액 확인")
    print("4: 거래 내역 확인")
    print("5: 종료")

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        amount = float(input("수입 금액을 입력하세요: "))
        description = input("수입 설명을 입력하세요: ")
        balance += amount
        transactions.append((amount, description, "수입"))
        print(f"현재 잔액: {balance} 원")

    elif func == "2":
        amount = float(input("지출 금액을 입력하세요: "))
        description = input("지출 설명을 입력하세요: ")
        balance -= amount
        transactions.append((-amount, description, "지출"))
        print(f"현재 잔액: {balance} 원")

    elif func == "3":
        print(f"현재 잔액: {balance} 원")

    elif func == "4":
        print("거래 내역:")
        for amount, description, type in transactions:
            print(f"{type}: {description} - {amount} 원")

    elif func == "?":
        print_help()

    elif func == "5":
        b_is_exit = 1
        print("프로그램을 종료합니다.")

    else:
        print("올바르지 않은 입력입니다. 다시 시도하세요.")
