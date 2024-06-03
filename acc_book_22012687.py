""" 수입/지출을 관리하는 가계부 클래스

@주요기능
        1. 내역 추가:     수입/지출 내역을 가계부에 추가
        2. 내역 수정:     가계부의 수입/지출 내역을 수정
        3. 내역 삭제:     가계부의 수입/지출 내역을 삭제
        4. 내역 조회:     가계부의 수입/지출 내역을 조회
        5. 날짜 입력:     사용자로부터 입력받은 날짜를 반환
        6. 요일 입력:     사용자로부터 입력받은 요일을 반환
        7. 금액 입력:     사용자로부터 입력받은 금액을 반환
        8. 카테고리 입력: 사용자로부터 입력받은 카테고리를 반환

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
        result, date = self.date_err_check()
        if result == True:
            self.date.append(date)
        
        result, day_of_week = self.DoW_err_check()
        if result == True:
            self.day_of_week.append(day_of_week)
        
        result, expense = self.exp_err_check()
        if result == True:
            self.expense.append(expense)

        print("\n작성 형식: 식비, 카페, 쇼핑, 이체, 교통 등")
        category = input("카테고리: ")
        self.category.append(category)
        print("\n가계부에 내역서가 추가되었습니다.\n")

    # 2. 내역 수정 기능
    def edit_statement(self):
        pass

    # 3. 내역 삭제 기능
    def del_statement(self):
        pass
                
    # 4. 내역 조회 기능
    def log_statement(self):
        pass
    
    # 5. 날짜 입력 검사 기능
    def date_err_check(self):
        while True:
            print("작성 형식: 2024-06-02-1\n(마지막 숫자는 같은 날짜의 내역서를 구분하기 위한 번호)") 
            date = input("날짜: ")
            try:
                int("".join(date.split('-')))
            except ValueError:
                print("\n잘못된 입력 형식입니다. 다시 입력해주세요.\n")
                continue
            try: 
                year = int(date.split('-')[0])
                if len(str(year)) != 4:
                    print("\n잘못된 입력 형식입니다. 다시 입력해주세요.\n")
                    continue
            except Exception:
                print("\n\'년도\'의 입력 형식이 잘못되었습니다. 다시 입력해주세요.\n")
                continue
            try:
                month = int(date.split('-')[1])
                if month <= 0 or month >= 13:
                    print("\n1 ~ 12월 내에서 입력해주세요\n")
                    continue
            except Exception:
                print("\n\'월\'의 입력 형식이 잘못되었습니다. 다시 입력해주세요.\n")
                continue
            try:
                day = int(date.split('-')[2])
                if day <= 0 or day >= 32:
                    print("\n1 ~ 31일 내에서 입력해주세요.\n")
                    continue
            except Exception:
                print("\n\'일\'의 입력 형식이 잘못되었습니다. 다시 입력해주세요.\n") 
                continue
            try:
                idx = int(date.split('-')[3])
                if idx <= 0:
                    print("\n1 이상 범위 내에서 번호를 입력해주세요.\n")
                    continue
            except Exception:
                print("\n\'번호\'의 입력 형식이 잘못되었습니다. 다시 입력해주세요.\n") 
                continue
            return True, date
        
    # 6. 요일 입력 검사 기능
    def DoW_err_check(self):
        pass

    # 7. 금액 입력 검사 기능
    def exp_err_check(self):
        pass

    # 8. 카테고리 오류 검사 기능
    def ctgry_err_check(self):
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
        title = "수입"
    else: 
        title = "지출"

    while True:
        print("\n========== 메뉴 ==========")
        print(f"[1] {title} 내역 추가")    
        print(f"[2] {title} 내역 수정")    
        print(f"[3] {title} 내역 삭제")
        print(f"[4] {title} 내역 조회")
        print("[0] 메인 화면으로 돌아가기")
        print("==========================")
        
        try:
            sel_num = int(input("메뉴 선택: "))
        except Exception:
            print("\n 숫자만 입력해주세요.\n")
            continue

        if sel_num == 0:
            break
        elif sel_num == 1:
            print(f"\n======= {title} 내역 추가 =======")
            statement.add_statement()
        elif sel_num == 2:
            print(f"\n======= {title} 내역 수정 =======")
            statement.edit_statement()
        elif sel_num == 3:
            print(f"\n======= {title} 내역 삭제 =======")
            statement.del_statement()
        elif sel_num == 4:
            print(f"\n======= {title} 내역 조회 =======")
            statement.log_statement()


def main():
    income = ACC_BOOK()
    spending = ACC_BOOK()

    print("\n가계부 프로그램 실행")

    while True:
        print("\n========== 메뉴 ==========")
        print("[1] 수입")    
        print("[2] 지출")  
        print("[0] 프로그램 종료")
        print("==========================")

        try:
            sel_num = int(input("메뉴 선택: "))
        except Exception:
            print("\n 숫자만 입력해주세요.\n")

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