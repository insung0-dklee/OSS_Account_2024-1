import Account

b_is_exit = 0

account_book = Account.account_book("목돈")

while not b_is_exit:
    func = input("기능 입력 '?' 입력시 도움말) : ")
   
    if func == "1":
        account_book.income()
        continue

    elif func == "2":
        account_book.expendse()
        continue

    elif func == "3":
        account_book.show_balance()
        continue

    elif func == "?":
        print("1: 수입, 2: 지출, 3: 잔고확인")
        continue

    else:
        b_is_exit = not b_is_exit