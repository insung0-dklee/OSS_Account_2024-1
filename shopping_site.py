import webbrowser

class ShoppingSite:
    def __init__(self, name, search_url):
        self.name = name
        self.search_url = search_url

class ShoppingSiteRegistry:
    def __init__(self):
        self.sites = {}

    def add_site(self, name, search_url):
        if name in self.sites:
            print(f"해당 쇼핑몰 '{name}'이 이미 등록되어 있습니다.")
            return
        self.sites[name] = ShoppingSite(name, search_url)
        print(f"쇼핑몰 '{name}'이 등록되었습니다.")

    def list_sites(self):
        if not self.sites:
            print("등록된 쇼핑몰이 없습니다.")
            return
        print("등록된 쇼핑몰 목록:")
        for i, (name, site) in enumerate(self.sites.items(), 1):
            print(f"{i}. 쇼핑몰 이름: {name}, 검색 URL: {site.search_url}")

    def open_site(self, index):
        if not self.sites:
            print("등록된 쇼핑몰이 없습니다.")
            return
        try:
            site_name = list(self.sites.keys())[index - 1]
            webbrowser.open(self.sites[site_name].search_url)
            print(f"쇼핑몰 '{site_name}'으로 이동합니다.")
        except IndexError:
            print("잘못된 입력입니다. 다시 시도하세요.")

def main():
    registry = ShoppingSiteRegistry()

    while True:
        print("\n메뉴:")
        print("1. 쇼핑몰 사이트 등록")
        print("2. 등록된 쇼핑몰 목록 보기")
        print("3. 쇼핑몰 사이트로 바로 이동")
        print("4. 종료")
        choice = input("선택: ")

        if choice == "1":
            name = input("쇼핑몰 이름을 입력하세요: ")
            search_url = input(f"{name}의 검색 URL을 입력하세요 (상품명을 검색어로 사용): ")
            registry.add_site(name, search_url)
        elif choice == "2":
            registry.list_sites()
        elif choice == "3":
            registry.list_sites()
            index = int(input("이동을 원하는 쇼핑몰의 번호를 입력하세요: "))
            registry.open_site(index)
        elif choice == "4":
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()