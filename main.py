import hashlib

userdata = {}

def user_reg():
    id = input("id 입력: ")
    pw = input("password 입력: ")
    h = hashlib.sha256()
    h.update(pw.encode())
    pw_data = h.hexdigest()
    f = open('login.txt', 'wb')
    userdata[id] = pw_data
    with open('login.txt', 'a', encoding='UTF-8') as fw:
        for user_id, user_pw in userdata.items():
            fw.write(f'{user_id} : {user_pw}\n')

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        expense_records = {}  # 지출 기록을 저장할 딕셔너리

        def record_expense():#지출 기록
            expense_amount = float(input("지출 금액을 입력하세요: "))#지출 금액 입력칸
            expense_item = input("지출 품목을 입력하세요: ")#지출 품목 입력칸
            expense_reason = input("지출 이유를 입력하세요: ")#지출 이유 입력칸

            # 지출 기록을 딕셔너리에 저장
            expense_records[expense_item] = {
                "amount": expense_amount,
                "reason": expense_reason
            }

            print("지출 기록이 성공적으로 추가되었습니다.")

        record_expense()  # 지출 기록 함수 호출

    elif func == "2":
        break

    elif func == "3":
        break

    elif func == "?":
         print("도움말 입력.")
         print("1: 지출 기록") #?입력시
         print("2: 수입 기록") #어떤기능이 있는지
         print("3: 기록 조회") #알려주는 부분
    else:
        b_is_exit = not b_is_exit

