# 24.05.30
# 21722610 주휘진 작성

# 수입을 추가하는 기능 제작



def add_income(balance):
    try:
        income = float(input("추가할 수입을 입력하세요: "))
        if income < 0:
            raise ValueError("수입은 음수가 될 수 없습니다.")
        balance += income
        print(f"현재 잔액: {balance} 원")
    except ValueError as e:
        print(f"입력 오류: {e}")
    return balance