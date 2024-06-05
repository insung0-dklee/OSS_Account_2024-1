import json
from datetime import datetime, timedelta

# 가계부 데이터 파일 경로
expenses_file = 'expenses.json'

class HouseholdAccount:
    def __init__(self):
        self.records = self.load_expenses()

    def load_expenses(self):
        """저장된 지출 기록을 불러옵니다."""
        try:
            with open(expenses_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_expenses(self):
        """지출 기록을 저장합니다."""
        with open(expenses_file, 'w', encoding='utf-8') as file:
            json.dump(self.records, file, ensure_ascii=False, indent=4)

    def add_expense(self, date, amount):
        """지출 내역을 추가합니다."""
        month = date.strftime('%Y-%m')
        year = date.strftime('%Y')
        if month not in self.records:
            self.records[month] = 0
        if year not in self.records:
            self.records[year] = 0
        self.records[month] += amount
        self.records[year] += amount
        self.save_expenses()

    def get_last_month_expense(self):
        """지난 달의 총 사용 금액을 반환합니다."""
        today = datetime.today()
        first_day_of_current_month = today.replace(day=1)
        last_month_last_day = first_day_of_current_month - timedelta(days=1)
        last_month_str = last_month_last_day.strftime('%Y-%m')
        return self.records.get(last_month_str, 0)

    def get_last_year_expense(self):
        """지난 해의 총 사용 금액을 반환합니다."""
        today = datetime.today()
        last_year = today.year - 1
        last_year_str = str(last_year)
        return self.records.get(last_year_str, 0)

    def check_and_print_expenses(self):
        """매월 첫날 및 매년 첫날에 지출 내역을 출력합니다."""
        today = datetime.today()

        # 매월 첫날이면 저번 달 사용 금액 출력
        if today.day == 1:
            last_month_expense = self.get_last_month_expense()
            print(f"지난 달의 총 사용 금액은: {last_month_expense}원 입니다.")
        
        # 매년 첫날이면 저번 해 사용 금액 출력
        if today.month == 1 and today.day == 1:
            last_year_expense = self.get_last_year_expense()
            print(f"지난 해의 총 사용 금액은: {last_year_expense}원 입니다.")

class BudgetSimulation:
    def __init__(self, goal_name, target_amount, target_date):
        self.goal_name = goal_name  # 목표 이름
        self.target_amount = target_amount  # 목표 금액
        self.target_date = datetime.strptime(target_date, "%Y-%m-%d")  # 목표 날짜
        self.current_savings = 0  # 현재 저축액
        self.household_account = HouseholdAccount()  # 가계부 클래스 인스턴스 생성

    def add_savings(self, amount):
        """저축 금액 추가"""
        self.current_savings += amount
        print(f"{amount}원이 저축되었습니다. 현재 저축액: {self.current_savings}원")

    def calculate_monthly_savings(self):
        """목표 달성 위해 필요한 월별 저축액 계산"""
        today = datetime.today()
        months_left = (self.target_date.year - today.year) * 12 + self.target_date.month - today.month
        if months_left <= 0:
            print("목표 날짜가 이미 지났습니다.")
            return None
        remaining_amount = self.target_amount - self.current_savings
        monthly_savings = remaining_amount / months_left
        print(f"매월 저축해야 할 금액: {monthly_savings:.2f}원, 남은 달 수: {months_left}개월")
        return monthly_savings, months_left

    def simulate_expenses(self):
        """미래 지출을 시뮬레이션"""
        monthly_savings, months_left = self.calculate_monthly_savings()
        if monthly_savings is None:
            return
        
        today = datetime.today()
        future_expenses = []
        
        for month in range(1, months_left + 1):
            future_date = (today + timedelta(days=month*30)).strftime('%Y-%m')
            future_expenses.append({
                'date': future_date,
                'amount': monthly_savings
            })
        
        print("미래 지출 시뮬레이션:")
        for expense in future_expenses:
            print(f"{expense['date']}: {expense['amount']:.2f}원")

    def save_simulation(self):
        """시뮬레이션 결과 저장"""
        simulation_result = {
            'goal_name': self.goal_name,
            'target_amount': self.target_amount,
            'target_date': self.target_date.strftime('%Y-%m-%d'),
            'current_savings': self.current_savings
        }
        with open('simulation_result.json', 'w', encoding='utf-8') as file:
            json.dump(simulation_result, file, ensure_ascii=False, indent=4)
        print("시뮬레이션 결과가 저장되었습니다.")

    def check_and_print_expenses(self):
        """가계부의 지출 내역을 확인하고 출력"""
        self.household_account.check_and_print_expenses()
