class Account_book: # 가계부 클래스

  bal = 0 #잔액 - 미설정시 0원
  income_total = 0 #수입 총액
  income_list = [] #수입 기록 리스트
  spend_total = 0 #지출 총액
  spend_list = [] #지출 기록 리스트
  name = " " #이름 - 미설정시 공백

  def __init__(self,name,bal): # 초기화
    self.name = name #이름 설정
    if(bal>0):  #잔액 설정
      self.income_total += bal
      self.bal = bal
    else: #잔액이 0원보다 낮으면 0원으로 설정
      print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

  def income(self):# 수입 입력시 추가
    income_money = int(input("수입을 입력하세요 "))
    if(income_money < 0):#수입 잘못 입력 방지
      print("0 미만의 값을 입력하셨습니다.")
      return 0
    self.bal += income_money #금액 추가 및 내역을 리스트에 넣기
    self.income_list.append (income_money)
    self.income_total += income_money

  def spend(self):#지출 입력시 추가
    spend_money = int(input("지출을 입력하세요 "))
    if(spend_money < 0 or spend_money > self.bal):#지출 잘못 입력 방지
      print("값을 잘못 입력하셨습니다.")
      return 0
    self.bal -= spend_money #금액 감소 및 내역을 리스트에 넣기
    self.spend_list.append(spend_money)
    self.spend_total += spend_money

  def show_account(self): #금액 출력
    print("현재 남은 금액은: ",self.bal, "원 입니다.")

  def show_total(self): #수입,지출 총액 출력
    print("현재까지 소득의 총합은 ",self.income_total,"원 입니다.")
    print("현재까지 지출의 총합은 ",self.spend_total,"원 입니다.")

  def show_sortedlist(self): #지출 및 수입 순위 출력
    print("보고싶은 내역을 선택하세요")
    button = input("1번 - 수입, 2번 - 지출: ")#수입 혹은 지출 선택
    if(button == "1"):#주의 - button값은 input으로 받아 char형 변수임
      print("현재까지의 수입 순위")
      sortedlist = sorted(self.income_list)[::-1] #수입 리스트 정렬
      for i in range(0,10):#10위 까지만 출력
        if(len(self.income_list) <= i):#만약 리스트 크기보다 작을 경우 탈출
          break
        print(i+1,"위:",sortedlist[i],"원")
    elif(button == "2"):
      print("현재까지 사용한 금액 순위")
      sortedlist = sorted(self.spend_list)[::-1]#지출 리스트 정렬
      for i in range(0,10):#10위 까지만 출력
        if(len(self.income_list) <= i):#만약 리스트 크기보다 작을 경우 탈출
          break
        print(i+1,"위 ",sortedlist[i],"원")
    else:
      print("잘못 입력하셨습니다.")


# 지출예산 설정 및 알림 기능
class AccountBook:
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

        if bal <= 0:
            print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

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
            self.check_budget(category)

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
            sortedlist = sorted(self.income_list)[::-1]
            for i in range(10):
                if len(self.income_list) <= i:
                    break
                print(i + 1, "위:", sortedlist[i], "원")
        elif button == "2":
            print("현재까지 사용한 금액 순위")
            sortedlist = sorted(self.spend_list)[::-1]
            for i in range(10):
                if len(self.spend_list) <= i:
                    break
                print(i + 1, "위 ", sortedlist[i], "원")
        else:
            print("잘못 입력하셨습니다.")

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