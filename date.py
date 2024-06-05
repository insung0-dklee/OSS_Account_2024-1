from datetime import datetime

class Expense:
    def __init__(self, name, amount, completed=False):
        self.name = name
        self.amount = amount
        self.completed = completed

    def __repr__(self):
        status = "완료" if self.completed else "미완료"
        return f"{self.name}: {self.amount}원 ({status})"

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def complete_expense(self, expense_name):
        for expense in self.expenses:
            if expense.name == expense_name:
                expense.completed = True
                break

    def total_cost(self):
        return sum(expense.amount for expense in self.expenses)

    def __repr__(self):
        return f"이벤트: {self.name} ({self.date})\n지출 목록:\n" + "\n".join(str(expense) for expense in self.expenses)

class Account_book:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.events = []

    def add_event(self, name, date):
        event = Event(name, date)
        self.events.append(event)
        print(f"이벤트 '{name}'가 추가되었습니다.")

    def view_events(self):
        if not self.events:
            print("이벤트가 없습니다.")
        else:
            for idx, event in enumerate(self.events, start=1):
                print(f"{idx}. {event.name} ({event.date})")

    # 다른 기능들을 추가하거나 수정할 수 있습니다.

def main():
    account = Account_book("가계부", 1000000)

    while True:
        print("\n1. 이벤트 추가")
        print("2. 이벤트 조회")
        print("3. 지출 항목 추가")
        print("4. 지출 항목 완료 처리")
        print("5. 총 지출 금액 조회")
        print("6. 종료")
        
        choice = input("원하는 작업의 번호를 선택하세요: ")

        if choice == '1':
            name = input("이벤트 이름: ")
            date = input("이벤트 날짜 (YYYY-MM-DD): ")
            account.add_event(name, date)

        elif choice == '2':
            account.view_events()

        elif choice == '3':
            name = input("지출 항목 이름: ")
            amount = int(input("지출 금액: "))
            event_idx = int(input("지출 항목을 추가할 이벤트 번호를 선택하세요: ")) - 1
            account.events[event_idx].add_expense(Expense(name, amount))

        elif choice == '4':
            event_idx = int(input("지출 항목 완료 처리를 할 이벤트 번호를 선택하세요: ")) - 1
            expense_name = input("완료 처리할 지출 항목 이름: ")
            account.events[event_idx].complete_expense(expense_name)
            print(f"지출 항목 '{expense_name}'가 완료 처리되었습니다.")

        elif choice == '5':
            event_idx = int(input("총 지출 금액을 조회할 이벤트 번호를 선택하세요: ")) - 1
            total_cost = account.events[event_idx].total_cost()
            print(f"총 지출 금액: {total_cost}원")

        elif choice == '6':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    main()
