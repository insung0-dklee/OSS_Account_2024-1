

b_is_exit = 0

def print_help():
    print("1: 수입 추가")
    print("2: 지출 추가")
    print("3: 내역 조회")
    print("4: 잔액 확인")
    print("?: 도움말")

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말 입력.")

        break

    else:
        b_is_exit = not b_is_exit

