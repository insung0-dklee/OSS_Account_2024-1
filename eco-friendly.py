# 각 소비 항목의 탄소 발자국 데이터 (kg CO2e 단위)
carbon_footprint_data = {
    '소고기': 27.0,        # kg 당
    '닭': 6.9,      # kg 당
    '야채': 2.0,   # kg 당
    '자가용': 2.3,          # km 당
    '버스': 0.1,          # km 당
    '기차': 0.05,       # km 당
    '비행기': 0.15,      # km 당
    '전기': 0.5,  # kWh 당
}

# 친환경적인 대안 제안
sustainable_alternatives = {
    '소고기': '소고기 소비를 줄이고 식물성 단백질을 시도해 보세요.',
    '자가용': '대중교통을 이용하거나 자전거를 타거나 걸어보세요.',
    '전기': '재생 가능 에너지원을 사용하거나 사용량을 줄이세요.'
}

def get_consumption_data():
    """
    사용자로부터 소비 내역을 입력받는 함수.
    '완료'를 입력할 때까지 소비 항목과 수량을 반복적으로 입력받습니다.
    """
    consumption = {}  # 소비 내역을 저장할 빈 딕셔너리
    print("소비 내역을 입력하세요. 완료하려면 '완료'라고 입력하세요.")
    while True:
        # 소비 항목 입력 받기
        item = input("항목을 입력하세요 (예: '소고기', '닭', '야채', '자가용', '버스', '기차', '비행기', '전기'): ").lower()
        if item == '완료':
            break
        if item not in carbon_footprint_data:
            # 입력된 항목이 탄소 발자국 데이터에 없는 경우
            print("항목을 인식할 수 없습니다. 유효한 항목을 입력하세요.")
            continue
        # 소비 수량 입력 받기
        quantity = float(input(f"{item}의 수량을 입력하세요 (적절한 단위로): "))
        # 소비 내역 딕셔너리에 항목과 수량을 추가하거나 기존 항목의 수량을 갱신
        consumption[item] = consumption.get(item, 0) + quantity
    return consumption

def calculate_carbon_footprint(consumption):
    """
    소비 내역에 따른 총 탄소 발자국과 각 항목별 탄소 발자국을 계산하는 함수.
    """
    total_carbon_footprint = 0  # 총 탄소 발자국을 저장할 변수
    itemized_footprint = {}  # 항목별 탄소 발자국을 저장할 딕셔너리
    for item, quantity in consumption.items():
        # 각 항목의 탄소 발자국을 계산
        footprint = carbon_footprint_data[item] * quantity
        itemized_footprint[item] = footprint
        total_carbon_footprint += footprint  # 총 탄소 발자국에 추가
    return total_carbon_footprint, itemized_footprint

def provide_feedback(total_footprint, itemized_footprint):
    """
    총 탄소 발자국과 항목별 탄소 발자국을 출력하고,
    각 항목에 대해 친환경적인 대안을 제안하는 함수.
    """
    print(f"\n총 탄소 발자국은 {total_footprint:.2f} kg CO2e 입니다.")
    print("\n항목별 탄소 발자국:")
    for item, footprint in itemized_footprint.items():
        print(f"{item}: {footprint:.2f} kg CO2e")
        if item in sustainable_alternatives:
            # 해당 항목에 대한 친환경 대안 출력
            print(f"제안: {sustainable_alternatives[item]}")
    print("\n지속 가능한 소비 실천에 감사드립니다!")

def main():
    """
    프로그램의 메인 함수. 소비 내역을 입력받고,
    탄소 발자국을 계산하여 피드백을 제공하는 전체 흐름을 제어합니다.
    """
    consumption = get_consumption_data()  # 소비 내역 입력 받기
    total_footprint, itemized_footprint = calculate_carbon_footprint(consumption)  # 탄소 발자국 계산
    provide_feedback(total_footprint, itemized_footprint)  # 피드백 제공

if __name__ == "__main__":
    main()  # 프로그램 실행
