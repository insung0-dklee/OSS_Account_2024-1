import json
import os

# 구독 파일 초기화
subscriptions_file = 'subscriptions.json'
if not os.path.exists(subscriptions_file):
    with open(subscriptions_file, 'w') as file:
        json.dump([], file)

# 구독 정보 저장 함수
def save_subscription(subscription):
    with open(subscriptions_file, 'r') as file:
        data = json.load(file)
    data.append(subscription)
    with open(subscriptions_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("구독 내역이 저장되었습니다.")

# 구독 정보 입력 함수
def input_subscription():
    name = input("구독 서비스 이름 (예: 유튜브 프리미엄, 넷플릭스): ")
    amount = float(input(f"{name} 구독 금액 (원): "))
    next_payment_date = input(f"{name} 다음 결제일 (예: 2024-06-30): ")
    subscription = {
        'name': name,
        'amount': amount,
        'next_payment_date': next_payment_date
    }
    save_subscription(subscription)

# 구독 정보 보기 함수
def view_subscriptions():
    with open(subscriptions_file, 'r') as file:
        data = json.load(file)
        if data:
            for idx, subscription in enumerate(data, start=1):
                print(f"{idx}. {subscription['name']} - {subscription['amount']}원, 다음 결제일: {subscription['next_payment_date']}")
        else:
            print("저장된 구독 내역이 없습니다.")

# 구독 정보 삭제 함수
def delete_subscription():
    with open(subscriptions_file, 'r') as file:
        data = json.load(file)
    view_subscriptions()
    index = int(input("삭제할 구독 항목의 번호를 입력하세요: "))
    if 1 <= index <= len(data):
        deleted_subscription = data.pop(index - 1)
        with open(subscriptions_file, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"다음 구독이 삭제되었습니다: {deleted_subscription}")
    else:
        print("잘못된 번호입니다. 다시 시도하세요.")

# 도움말 출력 함수
def print_help():
    print("""
    1: 구독 항목 추가
    2: 구독 항목 조회
    3: 구독 항목 삭제
    ?: 도움말 출력
    exit: 종료
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        input_subscription()
    elif func == "2":
        view_subscriptions()
    elif func == "3":
        delete_subscription()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    else:
        print("올바른 기능을 입력해 주세요.")
