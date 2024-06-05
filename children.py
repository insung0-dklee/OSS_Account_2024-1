def input_children_info():
    global children_allowance, children_spending
    children_allowance = {}
    children_spending = {}
    num_children = int(input("아이의 숫자를 입력하세요: "))
    for i in range(num_children):
        name = input("아이의 이름을 입력하세요: ")
        children_allowance[name] = 0
        children_spending[name] = []  
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

def check_spending():
    print("\n아이들의 소비 내역:")
    for name, spending_list in children_spending.items():
        total_spending = sum(spending_list)
        print("{}가 총 {} 원을 소비했습니다.".format(name, total_spending))
        allowance = children_allowance[name]
        if total_spending > allowance:
            print("⚠️ {}의 용돈에서 {} 원을 초과하여 소비했습니다!".format(name, total_spending - allowance))

# 아이들의 정보를 담을 딕셔너리 생성
children_allowance = {}

while True:
    print("\n1. 아이 정보 입력")
    print("2. 용돈 지급")
    print("3. 용돈 확인")
    print("4. 소비 내역 기록")
    print("5. 소비 내역 확인")
    print("6. 종료")
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
        check_spending()
    elif choice == '6':
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴를 선택하세요.")
