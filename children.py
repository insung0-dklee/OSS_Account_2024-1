def input_children_info():
    global children_allowance, children_spending, children_toy_price
    children_allowance = {}
    children_spending = {}
    children_toy_price = {}
    num_children = int(input("아이의 숫자를 입력하세요: "))
    for i in range(num_children):
        name = input("아이의 이름을 입력하세요: ")
        children_allowance[name] = 0
        children_spending[name] = []
        children_toy_price[name] = 0
    print("아이들의 정보가 성공적으로 입력되었습니다.")

def give_allowance():
    for name in children_allowance:
        allowance = float(input("{}에게 줄 용돈을 입력하세요: ".format(name)))
        children_allowance[name] += allowance
    print("용돈이 성공적으로 지급되었습니다.")

def check_allowance():
    print("\n아이들의 용돈:")
    for name, allowance in children_allowance.items():
        print("{}: {} 원".format(name, allowance))

def record_spending():
    name = input("소비한 아이의 이름을 입력하세요: ")
    if name not in children_allowance:
        print("등록된 아이가 아닙니다.")
        return
    amount = float(input("소비한 금액을 입력하세요: "))
    children_spending[name].append(amount)
    print("소비 내역이 성공적으로 기록되었습니다.")

def input_toy_price():
    for name in children_allowance:
        price = float(input("{}가 사고 싶은 장난감의 가격을 입력하세요: ".format(name)))
        children_toy_price[name] = price
    print("장난감 가격이 성공적으로 입력되었습니다.")

def check_toy_price():
    print("\n아이들이 사고 싶은 장난감의 가격:")
    for name, price in children_toy_price.items():
        print("{}: {} 원".format(name, price))

def check_spending():
    print("\n아이들의 소비 내역:")
    for name, spending_list in children_spending.items():
        total_spending = sum(spending_list)
        print("{}가 총 {} 원을 소비했습니다.".format(name, total_spending))
        allowance = children_allowance[name]
        if total_spending > allowance:
            print("⚠️ {}의 용돈에서 {} 원을 초과하여 소비했습니다!".format(name, total_spending - allowance))

def check_remaining_allowance():
    print("\n아이들에게 남은 용돈:")
    for name, allowance in children_allowance.items():
        total_spent = sum(children_spending[name])
        remaining_allowance = allowance - total_spent
        print("{}: {} 원".format(name, remaining_allowance))

def calculate_shortfall():
    print("\n아이들이 추가로 모아야 하는 금액:")
    for name, price in children_toy_price.items():
        total_spent = sum(children_spending[name])
        remaining_allowance = children_allowance[name] - total_spent
        shortfall = price - remaining_allowance
        if shortfall > 0:
            print("{}: {} 원".format(name, shortfall))
        else:
            print("{}: 추가로 모을 필요가 없습니다.".format(name))

# 아이들의 정보를 담을 딕셔너리 생성
children_allowance = {}
children_spending = {}
children_toy_price = {}

menu_displayed = False

while True:
    if not menu_displayed:
        print("\n1. 아이 정보 입력")
        print("2. 용돈 지급")
        print("3. 용돈 지급내역 확인")
        print("4. 소비 내역 기록")
        print("5. 아이들이 사고 싶은 장난감 가격 입력")
        print("6. 아이들이 사고 싶은 장난감 가격 확인")
        print("7. 소비 내역 확인")
        print("8. 아이들에게 남은 용돈 확인")
        print("9. 추가로 모아야 하는 금액 계산")
        print("0. 종료")
        menu_displayed = True

    choice = input("메뉴를 선택하세요: ")

    if choice == '1':
        input_children_info()
    elif choice == '2':
        give_allowance()
    elif choice == '3':
        check_allowance()
    elif choice == '4':
        record_spending()
    elif choice == '5':
        input_toy_price()
    elif choice == '6':
        check_toy_price()
    elif choice == '7':
        check_spending()
    elif choice == '8':
        check_remaining_allowance()
    elif choice == '9':
        calculate_shortfall()
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    elif choice == '?':
        print("도움말: 메뉴를 선택할 때 '1'부터 '9'까지의 숫자를 입력하세요.")
        menu_displayed = False
    else:
        print("올바른 메뉴를 선택하세요.")
