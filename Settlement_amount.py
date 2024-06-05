def calculate_individual_expenses():
    total_amount = 0  # 총 지출액을 저장할 변수 초기화
    num_people = int(input("인원 수를 입력하세요: "))  # 사용자로부터 인원 수를 입력받음

    expenses = []  # 각 사람의 총 지출액을 저장할 리스트 초기화
    names = []  # 각 사람의 이름을 저장할 리스트 초기화
    for i in range(num_people):
        name = input(f"사람 {i+1}의 이름을 입력하세요: ")  # 각 사람의 이름을 입력받음
        names.append(name)  # 입력받은 이름을 names 리스트에 추가
        person_expenses = input(f"{name}의 지출 금액을 입력하세요 (여러 개일 경우 띄어쓰기로 구분): ")  # 각 사람의 지출 금액을 입력받음
        person_expenses_list = list(map(float, person_expenses.split()))  # 입력받은 지출 금액들을 띄어쓰기로 구분하여 float 타입의 리스트로 변환
        expenses.append(sum(person_expenses_list))  # 각 사람의 총 지출액을 계산하여 expenses 리스트에 추가

    for i in range(num_people):
        print(f"{names[i]}의 지출액: {int(expenses[i])}")  # 각 사람의 이름과 지출액을 출력
        total_amount += int(expenses[i])  # 총 지출액을 계산하여 total_amount 변수에 더함

    print(f"총 지출액: {int(total_amount)}")  # 최종 총 지출액을 출력

if __name__ == "__main__":
    calculate_individual_expenses()  # 메인 함수 호출
