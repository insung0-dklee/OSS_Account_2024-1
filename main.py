b_is_exit = False
expenditures = []  # 지출 내역 저장
incomes = []       # 수입 내역 저장
balance = 0        # 잔액

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        # 지출 입력
        amount = float(input("지출 금액을 입력하세요: "))
        if amount > balance:
            print("잔액이 부족하여 지출을 할 수 없습니다.\n")
        else:
            reason = input("지출 사유를 입력하세요: ")
            date = input("지출 날짜를 입력하세요 (YYYY-MM-DD): ")
            expenditures.append((amount, reason, date))
            balance -= amount
            print("지출 내역이 저장되었습니다.\n")

    elif func == "2":
        # 수입 입력
        amount = float(input("수입 금액을 입력하세요: "))
        reason = input("수입 사유를 입력하세요: ")
        date = input("수입 날짜를 입력하세요 (YYYY-MM-DD): ")
        incomes.append((amount, reason, date))
        balance += amount
        print("수입 내역이 저장되었습니다.\n")

    elif func == "3":
        # 잔액 확인
        print(f"현재 잔액: {balance} 원\n")

    elif func == "4":
        # 총 지출 및 수입 내역 출력
        print("총 지출 내역:")
        for amount, reason, date in expenditures:
            print(f"날짜: {date}, 금액: {amount} 원, 사유: {reason}")

        print("\n총 수입 내역:")
        for amount, reason, date in incomes:
            print(f"날짜: {date}, 금액: {amount} 원, 사유: {reason}")

        print(f"\n현재 잔액: {balance} 원\n")

    elif func == "?":
        # 도움말 출력
        print("도움말:")
        print("1: 지출 내역 입력")
        print("2: 수입 내역 입력")
        print("3: 잔액 확인")
        print("4: 총 지출 및 수입 내역 출력")
        print("exit: 프로그램 종료\n")

    elif func.lower() == "exit":
        # 프로그램 종료
        b_is_exit = True
        print("프로그램을 종료합니다.\n")

    else:
        print("알 수 없는 명령어입니다. 도움말을 보려면 ? 를 입력하세요.\n")