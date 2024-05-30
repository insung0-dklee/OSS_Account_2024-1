"""
 카테고리 별 총액을 출력하는 함수

 @Param
 date : 가계부 기록 일자
 category : 돈 기록 카테고리
 amout : 지출 및 수입 금액
 income : 수입인지 지출인지 구별하는 변수, True일 경우 수입을, False일 경우 지출을 의미한다
 totals : 카테고리 별 총액을 저장
 entries : 가계부 기록



"""


class 가계부:
    def __init__(self):
        # 가계부 초기화, 항목들을 저장할 리스트 생성
        self.entries = []

    def add_entry(self, date, category, amount, income=True):
        # 새로운 가계부 항목 추가 : 날짜, 카테고리, 금액, 수입인지 지출인지
        self.entries.append({"date": date, "category": category, "amount": amount, "income": income})

    def total_by_category(self):
        # 카테고리별 총액 계산
        totals = {}
        for entry in self.entries:
            # 카테고리가 이미 존재하면 금액을 더하고, 아니면 새로 추가
            if entry["category"] in totals:
                totals[entry["category"]] += entry["amount"]
            else:
                totals[entry["category"]] = entry["amount"]
        # 카테고리별 총액 출력
        for category, total in totals.items():
            print(f"카테고리: {category}, 총액: {total}")

# 가계부 인스턴스 생성
my_budget = 가계부()

b_is_exit = 0

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        # 기능 1: 카테고리별 총액 보기
        my_budget.total_by_category()

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

