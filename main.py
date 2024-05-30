from add_income import add_income
from add_expense import add_expense
from remaining_balance import show_remaining_balance
from show_help import show_help

balance = 0.0
b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        balance = add_income(balance)

    elif func == "2":
        balance = add_expense(balance)

    elif func == "3":
        show_remaining_balance(balance)

    elif func == "?":
        show_help()

    else:
        print("프로그램을 종료합니다.")
        b_is_exit = not b_is_exit