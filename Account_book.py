# 지출비교 및 지출경고 메시지 기능
import datetime

class Account_book:
    def __init__(self, name, bal):
        self.name = name
        self.balance = bal if bal > 0 else 0
        self.income_total = self.balance
        self.income_list = [self.balance] if self.balance > 0 else []
        self.spend_total = 0
        self.spend_list = []
        self.transactions = [("Initial Balance", self.balance, "initial", "")]
        self.budgets = {}
        self.spending = {}
        self.monthly_spending = {}

        if bal <= 0:
            print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

    def get_current_month(self):
        now = datetime.datetime.now()
        return now.year, now.month

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount, "income", ""))
        self.income_total += amount
        self.income_list.append(amount)

    def withdraw(self, amount, description=""):
        category = self.categorize_expense(description)
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}원")
        else:
            self.balance -= amount
            self.transactions.append(("Withdrawal", amount, category, description))
            self.spend_total += amount
            self.spend_list.append(amount)
            self.spending[category] = self.spending.get(category, 0) + amount

            # Update monthly spending
            current_month = self.get_current_month()
            if current_month not in self.monthly_spending:
                self.monthly_spending[current_month] = 0
            self.monthly_spending[current_month] += amount

            self.check_budget(category)
            self.check_spending_increase()

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"Budget for {category} set to {amount}원")

    def check_budget(self, category):
        if category in self.budgets and self.spending.get(category, 0) > self.budgets[category]:
            print(f"Alert: You have exceeded the budget for {category}! (Budget: {self.budgets[category]}원, Spending: {self.spending[category]}원)")

    def categorize_expense(self, description):
        keywords = {
            "food": ["식비", "음식", "식료품", "식사"],
            "transportation": ["교통", "버스", "지하철", "택시"],
            "entertainment": ["문화", "영화", "공연", "놀이"],
            "shopping": ["쇼핑", "상점", "마트", "구매"],
            "utilities": ["요금", "공과금", "전기", "수도"]
        }
        category = "uncategorized"
        for key, values in keywords.items():
            for value in values:
                if value in description:
                    category = key
                    break
            if category != "uncategorized":
                break
        return category

    def check_spending_increase(self):
        current_month = self.get_current_month()
        previous_month = (current_month[0], current_month[1] - 1) if current_month[1] > 1 else (current_month[0] - 1, 12)

        if previous_month in self.monthly_spending:
            previous_spending = self.monthly_spending[previous_month]
            current_spending = self.monthly_spending.get(current_month, 0)
            if current_spending > previous_spending * 1.2:  # 20% increase threshold
                print(f"Warning: Your spending has increased significantly this month! (Previous: {previous_spending}원, Current: {current_spending}원)")

    def show_balance(self):
        print(f"Current balance: {self.balance}원")

    def show_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            if transaction[0] == "Deposit" or transaction[0] == "Initial Balance":
                print(f"{transaction[0]}: +{transaction[1]}원")
            else:
                print(f"{transaction[0]}: -{transaction[1]}원, Category: {transaction[2]}, Description: {transaction[3]}")

    def show_budgets(self):
        print("Budgets:")
        for category, amount in self.budgets.items():
            print(f"{category}: {amount}원")

    def show_spending(self):
        print("Spending:")
        for category, amount in self.spending.items():
            print(f"{category}: {amount}원")

    def income(self):
        try:
            income_money = int(input("수입을 입력하세요 "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return
        if income_money < 0:
            print("0 미만의 값을 입력하셨습니다.")
            return
        self.deposit(income_money)

    def spend(self):
        try:
            spend_money = int(input("지출을 입력하세요 "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            return
        description = input("지출 설명을 입력하세요: ")
        if spend_money < 0 or spend_money > self.balance:
            print("값을 잘못 입력하셨습니다.")
            return
        self.withdraw(spend_money, description)

    def show_total(self):
        print("현재까지 소득의 총합은 ", self.income_total, "원 입니다.")
        print("현재까지 지출의 총합은 ", self.spend_total, "원 입니다.")

    def show_sortedlist(self):
        print("보고싶은 내역을 선택하세요")
        button = input("1번 - 수입, 2번 - 지출: ")
        if button == "1":
            print("현재까지의 수입 순위")
            sortedlist = sorted(self.income_list, reverse=True)
            for i, amount in enumerate(sortedlist[:10]):
                print(i + 1, "위:", amount, "원")
        elif button == "2":
            print("현재까지 사용한 금액 순위")
            sortedlist = sorted(self.spend_list, reverse=True)
            for i, amount in enumerate(sortedlist[:10]):
                print(i + 1, "위:", amount, "원")
        else:
            print("잘못 입력하셨습니다.")

    # 추가 기능 1: 카테고리별 지출 비율 계산
    def category_spending_ratio(self):
        print("Category Spending Ratios:")
        total_spending = sum(self.spending.values())
        if total_spending == 0:
            print("No spending recorded.")
            return
        for category, amount in self.spending.items():
            ratio = (amount / total_spending) * 100
            print(f"{category}: {ratio:.2f}%")

    # 추가 기능 2: 최근 N개의 거래 내역 조회
    def recent_transactions(self, n):
        print(f"Recent {n} Transactions:")
        for transaction in self.transactions[-n:]:
            if transaction[0] == "Deposit" or transaction[0] == "Initial Balance":
                print(f"{transaction[0]}: +{transaction[1]}원")
            else:
                print(f"{transaction[0]}: -{transaction[1]}원, Category: {transaction[2]}, Description: {transaction[3]}")

    # 추가 기능 3: 예상 잔액 계산
    def projected_balance(self, months):
        average_income = self.income_total / len(self.income_list) if self.income_list else 0
        average_spending = self.spend_total / len(self.spend_list) if self.spend_list else 0
        projected_balance = self.balance + (average_income - average_spending) * months
        print(f"Projected balance after {months} months: {projected_balance}원")

# 가계부 인스턴스 생성
account_book = AccountBook("사용자1", 5000)

# 입출금 기록 및 예산 설정
account_book.deposit(5000)
account_book.set_budget("food", 1000)
account_book.set_budget("entertainment", 500)

account_book.withdraw(300, "편의점에서 음료 구매")
account_book.withdraw(800, "식사 비용")
account_book.withdraw(600, "영화 관람")

# 잔액, 거래 내역, 예산 및 지출 내역 출력
account_book.show_balance()
account_book.show_transactions()
account_book.show_budgets()
account_book.show_spending()
account_book.show_total()
account_book.show_sortedlist()