import json
import os

class HouseholdAccountBook:
    def __init__(self, data_file='account_book_data.json'):
        self.data_file = data_file
        self.monthly_budget = {}
        self.records = []
        self.load_data()

    def set_monthly_budget(self, month, year, budget):
        self.monthly_budget[f'{year}-{month:02d}'] = budget
        self.save_data()

    def get_monthly_budget(self, month, year):
        return self.monthly_budget.get(f'{year}-{month:02d}', None)

    def budget_status(self, month, year):
        budget = self.get_monthly_budget(month, year)
        if budget is None:
            return "요청하신 달은 지출 목표가 없습니다."
        else:
            return f"요청하신 달의 지출 목표는 {budget}."

    def save_data(self):
        data = {
            'monthly_budget': self.monthly_budget,
            'records': self.records
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.monthly_budget = data.get('monthly_budget', {})
                self.records = data.get('records', [])

def print_help():
    print("""
    1: 월별 예산 설정
    2: 현재 예산 상태 확인
    3: 없음
    ?: 도움말
    exit: 프로그램 종료
    """)

def main():
    account_book = HouseholdAccountBook()
    b_is_exit = 0

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
            year = int(input("년 입력 (YYYY): "))
            month = int(input("월 입력 (MM): "))
            budget = int(input("예산 금액 입력: "))
            account_book.set_monthly_budget(month, year, budget)
            print("월별 예산이 설정되었습니다.")

        elif func == "2":
            year = int(input("년 입력 (YYYY): "))
            month = int(input("월 입력 (MM): "))
            status = account_book.budget_status(month, year)
            print(status)

        elif func == "3":

            break
        elif func == "?":
            print_help()

        elif func.lower() == "exit":
            b_is_exit = 1

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
            print_help()

if __name__ == "__main__":
    main()
