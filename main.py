userdata = {}  #아이디, 비밀번호 저장해둘 딕셔너리
account_book = {}  # 수입과 지출을 날짜별로 저장할 딕셔너리

def add_entry():
    date = input("날짜 입력 (YYYY-MM-DD): ")  # 수입/지출 기록 날짜 입력
    entry_type = input("수입/지출 입력: ")  # 기록 유형 입력 (수입 또는 지출)
    amount = input("금액 입력: ")  # 기록 금액 입력

    if date not in account_book:  # 입력받은 날짜가 account_book에 없으면
        account_book[date] = []  # 해당 날짜에 대한 빈 리스트 생성

    # 입력받은 유형과 금액을 딕셔너리 형태로 저장하고, 해당 날짜의 리스트에 추가
    account_book[date].append({'type': entry_type, 'amount': int(amount)})
    print("기록이 추가되었습니다.")  # 사용자에게 기록 추가 완료 메시지 출력

def view_entries():
    for date, entries in account_book.items():  # account_book의 각 날짜와 기록들을 순회
        print(f"날짜: {date}")  # 날짜 출력
        for entry in entries:  # 해당 날짜의 각 기록들을 순회
            # 기록의 유형과 금액을 출력
            print(f"유형: {entry['type']}, 금액: {entry['amount']}")

def view_totals():
    total_income = 0  # 총 수입을 저장할 변수 초기화
    total_expense = 0  # 총 지출을 저장할 변수 초기화

    for entries in account_book.values():  # account_book의 모든 기록들을 순회
        for entry in entries:  # 각 날짜의 기록들을 순회
            if entry['type'] == '수입':  # 기록 유형이 수입이면
                total_income += entry['amount']  # 총 수입에 금액을 더함
            elif entry['type'] == '지출':  # 기록 유형이 지출이면
                total_expense += entry['amount']  # 총 지출에 금액을 더함

    # 총 수입과 총 지출을 출력
    print(f"총 수입: {total_income}원")
    print(f"총 지출: {total_expense}원")

def show_help():
    print("도움말:")  # 도움말 안내 메시지 출력
    print("1: 수입/지출 추가")
    print("2: 기록 보기")
    print("3: 총 수입/지출 보기")
    print("4: 프로그램 종료")
    print("?: 도움말")

b_is_exit = False  # 프로그램 종료 여부를 결정하는 변수 초기화

while not b_is_exit:  # 프로그램이 종료될 때까지 반복
    func = input("기능 입력 (? 입력시 도움말) : ")  # 사용자에게 기능 입력 받음

    if func == "1":
        add_entry()  # 수입/지출 추가 기능 실행
    elif func == "2":
        view_entries()  # 기록 보기 기능 실행
    elif func == "3":
        view_totals()  # 총 수입/지출 보기 기능 실행
    elif func == "4":
        print("프로그램을 종료합니다.")  # 프로그램 종료 메시지 출력
        b_is_exit = True  # 프로그램 종료 플래그를 True로 설정
    elif func == "?":
        show_help()  # 도움말 출력 기능 실행
    else:
        print("잘못된 입력입니다. 도움말을 보시려면 ?를 입력하세요.")  # 잘못된 입력 메시지 출력
