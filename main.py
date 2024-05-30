income = []
expense = []

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (1: 수입 입력, 2: 지출 입력, ?: 도움말, exit: 종료) : ")

    if func == "1":
        amount = float(input("수입 금액 입력: "))
        income.append(amount)
        print(f"수입 {amount}원 추가 완료")

    elif func == "2":
        amount = float(input("지출 금액 입력: "))
        expense.append(amount)
        print(f"지출 {amount}원 추가 완료")

    elif func == "?":
        print("도움말:")
        print("1: 수입 입력")
        print("2: 지출 입력")
        
    else:
        b_is_exit = not b_is_exit
