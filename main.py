class BudgetTracker:
    def __init__(self, budget):
        """
        BudgetTracker 클래스의 생성자.
        초기 예산을 설정하고 지출 목록을 초기화한다.
        
        Parameters:
        budget (float): 초기 예산 금액
        """
        self.budget = budget
        self.expenses = []

    def add_expense(self, amount, description):
        """
        새로운 지출 항목을 추가한다.
        지출을 추가한 후 예산 초과 여부를 확인한다.
        
        Parameters:
        amount (float): 지출 금액
        description (str): 지출 설명
        """
        self.expenses.append({'amount': amount, 'description': description})
        self.check_budget()

    def check_budget(self):
        """
        현재 총 지출 금액이 예산을 초과했는지 확인하고 메시지를 출력한다.
        """
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        if total_expenses > self.budget:
            print(f"Warning: You have exceeded your budget by {total_expenses - self.budget:.2f}!")
        else:
            print(f"Total expenses: {total_expenses:.2f}, Budget remaining: {self.budget - total_expenses:.2f}")

    def show_expenses(self):
        """
        지금까지 추가된 모든 지출 내역을 출력한다.
        """
        for expense in self.expenses:
            print(f"{expense['description']}: {expense['amount']:.2f}")

    def set_budget(self, new_budget):
        """
        예산을 변경하고 새로운 예산에 대해 초과 여부를 확인한다.
        
        Parameters:
        new_budget (float): 새로운 예산 금액
        """
        self.budget = new_budget
        self.check_budget()

# 초기 예산을 1000으로 설정하여 BudgetTracker 객체 생성
budget_tracker = BudgetTracker(1000.0)

# 새로운 지출 항목 추가
budget_tracker.add_expense(150.0, "Groceries")  # 식료품 지출 추가
budget_tracker.add_expense(200.0, "Utilities")  # 공과금 지출 추가
budget_tracker.add_expense(800.0, "Rent")       # 임대료 지출 추가

# 모든 지출 내역 출력
budget_tracker.show_expenses()

# 예산을 1500으로 변경
budget_tracker.set_budget(1500.0)
# 새로운 지출 항목 추가
budget_tracker.add_expense(100.0, "Entertainment")  # 오락비 지출 추가
