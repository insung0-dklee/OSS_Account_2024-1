ledger = []

def add_entry():
    date = input("날짜 (YYYY-MM-DD): ")
    category = input("카테고리: ")
    description = input("설명: ")
    amount = float(input("금액: "))
    emotion = input("당시 느낀 감정: ")
    entry = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
        "emotion": emotion
    }
    ledger.append(entry)
    print("항목이 추가되었습니다.")

def view_entries():
    for entry in ledger:
        print(entry)

# 예시 함수: 사용자가 추가한 항목들을 확인하는 기능
def print_help():
    print("""
    1: 지출 항목 추가
    2: 항목 조회
    ?: 도움말 출력
    exit: 종료
    """)

# 메인 코드
while True:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        add_entry()
    elif func == "2":
        view_entries()
    elif func == "?":
        print_help()
    elif func == "exit":
        break
    else:
        print("올바른 기능을 입력해 주세요.")
