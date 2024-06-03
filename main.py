# 가계부 프로그램

# 지출 내역을 저장할 데이터 구조 (리스트)
expenses = []

# 지출 내역을 추가하는 함수
def add_expense(expenses, date, category, amount):
    """
    지출 내역을 추가하는 함수

    Args:
        expenses (list): 지출 내역 리스트
        date (str): 지출 날짜 (예: "2024-06-01")
        category (str): 지출 카테고리 (예: "Food")
        amount (int): 지출 금액 (예: 10000)
    """
    expenses.append({"date": date, "category": category, "amount": amount})

# 지출 내역을 출력하는 함수
def print_expenses(expenses):
    """
    저장된 지출 내역을 출력하는 함수

    Args:
        expenses (list): 지출 내역 리스트
    """
    for expense in expenses:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}")

# 특정 기간 동안의 지출 합계를 비교하는 함수
def compare_expenses(expenses, start_date, end_date):
    """
    특정 기간 동안의 지출 합계를 계산하는 함수

    Args:
        expenses (list): 지출 내역 리스트
        start_date (str): 비교 시작 날짜 (예: "2024-06-01")
        end_date (str): 비교 종료 날짜 (예: "2024-06-03")

    Returns:
        int: 지정된 기간 동안의 지출 합계
    """
    total_amount = 0
    for expense in expenses:
        if start_date <= expense["date"] <= end_date:
            total_amount += expense["amount"]
    return total_amount

# 특정 기간 동안 카테고리별 지출 합계를 비교하는 함수
def compare_expenses_by_category(expenses, start_date, end_date):
    """
    특정 기간 동안 카테고리별 지출 합계를 계산하는 함수

    Args:
        expenses (list): 지출 내역 리스트
        start_date (str): 비교 시작 날짜 (예: "2024-06-01")
        end_date (str): 비교 종료 날짜 (예: "2024-06-03")

    Returns:
        dict: 카테고리별 지출 합계를 담은 딕셔너리
    """
    category_totals = {}
    for expense in expenses:
        if start_date <= expense["date"] <= end_date:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    return category_totals

# 예시 사용
# 지출 내역 추가
add_expense(expenses, "2024-06-01", "햄버거", 10000)
add_expense(expenses, "2024-06-01", "과자", 5000)
add_expense(expenses, "2024-06-02", "넷플릭스", 20000)
add_expense(expenses, "2024-06-03", "게임", 15000)

# 지출 내역 출력
print("Expenses:")
print_expenses(expenses)

# 특정 기간 동안의 지출 합계 비교
start_date = "2024-06-01"
end_date = "2024-06-03"
total = compare_expenses(expenses, start_date, end_date)
print(f"\nTotal expenses from {start_date} to {end_date}: {total}")

# 카테고리별 지출 합계 비교
category_totals = compare_expenses_by_category(expenses, start_date, end_date)
print(f"\nCategory-wise expenses from {start_date} to {end_date}:")
for category, total in category_totals.items():
    print(f"Category: {category}, Total: {total}")
