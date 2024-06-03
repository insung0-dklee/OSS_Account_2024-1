import datetime
import os

# 지출 항목을 저장할 리스트
ledger = []

def add_entry():
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    amount = float(input("금액: "))
    emotion = input("당시 느낀 감정: ")
    photo = input("사진 경로 (옵션): ")
    memo = input("메모 (옵션): ")
    location = input("위치 (옵션): ")
    
    entry = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
        "emotion": emotion,
        "photo": photo,
        "memo": memo,
        "location": location
    }
    ledger.append(entry)
    print("항목이 추가되었습니다.")

def view_entry_chronicle():
    date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
    entries = [entry for entry in ledger if entry["date"] == date]
    
    if entries:
        for entry in entries:
            print(f"날짜: {entry['date']}")
            print(f"카테고리: {entry['category']}")
            print(f"설명: {entry['description']}")
            print(f"금액: {entry['amount']}")
            print(f"감정: {entry['emotion']}")
            if entry["photo"]:
                print(f"사진 경로: {entry['photo']}")
                try:
                    if os.name == 'posix':
                        os.system(f'open "{os.path.dirname(entry["photo"])}"')
                    elif os.name == 'nt':
                        os.startfile(os.path.dirname(entry["photo"]))
                    elif os.name == 'mac':
                        os.system(f'open "{os.path.dirname(entry["photo"])}"')
                except Exception as e:
                    print(f"사진 경로를 열 수 없습니다: {e}")
            if entry["memo"]:
                print(f"메모: {entry['memo']}")
            if entry["location"]:
                print(f"위치: {entry['location']}")
            print("-" * 30)
    else:
        print("해당 날짜에 지출 기록이 없습니다.")

def print_help():
    print("""
    1: 지출 항목 추가
    2: 지출 연대기 조회
    ?: 도움말 출력
    exit: 종료!
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        add_entry()
    elif func == "2":
        view_entry_chronicle()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    else:
        print("올바른 기능을 입력해 주세요.")
