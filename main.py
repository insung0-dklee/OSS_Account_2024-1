import json
from datetime import datetime

# 빚 내역 저장 함수
def save_debt(debt):
    with open(debt_file, 'r') as file:
        data = json.load(file)
    data.append(debt)
    with open(debt_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# 빚 추가 함수
def add_debt():
    creditor = input("채권자: ")
    principal = float(input("원금 (원): "))
    rate = float(input("이율 (예: 0.05 for 5%): "))
    start_date = input("대출 시작 날짜 (YYYY-MM-DD): ")
    debt = {
        'creditor': creditor,
        'principal': principal,
        'rate': rate,
        'start_date': start_date
    }
    save_debt(debt)
    print("빚이 추가되었습니다.")

# 빚 이자 계산 함수
def calculate_interest():
    with open(debt_file, 'r') as file:
        debts = json.load(file)
    if debts:
        for debt in debts:
            start_date = datetime.strptime(debt['start_date'], "%Y-%m-%d")
            days_passed = (datetime.now() - start_date).days
            interest = debt['principal'] * debt['rate'] * (days_passed / 365)
            print(f"채권자: {debt['creditor']}, 원금: {debt['principal']} 원, 발생한 이자: {interest:.2f} 원")
    else:
        print("저장된 빚 내역이 없습니다.")

# 빚 파일 초기화
debt_file = 'debts.json'
if not os.path.exists(debt_file):
    with open(debt_file, 'w') as file:
        json.dump([], file)

# 도움말에 빚 관리 기능 추가
def print_help():
    print("""
    1: 수입/지출 항목 추가
    2: 항목 조회
    3: 월별 보고서 생성
    4: 예산 설정 및 초과 알림
    5: 지출 카테고리 분석
    6: 회원가입
    7: 예상 지출 항목
    8: 빚 추가
    9: 이자 계산
    ?: 도움말 출력
    exit: 종료
    """)
