""" 수입/지출을 관리하는 가계부 클래스

@주요기능
        1. 내역 추가: 사용자로부터 지출에 대한 정보를 입력받음
        2. 내역 수정: 사용자로부터 수정할 지출 정보를 입력받음
        3. 내역 삭제: 사용자로부터 삭제할 지출 정보를 입력받아 
        4. 내역 조회: 사용자로부터 조회할 지출 정보를 출력해줌

@멤버변수
        date:        내역서의 날짜들을 저장하는 변수 ('-'으로 년도-월-일-번호 구분)
        day_of_week: 내역서의 요일들을 저장하는 변수
        expense:     내역서의 비용들 저장하는 변수
        category:    내역서의 카테고리들을 저장하는 변수
"""

class ACC_BOOK:
    def __init__(self):
        self.date = []
        self.day_of_week = []
        self.expense = []
        self.category = []        

    # 1. 내역 추가 기능
    def add_statement(self):
        pass

    # 2. 내역 수정 기능
    def edit_statement(self):
        pass

    # 3. 내역 삭제 기능
    def del_statement(self):
        pass

    # 4. 내역 조회 기능
    def log_statement(self):
        pass


""" 
@주요기능
        가계부를 수입과 지출로 구분하는 기능

@매개변수
        type:       수입과 지출을 결정하는 변수
        statement:  가계부 객체를 전달받는 변수
"""
def income_spending(type, statement):
    if type == 1: 
        type = "수입"
    else: 
        type = "지출"

    while True:
        print("\n========== 메뉴 ==========")
        print(f"[1] {type} 내역 추가")    
        print(f"[2] {type} 내역 수정")    
        print(f"[3] {type} 내역 삭제")
        print(f"[4] {type} 내역 조회")
        print("[0] 메인 화면으로 돌아가기")
        print("==========================")
        sel_num = int(input("메뉴 선택: "))

        if sel_num == 0:
            break
        elif sel_num == 1:
            pass
        elif sel_num == 2:
            pass
        elif sel_num == 3:
            pass
        elif sel_num == 4:
            pass


def main():
    income = ACC_BOOK()
    spending = ACC_BOOK()

    print("\n가계부 프로그램 실행")

    while True:
        print("========== 메뉴 ==========")
        print("[1] 수입")    
        print("[2] 지출")  
        print("[0] 프로그램 종료")
        print("==========================")

        sel_num = int(input("메뉴 선택: "))

        if sel_num == 0:
            print("가계부 프로그램을 종료합니다.")
            break
        elif sel_num == 1 or sel_num == 2:
            if sel_num == 1:
                income_spending(sel_num, income)
            else:
                income_spending(sel_num, spending)
    

if __name__ == '__main__':
    main()