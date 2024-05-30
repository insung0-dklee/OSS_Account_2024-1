

b_is_exit = 0

def show_help():
    print("--- 도움말을 출력합니다. ---")
    print("기능 목록:")
    print("1: 수입 추가")
    print("2: 지출 추가")
    print("3: 거래 내역 보기")
    print("4: 요약 보기")
    print("0: 종료")

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        show_help()
        break
    else:
        b_is_exit = not b_is_exit

