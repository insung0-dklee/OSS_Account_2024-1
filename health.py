from datetime import datetime, timedelta

class Rental:
    def __init__(self, item, daily_rate, start_date, duration_days):
        self.item = item
        self.daily_rate = daily_rate
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.end_date = self.start_date + timedelta(days=duration_days)

    def total_cost(self):
        return self.daily_rate * self.duration_days

    def __repr__(self):
        return f"{self.item}: {self.daily_rate}원/일, {self.duration_days}일 대여, 반납일: {self.end_date.strftime('%Y-%m-%d')}"

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
    rental_manager = []
    health_manager = HealthExpenseManager()

    while True:
        print("\n1. 장기 대여 추가")
        print("2. 장기 대여 목록 조회")
        print("3. 총 대여 비용 조회")
        print("4. 건강 관련 지출 추가")
        print("5. 건강 관련 지출 조회")
        print("6. 총 건강 관련 지출 금액 조회")
        print("7. 건강 관련 지출 분석")
        print("8. 종료")

        choice = input("원하는 작업의 번호를 선택하세요: ")

        if choice == '1':
            item = input("대여 항목 이름: ")
            daily_rate = int(input("일일 대여 요금: "))
            start_date = input("대여 시작일 (YYYY-MM-DD): ")
            duration_days = int(input("대여 기간 (일): "))
            rental_manager.append(Rental(item, daily_rate, start_date, duration_days))
            print(f"장기 대여 항목 '{item}'가 추가되었습니다.")

        elif choice == '2':
            if not rental_manager:
                print("장기 대여 항목이 없습니다.")
            else:
                for rental in rental_manager:
                    print(rental)

        elif choice == '3':
            total_cost = sum(rental.total_cost() for rental in rental_manager)
            print(f"총 대여 비용: {total_cost}원")

        elif choice == '4':
            name = input("지출 항목 이름: ")
            amount = int(input("지출 금액: "))
            category = input("카테고리 (예: 헬스장, 건강 보조 식품 등): ")
            date = input("지출 날짜 (YYYY-MM-DD): ")
            health_manager.add_expense(HealthExpense(name, amount, category, date))
            print(f"지출 항목 '{name}'가 추가되었습니다.")

        elif choice == '5':
            health_manager.view_expenses()

        elif choice == '6':
            total_cost = health_manager.total_cost()
            print(f"총 건강 관련 지출 금액: {total_cost}원")

        elif choice == '7':
            health_manager.analyze_health_spending()

        elif choice == '8':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
