import datetime
import matplotlib.pyplot as plt

class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description=''):
        transaction = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.date.today()
        }
        self.transactions.append(transaction)

    def get_balance(self):
        return sum(t['amount'] for t in self.transactions)

    def get_transactions(self, start_date=None, end_date=None):
        if start_date and end_date:
            return [t for t in self.transactions if start_date <= t['date'] <= end_date]
        return self.transactions

    def generate_monthly_report(self, year, month):
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month, 28) if month == 2 else datetime.date(year, month, 30 if month in [4, 6, 9, 11] else 31)

        transactions = self.get_transactions(start_date, end_date)
        total_income = sum(t['amount'] for t in transactions if t['amount'] > 0)
        total_expense = sum(t['amount'] for t in transactions if t['amount'] < 0)
        net_income = total_income + total_expense

        expenses_by_category = {}
        for t in transactions:
            if t['amount'] < 0:
                category = t['category']
                expenses_by_category[category] = expenses_by_category.get(category, 0) + t['amount']

        # 리포트 출력 (텍스트)
        print(f"\n리포트 ({year}년 {month}월)")
        print(f"총 수입: {total_income}")
        print(f"총 지출: {total_expense}")
        print(f"순 수익: {net_income}")
        print("카테고리별 지출:")
        for category, amount in expenses_by_category.items():
            print(f"- {category}: {-amount}")

        # 차트 생성
        categories = list(expenses_by_category.keys())
        amounts = [-amount for amount in expenses_by_category.values()]  # 지출은 음수이므로 양수로 변환
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title(f"{year}년 {month}월 카테고리별 지출 비율")
        plt.show()

budget = Budget()
b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        amount = float(input("금액을 입력하세요: "))
        category = input("카테고리를 입력하세요: ")
        description = input("설명을 입력하세요 (선택사항): ")
        budget.add_transaction(amount, category, description)
        print("거래가 추가되었습니다.")
        print(f"현재 잔액: {budget.get_balance()}")

    elif func == "2":
        transactions = budget.get_transactions()
        for t in transactions:
            print(f"날짜: {t['date']}, 금액: {t['amount']}, 카테고리: {t['category']}, 설명: {t['description']}")
    
    elif func == "3":
        print(f"현재 잔액: {budget.get_balance()}")

    elif func == "4":
        year = int(input("연도를 입력하세요 (예: 2024): "))
        month = int(input("월을 입력하세요 (예: 5): "))
        budget.generate_monthly_report(year, month)

    elif func == "?":
        print("1: 거래 추가")
        print("2: 거래 내역 보기")
        print("3: 잔액 보기")
        print("4: 월별 리포트 생성")
        print("q: 종료")

    elif func == "q":
        b_is_exit = 1

    else:
        print("올바른 기능을 입력하세요.")
