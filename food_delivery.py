"""
포인트 적립 시스템이 있는 배달 음식 프로그램
단, 포인트는 프로그램 종료시 0원으로 초기화 된다.
단, 포인트는 1000원 이상 보유시 사용이 가능하고 1000원이상 사용하여야 한다.
배달 건당 포인트는 50원씩 적립된다. 
일회용 수저 포함 시 추가 0원 적립, 일회용 수저 미포함시 추가 50원 적립
영수증엔 총 음식 가격/배달비/포인트 사용 금액/총 금액/적립 금액/ 누적 포인트 금액이 출력된다.

start(self) : 메인 메뉴 출력 및 선택에 따른 세부 메뉴 출력 및 종료
show_main_menu(self) : 메인 메뉴 표시 및 선택 입력 받음
take_order(self,choice) : 선택한 음식 종류에 대한 주문 및 각 음식 수량 입력 받음
calculate_cost(self, choice, order) : 주문한 음식의 총 가격 계산 및 포인트 사용 여부 물음 
+ 포인트 적립
+ 최종 결제 정보 출력
apply_points(self, total_cost) : 포인트 사용에 따른 계산
+ 입력에 따라 총 금액에서 차감 및 포인트 잔액 계산
print_receipt(self, food_cost, delivery_fee, points_used, total_cost, points_earned) 
: 영수증 출력
"""

class FoodDelivery:
    def __init__(self):
        self.menus = {
            1: ["콩나물 비빔밥", "순두부 찌개 정식", "돼지 두루치기 정식"],
            2: ["동파육 세트", "짜장면", "1인 훠궈 세트"],
            3: ["연어 초밥 10pcs", "돈카츠 라멘", "치킨 카레"],
            4: ["1인용 피자", "토마토 파스타", "스테이크"],
            5: ["아이스크림 케이크", "망고 빙수", "스콘 세트"]
        }
        self.prices = {
            1: [8000, 10000, 13000],
            2: [12000, 8000, 13000],
            3: [15000, 8500, 8000],
            4: [16000, 10000, 25000],
            5: [18000, 11500, 12000]
        }
        self.delivery_fee = 3000
        self.point_balance = 0  # 프로그램 시작 시 포인트 잔액을 0으로 초기화
        self.point_used = 0

    def start(self):
        while True:
            choice = self.show_main_menu()
            try:
                if choice == 0:
                    print("프로그램을 종료합니다.")
                    break
                elif choice in range(1, 6):
                    order = self.take_order(choice)
                    if sum(order) == 0:
                        print("주문한 음식이 없습니다. 다시 선택해 주세요.")
                        continue
                    self.calculate_cost(choice, order)
                else:
                    print("잘못된 입력입니다. 다시 입력해 주세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해 주세요.")

    def show_main_menu(self):
        print("1. 한식\n2. 중식\n3. 일식\n4. 양식\n5. 후식\n0. 종료")
        while True:
            try:
                choice = int(input("옵션을 선택하세요: "))
                return choice
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해 주세요.")

    def take_order(self, choice):
        print(f"{choice}번 음식 종류를 선택하셨습니다. 다음 옵션 중에서 선택하세요:")
        for i, item in enumerate(self.menus[choice], start=1):
            print(f"{i}. {item} - {self.prices[choice][i-1]}원")

        order = [0, 0, 0]
        for i in range(3):
            while True:
                try:
                    order[i] = int(input(f"{i+1}번 음식을 몇 개 시키시겠습니까? "))
                    if order[i] < 0:
                        print("음수 값은 입력할 수 없습니다. 다시 입력해 주세요.")
                    else:
                        break
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력해 주세요.")
        return order

    def calculate_cost(self, choice, order):
        total_food_cost = sum(self.prices[choice][i] * order[i] for i in range(3))
        total_cost = total_food_cost + self.delivery_fee
        print(f"총 음식 가격: {total_food_cost}원")
        print(f"배달비: {self.delivery_fee}원")
        print(f"총 가격: {total_cost}원")

        if self.point_balance > 0:
            while True:
                try:
                    use_ornot_points = int(input(f"포인트를 사용하시겠습니까? [ 1(yes) / 2(no) ] 현재 포인트 {self.point_balance}원: "))
                    if use_ornot_points == 1:
                        if self.point_balance < 1000:
                            print("포인트는 1000원부터 사용 가능합니다.")
                        else:
                            total_cost = self.apply_points(total_cost)
                        break
                    elif use_ornot_points == 2:
                        print("포인트를 사용하지 않습니다.")
                        break
                    else:
                        print("1 또는 2를 입력하세요.")
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력해 주세요.")
        elif self.point_balance == 0:
            print("현재 포인트가 없습니다.")

        point_earned = 50  # 기본 배달 적립 포인트

        while True:
            try:
                use_cutlery = int(input("일회용 수저를 넣으시겠습니까? 1(yes)/2(no): "))
                if use_cutlery == 1:
                    print("일회용 수저를 넣습니다.")
                    break
                elif use_cutlery == 2:  # 수저 안 넣을 시 50원 추가 적립=>총 100원 적립
                    #self.point_balance = self.point_balance + 50
                    point_earned = point_earned + 50 
                    break
                else:
                    print("잘못된 입력입니다. 1 또는 2를 입력해 주세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해 주세요.")

        self.point_balance += point_earned
        self.print_receipt(total_food_cost, self.delivery_fee, self.point_used, total_cost, point_earned)

    def apply_points(self, total_cost):
        while True:
            try:
                points_to_use = int(input("사용할 포인트 금액을 입력하세요 (0원 입력 시 포인트 사용 안 함): "))
                if points_to_use == 0:
                    print("포인트를 사용하지 않습니다.")
                    return total_cost
                elif points_to_use < 1000:
                    print("포인트는 1000원부터 사용 가능합니다.")
                elif points_to_use > self.point_balance:
                    print("입력한 금액이 포인트 잔액보다 많습니다. 다시 입력해 주세요.")
                else:
                    self.point_used = points_to_use
                    total_cost -= points_to_use
                    self.point_balance -= points_to_use
                    print(f"포인트를 사용하여 최종 가격은 {total_cost}원 입니다.")
                    return total_cost
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력해 주세요.")
    
    def print_receipt(self, food_cost, delivery_fee, points_used, total_cost, points_earned):
            print("----------영수증----------")
            print(f"음식 금액: {food_cost}원")
            print(f"배달비: {delivery_fee}원")
            print(f"포인트 사용 금액: {points_used}원")
            print(f"총 금액: {total_cost}원")
            print(f"적립 금액: {points_earned}원")
            print(f"누적 포인트 금액: {self.point_balance}원")
            print("--------------------------")

if __name__ == "__main__":
    delivery_app = FoodDelivery()  
    delivery_app.start() 

