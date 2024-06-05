"""
- 위시리스트에 물건이름, 금액, 중요도를 저장하여
      원하는 물건 리스트를 만들고 금액을 관리하여 
      소비 습관 형성에 도움을 주기 위한 클래스이다.
"""
class WishList:
    # 위시리스트 항목을 저장할 리스트
    def __init__(self) -> None:
        self.wish_list = []
    
    """
    input: 원하는 물건 이름, 금액, 중요도
    output: .
    - 위시리스트에 관련 정보를 저장하는 함수이다.
      만약 입력하는 중 오류가 난다면 처음부터 다시 입력한다.
    """
    # 위시리스트 추가 기능
    def add_to_wish_list(self):
        while True:
            try:
                item_name = input("물건 이름: ")
                item_price = float(input("금액: "))
                if item_price <= 0:
                    print("금액은 양수여야 합니다.")
                    continue
                item_priority = int(input("중요도(1-5): "))
                if item_priority < 1 or item_priority > 5:
                    print("중요도는 1부터 5 사이의 값이어야 합니다.")
                    continue
                break
            except ValueError:
                print("금액은 숫자여야 하며, 중요도는 1부터 5 사이의 정수여야 합니다.")

        self.wish_list.append({
            "name": item_name,
            "price": item_price,
            "priority": item_priority
        })

        print("위시리스트에 추가되었습니다.")

    # 중요도 순으로 정렬
    def sort_by_priority(self):
        self.wish_list.sort(key=lambda x: x["priority"], reverse=True)
        self.print_wish_list()

    # 금액 순으로 정렬  
    def sort_by_price(self):
        self.wish_list.sort(key=lambda x: x["price"])
        self.print_wish_list()

    # 위시리스트 출력
    def print_wish_list(self):
        if not self.wish_list:
            print("위시리스트가 비어있습니다.")
        else:
            print("위시리스트:")
            for item in self.wish_list:
                print(f"- {item['name']} ({item['price']}원, 중요도: {item['priority']})")

    
    def wish_list_main(self):
        # 메인 루프
        while True:
            print("1. 위시리스트 추가")
            print("2. 중요도 순으로 정렬")
            print("3. 금액 순으로 정렬")
            print("4. 종료")
    
            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                self.add_to_wish_list()
            elif choice == "2":
                self.sort_by_priority()
            elif choice == "3":
                self.sort_by_price()
            elif choice == "4":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")

if __name__=='__main__':
    wish_list=WishList()
    wish_list.wish_list_main()