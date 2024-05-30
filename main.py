# 가계부 기능 
# 프로그램 종료 여부를 나타내는 변수
b_is_exit = 0
# 지출 내역을 저장하는 리스트
spending_list = []

# 도움말을 출력하는 함수
def display_help():
    print("""
    도움말:
    1 - 프로그램 종료 
    2 - 지출 기록 추가
    3 - 전체 지출 내역 표시
    ? - 도움말 표시
    """)

# 입력된 값이 숫자인지 확인하는 함수
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# 지출 내역을 추가하는 함수
def add_spending():
    # 사용자로부터 지출 항목 입력 받기
    # 지출 항목에 숫자가 포함되어 있는지 확인
    item = input("지출 항목: ")
    if any(char.isdigit() for char in item):
        print("지출 항목에 숫자는 포함될 수 없습니다. 다시 입력해주세요.")
        return
    # 사용자로부터 지출 금액 입력 받기
     # 지출 금액에 소수점이나 숫자가 아닌 문자가 포함되어 있는지 확인
    amount = input("지출 금액: ")
    if not amount.isdigit():  
        print("지출 금액에는 소수점이 포함될 수 없습니다. 다시 입력해주세요.")
        return
    spending_list.append({'item': item, 'amount': int(amount)}) 
    print("지출 기록이 추가되었습니다.")

# 전체 지출 내역을 출력하는 함수
def display_spending():
    # 지출 내역이 존재하지 않을 때
    if not spending_list:
        print("지출 내역이 없습니다.")
        # 각 내역을 출력하고 합계를 계산
         # 전체 합계 출력
    else:
        total_amount = 0
        print("전체 지출 내역:")
        for idx, spending in enumerate(spending_list):
            total_amount += spending['amount']
            print(f"{idx + 1}. 항목: {spending['item']}, 금액: {spending['amount']}")
        print(f"전체 합계: {total_amount}")

# 사용자로부터 기능을 입력받고 해당 기능을 실행
# 0 : 프로그램 종료
# 1 : 지출 금액 입력
# 2 : 전체 지출 금액 확인
# 그외의 숫자값: 기능 재 입력
while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "0" or func.lower() == "exit":
        b_is_exit = True
        

    elif func == "1":
        add_spending()

    elif func == "2":
        display_spending()

    elif func == "?":
        display_help()

    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
