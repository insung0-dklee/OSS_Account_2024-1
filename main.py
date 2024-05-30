
b_is_exit = 0  

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")  # 사용자로부터 기능 입력 받음

    if func == "1":
        # '1'을 입력하면 식비 추가 기능 실행
        expense_type = '식비'
        amount = float(input(f"{expense_type} 금액 입력: "))  # 금액 입력 받음
        print(f"{expense_type}에 {amount}원이 추가되었습니다.")  # 결과 출력
        break

    elif func == "2":
        # '2'을 입력하면 교통비 추가 기능 실행
        expense_type = '교통비'
        amount = float(input(f"{expense_type} 금액 입력: "))  # 금액 입력 받음
        print(f"{expense_type}에 {amount}원이 추가되었습니다.")  # 결과 출력
        break

    elif func == "3":
        #  '3'을 입력하면 기타 지출 추가 기능 실행
        expense_type = '기타'
        amount = float(input(f"{expense_type} 금액 입력: "))  # 금액 입력 받음
        print(f"{expense_type}에 {amount}원이 추가되었습니다.")  # 결과 출력
        break

    elif func == "?":
        # '?'을 입력하면 도움말 출력
        print("도움말:\n1: 식비 추가\n2: 교통비 추가\n3: 기타 지출 추가\n종료하려면 'exit'를 입력하세요.")

    elif func.lower() == "exit":
        #  'exit'를 입력하면 프로그램 종료
        print("프로그램을 종료합니다.")
        b_is_exit = 1

    else:
        # 잘못된 입력이 있을 경우, 오류 메시지 출력
        print("잘못된 입력입니다. 다시 시도하세요.")