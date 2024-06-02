import json
import os

# 파일 초기화
wishlist_file = 'wishlist.json'
if not os.path.exists(wishlist_file):
    with open(wishlist_file, 'w') as file:
        json.dump([], file)

# 위시리스트 저장 함수
def save_wishlist(item):
    with open(wishlist_file, 'r') as file:
        data = json.load(file)
    data.append(item)
    with open(wishlist_file, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print("위시리스트에 저장되었습니다.")

# 위시리스트 추가 함수
def add_to_wishlist():
    url = input("상품 URL을 입력하세요: ")
    target_price = float(input("목표 가격을 입력하세요 (원): "))
    item = {
        'url': url,
        'target_price': target_price
    }
    save_wishlist(item)

# 할인 알림 확인 함수
def check_wishlist():
    with open(wishlist_file, 'r') as file:
        data = json.load(file)
    for item in data:
        current_price = float(input(f"{item['url']}의 현재 가격을 입력하세요 (원): "))
        if current_price and current_price <= item['target_price']:
            print(f"할인된 가격: {current_price}원 - {item['url']}\n이제 구매를 추천합니다!")

# 도움말 출력 함수
def print_help():
    print("""
    1: 위시리스트 항목 추가
    2: 할인 가격 확인
    ?: 도움말 출력
    exit: 종료
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        add_to_wishlist()
    elif func == "2":
        check_wishlist()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    else:
        print("올바른 기능을 입력해 주세요.")
