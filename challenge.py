import random
import json
import os

# 초기 포인트 값을 파일에서 불러오거나 0으로 설정
points_file = "points.json"

def load_points():
    if os.path.exists(points_file):
        with open(points_file, "r") as file:
            return json.load(file).get("points", 0)
    return 0

points = load_points()

def save_points():
    with open(points_file, "w") as file:
        json.dump({"points": points}, file)

def assign_challenge():
    """
    랜덤으로 도전 과제를 선택하여 반환하는 함수
    """
    challenges = [
        ("오늘은 가계부에 3개 이상의 지출을 기록해 볼까요~", 10),
        ("오늘은 점심시간에 외식을 하지 말고 집에서 저녁을 해결해 보세요!", 15),
        ("오늘은 필요한 것만 사는 쇼핑을 해보자구요!", 20)
    ]
    today_challenge = random.choice(challenges)
    return today_challenge

def complete_challenge(points_awarded):
    """
    도전 과제를 완료했을 때 포인트를 추가하고 메시지를 출력하는 함수
    """
    global points
    points += points_awarded
    save_points()
    print(f"도전과제 완료! 티끌 모아 태산~ {points_awarded} 포인트를 받았습니다.")
    print(f"현재 포인트: {points}점")

def get_points():
    """
    현재 포인트를 반환하는 함수
    """
    return points

if __name__ == "__main__":
    today_challenge, points_awarded = assign_challenge()
    print(today_challenge)
    
    user_input = input("이 도전과제를 완료했나요? (y/n): ").strip().lower()
    if user_input == "y":
        complete_challenge(points_awarded)
    else:
        print("도전과제를 완료하지 못했군요. 내일 다시 도전해보세요!")
    print(f"현재 포인트: {get_points()}점")
