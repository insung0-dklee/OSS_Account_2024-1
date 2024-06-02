import json
import os
from datetime import datetime, timedelta

# 저축 파일 초기화
savings_file = 'savings.json'
if not os.path.exists(savings_file):
    with open(savings_file, 'w') as file:
        json.dump({"total_savings": 0, "last_saved_date": str(datetime.now().date())}, file)

# 저축 설정 저장 함수
def save_savings_settings(amount, frequency):
    settings = {
        "amount": amount,
        "frequency": frequency
    }
    with open('savings_settings.json', 'w') as file:
        json.dump(settings, file, ensure_ascii=False, indent=4)

# 저축 설정 로드 함수
def load_savings_settings():
    if not os.path.exists('savings_settings.json'):
        return None
    with open('savings_settings.json', 'r') as file:
        settings = json.load(file)
    return settings

# 자동 저축 실행 함수
def auto_save():
    with open(savings_file, 'r') as file:
        savings_data = json.load(file)

    settings = load_savings_settings()
    if not settings:
        print("저축 설정이 없습니다. 먼저 설정을 해주세요.")
        return

    last_saved_date = datetime.strptime(savings_data["last_saved_date"], "%Y-%m-%d").date()
    today = datetime.now().date()

    if settings["frequency"] == "daily":
        delta = timedelta(days=1)
    elif settings["frequency"] == "weekly":
        delta = timedelta(weeks=1)
    elif settings["frequency"] == "monthly":
        delta = timedelta(days=30)
    else:
        print("잘못된 주기 설정입니다.")
        return

    while last_saved_date + delta <= today:
        last_saved_date += delta
        savings_data["total_savings"] += settings["amount"]

    savings_data["last_saved_date"] = str(last_saved_date)
    with open(savings_file, 'w') as file:
        json.dump(savings_data, file, ensure_ascii=False, indent=4)

    print(f"현재 총 저축 금액: {savings_data['total_savings']} 원")

# 저축 설정 함수
def set_savings():
    amount = float(input("저축할 금액 (원): "))
    frequency = input("저축 주기 (daily, weekly, monthly): ")
    save_savings_settings(amount, frequency)
    print("저축 설정이 완료되었습니다.")

# 도움말 출력 함수
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
    10: 저축 설정
    11: 자동 저축 실행
    ?: 도움말 출력
    exit: 종료
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        input_expense()
    elif func == "2":
        view_expenses()
    elif func == "3":
        generate_monthly_report()
    elif func == "4":
        set_budget()
    elif func == "5":
        analyze_categories()
    elif func == "6":
        user_reg()
    elif func == "7":
        predict_next_month_expense()
    elif func == "8":
        add_debt()
    elif func == "9":
        calculate_interest()
    elif func == "10":
        set_savings()
    elif func == "11":
        auto_save()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    else:
        print("올바른 기능을 입력해 주세요.")
