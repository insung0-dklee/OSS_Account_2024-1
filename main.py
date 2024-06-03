import json
from datetime import datetime, timedelta

def record_credit_score():
    # 현재 날짜를 가져옵니다.
    today = datetime.today().strftime('%Y-%m-%d')

    # 이전에 저장된 신용점수 데이터를 불러옵니다.
    try:
        with open('credit_score.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # 만약 파일이 없으면 빈 데이터를 생성합니다.
        data = {}

    # 현재 날짜를 키로 사용하여 신용점수를 입력받습니다.
    current_score = float(input("현재 신용점수를 입력하세요: "))

    # 이전 달의 신용점수를 입력받습니다.
    last_month = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    if last_month in data:
        last_month_score = data[last_month]
        print(f"저번 달의 신용점수: {last_month_score}")
        # 현재 신용점수와 비교하여 상승인지 하락인지 출력합니다.
        if current_score > last_month_score:
            trend = "상승"
        elif current_score < last_month_score:
            trend = "하락"
        else:
            trend = "변동 없음"
        print(f"전체적인 신용점수 변동: {trend}")

    # 현재 날짜를 키로 사용하여 신용점수를 저장합니다.
    data[today] = current_score

    # 데이터를 파일에 저장합니다.
    with open('credit_score.json', 'w') as file:
        json.dump(data, file, indent=4)

    # 다음 달의 예상 신용점수를 계속해서 입력받습니다.
    while True:
        next_month = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')
        next_month_score = float(input("다음 달 예상 신용점수를 입력하세요: "))
        data[next_month] = next_month_score

        # 데이터를 파일에 저장합니다.
        with open('credit_score.json', 'w') as file:
            json.dump(data, file, indent=4)

        # 사용자가 더 이상 입력할 지 여부를 물어봅니다.
        more_input = input("더 입력하시겠습니까? (y/n): ")
        if more_input.lower() != 'y':
            break

def check_credit_score_trend():
    try:
        with open('credit_score.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("신용점수 데이터가 없습니다.")
        return

    if len(data) < 2:
        print("데이터가 충분하지 않습니다.")
        return

    scores = list(data.values())
    if scores[-1] > scores[0]:
        trend = "상승"
    elif scores[-1] < scores[0]:
        trend = "하락"
    else:
        trend = "변동 없음"
    
    print(f"전체적인 신용점수 변동: {trend}")

# 테스트용으로 함수를 호출합니다.
record_credit_score()
check_credit_score_trend()
