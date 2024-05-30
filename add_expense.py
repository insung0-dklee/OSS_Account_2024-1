# 24.05.30
# 21722610 주휘진 작성

# 지출을 추가하는 기능 제작

def add_expense(balance):
    try:
        expense = float(input("추가할 지출을 입력하세요: "))
        if expense < 0:
            raise ValueError("지출은 음수가 될 수 없습니다.")
        balance -= expense
        print(f"현재 잔액: {balance} 원")
    except ValueError as e:
        print(f"입력 오류: {e}")
    return balance