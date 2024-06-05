def manage_healthcare_expenses():
    healthcare_expenses = []
    #헬스케어 도움말 출력
    def print_help():
        print("\n헬스케어 지출 관리 기능:")
        print("1. 추가 - 새로운 헬스케어 지출 항목을 추가합니다.")
        print("2. 삭제 - 특정 설명에 해당하는 지출 항목을 삭제합니다.")
        print("3. 조회 - 현재까지 등록된 모든 헬스케어 지출 항목을 조회합니다.")
        print("4. 수정 - 특정 지출 항목을 수정합니다.")
        print("5. 리포트 - 카테고리별 및 전체 헬스케어 지출에 대한 요약 리포트를 제공합니다.")
        print("0. 종료 - 헬스케어 지출 관리를 종료합니다.\n")

    while True:
        action = input("헬스케어 지출 관리 기능을 선택하세요 (1: 추가, 2: 삭제, 3: 조회, 4: 수정, 5: 리포트, 0: 종료, ?: 도움말): ").strip()
        
        #추가 기능 (1): 사용자로부터 지출 설명, 금액, 날짜 및 카테고리를 입력받아 헬스케어 지출 항목을 추가합니다.
        if action == "1":
            # 헬스케어 지출 항목 추가
            description = input("지출 설명을 입력하세요 (예: 병원비, 약품비): ")
            amount = float(input("금액을 입력하세요: "))
            date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
            category = input("카테고리를 입력하세요 (예: 의료비, 보험료): ")
            healthcare_expenses.append({"description": description, "amount": amount, "date": date, "category": category})
            print(f"헬스케어 지출이 추가되었습니다: {description}, {amount}원, {date}, 카테고리: {category}")
        
        #삭제 기능 (2): 사용자로부터 삭제할 지출 항목의 번호를 입력받아 해당 항목을 삭제합니다.
        elif action == "2":
            # 특정 설명에 해당하는 지출 항목 삭제
            if not healthcare_expenses:
                print("삭제할 지출 항목이 없습니다.")
            else:
                print("헬스케어 지출 목록:")
                for index, expense in enumerate(healthcare_expenses, start=1):
                    print(f"{index}. {expense['description']}, {expense['amount']}원, {expense['date']}, {expense['category']}")
                try:
                    index = int(input("삭제할 지출 항목의 번호를 입력하세요: "))
                    if 1 <= index <= len(healthcare_expenses):
                        del healthcare_expenses[index - 1]
                        print("지출 항목이 삭제되었습니다.")
                    else:
                        print("잘못된 번호입니다.")
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력하세요.")
        #조회 기능 (3): 현재까지 등록된 모든 헬스케어 지출 항목을 조회합니다.
        elif action == "3":
            # 등록된 모든 헬스케어 지출 항목 조회
            if not healthcare_expenses:
                print("등록된 헬스케어 지출이 없습니다.")
            else:
                print("헬스케어 지출 목록:")
                for e in healthcare_expenses:
                    print(f"- 설명: {e['description']}, 금액: {e['amount']}원, 날짜: {e['date']}, 카테고리: {e['category']}")
        #수정 기능 (4): 특정 지출 항목의 정보를 수정합니다. 사용자로부터 수정할 항목의 번호를 입력받아 해당 항목의 정보를 수정합니다.
        elif action == "4":
            # 특정 지출 항목 수정
            if not healthcare_expenses:
                print("수정할 지출 항목이 없습니다.")
            else:
                print("헬스케어 지출 목록:")
                for index, expense in enumerate(healthcare_expenses, start=1):
                    print(f"{index}. {expense['description']}, {expense['amount']}원, {expense['date']}, {expense['category']}")
                try: # 수정할 지출 항목의 번호를 입력받습니다.
                    index = int(input("수정할 지출 항목의 번호를 입력하세요: "))
                    if 1 <= index <= len(healthcare_expenses):
                         # 선택한 지출 항목의 정보를 가져옵니다.
                        expense = healthcare_expenses[index - 1]
                           # 새로운 정보를 입력받습니다. 입력하지 않으면 기존 값 유지합니다.
                        print("수정을 원하는 정보를 입력하세요 (입력하지 않으면 기존 값 유지):")
                        new_description = input(f"현재 설명: {expense['description']}, 새로운 설명: ") or expense['description']
                        new_amount = input(f"현재 금액: {expense['amount']}원, 새로운 금액: ") or str(expense['amount'])
                        new_date = input(f"현재 날짜: {expense['date']}, 새로운 날짜: ") or expense['date']
                        new_category = input(f"현재 카테고리: {expense['category']}, 새로운 카테고리: ") or expense['category']
                        # 선택한 지출 항목을 새로운 정보로 업데이트합니다.
                        healthcare_expenses[index - 1] = {"description": new_description, "amount": float(new_amount), "date": new_date, "category": new_category}
                        print("지출 항목이 수정되었습니다.")
                    else:
                        print("잘못된 번호입니다.")
                except ValueError:
                    print("잘못된 입력입니다. 숫자를 입력하세요.")
        #리포트 기능 (5): 카테고리별 및 전체 헬스케어 지출에 대한 요약 리포트를 제공합니다.
        elif action == "5":
            # 헬스케어 지출 리포트 제공
            if not healthcare_expenses:
                print("리포트를 생성할 지출 항목이 없습니다.")
            else: # 모든 카테고리를 가져옵니다.
                categories = set(e['category'] for e in healthcare_expenses)
                print("\n헬스케어 지출 리포트\n----------------------")
                # 각 카테고리별 지출을 계산하여 출력합니다.
                for category in categories:
                    total_expenses = sum(float(e['amount']) for e in healthcare_expenses if e['category'] == category)
                    print(f"{category} 지출: {total_expenses:.2f}원")
                total_expenses = sum(float(e['amount']) for e in healthcare_expenses)
                   # 전체 헬스케어 지출을 계산하여 출력합니다.
                print(f"총 헬스케어 지출: {total_expenses:.2f}원")
                print("----------------------\n")

        elif action == "0":
            # 헬스케어 지출 관리 종료
            print("헬스케어 지출 관리를 종료합니다.")
            break

        elif action == "?":
            # 도움말 출력
            print_help()

        else:
            # 올바른 명령어가 입력되지 않았을 때
            print("올바른 명령어를 입력해 주세요.")

manage_healthcare_expenses()
