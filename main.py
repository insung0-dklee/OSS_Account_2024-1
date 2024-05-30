b_is_exit = False

# 가계부 데이터를 저장할 리스트
transactions = []

# 지출 항목 추가 함수
def add_expense():
    date = input("날짜 (YYYY-MM-DD): ")  # 날짜 입력
    category = input("카테고리: ")       # 카테고리 입력
    amount = float(input("금액: "))      # 금액 입력
    # 거래 내역에 추가
    transactions.append({"type": "expense", "date": date, "category": category, "amount": amount})
    print("지출 항목이 추가되었습니다.")  # 추가 확인 메시지

# 수입 항목 추가 함수
def add_income():
    date = input("날짜 (YYYY-MM-DD): ")  # 날짜 입력
    category = input("카테고리: ")       # 카테고리 입력
    amount = float(input("금액: "))      # 금액 입력
    # 거래 내역에 추가
    transactions.append({"type": "income", "date": date, "category": category, "amount": amount})
    print("수입 항목이 추가되었습니다.")  # 추가 확인 메시지

# 거래 내역 보기 함수
def view_transactions():
    if not transactions:
        print("거래 내역이 없습니다.")  # 거래 내역이 없을 경우 메시지 출력
        return

    # 거래 내역 출력
    for t in transactions:
        t_type = "수입" if t["type"] == "income" else "지출"  # 거래 타입 설정
        print(f"{t['date']} - {t_type} - {t['category']} - {t['amount']}원")

# 총 수입과 지출 및 잔액 보기 함수
def view_summary():
    # 총 수입 계산
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    # 총 지출 계산
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    # 잔액 계산
    balance = total_income - total_expense
    # 결과 출력
    print(f"총 수입: {total_income}원")
    print(f"총 지출: {total_expense}원")
    print(f"잔액: {balance}원")

# 도움말 보기 함수
def show_help():
    print("1: 지출 항목 추가")
    print("2: 수입 항목 추가")
    print("3: 지출 및 수입 내역 보기")
    print("4: 총 수입과 지출 및 잔액 보기")
    print("?: 도움말 보기")
    print("exit: 프로그램 종료")

# 메인 루프
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")  # 사용자로부터 기능 입력받기

    # 각 기능에 따라 함수 호출
    if func == "1":
        add_expense()
    elif func == "2":
        add_income()
    elif func == "3":
        view_transactions()
    elif func == "4":
        view_summary()
    elif func == "?":
        show_help()
    elif func.lower() == "exit":  # 'exit' 입력 시 프로그램 종료
        b_is_exit = True
    else:
        print("알 수 없는 명령입니다. 도움말을 보려면 ? 를 입력하세요.")  # 잘못된 입력 시 메시지 출력

print("프로그램을 종료합니다.")  # 프로그램 종료 메시지
