

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
         # 거래 내역 추가 입력 받기
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            trans_type = input("Enter type (income/expense): ")
            amount = input("Enter amount: ")

            # 예외 처리를 통해 잘못된 입력 처리
            try:
                # 금액을 float으로 변환
                amount = float(amount)
                # 거래 유형이 유효한지 확인
                if trans_type not in ['income', 'expense']:
                    raise ValueError("Transaction type must be 'income' or 'expense'.")
                # 거래 내역 추가
                system.add_transaction(date, description, trans_type, amount)
            except ValueError as e:
                # 잘못된 입력이 있을 경우 에러 메시지 출력
                print(f"Invalid input: {e}")
        
    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

