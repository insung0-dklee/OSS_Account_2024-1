class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item}이(가) 쇼핑 예정 목록에 올바르게 추가되었습니다.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item}이(가) 쇼핑 목록에서 제거되었습니다.")
        else:
            print(f"{item}이(가) 현재 쇼핑 목록에 없습니다.")

    def display_list(self):
        print("\n쇼핑 목록:")
        if self.items:
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item}")
        else:
            print("현재 쇼핑 목록이 비어 있습니다.")

def main():
    shopping_list = ShoppingList()

    while True:
        print("\n1. 쇼핑 목록 추가")
        print("2. 쇼핑 목록 제거")
        print("3. 쇼핑 목록 표시")
        print("4. 종료")

        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            item = input("쇼핑 목록에 추가할 상품을 입력하세요: ")
            shopping_list.add_item(item)
        elif choice == '2':
            item = input("쇼핑 목록에서 제거할 상품을 입력하세요: ")
            shopping_list.remove_item(item)
        elif choice == '3':
            shopping_list.display_list()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
