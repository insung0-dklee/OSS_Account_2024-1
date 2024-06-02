import random  # 랜덤 모듈을 가져옴

points = 0  # 초기 포인트 값을 0으로 설정

def assign_challenge():
    """
    랜덤으로 도전 과제를 선택하여 반환하는 함수
    """
    challenges = [
        "오늘은 가계부에 3개 이상의 지출을 기록해 볼까요~",
        "오늘은 점심시간에 외식을 하지 말고 집에서 저녁을 해결해 보세요!",
        "오늘은 필요한 것만 사는 쇼핑을 해보자구요!"
    ]
    today_challenge = random.choice(challenges)  # 도전 과제를 랜덤으로 선택
    return today_challenge

def complete_challenge():
    """
    도전 과제를 완료했을 때 포인트를 추가하고 메시지를 출력하는 함수
    """
    global points
    points += 10  # 도전 과제 완료 시 10 포인트 추가
    print("도전과제 완료! 티끌 모아 태산~")
    print(f"현재 포인트: {points}점")

def get_points():
    """
    현재 포인트를 반환하는 함수
    """
    return points
