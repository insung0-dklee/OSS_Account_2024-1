# points_system.py

import json
import os
import random

points_file = 'points.json'

# 포인트 적립 함수
def earn_points(user_id, amount):
    points = amount * 0.01  # 1% 적립
    user_points = load_points(user_id)
    user_points += points
    save_points(user_id, user_points)
    print(f"{points} 포인트가 적립되었습니다. 현재 포인트: {user_points}")

# 포인트 사용 함수
def use_points(user_id, points):
    user_points = load_points(user_id)
    if user_points >= points:
        user_points -= points
        save_points(user_id, user_points)
        print(f"{points} 포인트를 사용했습니다. 남은 포인트: {user_points}")
    else:
        print("포인트가 부족합니다.")

# 포인트 조회 함수
def check_points(user_id):
    user_points = load_points(user_id)
    print(f"현재 {user_id}님의 포인트: {user_points}")

# 포인트 로드 함수
def load_points(user_id):
    if os.path.exists(points_file):
        with open(points_file, 'r') as file:
            data = json.load(file)
        return data.get(user_id, 0)
    return 0

# 포인트 저장 함수
def save_points(user_id, points):
    if os.path.exists(points_file):
        with open(points_file, 'r') as file:
            data = json.load(file)
    else:
        data = {}
    data[user_id] = points
    with open(points_file, 'w') as file:
        json.dump(data, file)

# 포인트 시스템 테스트용 메인 함수
if __name__ == "__main__":
    test_user = "test_user"
    earn_points(test_user, 1000)  # 1000원 지출로 10포인트 적립
    check_points(test_user)
    use_points(test_user, 5)
    check_points(test_user)

# 복권 구매 함수
def buy_lottery(user_id):
    ticket_cost = 5     # 복권 한 장의 비용을 5 포인트로 고정
    prize = 100         # 당첨 시 획득 포인트를 100으로 고정
    probability = 0.01  # 당첨 확률을 1%로 고정
    num_digits = 5      # 복권 번호를 5자리로 고정
    
    try:
        user_points = load_points(user_id)
        if user_points >= ticket_cost:
            user_points -= ticket_cost
            save_points(user_id, user_points)
            print(f"복권을 구매했습니다. 티켓 비용: {ticket_cost} 포인트, 남은 포인트: {user_points}")

            # 복권 번호 생성
            winning_number = random.randint(0, 10**num_digits - 1)
            user_number = random.randint(0, 10**num_digits - 1)
            print(f"당첨 번호: {winning_number:0{num_digits}d}, 사용자 번호: {user_number:0{num_digits}d}")

            if user_number == winning_number and random.random() < probability:
                user_points += prize
                save_points(user_id, user_points)
                print(f"축하합니다! 복권에 당첨되어 {prize} 포인트를 획득했습니다. 현재 포인트: {user_points}")
            else:
                print("아쉽게도 복권에 당첨되지 않았습니다.")
        else:
            print("포인트가 부족하여 복권을 구매할 수 없습니다.")