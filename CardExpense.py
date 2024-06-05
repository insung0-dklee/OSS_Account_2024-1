"""
@주요기능
1 초기화 메서드: expenses 리스트를 초기화합니다.
2 항목 추가 메서드: 금액과 카드 이름을 받아서 expenses 리스트에 추가합니다.
3 항목 보기 메서드: 기록된 모든 항목을 출력합니다.
"""

class CardExpense:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, card):
        self.expenses.append({"amount": amount, "card": card})

    def view_expenses(self):
        if not self.expenses:
            print("기록된 항목이 없습니다.")
            return

        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. 금액: {expense['amount']}, 카드 이름: {expense['card']}")

"""
@주요기능
1 메인 루프: 사용자가 종료를 선택할 때까지 반복됩니다.
2 항목 추가 선택: 금액과 카드 이름을 입력받아 항목을 추가합니다.
3 항목 보기 선택: 기록된 모든 항목을 출력합니다.
4 종료 선택: 프로그램을 종료합니다.
5 @ 잘못된 선택: 유효하지 않은 입력에 대해 메시지를 출력합니다.
"""

def main():
    tracker =  CardExpense()

    while True:
        print("\n가계부 프로그램")
        print("1. 항목 추가")
        print("2. 항목 보기")
        print("3. 종료")
        choice = input("선택: ")

        if choice == '1':
            amount = input("금액을 입력하세요: ")
            card = input("카드 이름을 입력하세요: ")

            try:
                amount = float(amount)
            except ValueError:
                print("금액은 숫자여야 합니다.")
                continue

            tracker.add_expense(amount, card)
            print("항목이 추가되었습니다.")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
