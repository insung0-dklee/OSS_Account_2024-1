class Account_book:
  
    def __init__(self, name, bal):  # 초기화
        self.bal = 0  # 잔액 - 미설정시 0원
        self.income_total = 0  # 수입 총액
        self.income_list = []  # 수입 기록 리스트
        self.spend_total = 0  # 지출 총액
        self.spend_list = []  # 지출 기록 리스트
        self.name = name  # 이름 설정
        if bal > 0:  # 잔액 설정
            self.income_total += bal
            self.bal = bal
        else:  # 잔액이 0원보다 낮으면 0원으로 설정
            print("금액이 너무 적습니다. 초기값(0원)으로 지정합니다.")

    def income(self):  # 수입 입력시 추가
        while True:
            income_money = int(input("수입을 입력하세요 (그만하려면 -1을 입력하세요): "))
            if income_money == -1:
                break
            if income_money < 0:  # 수입 잘못 입력 방지
                print("0 미만의 값을 입력하셨습니다.")
                continue
            category = input("수입의 카테고리를 입력하세요: ")
            date = input("수입 날짜를 입력하세요 (YYYY-MM-DD): ")
            self.bal += income_money  # 금액 추가 및 내역을 리스트에 넣기
            self.income_list.append({"amount": income_money, "category": category, "date": date})
            self.income_total += income_money

    def spend(self):  # 지출 입력시 추가
        while True:
            spend_money = int(input("지출을 입력하세요 (그만하려면 -1을 입력하세요): "))
            if spend_money == -1:
                break
            if spend_money < 0 or spend_money > self.bal:  # 지출 잘못 입력 방지
                print("값을 잘못 입력하셨습니다.")
                continue
            category = input("지출의 카테고리를 입력하세요: ")
            date = input("지출 날짜를 입력하세요 (YYYY-MM-DD): ")
            self.bal -= spend_money  # 금액 감소 및 내역을 리스트에 넣기
            self.spend_list.append({"amount": spend_money, "category": category, "date": date})
            self.spend_total += spend_money

    def show_account(self):  # 금액 출력
        print("현재 남은 금액은:", self.bal, "원 입니다.")

    def show_total(self):  # 수입, 지출 총액 출력
        print("현재까지 소득의 총합은", self.income_total, "원 입니다.")
        print("현재까지 지출의 총합은", self.spend_total, "원 입니다.")

    def show_sortedlist(self):  # 지출 및 수입 순위 출력
        print("보고싶은 내역을 선택하세요")
        data_type = input("1번 - 수입, 2번 - 지출: ")  # 수입 혹은 지출 선택
        if data_type not in ["1", "2"]:
            print("잘못 입력하셨습니다.")
            return
        sort_type = input("1번 - 전체, 2번 - 카테고리별, 3번 - 기간별: ")  # 정렬 기준 선택
        if sort_type not in ["1", "2", "3"]:
            print("잘못 입력하셨습니다.")
            return

        if data_type == "1":
            print("수입 내역")
            if sort_type == "1":
                sortedlist = sorted(self.income_list, key=lambda x: x["amount"], reverse=True)
            elif sort_type == "2":
                category = input("카테고리를 입력하세요: ")
                sortedlist = [x for x in self.income_list if x["category"] == category]
                sortedlist = sorted(sortedlist, key=lambda x: x["amount"], reverse=True)
            elif sort_type == "3":
                start_date = input("시작 날짜를 입력하세요 (YYYY-MM-DD): ")
                end_date = input("끝 날짜를 입력하세요 (YYYY-MM-DD): ")
                sortedlist = [x for x in self.income_list if start_date <= x["date"] <= end_date]
                sortedlist = sorted(sortedlist, key=lambda x: x["amount"], reverse=True)
        else:
            print("지출 내역")
            if sort_type == "1":
                sortedlist = sorted(self.spend_list, key=lambda x: x["amount"], reverse=True)
            elif sort_type == "2":
                category = input("카테고리를 입력하세요: ")
                sortedlist = [x for x in self.spend_list if x["category"] == category]
                sortedlist = sorted(sortedlist, key=lambda x: x["amount"], reverse=True)
            elif sort_type == "3":
                start_date = input("시작 날짜를 입력하세요 (YYYY-MM-DD): ")
                end_date = input("끝 날짜를 입력하세요 (YYYY-MM-DD): ")
                sortedlist = [x for x in self.spend_list if start_date <= x["date"] <= end_date]
                sortedlist = sorted(sortedlist, key=lambda x: x["amount"], reverse=True)

        for i in range(0, 10):  # 10위 까지만 출력
            if len(sortedlist) <= i:  # 만약 리스트 크기보다 작을 경우 탈출
                break
            print(f"{i+1}위: {sortedlist[i]['amount']}원, 카테고리: {sortedlist[i]['category']}, 날짜: {sortedlist[i]['date']}")
