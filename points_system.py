# points_system.py

import json
import os

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
