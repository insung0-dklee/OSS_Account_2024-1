import json
from datetime import datetime

# 쿠폰 정보 저장
coupons = {}

# 사용자의 지출 내역 저장
user_expenses = []

def add_coupon():
    """
    쿠폰을 추가하는 함수
    """
    name = input("쿠폰 이름: ")
    category = input("쿠폰 카테고리: ")
    discount = input("할인율 또는 할인 금액: ")
    expiration_date = input("유효기간 (YYYY-MM-DD): ")
    coupons[name] = {
        "category": category,
        "discount": discount,
        "expiration_date": expiration_date
    }
    print("쿠폰이 추가되었습니다.")

def add_expense():
    """
    사용자 지출 내역을 추가하는 함수
    """
    date = input("지출 일자 (YYYY-MM-DD): ")
    category = input("지출 카테고리: ")
    amount = float(input("지출 금액: "))
    description = input("지출 설명: ")
    user_expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    print("지출 내역이 추가되었습니다.")

def recommend_coupon():
    """
    사용자 지출 내역을 기반으로 쿠폰을 추천하는 함수
    """
    if not user_expenses:
        print("지출 내역이 없습니다. 먼저 지출 내역을 추가하세요.")
        return

    # 지출 내역을 카테고리별로 합산
    category_totals = {}
    for expense in user_expenses:
        category = expense["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense["amount"]

    # 가장 많이 지출한 카테고리 찾기
    most_spent_category = max(category_totals, key=category_totals.get)

    # 해당 카테고리의 쿠폰 추천
    recommended_coupons = [coupon for coupon, details in coupons.items() if details["category"] == most_spent_category]

    if recommended_coupons:
        print(f"추천 쿠폰 (카테고리: {most_spent_category}):")
        for coupon in recommended_coupons:
            details = coupons[coupon]
            print(f"- {coupon}: {details['discount']} (유효기간: {details['expiration_date']})")
    else:
        print(f"카테고리 '{most_spent_category}'에 대한 추천 쿠폰이 없습니다.")

def coupon_management():
    while True:
        print("\n---- 쿠폰 관리 메뉴 ----")
        choice = input("쿠폰 기능 입력 (? 입력시 도움말) : ")

        if choice == '1':
            add_coupon()
        elif choice == '2':
            recommend_coupon()
        elif choice == '0':
            print("메인 메뉴로 돌아갑니다. \n")
            break
        elif choice == '?':
            print("1. 쿠폰 추가")
            print("2. 쿠폰 추천")
            print("0. 메인 메뉴로 돌아가기")
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
