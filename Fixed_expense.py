from datetime import datetime
#유튜브,넷플릭스 등과 같은 매달 정기결제 목록,금액을 기록하는 기능
class FixedExpense:
    def __init__(self, name, price, due_date):
        self.name = name
        self.price = price
        self.due_date = due_date

# 고정 지출 항목 입력 함수
def add_fixed_expense():
    name = input("고정 지출 항목 이름을 입력하세요: ")
    price = int(input("가격을 입력하세요: "))
    due_date = int(input("매달 정기 결제 일을 입력하세요(ex 1일): "))
    fixed_expenses.append(FixedExpense(name, price, due_date))
    print("고정 지출 항목이 추가되었습니다.")

# 고정 지출 항목 삭제 함수
def remove_fixed_expense():
    if not fixed_expenses:
        print("고정 지출 항목이 없습니다.")
        return
    print("삭제할 고정 지출 항목을 선택하세요:")
    for i, expense in enumerate(fixed_expenses):
        print(f"{i + 1}. 이름: {expense.name}, 가격: {expense.price}, 지출 날짜: {expense.due_date}")
    choice = int(input("삭제할 항목 번호를 입력하세요: "))
    del fixed_expenses[choice - 1]
    print("고정 지출 항목이 삭제되었습니다.")

# 고정 지출 목록 출력 함수
def display_fixed_expenses():
    if not fixed_expenses:
        print("고정 지출 항목이 없습니다.")
        return
    print("고정 지출 목록:")
    for expense in fixed_expenses:
        print(f"이름: {expense.name}, 가격: {expense.price}, 지출 날짜: {expense.due_date}")

# 이번 달의 남은 고정 지출액 계산 함수
def calculate_remaining_fixed_expenses():
    current_day = datetime.now().day
    total_fixed_expenses = sum(expense.price for expense in fixed_expenses)
    remaining_fixed_expenses = total_fixed_expenses - sum(expense.price for expense in fixed_expenses if expense.due_date < current_day)
    return remaining_fixed_expenses

# 고정 지출 목록
fixed_expenses = []

# 메뉴 표시
while True:
    print("\n======= 가계부 메뉴 =======")
    print("1. 고정 지출 항목 입력")
    print("2. 고정 지출 항목 삭제")
    print("3. 고정 지출 목록 표시")
    print("4. 이번 달 남은 고정 지출금액 표시")
    print("5. 종료")
    choice = int(input("메뉴를 선택하세요: "))

    if choice == 1:
        add_fixed_expense()
    elif choice == 2:
        remove_fixed_expense()
    elif choice == 3:
        display_fixed_expenses()
    elif choice == 4:
        remaining_expenses = calculate_remaining_fixed_expenses()
        print(f"이번 달의 남은 고정 지출액: {remaining_expenses}원")
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴 번호를 입력하세요.")
