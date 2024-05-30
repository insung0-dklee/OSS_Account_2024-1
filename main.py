def minusMoney(origin,money) :
    return origin - money




b_is_exit = 0

while not b_is_exit:
    money = 1000;
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        deposit = int(input("지출 할 돈을 입력하세요 : "))
        if deposit >money :
            print("지출하는 돈이 더 많습니다!")
            continue;
        else :
            money = minusMoney(money,deposit)
            print("잔고 : " + money)
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

