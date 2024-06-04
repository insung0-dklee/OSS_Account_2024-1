class HealthExpense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __repr__(self):
        return f"{self.date}: {self.name} - {self.amount}원 ({self.category})"

class HealthExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("기록된 건강 관련 지출이 없습니다.")
        else:
            for expense in self.expenses:
                print(expense)

    def total_cost(self):
        return sum(expense.amount for expense in self.expenses)

    def analyze_health_spending(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0
            categories[expense.category] += expense.amount

        print("건강 관련 지출 분석:")
        for category, total in categories.items():
            print(f"{category}: {total}원")

def main():
    manager = HealthExpenseManager()

    while True:
        print("\n1. 건강 관련 지출 추가")
        print("2. 건강 관련 지출 조회")
        print("3. 총 건강 관련 지출 금액 조회")
        print("4. 건강 관련 지출 분석")
        print("5. 종료")

        choice = input("원하는 작업의 번호를 선택하세요: ")

        if choice == '1':
            name = input("지출 항목 이름: ")
            amount = int(input("지출 금액: "))
            category = input("카테고리 (예: 헬스장, 건강 보조 식품 등): ")
            date = input("지출 날짜 (YYYY-MM-DD): ")
            manager.add_expense(HealthExpense(name, amount, category, date))
            print(f"지출 항목 '{name}'가 추가되었습니다.")

        elif choice == '2':
            manager.view_expenses()

        elif choice == '3':
            total_cost = manager.total_cost()
            print(f"총 건강 관련 지출 금액: {total_cost}원")

        elif choice == '4':
            manager.analyze_health_spending()

        elif choice == '5':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
