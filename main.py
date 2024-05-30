

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":

        break

    elif func == "2":

        break

    elif func == "3":

        break

    elif func == "?":
        print("도움말: 1 - 거래 추가, 2 - 잔액 조회, 3 - 거래 내역 조회, 4 - 종료")

        

    else:
        b_is_exit = not b_is_exit

